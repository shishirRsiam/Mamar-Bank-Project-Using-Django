# Email_Sent/tasks.py
from . import sent_email
from celery import shared_task
from .models import Transaction
from Accounts.models import User
from django.core.cache import cache
from .models import *
from Mamar_Bank.helper import Helper

import time

@shared_task
def account_create_task(user_id):
    user = User.objects.get(id=user_id)
    sent_email.sent_account_create_email(user)


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
def loan_approve_task(loan_id):
    loan = Loan.objects.get(id=loan_id)
    sent_email.sent_loan_approve_email(loan)

@shared_task
def daily_bonus_task(transaction_id):
    DailyBonus = Transaction.objects.get(id=transaction_id)
    sent_email.sent_daily_bonus_email(DailyBonus)


@shared_task
def change_password_task(user_id):
    user = User.objects.get(id=user_id)
    sent_email.sent_change_password_email(user)


def check_daily_bonus(user_id):
    print()

    log_file_path = 'logs/deily_check_log.txt'

    key = f"daily_bonus_{user_id}"
    user = User.objects.get(id=user_id)
    first_str = f"--> [{time.strftime('%Y-%m-%d %H:%M:%S')}] check_daily_bonus: @{user.username}: {key}"
    with open(log_file_path, 'a', encoding='utf-8') as f:
        f.write(first_str + '\n')
    print(first_str)

    if cache.get(key):
        ttl = cache.ttl(key)
        second_str = f"Daily Bonus @{user.username} already added at: {cache.get(key)} and Time Left: {int((ttl / 60) / 60)} hours {int(ttl / 60) % 60} minutes"
        print(second_str)
        with open(log_file_path, 'a', encoding='utf-8') as f:
            f.write(second_str + '\n\n')
        return False
    
    current_local_time, next_day_second_remain = Helper.get_cur_time_and_next_day_remain_second()
    cache.set(key, current_local_time.strftime('%Y-%m-%d %H:%M:%S'), next_day_second_remain)

    user.account.balance += 100
    user.account.save()
    
    DailyBonus = Transaction.objects.create(
        transaction_type='Daily Bonus', user=user, 
        amount=25, description="Daily Check Bonus", status=1,
        after_transaction_balance=user.account.balance
    )
    DailyBonus.save()


    # Sent Daily Bonus Email
    daily_bonus_task.delay(DailyBonus.id)
    # sent_email.sent_daily_bonus_email(DailyBonus)

    success_str = f"Daily Bonus @{user.username} Added Successfully!"
    with open(log_file_path, 'a', encoding='utf-8') as f:
        f.write(success_str + '\n\n')
    print(second_str)
    return True

