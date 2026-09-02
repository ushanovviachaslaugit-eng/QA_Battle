def is_even(number):
    return number %2 ==0 #проверяет четность
pass
def max_of_two(a,b):
    if a>b:
        return a
    else: return b
pass
def greet(name):
    print("Привет, ",name,"!")

print("10 чётное?", is_even(10))
print("7 чётное?", is_even(7))

print("Наибольшее из 15 и 8:", max_of_two(15, 8))
print("Наибольшее из 3 и 9:", max_of_two(3, 9))

greet("Анна")
greet("Иван")