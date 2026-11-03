def fizz_buzz():
    for i in range(1, 101):
        if (
            i % 3 == 0 and i % 5 == 0
        ):  # if item is divisible by both 3 and 5 without a remainder, print FizzBuzz
            print("FizzBuzz")
        elif i % 3 == 0:  # if item is divisible by 3 without a remainder, print Fizz
            print("Fizz")
        elif i % 5 == 0:  # if item is divisible by 5 without a remainder, print Buzz
            print("Buzz")
        else:
            print(i)


fizz_buzz()
