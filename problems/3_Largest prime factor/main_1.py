# This code suppose that the factor can will be any number, not only prime numbers.
# Exist algorithms more efficient off course

import time

start_time = time.time()

main_number: int = 600851475143
main_number_remainder: int = main_number
prime_number: int = 2
primes_factor: list = []
main_number_remainder_more_than_one = True

while main_number_remainder_more_than_one:
    if main_number_remainder / prime_number >= 1:
        if main_number_remainder % prime_number == 0:
            main_number_remainder = int(main_number_remainder / prime_number)
            primes_factor.append(prime_number)
        else:
            no_found_new_prime_number: bool = True
            while no_found_new_prime_number:
                prime_number += 1
                if prime_number < main_number:
                    for x in range(prime_number, main_number):
                        if prime_number % x == 0:
                            no_found_new_prime_number = False
                            break
                else:
                    break
    else:
        break

print(f"The last prime factor of number is: {primes_factor[-1]}")

print(f"Time exec: {(time.time() - start_time)} seconds")
