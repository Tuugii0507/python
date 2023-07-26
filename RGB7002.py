# Өгөгдсөн гурвалжны периметрийг ол.

# Input
# Гурвалжны талууд бүхэл тоогоор нэг мөрөнд зайгаар тусгаарлагдан өгөгдөнө.

# Output
# Гурвалжны периметр.

# Example
# Input:
# 3 4 5

# Output:
# 12

numbers = input().split()
number1 = int(numbers[0])
number2 = int(numbers[1])
number3 = int(numbers[2])
result = number1 + number2 + number3

if len(numbers) > 3: 
    print("sorry, do you know .gurvaljin!.")
else:
    print("периметр: " , result) 
