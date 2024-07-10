#sum of the squares of the first ten natural numbers

thislist = []
for x in range(1,101):
    x *=x
    thislist.append(x)

sum_of_squares=sum(thislist)

print(sum_of_squares)

#square of the sum of the first ten natural numbers

thislist = []
for x in range(1,101):
    thislist.append(x)

square_of_sum=sum(thislist)*sum(thislist)

print(square_of_sum)

difference=square_of_sum-sum_of_squares

print(difference)
