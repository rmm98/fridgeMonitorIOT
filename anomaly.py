import conf,time,json,math,statistics
from boltiot import Bolt,Email

mybolt = Bolt(conf.boltApiKey,conf.deviceId)
email = Email(conf.mailgunApiKey,conf.sandboxUrl,conf.sender,conf.receiver)

frame = 10
factor = 6
history = []

def computeBounds(history,frame,factor):
    if len(history) < frame:
        return None
    if len(history) > frame:
        del history[0:len(history)-frame]
    mn = statistics.mean(history)
    variance = 0
    for data in history:
        variance += math.pow((data-mn),2)
    z = factor * math.sqrt(variance/frame)
    high = history[frame-1] + z
    low = history[frame-1] - z
    return [high,low]

while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    sv = int(data["value"])
    temp = (100*sv)/1024
    print("The temperature is ",temp)

    bounds = computeBounds(history,frame,factor)
    if not bounds:
        rdc = frame - len(history)
        print("Not enough data to compute Z-score. Need",rdc,"more data points.")
        history.append(temp)
        time.sleep(10)
        continue
        
    if temp < bounds[1]:
        print("Someone has opened the Fridge door")
        print("Sending Email request")
        response = email.send_email("Someone has opened the Fridge door","The temperature is "+str(temp))
        print("Mailgun response: ",response.text)

    elif temp > bounds[0]:
        print("Someone has opened the Fridge door")
        print("Sending Email request")
        response = email.send_email("Someone has opened the Fridge door","The temperature is "+str(temp))
        print("Mailgun response: ",response.text)

    time.sleep(10)