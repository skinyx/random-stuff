def presents_counter(house_number):
    sum_ = house_number * 10
    for i in range(1, house_number // 2 + 1):
        if not house_number % i:
            sum_ += i * 10
    return sum_

'''
counter = 36000000//41
number = 0
list_ = []
while number < 36000000:
    number = presents_counter(counter)
    list_.append(number/counter)
    counter += 1
print(counter)
'''

counter = 0
number = 0
list_ = []
while number < 36000000:
    counter += 420
    number = presents_counter(counter)
print(counter)
