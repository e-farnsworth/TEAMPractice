#This is a practice file

# Write individual functions here

def display_frac_as_decimal(top_of_frac, bot_of_frac):
    dec = top_of_frac / bot_of_frac
    max_digit = max(len(str(top_of_frac)),len(str(bot_of_frac)))
    print(top_of_frac)
    for i in range(max_digit):
        print('-',end='')
    print(f'Result  = {dec:.3f}')
    print (f' Result {bot_of_frac}\n')
    
    

def addleo():
    print("Leo added this :)")

# Then add call to main
def main():
    display_frac_as_decimal(52,234)
    addleo()
    

main()