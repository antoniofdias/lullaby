import paho.mqtt.client as mqtt
import mqtt_methods

host = "127.0.0.1"
port = 1883

client = mqtt.Client()
client.on_connect = mqtt_methods.on_connect
client.on_disconnect = mqtt_methods.on_disconnect

try:
    client.connect(host, port)
except:
    print("Error has ocurred!")
    exit()