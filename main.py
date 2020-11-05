# import the fizz buzz class
from FizzBuzz_class import FizzBuzz

# Run main if ran from this file
if __name__ == "__main__":
    #replace 3 with fizz, and 5 with buzz
    three_five = FizzBuzz(3, 5)
    # loop round the list and print each number
    for num in three_five.fizz_buzz():
        print(num)