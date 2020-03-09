import paho.mqtt.client as mqtt


def mqtt_publish(prediction):
    client = mqtt.Client()

    client.connect("localhost", 1883, 60)

    client.publish("server/network-prediction", prediction)

    client.disconnect()
