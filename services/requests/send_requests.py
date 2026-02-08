import requests
import time
import random
import json

SERVICE_URL = "http://ml_service:8000/api/prediction"

SAMPLE_DATA = [
    {
        "battery_power": 1403,
        "blue": 0,
        "clock_speed": 2.7,
        "dual_sim": 0,
        "fc": 2,
        "four_g": 1,
        "int_memory": 26,
        "m_dep": 0.1,
        "mobile_wt": 164,
        "n_cores": 5,
        "pc": 10,
        "px_height": 1200,
        "px_width": 1251,
        "ram": 3371,
        "sc_h": 13,
        "sc_w": 9,
        "talk_time": 9,
        "three_g": 1,
        "touch_screen": 0,
        "wifi": 1,
        "battery_efficiency": 8.554878,
        "screen_size": 15.811388
    },
    {
        "battery_power": 1600,
        "blue": 0,
        "clock_speed": 2.5,
        "dual_sim": 1,
        "fc": 1,
        "four_g": 0,
        "int_memory": 19,
        "m_dep": 0.6,
        "mobile_wt": 88,
        "n_cores": 6,
        "pc": 5,
        "px_height": 1500,
        "px_width": 1713,
        "ram": 1179,
        "sc_h": 10,
        "sc_w": 3,
        "talk_time": 18,
        "three_g": 0,
        "touch_screen": 0,
        "wifi": 1,
        "battery_efficiency": 18.181818,
        "screen_size": 10.440307
    },
    {
        "battery_power": 1122,
        "blue": 0,
        "clock_speed": 0.5,
        "dual_sim": 0,
        "fc": 0,
        "four_g": 1,
        "int_memory": 40,
        "m_dep": 0.3,
        "mobile_wt": 156,
        "n_cores": 7,
        "pc": 8,
        "px_height": 900,
        "px_width": 1163,
        "ram": 1456,
        "sc_h": 9,
        "sc_w": 3,
        "talk_time": 20,
        "three_g": 1,
        "touch_screen": 1,
        "wifi": 0,
        "battery_efficiency": 7.192308,
        "screen_size": 9.486833
    },
    {
        "battery_power": 502,
        "blue": 0,
        "clock_speed": 1.5,
        "dual_sim": 1,
        "fc": 7,
        "four_g": 0,
        "int_memory": 37,
        "m_dep": 0.2,
        "mobile_wt": 199,
        "n_cores": 2,
        "pc": 12,
        "px_height": 600,
        "px_width": 1810,
        "ram": 1649,
        "sc_h": 6,
        "sc_w": 1,
        "talk_time": 14,
        "three_g": 0,
        "touch_screen": 1,
        "wifi": 0,
        "battery_efficiency": 2.522613,
        "screen_size": 6.082763
    },
    {
        "battery_power": 1722,
        "blue": 1,
        "clock_speed": 1.0,
        "dual_sim": 0,
        "fc": 7,
        "four_g": 0,
        "int_memory": 25,
        "m_dep": 0.8,
        "mobile_wt": 88,
        "n_cores": 6,
        "pc": 15,
        "px_height": 1800,
        "px_width": 1638,
        "ram": 2376,
        "sc_h": 5,
        "sc_w": 1,
        "talk_time": 19,
        "three_g": 0,
        "touch_screen": 0,
        "wifi": 1,
        "battery_efficiency": 19.568182,
        "screen_size": 5.099020
    }
]

def send_request(item_id):
    try:
        features = random.choice(SAMPLE_DATA)
        params = {"item_id": item_id}

        response = requests.post(
            SERVICE_URL,
            params=params,
            json=features,
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()
            print(f"Request #{item_id}: Prediction = {result['price']:.2f}, Status = {response.status_code}")
        else:
            print(f"Request #{item_id}: Error, Status = {response.status_code}")

        return response.status_code

    except requests.exceptions.RequestException as e:
        print(f"Request #{item_id}: Connection error - {e}")
        return None

def main():
    print("=" * 60)
    print("Starting request service...")
    print(f"Target URL: {SERVICE_URL}")
    print("Sending requests with random intervals (0-5 seconds)")
    print("=" * 60)

    item_id = 1

    while True:
        send_request(item_id)
        item_id += 1
        delay = random.uniform(0, 5)
        time.sleep(delay)

if __name__ == "__main__":
    main()
