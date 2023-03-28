import time

start_time = time.time()

fibonacci_sequence = [1, 2]

sum_even_values = 2

while fibonacci_sequence[-1] < 4_000_000:
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if fibonacci_sequence[-1] % 2 == 0:
        sum_even_values += fibonacci_sequence[-1]

print(f"sum even values of fib:", sum_even_values)

print("Time exec: %s seconds" % (time.time() - start_time))
