from datetime import date, datetime

def convert_user_date(user): # перетворюємо дату народження користувача у дату в поточному році
    today_date = date.today()

    birthday_user_date = user['birthday']
    birthday_user_moth = int(birthday_user_date.month)
    current_year = int(today_date.year)
    if  birthday_user_moth == 12: # якщо дата народження припадає ще на цей рік
        user_date = birthday_user_date.replace(year=current_year)
    else:   # якщо дата народження припадає вже на наступний рік, дні якого розпочнуться поточного тижня
        user_date = birthday_user_date.replace(year=current_year+1)
    return user_date

def get_birthdays_per_week(users):
    result=dict()
    names_0, names_1, names_2, names_3, names_4 = list(), list(), list(), list(), list() #у ці списки будемо заносити користувачів залежно від дня - пон, вівт, сер, четв чи п'ятн 
    today_date = date.today() #визначаємо поточну дату
    
    if users == list(): #для порожнього списку користувачів повертаємо порожній словник
       return result 
    else:
        for user in users:           
            user_date = convert_user_date(user)
            user_weekday = int(convert_user_date(user).weekday()) #визначаємо день тижня дати народження користувача 
            delta_days = int(abs(user_date - today_date).days) #визначаємо додатню кількість днів від поточної дати до дати народження користувача
        
            if user_date < today_date: # у разі якщо дата народження користувача вже минула
                if (delta_days <=2 and user_weekday == 5 or user_weekday == 6): # то різниця із поточною датою не може бути більше двох днів
                # - значить, його день народження був у минулу суботу чи неділю
                    names_0.append(user['name'])
            else: # якщо дата народження користувача буде у майбутньому
                if delta_days <=6: #то це не більше, ніж 6 днів уперед        
                    if user_weekday == 0 or user_weekday == 5 or user_weekday == 6: #якщо ця дата припадає на понеділок, суботу, чи неділю
                        names_0.append(user['name']) #то ім'я користувача заноситься у список понеділка
                    if user_weekday == 1: #решта користувачів заносяться у списки свого дня тижня - вівторка, середи, четверга чи п'ятниці
                        names_1.append(user['name'])
                    if user_weekday == 2:
                        names_2.append(user['name'])
                    if user_weekday == 3:
                        names_3.append(user['name'])
                    if user_weekday == 4:
                        names_4.append(user['name'])
                    
            if names_0: #заповнюємо словник із результатами - списками імен користувачів у цей день
                result['Monday'] = names_0
            if names_1:
                result['Tuesday'] = names_1
            if names_2:
                result['Wednesday'] = names_2
            if names_3:
                result['Thursday'] = names_3
            if names_4:
                result['Friday'] = names_4
  
    return result

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
