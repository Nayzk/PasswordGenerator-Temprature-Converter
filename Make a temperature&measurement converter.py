import sys


class Converter:
    def __init__(self):
        while True:
            print('''

            Wlcome to converter calculator ...
            Choose the type you need to convert to ..

                1 : Fahrenheit Converter.
                2 : Celcius Converter.
                3 : Press Q to exit.

            ''')



            user_choice = int(input('Enter your choice : '))
            if user_choice == 1:
                x = int(input(' Enter your Celcius degree : '))
                self.Fahrenheit_Converter(x)
            elif user_choice == 2:
                y = int(input(' Enter your Fahrenheit degree : '))
                self.Celcius_Converter(y)


            play_again = input('Press any key to play again, Q for Exit : ' )
            if play_again == 'Q' or play_again == 'q':
                sys.exit()


    def Fahrenheit_Converter(self,x):
        fah = (x * 1.8) + 32
        print(fah)


    def Celcius_Converter(self,y):
        cel = (y - 32) / 1.8
        print(cel)



d1 = Converter()
#Fahrenheit_Converter()    
#Celcius_Converter()
