# Created by: Hiab G
# Date: Wed, Feb. 28th
# This program checks if there are the correct number of students (4) is correct
import constants_num


def main():
    # get nummber of students
    number_of_students = int(input("Enter the number of students: "))
    print("")
    # check if number if there are too many students
    if number_of_students > constants_num.MAX_Students:
        print("Too many students!")
# check if number if there are correct number of students
    if number_of_students == constants_num.MAX_Students:
        print("Correct!")


if __name__ == "__main__":
    main()
