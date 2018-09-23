import paho.mqtt.client as mqtt
import time

# set broker ip address
ip = "192.168.50.5"
#ip = "192.168.0.53"
#ip = "192.168.0.23"
# set client number
num = 150
# client array
client = []
# set topic
topic = "WL"
# total message send broker
total = 0

for i in range(0, num):
    client.append(mqtt.Client("Workload_Pub_"+str(i)))
    client[i].connect(ip)

print("All publishers connected. \n")

for j in range(0, 999999):
    for i in range(0, num):
        client[i].publish(topic,"N" , qos = 1)
    total = total + num
    print("Total Message send Broker #" + str(int(total/180)) + " : " + str(total) + " \n")
    time.sleep(1)
