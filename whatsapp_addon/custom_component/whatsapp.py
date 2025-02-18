import requests, os
from url_normalize import url_normalize

whatsapp_hostname = os.getenv('WHATSAPP_HOSTNAME')
whatsapp_port = os.getenv('WHATSAPP_PORT')

if whatsapp_port is None :
	HOST = f'http://{whatsapp_hostname}:3000/'
else :
	HOST = f'http://{whatsapp_hostname}:{whatsapp_port}/'

print (HOST, "is the hostname used in the python script") 

class Whatsapp:
    def send_message(self, data):
        return requests.post(url_normalize(f'{HOST}/sendMessage'), json=data).content == 'OK'

    def set_status(self, data):
        return requests.post(url_normalize(f'{HOST}/setStatus'), json=data).content == 'OK'

    def presence_subscribe(self, data):
        return requests.post(url_normalize(f'{HOST}/presenceSubscribe'), json=data).content == 'OK'

    def send_presence_update(self, data):
        return requests.post(url_normalize(f'{HOST}/sendPresenceUpdate'), json=data).content == 'OK'

    def send_infinity_presence_update(self, data):
        return requests.post(url_normalize(f'{HOST}/sendInfinityPresenceUpdate'), json=data).content == 'OK'
