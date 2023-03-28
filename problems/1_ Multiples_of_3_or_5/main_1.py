import time

start_time = time.time()

naturals_numbers_below_1000 = range(1, 1000)
sum_numbers_divided_by_3_or_5: float = 0.0
for number in naturals_numbers_below_1000:
    if (number % 3 == 0) or (number % 5 == 0):
        sum_numbers_divided_by_3_or_5 += number
print(sum_numbers_divided_by_3_or_5)

print("Time exec: %s seconds" % (time.time() - start_time))
