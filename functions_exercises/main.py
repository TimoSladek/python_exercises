def difference(a, b):
    return a - b
def product(a, b):
    return a * b
def print_day(a):
    if(a>7 or a<1):
        return None
    elif(a == 1):
        return "Sunday"
    elif (a == 2):
        return "Monday"
    elif (a == 3):
        return "Tuesday"
    elif (a == 4):
        return "Wednesday"
    elif (a == 5):
        return "Thursday"
    elif (a == 6):
        return "Friday"
    else:
        return "Saturday"
def last_element(list):
    if(list == []):
        return None
    else:
        return list[len(list)-1]
def number_compare(a, b):
    if(a > b):
        return "First is greater"
    elif(a < b):
        return "Second is greater"
    else:
        return "Numbers are equal"
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())
def multiple_letter_count(word):
    return { letter: word.count(letter) for letter in word }
def list_manipulation(list, command, location, value=0):
    if(command == "add"):
        if(location == "end"):
            list.append(value)
        else:
            list.insert(0, value)
        return list
    else:
        if (location == "end"):
            return list.pop()
        else:
            return list.pop(0)
def is_palindrome(word):
    if(word.lower().replace(" ", "") == word[:: -1].lower().replace(" ", "")):
        return True
    else:
        return False
def frequency(list, search_term):
    return list.count(search_term)
def flip_case(string, letter):
    return "".join([char.swapcase() if char.lower() == letter.lower() else char for char in string])
def multiply_even_numbers(list):
    product = 1
    new_list = [num for num in list if num%2==0]
    for num in new_list:
        product *= num
    return product
def mode(list):
    number_frequency = 0
    number = -1
    i = 0
    while(i < len(list)):
        search = list[i]
        if(frequency(list, search) > number_frequency):
            number_frequency = frequency(list, search)
            number = search
        i += 1
    return number
def capitalize(string):
    return string.capitalize()
def compact(list):
    return [x for x in list if bool(x) ]
def is_even(num):
    return num % 2 == 0
def partition(list, fn):
    first_list = [x for x in list if fn(x)]
    second_list = [x for x in list if not fn(x)]
    final_list = []
    final_list.append(first_list)
    final_list.append(second_list)
    return final_list
def intersection(list1, list2):
    return [x for x in list1 if x in list2]
def add(a,b):
    return a + b
def once(fn):
    def inner(*args):
        return fn(*args)
    return inner