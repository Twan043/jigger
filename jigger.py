import csv
import requests
from faker import Faker
import random
import time
import string

loop = int(input('How much times you want to j1g your file? [f.e 5] '))
name = input('What do you want as the file name? ')
password = input('What do you want as password? ')
adress = input('What is your adress? ')
length_of_string = int(input(f'How much letters do you want before your adress? '))
city = input('What do you want as the city? ')
house_number = int(input('What is your house number? '))
state = input('What is your state ? ')
zip = input('What is your zip code? ')
country = input('What do you want as the country? ')
prefix = input('What do you want as the prefix? ')
catchall = input('What is your catchall? [f.e test.com] ')

with open(f'{name}.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['EMAIL', 'FIRST NAME', 'LAST NAME', 'HOUSE NUMBER', 'ADRESS LINE 1', 'ADRESS LINE 2', 'CITY', 'POSTCODE / ZIP', 'STATE/PROVINCE/REGION', 'COUNTRY', 'PASSWORD', 'PHONE PREFIX (e.g. +49)', 'INSTAGRAM', 'QUESTION'])


for i in range(loop):
    faker = Faker()
    first = faker.first_name()
    last = faker.last_name()
    numbers = ''.join((random.choice(string.digits) for x in range(3)))
    abc = random_string = "".join(random.choice(string.ascii_uppercase) for i in range(length_of_string))
    with open(f'{name}.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f'{first}{last}{numbers}@{catchall}', f'{first}', f'{last}', f'{house_number}', f'{abc} {adress}', f'', f'{city}', f'{zip}', f'{state}', f'{country}', f'{password}', f'{prefix}', f'', f''])

print(f'Succesfully generated file, check {file}.csv')
time.sleep(100) 
