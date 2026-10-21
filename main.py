from datetime import datetime, timedelta
import random
import re




def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        difference = current_date - given_date
        return difference.days
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат РРРР-ММ-ДД.")
        return None




def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max:
        return []
    if quantity < 1 or quantity > max - min + 1:
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)




def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    if phone_number.startswith("+"):
        return phone_number
    if phone_number.startswith("380"):
        return "+" + phone_number
    return "+38" + phone_number




def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Отримуємо дату народження
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # День народження в поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо найближчі 7 днів
        days_difference = (birthday_this_year - today).days

        if 0 <= days_difference <= 7:
            congratulation_date = birthday_this_year

            # Переносимо вихідні на понеділок
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays




def main():
    # ------------------ Завдання 1 ------------------ 
    print(get_days_from_today("2022-02-24"))

    # ------------------ Завдання 2 ------------------
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

    # ------------------ Завдання 3 ------------------
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
    
    # ------------------ Завдання 4 ------------------
    users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)

if __name__ == "__main__":
    main()