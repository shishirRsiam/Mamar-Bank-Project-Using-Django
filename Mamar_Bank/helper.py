from django.utils import timezone


class Helper:
    def get_user_transactions(user, max_transactions=int(1e5)):
        print("get_user_transactions called")
        print(user.is_superuser)
        if user.is_superuser:
            data = user.admin_transactions.all().order_by('-updated_at')[:max_transactions]
            print(data)
            return data
        return user.transactions.all().order_by('-updated_at')[:max_transactions]
    
    def get_cur_time_and_next_day_remain_second():
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
