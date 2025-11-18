# Email_Sent/tasks.py
from celery import shared_task
import time

@shared_task
def send_welcome_email(user_id):
    print('(-)'*30)
    print("Sleep for 5 seconds")
    time.sleep(5)
    print('(-)'*30)
    print('send_welcome_email')
    print(f"User ID: {user_id}\n" * 10)
    pass


