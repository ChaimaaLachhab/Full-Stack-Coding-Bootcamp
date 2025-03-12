from datetime import datetime

def get_birthdate():
    birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
    return datetime.strptime(birthdate_str, "%d/%m/%Y")

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def print_cake(age):
    candles = age % 10
    candle_str = "i" * candles if candles > 0 else " "
    
    cake = f"""
       ___{candle_str}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
    """
    print(cake)

birthdate = get_birthdate()
age = calculate_age(birthdate)
print_cake(age)