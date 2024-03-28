import network
import time
import urandom
from umqtt.simple import MQTTClient

mqtt_client_identifier = "NS8OMCEaHiERHRcULzsoKCM"
mqtt_username = "NS8OMCEaHiERHRcULzsoKCM"
mqtt_secret = "4Y0oYJFwZdgptBFyaRApEw1N"
mqtt_host = "mqtt3.thingspeak.com"
mqtt_connection_port = 1883
topic_temperature = "channels/2488510/publish/fields/field1"
topic_humidity = "channels/2488510/publish/fields/field2"
topic_co2_level = "channels/2488510/publish/fields/field3"

wifi_network_name = "Wokwi-GUEST"
wifi_network_password = ""

def create_sensor_data():
    temp_data = urandom.uniform(-50, 50)
    humidity_data = urandom.uniform(0, 100)
    co2_data = urandom.uniform(300, 2000)
    return temp_data, humidity_data, co2_data

def send_data_to_thingspeak(temp, humidity, co2):
    mqtt_client = MQTTClient(mqtt_client_identifier, mqtt_host, user=mqtt_username, password=mqtt_secret)
    mqtt_client.connect()
    mqtt_client.publish(topic_temperature, str(temp))
    mqtt_client.publish(topic_humidity, str(humidity))
    mqtt_client.publish(topic_co2_level, str(co2))
    mqtt_client.disconnect()

wifi_interface = network.WLAN(network.STA_IF)
wifi_interface.active(True)
wifi_interface.connect(wifi_network_name, wifi_network_password)

while not wifi_interface.isconnected():
    pass

print("Successfully connected to WiFi!")

while True:
    temp, humidity, co2 = create_sensor_data()
    send_data_to_thingspeak(temp, humidity, co2)
    print(f"Data Published: Temperature={temp:.2f}C, Humidity={humidity:.2f}%, CO2={co2:.2f}ppm")
    time.sleep(10)
  