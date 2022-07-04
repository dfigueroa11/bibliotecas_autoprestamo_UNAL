from MQTTconnection import *

class Communications:
        
    
    def __init__(self):

        # WLAN network
        net_name = "UNAL"
        net_password = ""

        conect_to(net_name,net_password)

        try:
            self.client = connect_and_subscribe()
            self.localID='2'
            self.ticket=0 # Current ticket
            self.last_topic='SI/Petition'
            self.last_message={"LocalID":"2"}
            self.pending_incoming_message=False
            self.last_pending=False
        except OSError as e:
            restart_and_reconnect()

    def check_message(self):
        self.client.check_msg()
    
    def receive(self):
        topic, message = getValues()
        if self.pending_incoming_message==False and  self.pending_incoming_message!=self.last_pending:
            self.last_topic=str(topic,'utf-8')
            self.last_message=message
        if (str(topic,'utf-8')!= self.last_topic) or (message!=self.last_message):
            self.pending_incoming_message=True
        self.last_pending=self.pending_incoming_message
        return topic, message, self.pending_incoming_message

    def send(self, topic, ID_user ='', ID_book ='', current_use=''):
        data={'LocalID':self.localID,
            'group': 2
            }
        if topic=='Bibliotecas/Validate_user':
            data={
            'LocalID':self.localID,
            'id': ID_user
            }
            self.client.publish(topic, json.dumps(data),True,1)
        if topic=='Bibliotecas/Validate_book':
            data={
            'LocalID':self.localID,
            'id': ID_book
            }
            self.client.publish(topic, json.dumps(data),True,1)
        elif topic=='Bibliotecas/Give_back':
            data={
            'LocalID':self.localID,
            'id': ID_book
            'current_use':current_use
            }
            self.client.publish(topic, json.dumps(data),True,1)
        elif topic=='Bibliotecas/Borrow':
            data={
            'LocalID':self.localID,
            'id_user': ID_user
            'id_book': ID_book

            }
            self.client.publish(topic, json.dumps(data),True,1)
        elif topic=='SI/Petition':
            print('Loop SI availability secured', '\n')
            self.client.publish('SI/Petition', json.dumps(data),True,1)
        else:
            print('Misstyped topic')
        

    def sendTest(self):

        last_publish_time = 0
        message_interval = 2
        received = True
    
        myMsg={
            'LocalID':'2',
            'ID': '101006'
            }
    
        while True:
          try:
            #client.check_msg()
            if (time.time() - last_publish_time) > message_interval:
                if received:
                    self.client.publish('SI/Petition', json.dumps(myMsg),True,1)
                    received = False
                else:
                 #   client.check_msg()
                    received = True
                last_publish_time = time.time()
          except OSError as e:
            restart_and_reconnect()
