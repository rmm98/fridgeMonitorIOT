import conf,time,json
from boltiot import Bolt,Email

mybolt = Bolt(conf.boltApiKey,conf.deviceId)
email = Email(conf.mailgunApiKey,conf.sandboxUrl,conf.sender,conf.receiver)

min = 9.2
max = 10

while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    sv = int(data["value"])
    temp = (100*sv)/1024
    print("The temperature is ",temp)
    if temp < min:
        print("The temperature is lower than ",min)
        print("Sending Email request")
        response = email.send_email("Alert","The temperature is "+str(temp))
        print("Mailgun response: ",response.text)
    elif temp > max:
        print("The temperature is greater than ",max)
        print("Sending Email request")
        response = email.send_email("Alert","The temperature is "+str(temp))
        print("Mailgun response: ",response.text)
    time.sleep(10)