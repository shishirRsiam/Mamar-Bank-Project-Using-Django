# Email_Sent/tasks.py
from . import sent_email
from celery import shared_task
from .models import Transaction
from Accounts.models import User
from django.core.cache import cache
from .models import *
from Mamar_Bank_Project.helper import Helper

@shared_task
def send_welcome_email(user_id):
    return True




@shared_task
def loan_task(loan_id):
    loan = Loan.objects.get(id=loan_id)
    sent_email.sent_loan_request_email_to_user(loan)
    sent_email.sent_loan_request_email_to_admin(loan)


@shared_task
def withdrawal_task(transaction_id):
    withdrawal = Transaction.objects.get(id=transaction_id)
    sent_email.sent_withdow_confirmation_email(withdrawal)
    return True

@shared_task
def deposit_task(transaction_id):
    deposit = Transaction.objects.get(id=transaction_id)
    sent_email.sent_deposit_confirmation_email(deposit)

@shared_task
def transfer_task(sent_money_id, received_money_id):
    SentMoney = B2B.objects.get(id=sent_money_id)
    ReceiveMoney = B2B.objects.get(id=received_money_id)

    sent_email.sent_sent_money_confirmation_email(SentMoney)
    sent_email.sent_receive_money_confirmation_email(ReceiveMoney)
    # sent_email.sent_transfer_confirmation_email(transfer)

@shared_task
def loan_approve_task(transaction_id):
    loan_payment = Transaction.objects.get(id=transaction_id)
    # sent_email.sent_loan_payment_confirmation_email(loan_payment)


@shared_task
def daily_bonus_task(transaction_id):
    DailyBonus = Transaction.objects.get(id=transaction_id)
    sent_email.sent_daily_bonus_email(DailyBonus)

def check_daily_bonus(user_id):
    print()

    key = f'daily_bonus_{user_id}'
    print(f"check_daily_bonus: {user_id}")
    if cache.get(key):
        print("Daily Bonus Already Added!")
        print("Bonus Added At:", cache.get(key))
        return
    
    current_local_time, next_day_second_remain = Helper.get_cur_time_and_next_day_remain_second()
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
    daily_bonus_task.delay(DailyBonus.id)
    # sent_email.sent_daily_bonus_email(DailyBonus)

    print("Daily Bonus Added Successfully!")