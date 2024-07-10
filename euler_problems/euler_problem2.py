
list = []

def Fibonacci(number):
           if(number == 0):
                      return 0
           elif(number == 1):
                      return 1
           else:
                      return (Fibonacci(number - 2)+ Fibonacci(number - 1))

number = 1

for n in range(0, 34):
    if Fibonacci(n)%2 == 0:
           list.append((Fibonacci(n)))

print(sum(list))
