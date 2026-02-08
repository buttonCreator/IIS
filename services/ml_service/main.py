from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
from api_handler import FastAPIHandler
from prometheus_client import Histogram, Counter, generate_latest, CONTENT_TYPE_LATEST
import time

app = FastAPI()
handler = FastAPIHandler()

prediction_histogram = Histogram(
    'ml_model_predictions',
    'Histogram of ML model predictions',
    buckets=(0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5)
)

request_counter = Counter('ml_service_requests_total', 'Total number of requests to ML service')

error_counter = Counter('ml_service_errors_total', 'Total number of errors', ['status_code'])

request_latency = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['method', 'endpoint']
)

@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    if request.url.path == "/metrics":
        return await call_next(request)

    start_time = time.time()
    response = await call_next(request)
    latency = time.time() - start_time

    request_latency.labels(
        method=request.method,
        endpoint=request.url.path
    ).observe(latency)

    if response.status_code >= 400:
        error_counter.labels(status_code=str(response.status_code)).inc()

    return response

class MobileFeatures(BaseModel):
    battery_power: int
    blue: int
    clock_speed: float
    dual_sim: int
    fc: int
    four_g: int
    int_memory: int
    m_dep: float
    mobile_wt: int
    n_cores: int
    pc: int
    px_height: int
    px_width: int
    ram: int
    sc_h: int
    sc_w: int
    talk_time: int
    three_g: int
    touch_screen: int
    wifi: int
    battery_efficiency: float
    screen_size: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/prediction")
def predict(item_id: int, features: MobileFeatures):
    request_counter.inc()
    features_dict = features.dict()
    prediction = handler.predict(features_dict)
    prediction_histogram.observe(prediction)
    return {
        "item_id": item_id,
        "price": prediction
    }

@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
