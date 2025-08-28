def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:          
            even += 1
        else:
            odd += 1
    return even, odd


lists = [12, 45, 25, 32, 22, 87, 99]
evens, odds = count(lists)
print("There are {} even numbers and {} odd numbers" .format(evens, odds))


names = ['Sophia', 'James', 'Vera', 'Daniella']
names.insert(3, 55)
print(names)


school = 'Miva'
print(id(school))
