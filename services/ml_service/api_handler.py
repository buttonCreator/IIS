import os
import pickle
import pandas as pd

class FastAPIHandler:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, "../models/model.pkl")

        if os.path.exists(model_path):
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
            print(f"Модель успешно загружена из: {model_path}")
        else:
            raise FileNotFoundError(f"Файл модели не найден по пути: {model_path}")

    def predict(self, features: dict):
        df = pd.DataFrame([features])
        result = self.model.predict(df)
        return float(result[0])
