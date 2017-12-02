import requests
import json
import os.path

pricediff = 20000
tmpfile = "tmpbuy"

def writeData(data):
        file = open(tmpfile,"w+")
        file.write(str(data))
        file.close()

def readData():
        if not os.path.isfile(tmpfile):
                writeData("0")
        file = open(tmpfile, "r")
        return file.read()

def sendmessage(message):
        if message != "":
                print(message)
                #make a sms api call or rest call to alert
                

request = requests.get("https://www.zebapi.com/api/v1/market/ticker/btc/inr")
data = json.loads(request.content.decode('utf-8'))
newprice = data["buy"]
oldprice = readData()
oldprice = float(oldprice)
message = ""
if oldprice - newprice > pricediff:
        message = "London bridge is falling down! :D. Current price is " + str(newprice) + "INR and Old Price is " + str(oldprice) + "INR. "+str(pricediff)+"INR Diff Set";
        oldprice = newprice
        print(message)

if newprice - oldprice > pricediff:
        message = "Boom Boom!!. Current price is " + str(newprice) + "INR and Old Price is " + str(oldprice) + "INR. "+str(pricediff)+"INR Diff Set";
        oldprice = newprice
        print(message)

writeData(newprice)
sendmessage(message)
