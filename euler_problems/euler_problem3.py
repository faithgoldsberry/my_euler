

my_number= 600851475143

def find_factors(big_number):
    list_factors= []
    for number in range(1,big_number):
        if big_number % number == 0:
            list_factors.append(number)
    return list_factors

def is_prime(big_number):
    list_factors= []
    for number in range(1,big_number):
        if big_number % number == 0:
            list_factors.append(number)
    return list_factors == [1, big_number]

print(find_factors(my_number))
