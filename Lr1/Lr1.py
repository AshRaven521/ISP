def fib_numbers(input_number):
    fib_number1 = 1
    fib_number2 = 2
    if input_number < 3:
        raise Exception
    print(fib_number1, fib_number2, end=" ")
    for i in range(3,input_number+1):
        print(fib_number1+fib_number2, end=" ")
        #В fib_number2 хранится последнее число, для записи в него следующего запишем его нынешнее значение в fib_number1, а текущее значение fib_number1 в temp
        temp = fib_number1
        fib_number1 = fib_number2
        fib_number2 = temp+fib_number1
    print()
    
#Для осуществления повторного ввода при ошибке
while True:
    try:
        user_input = int(input("Введите количество чисел Фибоначчи:"))
        fib_numbers(user_input)
        break
    except:
        print("Неправильный ввод!")