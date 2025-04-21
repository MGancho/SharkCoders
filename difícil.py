list = [

]
numbers = input("crie uma lista de números: ")
list.append(numbers)

length = len(numbers)
if numbers[0] == numbers[length - 1]:
    print("deu")
else:
    print("n deu")

