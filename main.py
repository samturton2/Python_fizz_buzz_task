# import the fizz buzz class
from FizzBuzz_class import FizzBuzz

# make function that requests fizz number
def request_fizz():
    return int(input("Please enter number for Fizz to replace\n=>"))

# make function that requests buzz number
def request_buzz():
    return int(input("Please enter number for Buzz to replace\n=>"))

# make function that loops through a list printing each number
def print_list(my_list):
    for item in my_list:
        print(item)

# Run main if ran from this file
if __name__ == "__main__":
    # run functions to request fizz and buzz
    fizz_number = request_fizz()
    buzz_number = request_buzz()

    # create object from fizzbuzz class
    fizz_buzz_object = FizzBuzz(fizz_number, buzz_number)

    # print final output using print_list function made
    print_list(fizz_buzz_object.fizz_buzz_list())