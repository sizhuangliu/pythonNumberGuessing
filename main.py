import random


class NumberCompare:
    '''
    Number Guessing game is finished.'''

    def __init__(self, num, randnum):
        self.num = num
        self.randnum = randnum

    def guess_num(self):

        if self.num == "g":
            print('You are closing, the guess number is ' + str(self.randnum))
            return False
        elif self.num.isnumeric():
            if int(self.num) == self.randnum:
                print('Congratulations!!!!')
                return False
            elif int(self.num) < self.randnum:
                print('Sorry, too small')
                return True
            else:
                print('Sorry, too big')
                return True
        else:
            print("Invalid input, please type a number or 'G' if you want to give up")
            return True

    __version__ = '0.2'


number_to_guess = random.randint(1, 100)
guess = input('Enter an integer between 1 to 100 : ')

p = NumberCompare(guess, number_to_guess)

while p.guess_num():
    p.num = input('Enter an integer between 1 to 100 : ')

print(NumberCompare.__doc__)
print('version', NumberCompare.__version__)
