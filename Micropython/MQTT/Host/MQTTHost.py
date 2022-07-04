import time
import json
import paho.mqtt.client as paho
from paho import mqtt

usersID=[b"101006",b"100743"]

for x in range(len(usersID)):
    usersID[x-1] = usersID[x-1].decode('utf8').replace("'", '"')

usersData={
    "LocalID":"1",
    "Registered": True,
    "Name":"Maria",
    "Rol":"Estudiante"
    }

def extract_dict_data(dictionary, key='LocalID'): # Key is a string
    result=[]
    for x in range(len(list(dictionary.items()))):
        if list(dictionary.items())[x-1][0]==key:
            result=list(dictionary.items())[x-1]
    return result

def on_connect(client, userdata, flags, rc, properties=None): # rc=0 means everything is right, else do worry
    print("Connected with result code "+str(rc))

def on_publish(client, userdata, mid, properties=None): # Succesfully published
    print("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
  #  print("Received: "+msg.topic+" "+str(msg.payload))
    message=json.loads(msg.payload)
    print('Received: ' + str(list(message.items())) + '. On topic: ' + msg.topic)
    try:
        externalID=extract_dict_data(message,'LocalID')[1]
    except IndexError as e:
        print('Error: message contains no local ID')
        print('I give up')
        pass
    #print ('Reading LocalID: ' + str(extract_dict_data(message,'LocalID')[1]))
    if externalID!=str(1):
        if msg.topic=='SI/Petition':
            data={"LocalID":"1"}
            client.publish(msg.topic, json.dumps(data),True,1)
            print('Sent: ', data, '. Topic: ', msg.topic, '\n')
        
        elif msg.topic=='Bibliotecas/Validate_user':
            try:
                user=message["user"]
                data={"IDcarne" : "0x99dc293c",
                    "cedula": "123456789",
                    "IDlibro_prestado": "1234567890",
                    "user_type": "Estudiante",
                    "clave": "asdf123"
                      }
                client.publish(msg.topic, json.dumps(data),True,1)
            except KeyError as e:
                print('Error: message contains no user')
                print('I give up')
                pass
            print('Sent: ', usersData, '. Topic: ', msg.topic, '\n')

        elif msg.topic=='Bibliotecas/Validate_book':
            try:
                book=message["book"]
                data={"IDlibro": "0x99dc293c",
                    "name": "Hola",
                    "current_use" : "False"
                      }
                client.publish(msg.topic, json.dumps(data),True,1)
            except KeyError as e:
                print('Error: message contains no book')
                print('I give up')
                pass
            print('Sent: ', usersData, '. Topic: ', msg.topic, '\n')
            
    else:
        print('I dont really care \n')
        

client = paho.Client()
client.on_connect = on_connect
client.connect("broker.hivemq.com", 1883,60)

client.on_subscribe = on_subscribe
client.on_message = on_message
#client.on_publish = on_publish

# subscribe 
client.subscribe("SI/Petition", qos=1)
client.subscribe("Bibliotecas/#", qos=1)

client.loop_start()


while True:
    client.on_message = on_message 