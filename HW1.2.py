# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


def converter(seconds):
    seconds = seconds % (24 * 3600)


    hours = seconds // 3600   #В часе 3600 секунд
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d:%d" % (hours, minutes, seconds)


user_seconds=int(input("Введите количество секунд, которое мы преобразуем во время в формате 'чч:мм:сс'"))

print(converter(user_seconds))

#Стоит отметить что программа будет не совсем корректно работать если секунд больше 86400




#Попробовал найти альтернативное решение, которое будет дополнять основное и уже учитывать дни.

def true_converter(seconds):

    min, sec = divmod(seconds, 60)
    hours, min = divmod(min, 60)
    days, hours = divmod(hours,24)
    return "%02d дней. %02d:%02d:%02d" % (days, hours, min, sec)

user_second=int(input("Введите количество секунд, которое мы преобразуем во время в формате 'дд. чч:мм:сс'"))

print(true_converter(user_second))