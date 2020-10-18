from utils import *
import time
from utils_db import *

while(True):
    current_time = time.time()
    print('check list message in db')
    list_message = Message.select()
    for message in list_message:
        chat_id = message.chat_id
        msg_res = message.text
        if not message.is_send_1:
            if current_time > message.review_time_1:
                #send message nhac nho 1 ngay sau
                ky_ten = "Đây là tin nhắc nhắc bạn sau 1 ngày bạn tạo ghi chú !"
                msg_res = "%s\n%s"%(msg_res,ky_ten)
                send_message(chat_id,msg_res)
                message.is_send_1 = 1
                message.save()
        
        elif not message.is_send_2:
            if current_time > message.review_time_2:
                #send message nhac nho 1 tuan sau
                ky_ten = "Đây là tin nhắc nhắc bạn sau 1 ngày bạn tạo ghi chú !"
                msg_res = "%s\n%s"%(msg_res,ky_ten)
                send_message(chat_id,msg_res)
                message.is_send_2 = 1
                message.save()
        
        elif not message.is_send_3:
            if current_time > message.review_time_3:
                #send message nhac nho 2 tuan sau
                ky_ten = "Đây là tin nhắc nhắc bạn sau 2 tuần bạn tạo ghi chú !"
                msg_res = "%s\n%s"%(msg_res,ky_ten)
                send_message(chat_id,msg_res)
                message.is_send_3 = 1
                message.save()
        
        elif not message.is_send_4:
            if current_time > message.review_time_4:
                #send message nhac nho 1 thang sau
                ky_ten = "Đây là tin nhắc nhắc bạn sau 1 tháng bạn tạo ghi chú !"
                msg_res = "%s\n%s"%(msg_res,ky_ten)
                send_message(chat_id,msg_res)
                message.is_send_4 = 1
                message.save()
        
        elif not message.is_send_5:
            if current_time > message.review_time_5:
                #send message nhac nho 3 thang sau
                ky_ten = "Đây là tin nhắc nhắc bạn sau 3 tháng bạn tạo ghi chú !"
                msg_res = "%s\n%s"%(msg_res,ky_ten)
                send_message(chat_id,msg_res)
                message.is_send_5 = 1
                message.save()

        else:
            pass
    
    time.sleep(30*60) # 30 phut check 1 lan