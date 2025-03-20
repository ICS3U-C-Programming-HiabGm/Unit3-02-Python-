# Created by: Hiab G
# Date: Wed, Feb. 28th
# This program checks if there are the correct number of students (555) is correct
import constants_num


def main():
    # get number of students
    correct_number = int(input("Guess the number of students between 55-590: "))
    print("")
    # check if number if there are too many students
    if correct_number != constants_num.RIGHT_number:
        print("Wrong!")
        
   
# check if number if there are correct number of students
    if correct_number == constants_num.RIGHT_number:
        print("Correct!")


if __name__ == "__main__":
    main()
