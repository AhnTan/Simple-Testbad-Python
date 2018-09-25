import paho.mqtt.client as mqtt
import time

# set broker ip address
ip = "192.168.50.5"
#ip = "192.168.0.23"
# set client number
num = 150
# set topic
topic = "WL"
# total message recv broker
total = 0

def on_message(client, userdata, message):
    global total
    total = total + 1
    if(str(message.payload) == str("normal message") or str(message.payload) == str("urgent message")):
    	print(str(message.payload))
    if total % 180 == 0:
        print("Total Message recv Broker #" + str(int(total/180)) + " : " + str(total) + " \n")
    
for i in range(0,num):
    client = mqtt.Client("Workload_Sub_" + str(i))
    client.connect(ip)
    client.subscribe(topic)
    if i == 90:
        client.on_message = on_message
    client.loop_start()

while(True):
	time.sleep(1)


