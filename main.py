# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

# The constant K in the half life formula
K = -8266.64258429376


def main():
    calculate_age_single_sample()


def calculate_age_single_sample():
    # Ask the user to enter the percent of c14 left in their sample
    pct_left = float(input("% of natural c14: "))
    # Calculate the age: https://en.wikipedia.org/wiki/Radiocarbon_dating

    age = K * math.log(pct_left / 100)
    # Print the result
    print("Sample is " + str(age) + " years old.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
