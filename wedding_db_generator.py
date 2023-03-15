import csv
from random import randint
import datetime
import time
import faker


fake = faker.Faker('ru_RU')

def create_couple():
    male_name = ' '.join([fake.last_name_male(),fake.first_name_male(),fake.middle_name_male()])
    male_bday = datetime.date(randint(1960,2000),randint(1,12),randint(1,28))
    female_name = ' '.join([fake.last_name_female(),fake.first_name_female(),fake.middle_name_female()])
    female_bday = datetime.date(randint(1960, 2000), randint(1, 12), randint(1, 28))
    wedding_date = datetime.date(randint(max(male_bday.year,female_bday.year)+18, 2020), randint(1, 12), randint(1, 28))
    zags_number = randint(1,10)

    return [male_name,str(male_bday),female_name,str(female_bday),str(wedding_date),zags_number]

def generate_n_couples(n):
    return [create_couple() for _ in range(n)]



files = ['couples100.csv','couples500.csv','couples1000.csv','couples2000.csv','couples5000.csv','couples10000.csv','couples50000.csv','couples100000.csv']
amount = [100,500,1000,2000,5000,10000,50000,100000]

start = time.time()
for i in files:
    with open(i, 'a', newline='', encoding="windows-1251") as state_file:
        writer = csv.writer(state_file)
        writer.writerows(generate_n_couples(amount[files.index(i)]))
end = time.time()-start
print(end)


