from peewee import *
import time

# host='localhost'
# db_name = 'bot_telegram'
# db_user='root'
# db_pass=''

host='45.77.36.114'
db_name = 'bot_telegram'
db_user='nghiahsgs4'
db_pass='261997'

db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)

class Message(Model):
    update_id = CharField()
    chat_id = CharField()
    first_name = CharField()
    last_name = CharField()
    text = CharField()

    create_at = IntegerField()
    review_time_1 = IntegerField() # 1 ngay sau
    is_send_1 = IntegerField()
    review_time_2 = IntegerField() # 1 tuan sau
    is_send_2 = IntegerField()
    review_time_3 = IntegerField() # 2 tuan sau
    is_send_3 = IntegerField()
    review_time_4 = IntegerField() # 1 thang sau
    is_send_4 = IntegerField()
    review_time_5 = IntegerField() # 3 thang sau
    is_send_5 = IntegerField()

    class Meta:
        database=db

if __name__=="__main__":
    Message.create_table()