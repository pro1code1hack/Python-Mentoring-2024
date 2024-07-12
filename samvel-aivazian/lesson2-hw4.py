def is_prime(number: int) -> None:
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                print(f"{number} is not a prime number.")
                break
        else:
            print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


test_number = 11
is_prime(test_number)
