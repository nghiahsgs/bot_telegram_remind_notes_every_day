from utils import *
import time
from utils_db import *

while(True):
    current_time = time.time()

    list_message = Message.select()
    for message in list_message:
        if not message.is_send_1:
            if current_time > message.review_time_1:
                #send message nhac nho 1 ngay sau
                pass
        elif not message.is_send_2:
            if current_time > message.review_time_2:
                #send message nhac nho 1 tuan sau
                pass
        elif not message.is_send_3:
            if current_time > message.review_time_3:
                #send message nhac nho 2 tuan sau
                pass
        elif not message.is_send_4:
            if current_time > message.review_time_4:
                #send message nhac nho 1 thang sau
                pass
        elif not message.is_send_5:
            if current_time > message.review_time_5:
                #send message nhac nho 3 thang sau
                pass

        else:
            pass
    
    time.sleep(5*60) # 5 phut check 1 lan