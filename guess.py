import random
choice  = 'y'
list = []
random_number = random.randint(0,10)
while(choice == 'y' or choice == 'Y'):
    user_input = int (input("Enter your Number : "))
    if(user_input>random_number):
        list.append(user_input)
        print("Your Guess Is too High .")  
    elif(user_input<random_number):
        list.append(user_input)
        print("Your Guess is too Low.")
    elif(user_input == random_number and len(list)==0):
        print("you gussed the number with zero steps. Number was : " , random_number)
    else : 
        length=len(list)
        print("Number of step taken to reach to the Number : " ,length)
        print("The Numbers you print are " , list)
        print("You gussed the Number and the Number Was : " , random_number)
    choice = str(input("Do you want another Attempt : "))



