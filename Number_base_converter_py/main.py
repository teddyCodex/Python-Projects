# from art import logo

def to_base_10(num_list, base):
    '''
    takes a list and its base and returns the 
    equivalent in base 10.
    '''
    num_length = len(num_list)
    num_in_base10 = 0

    for i in num_list:
        num_in_base10 += int(i) * base ** (num_length-1)
        num_length -= 1
    return num_in_base10


def from_base_10(num, base):

    def division(number, divisor):
        return number // divisor, number % divisor

    remainder_list = []
    new_set = division(num, base)
    numerator = new_set[0]
    remainder = new_set[1]
    remainder_list.append(remainder)

    while new_set[0] > 0 or new_set[1] > 0:
        new_set = division(numerator, base)
        numerator = new_set[0]
        remainder = new_set[1]
        remainder_list.append(remainder)
    
    if remainder_list[-1] == 0:
        remainder_list = remainder_list[:-1]
        remainder_list.reverse()
    return remainder_list


def rebase(input_base, digits, output_base):
    if type(input_base) != int or type(digits) != list or type(output_base) != int:
        raise TypeError("Invalid input type")
    elif input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    elif digits == [] or sum(digits) == 0:
        return [0]
    else:
        for i in digits:
            if i >= input_base or i < 0:
                raise ValueError("all digits must satisfy 0 <= d < input base")
        num_to_base10 = to_base_10(digits, input_base)
        num_from_base10 = from_base_10(num_to_base10, output_base)
        return num_from_base10

print(rebase(2, [1, 0, 1, 0, 1, 0], 10), 42)

# def main():
#     print(logo)
#     num = input('Number to be converted (separate w comma): ')
#     input_base = int(input('Base to be converted from: '))
#     output_base = int(input('Base to be converted to: '))
#     digits = [int(x) for x in num.split(',')]

#     print(rebase(input_base, digits, output_base))


# if __name__ == "__main__":
#     main()
