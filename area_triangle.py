# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program calculates the area of the triangle


def calculate_area(base, height):
    # this function calculates area of the triangle

    # process
    area = (base * height) / 2

    # output
    print("The area of the triangle is {} cm²".format(round(area)))


def main():
    # input from user
    base_from_user = int(input("Please enter the base of triangle (cm): "))
    height_from_user = int(input("Please enter the height of triangle (cm): "))

    # calling functions
    calculate_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
