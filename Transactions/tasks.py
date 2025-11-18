# Email_Sent/tasks.py
from celery import shared_task

@shared_task
def send_welcome_email(user_id):
    print('send_welcome_email')
    print(f"User ID: {user_id}\n" * 10)
    pass


