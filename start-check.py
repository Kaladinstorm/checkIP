import socket
import json

def readJSON():
    jsonData = json.loads(open('hostnames.json').read())
    arrayHostname = jsonData['hostname']

    for hosts in arrayHostname:
        #print(hosts)
        getIPByHostname(hosts)

def generateHostnames():
    for hostnameNumber in range(200, 300):
        print("\"pconvm", hostnameNumber, "\",", sep="")
    

def getIPByHostname(host):
    try:
        hostName = host
        hostIP = socket.gethostbyname(hostName)
        print("{ \"", host, "\":\"", hostIP, "\" }", sep="")
    except:
        print("{ \"", host, "\":\"Unable to get IP\" }", sep="")

#getIPByHostname()
readJSON()
#generateHostnames()