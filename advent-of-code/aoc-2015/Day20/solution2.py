def presents_counter(house_number):
    sum_ = house_number * 11
    for i in range(house_number // 50 + 1, house_number // 2 + 1):
        if not house_number % i:
            sum_ += i * 11
    return sum_


counter = 0
number = 0
list_ = []
while number < 36000000:
    counter += 420
    number = presents_counter(counter)
print(counter)
