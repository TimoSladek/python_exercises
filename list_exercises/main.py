for val in [1, 2, 3, 4]:
    print(val)

for val in [1, 2, 3, 4]:
    print(val * 20)

result = [val[0] for val in ["Elie", "Tim", "Matt"]]

even_values = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]

numbers = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]

reverse_names = [name.lower()[::-1] for name in ["Elie", "Tim", "Matt"]]

letters = [letter for letter in "first" if letter in "third"]

numbers_divisible_by_twelve = [num for num in range(1, 101) if num % 12 == 0]

consonants = [letter for letter in "amazing" if letter not in ['a', 'e', 'i', 'o', 'u']]

list = [[val for val in range(0, 3)] for val in range(0, 3)]

bigger_list = [[val for val in range(0, 10)] for val in range(0, 10)]