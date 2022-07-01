import re
import csv
with open('students.txt', 'r+') as file:
    file.write("\nI'm at the beginning\n")
    file.seek(100)
    file.write("\nI'm in the middle\n")
    file.seek(0)
    print(file.read())

def add_student(name):
    with open('students.txt', 'a+') as file:
        file.read()
        file.write(f"\n{name}\n")

def find_student(name):
    with open('students.txt', 'r') as file:
        for f in file:
            if f == name:
                print(f"{name} was found")

def update_student(name, new_name):
    with open('students.txt', 'r+') as file:
        text = file.read()
        text = re.sub(name, new_name, text)
        file.seek(0)
        file.write(text)
        file.truncate()

def remove_student(name):
    with open('students.txt', 'r+') as file:
        text = file.read()
        text = re.sub(name, '', text)
        file.seek(0)
        file.write(text)
        file.truncate()

def print_out_all_users():
    with open('users.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter="|")
        rows = list(reader)
        for row in rows:
            print(' '.join(row))

def add_user():
    with open('users.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter="|")
        first = input("What is your first name?")
        last = input("What is your last name?")
        writer.writerow([first, last])

print_out_all_users()