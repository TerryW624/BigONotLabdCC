#Task 1
#time complexity is linear Big O Notatin = O(n)
n = int(input("Choose a number > "))

def evens_and_odds(num):
    if num % 2 == 0:
        is_even = True
    else:
        is_even = False
    return is_even

true_or_false = evens_and_odds(n)
print(true_or_false)

#Task 2
#time complexity is linear Big O Notation = O(n)
numbers = []

def add_number_to_numbers(list):
    for i in range(5):
        user_number = int(input("What number do you wish to add to the list? > "))
        list += [user_number]
    return list

numbers = add_number_to_numbers(numbers)
def high_and_low(number_list):
    for n in number_list:
        if n >= 100:
            print(False)
            return
    print(True)
high_and_low(numbers)

#Task 3
#set up for user input
name_list = []

def add_names_to_name_list(list):
    for i in range(5):
        user_name = input("What name do you wish to add to the list? > ")
        list += [user_name]
    return list
name_list = add_names_to_name_list(name_list) 
#time complexity is quadratic or n^2 this is the function that answers the lab task 3 Big O Notation = O(n^2)
def your_name_is_my_name(name_list):
    index = 0
    for name in name_list:
        counter = 0
        name_list = name_list
        index += 1
        for name in name_list:
            counter += 1
            displaced_name = name_list[index - 1]
            if counter != index:
                if name == displaced_name:
                    print(True)
                    return
            else:
                continue
    print(False)
your_name_is_my_name(name_list)

#Task 4
#time complexity is quadratic or Big O Notation = O(n^2)
def same_number(list, displaced_number):
    for number in list:
        displaced_number = displaced_number
        if number == displaced_number:
             return True
        else:
             continue
    return False

unsorted_numbers = []
unsorted_numbers = add_number_to_numbers(unsorted_numbers)
print(unsorted_numbers)

def sort_list(numbers_list):
    ordered_list = []
    for number in numbers_list:
        if numbers_list.index(number) == 0:
            ordered_list += [number]
        elif numbers_list.index(number) != 0:
            for num in ordered_list:
                if number <= num:
                    index = ordered_list.index(num)
                    ordered_list.insert(index, number)
                    break
                else:
                    continue
            is_number_same = same_number(ordered_list, number)
            if is_number_same == False:
                ordered_list.append(number)
    numbers_list = ordered_list
    print(numbers_list)
sort_list(unsorted_numbers)

