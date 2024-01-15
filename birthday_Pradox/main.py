import datetime
import random


def getBirthdays(numberOfBirthdays):
    "return list of number random date objext for birthdays"
    birthdays = []

    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation,as long  as all
        # birthdys have the same year

        startOFyear = datetime.date(2001, 1, 1)

        randomNummberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOFyear + randomNummberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):

    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique,so return None

    for a, birthdayA in enumerate(birthdays):

        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


while True:
    print('How many birthdys shall i generate ? max 100')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
    print()


print('Here are', numBDays, 'birthdays')

birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end="")
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()


match = getMatch(birthdays)
print("int this simulation ,", end='')

if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print("the are no match")

print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')

simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulation run. ..')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

print('100,000 simulations run.')
