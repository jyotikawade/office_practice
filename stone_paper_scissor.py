import random

def choice_Check(user_choice1):
    if(user_choice1==1):
        return "stone"
    elif(user_choice1==2):
        return "paper"
    
    return "scissor"
    
#------------------------------------------------------------------------------------------------
def game(computer,user):
   # print('computer=',computer)
    #print('user=',user)
    
    print("computer choice is = ",computer)
    print("\nyour choice is = ",user)
    
    if(computer=='stone' and user=='scissor') or (computer=='paper' and user=='stone') or (computer=='scissor' and user=='paper'):
        return 0
    elif(computer=='stone' and user=='paper') or (computer=='paper' and user=='scissor') or (computer=='scissor' and user=='stone'):
        return 1
    return -1
    
#--------------------------------------------------------------------------------------------------
    
def main():
    
    again=1
    
    while(again==1):
    
        com_Choice = random.choice(['stone','paper','scissor'])
        print(''' enter your choice
                  1 = stone
                  2 = paper
                  3 = scissor ''')
    
        user_choice = int(input())
        
        if(user_choice<1) or(user_choice>3):
            print("invalid choice")
            break
    
        choice=choice_Check(user_choice)

        result_match=game(com_Choice,choice)
    
        if(result_match==0):
            print("\nyou lost")
        elif(result_match==1):
            print("\nyou won")
        else:
            print("\ntie")
            
        print("\n------------------------------------------------------------------------\n")  
        
        print("do you want to play again\n 1 = yes\n 2 = no")
        again=int(input())
        
        if(again!=1)or(again!=2):
            print("invalid choice")
            break
        
        

        
#------------------------------------------------------------------------------------------------------------------    

if(__name__== "__main__"):
    main()



