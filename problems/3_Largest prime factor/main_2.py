# This code suppose that the factor can will be any number, not only prime numbers.
# Exist algorithms more efficient off course

import time

start_time = time.time()

main_number: int = 600851475143
main_number_remainder: int = main_number
posible_prime_number_factor: int = 2

while main_number_remainder / posible_prime_number_factor > 1:
    if main_number_remainder % posible_prime_number_factor != 0:
        posible_prime_number_factor += 1
    else:
        main_number_remainder /= posible_prime_number_factor

print(f"The last prime factor of number is: {posible_prime_number_factor}")

print(f"Time exec: {(time.time() - start_time)} seconds")
