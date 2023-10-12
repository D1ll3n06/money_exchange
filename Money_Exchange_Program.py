# Money Exchange Program Solution

#Set total to zero
total = 0

#Header
print()
print('This program will add up you change.')
print('Then determine if you have enough change for a $1, $5, or $10 dollar bill')

#Calculate users $ amount with given amounts of coins
while total!=1.0 and total!=5.0 and total!=10.0:
    #Set all values back to 0 at each new loop
    pennies = 0
    nickels = 0
    dimes = 0
    quarters = 0
    total = 0
    
    #Get total number of pennies from user and add to total   
    pennies += int(input('Enter total number of pennies: '))
    total += (pennies * .01)
    
    #Get total number of nickels and add to total
    nickels += int(input('Enter total number of nickels: '))
    total += (nickels * .05)
    
    #Get total number of dimes and add to total
    dimes += int(input('Enter total number of dimes: '))
    total += (dimes * .10)
    
    #Get total number of quarters and add to total
    quarters += int(input('Enter total number of quarters: '))
    total += (quarters * .25)
    
    #determine whether total amount of coins is equal to one, five, or ten dollars
    if total==1.0:
        print('------------------------------------------------')
        print('You have the exact change to convert the coins to a dollar-bill.')
    elif total==5.0:
        print('------------------------------------------------')
        print('You have the exact change to convert the coins to a five-dollar-bill.')
    elif total==10.0:
        print('------------------------------------------------')
        print('You have the exact change to convert the coins to a ten-dollar-bill')
    else:
        print('------------------------------------------------')
        print('The change does not equal a one, five, nor ten-dollar-bill. ')
        print(f'However, your total is ${total:,.2f}')
        print('Try again:')
 # End of program