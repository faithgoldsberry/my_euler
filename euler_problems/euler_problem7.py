def factors(n):
    results = [ ]
    prime = [ ]
    for k in range(1,n+1):
        if n % k == 0: results.append(k)
# traditional function that computes factors # store factors in a new list
# divides evenly, thus k is a factor # add k to the list of factors
# return the entire list
    if results == [1, n]: return results

def prime_filter(x):
  if x == None:
    return False
  else:
    return True

numbers = range(100000,10000000)
result = map(factors, numbers)
primes = list(filter(prime_filter,list(result)))

num_of_primes = len(primes)
print(num_of_primes)

for x in primes:
  print(x)
