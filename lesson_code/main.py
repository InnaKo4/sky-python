from pin import check_pin
print("Введите ваш ПИН-код")
user_input = input()
if check_pin(user_input) == True:
     print("Такой ПИН-код подходит")
else:
     print("Такой ПИН-код не подходит")

     