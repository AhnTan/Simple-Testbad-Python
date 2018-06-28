# 워크로드 구독자 위에쉘
# 쉘에서 컨트롤 에프6 이 종료
# 스크립트에서 에프5가 시작
import paho.mqtt.client as mqtt
import time

# set broker ip address
ip = "192.168.43.193"
#ip = "192.168.0.23"
# set client number
num = 100
# set topic
topic = "WL"
# total message recv broker
total = 0

def on_message(client, userdata, message):
    global total
    total = total + 1
    if total % 180 == 0:
        print("Total Message recv Broker #" + str(int(total/180)) + " : " + str(total) + " \n")
    
for i in range(0,num):
    client = mqtt.Client("Workload_Sub_" + str(i))
    client.connect(ip)
    client.subscribe(topic)
    if i == 90:
        client.on_message = on_message
    client.loop_start()
    if i % 10 == 0 and i != 0:
        time.sleep(1)


