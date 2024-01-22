from datetime import date, datetime

def convert_user_date(user):
    today_date = date.today()
    current_year = int(today_date.year)
    
    birthday_user_date = user['birthday']
    birthday_user_moth = int(birthday_user_date.month)
    
    if  birthday_user_moth == 12:
        user_date = birthday_user_date.replace(year=current_year)
    else: 
        user_date = birthday_user_date.replace(year=current_year+1)
    return user_date

def get_birthdays_per_week(users):
    result=dict()
    names_0, names_1, names_2, names_3, names_4 = list(), list(), list(), list(), list()
    today_date = date.today()
    
    if users == list():
       return result 
    else:
        for user in users:
           
            user_date = convert_user_date(user)
            user_weekday = int(convert_user_date(user).weekday())
            delta_days = int(abs(user_date - today_date).days)
        
            if user_date < today_date:
                if (delta_days <=2 and user_weekday == 5 or user_weekday == 6):
                    names_0.append(user['name'])
                    print('names_0', names_0)
            else:
                if delta_days <=6:         
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
                        print('names_4', names_4)
            if names_0:
                result['Monday'] = names_0
            if names_1:
                result['Tuesday'] = names_1
            if names_2:
                result['Wednesday'] = names_2
            if names_3:
                result['Thursday'] = names_3
            if names_4:
                result['Friday'] = names_4

    print(result)   
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
