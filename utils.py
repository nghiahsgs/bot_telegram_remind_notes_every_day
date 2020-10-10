import requests
import json
from high_order_framework_requests_python import utils_class

string_Interact1 = utils_class.String_Interact()
# string_Interact1

token = 'bot988642401:AAGGUoGLeqpEOCv7sP9m3Yp0-TSNIMntjNU'

def get_last_update_id():
    url = 'https://api.telegram.org/%s/getUpdates'%token
    data = requests.get(url).text

    data = json.loads(data)
    last_update_id = data['result'][-1]['update_id']
    return last_update_id

def get_detel_of_one_update_id(update_id):
    url = 'https://api.telegram.org/%s/getUpdates?offset=%s'%(token,update_id)
    data = requests.get(url).text
    data = json.loads(data)

    chat_id,first_name,last_name,text = '','','',''

    if len(data['result']):
        chat_id = data['result'][0]['message']['from']['id']
        first_name = data['result'][0]['message']['from']['first_name']
        last_name = data['result'][0]['message']['from']['last_name']
        text =  data['result'][0]['message']['text']

    return chat_id,first_name,last_name,text

def send_message(chat_id,ndung):
    # ndung = utils_class.File_Interact('code.html').read_file()
    url = 'https://api.telegram.org/%s/sendMessage?chat_id=%s&text=%s'%(token,chat_id,ndung)
    data = requests.get(url).text
    data = json.loads(data)
    return data['ok']

if __name__=="__main__":
    last_update_id = get_last_update_id()
    chat_id,first_name,last_name,text = get_detel_of_one_update_id(last_update_id)

    send_message(chat_id,text)

    #send text thuong, ko can mark down