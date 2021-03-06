# create a parent class that has functions needed for list to 100 being outputted
class FizzBuzz:
    def __init__(self, Fizz, Buzz):
        self.Fizz = Fizz
        self.Buzz = Buzz
        self.FizzBuzz = Fizz * Buzz

    # create function that takes an empty list, and appends 1-100 with fizz and buzz replaced
    def fizz_buzz_list(self):
        my_list = []
        for num in range(1,101):
            if num % self.FizzBuzz == 0:
                my_list.append("FizzBuzz")
            elif num % self.Fizz == 0:
                my_list.append("Fizz")
            elif num % self.Buzz == 0:
                my_list.append("Buzz")
            else:
                my_list.append(num)
        return my_list

if __name__ == "__main__":
    # if file ran from this file, run test on class to check it works as intended
    four_five = FizzBuzz(4, 5)
    print(four_five.fizz_buzz_list())