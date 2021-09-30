def calcValues(low_num,upper_num,choice):
    evenlist = []
    oddlist = []
    for value in range(low_num,upper_num):
        if(value%2==0):
            evenlist.append(value)
        else:
            oddlist.append(value)
    if choice == 'E':
        print(evenlist)
    elif choice == 'O':
        print(oddlist)
    else:
        print('Invalid')
def UserInput():
    while True:
        try:
            Lower_limit=int(input("Enter the first number for range: "))
        except ValueError:
            print('Sorry I did not understand that')
            continue
        else:
            break
    while True:
        try:
            Upper_limit=int(input("Enter the second number for range: "))
        except ValueError:
            print('Sorry I did not understand that')
            continue
        else:
            break
    userchoice = str(input('Do you want to display even(E) or odd(O)?  '))
    return calcValues(Lower_limit,Upper_limit,userchoice)
UserInput()
tryAgain = str(input('Do you want to run this again? Y/N:  '))
while tryAgain != 'N':
    UserInput()
    tryAgain = str(input('Do you want to run this again? Y/N:  '))
else:
    print('Thank You for using the program')





