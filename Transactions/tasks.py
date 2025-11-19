# Email_Sent/tasks.py
import time
from . import sent_email
from celery import shared_task
from .models import Transaction
from Accounts.models import User
from django.utils import timezone
from django.core.cache import cache

@shared_task
def send_welcome_email(user_id):
    print('(-)'*30)
    print("Sleep for 5 seconds")
    time.sleep(5)
    print('(-)'*30)
    print('send_welcome_email')
    print(f"User ID: {user_id}\n" * 10)
    return True

def get_next_day_remain_minute():
    # 1. Get the current local timezone-aware time
    current_utc_time = timezone.now()
    current_local_time = current_utc_time.astimezone(timezone.get_current_timezone())

    # 2. Get 12:00 AM (midnight) for the current day
    # The .date() method extracts the date part (2025-11-18)
    # The .time() method sets the time to 00:00:00.000000
    midnight_local = current_local_time.replace(hour=0, minute=0, second=0, microsecond=0)

    # 3. Calculate the time difference (timedelta)
    time_difference_in_minute = current_local_time - midnight_local
    print('current_local_time:', time_difference_in_minute)

    # 4. Convert the timedelta to total minutes
    minutes_since_midnight = time_difference_in_minute.total_seconds() / 60

    day_in_minute = 24 * 60
    next_day_minute_remain = day_in_minute - minutes_since_midnight
    print('next_day_minute_remain:', next_day_minute_remain)
    return current_local_time, int(next_day_minute_remain * 60)




def check_daily_bonus(user_id):
    print()

    key = f'daily_bonus_{user_id}'
    print(f"check_daily_bonus: {user_id}")
    if cache.get(key):
        print("Daily Bonus Already Added!")
        print("Bonus Added At:", cache.get(key))
        return
    
    current_local_time, next_day_second_remain = get_next_day_remain_minute()
    cache.set(key, current_local_time, next_day_second_remain)

    user = User.objects.get(id=user_id)
    user.account.balance += 100
    user.account.save()
    
    DailyBonus = Transaction.objects.create(
        transaction_type='Daily Bonus', user=user, 
        amount=100, description="Daily Check Bonus", status=1,
        after_transaction_balance=user.account.balance
    )
    DailyBonus.save()



    # Sent Daily Bonus Email
    sent_email.sent_daily_bonus_email(DailyBonus)

    print("Daily Bonus Added Successfully!")