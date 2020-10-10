from utils import *

last_update_id = get_last_update_id()

update_id = last_update_id

while True:
    try:
        chat_id,first_name,last_name,text = get_detel_of_one_update_id(update_id)
        if text == '/start':
            #insert to db
            create_at = int(time.time())

            update_id = update_id
            chat_id = chat_id
            first_name = first_name
            last_name = last_name
            text = text
            create_at = create_at
            review_time_1 = create_at + 24*3600
            is_send_1 = 0
            review_time_2 = create_at + 7*24*3600
            is_send_2 = 0
            review_time_3 = create_at + 2*7*24*3600
            is_send_3 = 0
            review_time_4 = create_at + 30*24*3600
            is_send_4 = 0
            review_time_5 = create_at + 3*30*24*3600
            is_send_5 = 0

            instance = Message(update_id = update_id,chat_id = chat_id,first_name = first_name,last_name = last_name,text = text,create_at = create_at,review_time_1 = review_time_1,is_send_1 = is_send_1,review_time_2 = review_time_2,is_send_2 = is_send_2,review_time_3 = review_time_3,is_send_3 = is_send_3,review_time_4 = review_time_4,is_send_4 = is_send_4,review_time_5 = review_time_5,is_send_5 = is_send_5)
            instance.save()
        else:
            msg_res = 'Chào mừng bạn đến với bot nhắc nhở bạn học một cái gì đó.\n Như các bạn đã biết, việc ôn lại là rất quan trọng cho quá trình hình thành trí nhớ dài hạn (spaced repetition).\n Bot này ra đời để nhắc bạn học vào 1 ngày, 1 tuần, 2 tuần, 1 tháng, 3 tháng sau khi bạn học một cái gì đó, chúng tôi sẽ nhắc lại để bạn nhớ nhé =))'
            send_message(chat_id,msg_res)

        #increase update_id
        update_id = update_id+1
    except:
        pass