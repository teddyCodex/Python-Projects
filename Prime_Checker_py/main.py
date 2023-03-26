def prime_checker(number):
    divisor_list = []
    divisor = number

    while divisor > 1:
        if number % divisor == 0:
            divisor_list.append(divisor)
        divisor -= 1

    if len(divisor_list) > 2:
        print("\nNot a Prime Number\n")
    else:
        print("\nPrime Number\n")

n = int(input('\nWhat number do you want to check?: '))
prime_checker(number=n)