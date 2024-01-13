from datetime import date, datetime

result = dict()

def get_user_date(user):
    return user['birthday']

def get_date_year(some_date):
            l = str(some_date).split('-')
            current_year = l[0]
            return current_year 

def get_date_month(some_date):
            l = str(some_date).split('-')
            current_month = l[1]
            return current_month

def get_date_day(some_date):
            l = str(some_date).split('-')
            current_day = l[2]
            return current_day

def convert_user_date(user):
    today_date = date.today()

    birthday_user_date = get_user_date(user)
    birthday_user_moth = int(get_date_month(some_date=user['birthday']))
    current_year = int(get_date_year(today_date))
    if  birthday_user_moth == 12:
        user_date = birthday_user_date.replace(year=current_year)
    else: 
        user_date = birthday_user_date.replace(year=current_year+1)
    print('user_date', user_date)
    return user_date
     
def delta_days(user_date, today_date):
    delta_days = int((user_date - today_date).total_seconds())//(24*60*60)
    abs_delta_days = delta_days if delta_days >= 0 else -delta_days
    return abs_delta_days

result=dict()
names_0, names_1, names_2, names_3, names_4 = list(), list(), list(), list(), list()

def get_birthdays_per_week(users):
    today_date = date.today()
    
    if users == list():
       return result 
    else:
        for user in users:
            print(user)
        
            for k, v in user.items():
                print(k, v)         
                user_date = convert_user_date(user)
                print(user_date)
                user_weekday = int(convert_user_date(user).weekday())
                print(user_weekday)
                abs_delta_days = delta_days(user_date, today_date)
                print('abs_delta_days', abs_delta_days)
            if user_date < today_date:
                if abs_delta_days <=2 and (user_weekday == 5 or user_weekday == 6):
                    names_0.append(user['name'])
                    print('names_0', names_0)
            else:
                if abs_delta_days <=6:         
                    if user_weekday == 0:
                        names_0.append(user['name'])
                        print('names_0', names_0)
                    if user_weekday == 1:
                        names_1.append(user['name'])
                        print('names_1', names_1)
                    if user_weekday == 2:
                        names_2.append(user['name'])
                        print('names_2', names_2)
                    if user_weekday == 3:
                        names_3.append(user['name'])
                        print('names_3', names_3)
                    if user_weekday == 4:
                        names_4.append(user['name'])
                        print('names_4', names_4)
                    if user_weekday == 5:
                        names_0.append(user['name'])
                    if user_weekday == 6:
                        names_0.append(user['name'])
                           #print('names_4', names_4)
            if names_0:
                result['Mon'] = names_0
            if names_1:
                result['Tue'] = names_1
            if names_2:
                result['Wed'] = names_2
            if names_3:
                result['Thu'] = names_3
            if names_4:
                result['Fri'] = names_4
     
    return result

    # Реалізуйте тут домашнє завдання
    


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
