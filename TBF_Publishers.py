# 워크로드 발행자 위에 쉘
# 쉘에서 컨트롤 에프6 이 종료
# 스크립트에서 에프5가 시작
import paho.mqtt.client as mqtt
import time

# set broker ip address
ip = "192.168.0.54"
#ip = "192.168.0.53"
#ip = "192.168.0.23"
# set client number
num = 50
# client array
client = []
# set topic
topic = "work/load"
# total message send broker
total = 0

for i in range(0, num):
    client.append(mqtt.Client("Workload_Pub_"+str(i)))
    client[i].connect(ip)

print("All publishers connected. \n")

while(True):
    for i in range(0, num):
        client[i].publish(topic,"N" , qos = 0)
    total = total + num
    print("Total Message send Broker #" + str(int(total/180)) + " : " + str(total) + " \n")
    time.sleep(0.1)
