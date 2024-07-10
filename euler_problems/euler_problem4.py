palindrome = []

def backwards_string(x):
  return x[::-1]

for first_multiple in range(100,999):
    for second_multiple in range(100,999):
        product=first_multiple*second_multiple
        if str(product) == backwards_string(str(product)):
            palindrome.append(product)

max_palindrome=max(palindrome)

print(max_palindrome)
