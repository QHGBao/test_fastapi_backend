import requests
import threading

URL = "http://127.0.0.1:8000/predict"

data = {
    "area": 80,
    "rooms": 3
}

def send_request():
    res = requests.post(URL, json=data)
    print(res.json())

threads = []

# tạo 100 request cùng lúc
for i in range(100):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

# chờ tất cả chạy xong
for t in threads:
    t.join()