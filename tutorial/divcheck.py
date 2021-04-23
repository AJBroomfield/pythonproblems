num = int(input("Give me a whole number: "))
div = int(input("Give me another whole number: "))


if num % div == 0:
    print(f'{num} is divisible by {div}')
else:
    print(f'{num} isn\'t divisible by {div}')
