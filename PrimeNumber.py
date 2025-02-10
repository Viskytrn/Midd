def is_prime(num):
    if num <=1:
        return False
    for i in range(2, int(num ** 0.5)+1):
      if num % i == 0:
        return False
      return True

#Main Function
def prime_checker():
    num=int(input("Enter a number to check if it is a prime number:"))

    if is_prime(num):
        print(f"{num}is a prime number.")
    else:
        print(f"{num}is not a prime number.")

#Calling

if prime_checker() == "Main":
    prime_checker()