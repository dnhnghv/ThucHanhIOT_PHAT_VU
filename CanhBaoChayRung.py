import paho.mqtt.client as mqtt
from datetime import datetime
import json
import random
import time

# Cấu hình MQTT
MQTT_BROKER = "192.168.0.103"  # Địa chỉ IP của MQTT Broker
MQTT_PORT = 1883  # Cổng MQTT (mặc định là 1883)
MQTT_TOPIC = "Phát Vũ"  # Tên topic để gửi dữ liệu
CLIENT_ID = "MQTT_client_sender"  # Tên client gửi

# Tạo client MQTT
client = mqtt.Client(CLIENT_ID)

# Kết nối đến MQTT Broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Gửi dữ liệu
try:
    while True:
        # Tạo dữ liệu ngày giờ và dữ liệu ngẫu nhiên
        data = {
            "time": datetime.now().strftime("%H:%M:%S"),  # Thời gian hiện tại
            "data": random.randint(0, 100),  # Dữ liệu ngẫu nhiên từ 0 đến 100
        }

        # Chuyển đổi dữ liệu thành JSON
        payload = json.dumps(data)

        # Gửi dữ liệu lên topic MQTT
        client.publish(MQTT_TOPIC, payload)
        print(f"Đã gửi: {payload}")

        # Chờ 2 giây trước khi gửi dữ liệu tiếp theo
        time.sleep(2)
except KeyboardInterrupt:
    print("Dừng chương trình gửi dữ liệu.")
finally:
    client.disconnect()
