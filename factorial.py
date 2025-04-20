#!/usr/bin/env python3
# Created By: chanella
# Date: April 15, 25
# This program calculates the factorial of the number entered by a user 


def main ():
    #initializations
    loop_counter = 0
    factorial_answer = 1

    #get the user number
    user_number = int(input("Enter a positive integer:"))
    print("")

    #replicates a do ..while loop
    #calculates the factorial of the user number using a loop
    while True:
     loop_counter = loop_counter + 1
     factorial_answer = factorial_answer * loop_counter
     print("Tracking {} times through loop".format(loop_counter))
     if loop_counter >= user_number:
        break

     print("") 
     print("{}! = {}".format(user_number,factorial_answer))

if __name__ == "__main__" :
    main()