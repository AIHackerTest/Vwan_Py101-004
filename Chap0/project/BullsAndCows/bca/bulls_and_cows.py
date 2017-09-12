#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program name: Bulls And Cows
Author: Vwan
Github: https://github.com/Vwan/Py101-004
Revision：v1.0
Edit date: 2017.08.15
"""
from random import randint
import sys

class bulls_and_cows(object):
    def __is_valid_num(self,user_num):
        # check if user input number is eligible for the game
        if 20 < user_num or user_num < 1:
            print("Number out of range, please make sure you enter a value between 1 and 20")
            return False
        else:
            return True

    def check_num(self,sys_num,user_num):
        # check if the user input number is correct against the system generated number
        msg, flag = '',False
        if user_num > sys_num:
            msg = "Larger than expected\n"
        elif user_num < sys_num:
            msg = "Smaller than expected\n"
        else:
            msg = "Correct, Game Over"
            flag = True
        return flag, msg

    def play(self,num_of_trials):
        """
        Play the Game

        System generates a random number between 1 and 20,
        Ask user to enter a number between 1 and 20,
        if it's a valid number, then check if it is the same as user input
        quit the game when user guess right or exceeds maximum allowed number of trials

        Args:
            num_of_trials (int): maximum allowed number of user trials
        """
        sys_num = randint(1,20)
        print("Welcome to Bulls and Cows, you have 10 trials to guess right the system random number, enjoy!\n")
        count = 1
        while count <= num_of_trials:
            print(f"Trial N0.{count}, you have {num_of_trials - count} chances left")
            number = input("> Your number:")
            if not number.isdigit():
                print ("Please enter a number between 1 and 20!\n ")
                continue
            else:
                number = int(number)
                if self.__is_valid_num(number):
                    flag, msg = self.check_num(sys_num,number)
                    print(msg)
                    if flag:
                        sys.exit(0)
                    else:
                        count += 1
        print (f"No more chances left, the correct number is {sys_num}")

if __name__ == '__main__':
    bulls_and_cows().play(10)
