"""
Create fake data using the IT providers for fiscal codes and dates.
The random lib is used to create doc number and decide the doc type.
"""

from random import randint, choice
from faker import Faker


#@num_people2create: how many fake rows I want to create. If no parameter is passed, the default is 1.
def create_fake_data(num_people2create=1):

    fake = Faker('it_IT')
    doc_types = ['CI', 'PA', 'PI']
    fakes = []
    for _ in range(num_people2create):
        new_person = (fake.ssn(), randint(111111, 999999), choice(doc_types), fake.date(),
                      fake.date_between('-10y', '+90d'))
        fakes.append(new_person)

    return fakes


if __name__ == '__main__':
    print(create_fake_data())
