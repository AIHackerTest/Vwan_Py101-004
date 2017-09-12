
from sys import exit as sysexit
from random import randint

class bulls_and_cows_advanced(object):
    def __is_valid_num(self,number):
        if number < 1000 or number >= 10000:
            print ("Number out of range, please make sure you enter a value between 1000 and 9999")
            return False
        elif len(set(list(str(number)))) != 4:
            print ("Duplicate digits are not allowed, please retry")
            return False
        else:
            return True

    def __generate_num(self):
        while True:
            num = randint(1000,9999)
            numlist = [int(i) for i in str(num)]
            if (len(set(numlist)) )==4:
                break
        print(f"{num}")
        return num

    def check_num(self,n1,n2):
        if (n1 == n2):
            return "4A0B"
        else:
            numlist1 = [int(i) for i in str(n1)]
            numlist2 = [int(i) for i in str(n2)]
            numlist = [x - y for x,y in zip(numlist1,numlist2)]
            count_a = numlist.count(0)
            count_b = len(set(numlist1) & set(numlist2)) - count_a
            return f"{count_a}A{count_b}B"

    def play(self,num_of_trials):
        """
        Play the Game

        System generates a random number between 1000 and 9999, no dupliate digits
        User enter a 4-digit number,
        Check if the user_num fully matches the sys_num and return 4A0B
        Check if the user_num partially matches the sys_num, return {count_a}A{count_b}B,
        where count_a for numbers of digit fully matches, count_b for numbers of digit partially matches
        Exit when user exceeds max. allowed trials or user_num fully matches sys_num

        :param num_of_trials (int): maximum allowed number of user trials
        """

        # generate a random number
        sys_num = self.__generate_num()
        print("Welcome to Bulls and Cows Advanced, you have 10 trials to guess right the system random number, enjoy!\n")
        count = 1
        while count <= num_of_trials:
            print(f"Trial N0.{count}, you have {num_of_trials - count} chances left")
            try:
                number = int( input("> Your number:"))
            except:
                print ("Please enter a number between 1000 and 9999!\n ")
                continue
            else:
                if self.__is_valid_num(number):
                    result = self.check_num(sys_num,number)
                    if int(result[0]) == 4:
                        print(f"Congratulations, {result} is correct!")
                        sysexit(0)
                    else:
                        print (f"Sorry, your guess result {result} is incorrect, try again to make it 4A0B! ")
                    count += 1
        print (f"No more chances left, the correct number is {sys_num}")

if __name__ == '__main__':
    bulls_and_cows_advanced().play(10)
