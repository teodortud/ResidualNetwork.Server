import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time


def mqtt_publish(result):
    broker = "192.168.43.215"

    client = mqtt.Client()
    print("Connect to broker", broker)

    client.connect(broker, 1883, 60)

    client.publish("prediction", result)

    client.disconnect()

