#Number Separator#
import random

def generate_random_list(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

def separate_even_odd_return_lists(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers, odd_numbers

def separate_even_odd_compact(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)


print("Welcome to the number separater\n")
ready_to_generate = False
ready_to_generate_answer = input("Would you like to generate a random list? Please reply 'Yes' or 'No' ")
if ready_to_generate_answer.lower() == "yes":
    ready_to_generate = True
    while ready_to_generate == True:
        try:
            generate_how_many = int(input("How big should the list be? "))
            if generate_how_many < 1 or generate_how_many > 100:
                while True:
                    try:
                        generate_how_many = int(input("Please input a list size from 1-100"))
                        if 1 <= generate_how_many <= 100:
                            break
                    except ValueError:
                        pass
                ready_to_generate = False
            else:
                ready_to_generate = False
        except ValueError:
            while True:
                try:
                    generate_how_many = int(input("Please input a list size from 1-100"))
                    if 1 <= generate_how_many <= 100:
                        break
                except ValueError:
                    pass
            ready_to_generate = False
            
    print("Generating random list with " + generate_how_many + " numbers.")
    generate_random_list(generate_how_many)

    
else:
    print("Ok then. Goodbye.")