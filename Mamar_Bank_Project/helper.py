

class Helper:
    def get_user_transactions(user, max_transactions=int(1e5)):
        print("get_user_transactions called")
        print(user.is_superuser)
        if user.is_superuser:
            data = user.admin_transactions.all().order_by('-updated_at')[:max_transactions]
            print(data)
            return data
        return user.transactions.all().order_by('-updated_at')[:max_transactions]
    
