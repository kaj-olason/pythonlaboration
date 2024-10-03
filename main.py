import random

guess = ['sten', 'sax', 'påse']

class choice:
    def __init__(self, yourChoice):
        self.yourChoice = yourChoice
        
    def __str__(self):
        return f"Du valde {guess[self.yourChoice -1]}"
    
    def getChoice(self):
        return self.yourChoice
        


for pos, employee in enumerate(guess):
    print(f"{str(pos+1)}. {employee.split()[0]}")
    
    
your_select = choice(int(input('Välj från alternativ: ')))
print(your_select)
your_choice = your_select.getChoice()


computor_choice = random.choice(guess)
print('Datorn valde ', computor_choice)

if computor_choice == 'sten':
    computor_selected = 1
    
if computor_choice == 'sax':
    computor_selected = 2
    
if computor_choice == 'påse':
    computor_selected = 3
    

    
if your_choice == 1 and computor_selected == 2:
    print('Du vann!')
    
elif your_choice == 2 and computor_selected == 1:
    print('Du förlorade!')
    
elif your_choice == 1 and computor_selected == 3:
    print('Du förlorade!')
    
elif your_choice == 3 and computor_selected == 1:
    print('Du vann!')
    
elif your_choice == 2 and computor_selected == 3:
    print('Du vann!')
    
elif your_choice == 3 and computor_selected == 2:
    print('Du förlorade!')
    
    
if your_choice == computor_selected:
    print('Wow, de blev oavgjort mellan dig och datorn!')
    print('Spelet fortsätter med spänning!')
    your_select = choice(int(input('Välj än en gång från alternativ: ')))
    print(your_select)
    your_choice = your_select.getChoice()
    
    computor_choice = random.choice(guess)
    print('Datorn valde ', computor_choice)
    
    if your_choice == 1 and computor_selected == 2:
        print('Du vann!')
    
    elif your_choice == 2 and computor_selected == 1:
        print('Du förlorade!')
    
    elif your_choice == 1 and computor_selected == 3:
        print('Du förlorade!')
    
    elif your_choice == 3 and computor_selected == 1:
        print('Du vann!')
    
    elif your_choice == 2 and computor_selected == 3:
        print('Du vann!')
    
    elif your_choice == 3 and computor_selected == 2:
        print('Du förlorade!')
    


