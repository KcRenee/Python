lists = [12, 45, 25, 32, 22, 87, 99]
names = ['Sophia', 'James', 'Vera', 'Daniella', 'Monica', 'Rachel']
school = 'Miva'
Luxury = {
    1: 'Chanel',
    2: 'LV',
    3: 'Prada',
    4: ['YSL', 'Cartier']
}


# List to a function


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


evens, odds = count(lists)
print("There are {} even numbers and {} odd numbers" .format(evens, odds))

# List in python
names.insert(3, 'Zoey')
lists.sort()
print(lists)
print(names)

# Variables
print(id(school))

# Dictionaries
print(Luxury)
age = dict(zip(names, lists))
print(age)

# for loop
for j in Luxury.values():
    print(j)

# while loop
k = 1
while k <= 4:
    print(school)
    k = k + 1
