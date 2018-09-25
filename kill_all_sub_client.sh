sudo kill -9 `ps -ef | grep mosquitto_sub* | awk '{print $2}'`
