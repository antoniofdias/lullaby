def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected!")
    else:
        print("Bad connection!")

def on_log(client, userdata, level, buf):
    print("Log: " +  buf)

def on_disconnect(client, userdata, flags, rc):
    print("Disconnected! Result code: " + rc)
