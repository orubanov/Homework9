x = 38
print('Привет оператор if')
if x < 0:
    print('Меньше нуля')

gj = 'успех'

# примеры

a, b = 10, 5
if a > b:
    print('a > b')

if a > b and a > 0:
    print(gj)

if (a > b) and (a > 0 or b < 1000):
    print(gj)

if 5 < b and b < 10:
    print(gj)

#можно сравнивать все типы данных

if '34' > '123':
    print(gj)

if '123' > '12':
    print(gj)

if [1, 2] > [1, 1]:
    print(gj)
#нельзя сравнивать разные типы данных

if '6' > 5:
    print(gj)

if [5, 6] > 5:
    print(gj)

if '6' != 5: #в подобны случая значения условия True
    print(gj)