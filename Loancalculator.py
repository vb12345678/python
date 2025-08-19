#get the details of the loan from the user
money_owed = float(input('how much money do you owe in dollars?\n'))
apr = float(input('what is the annual percentage rate of the loan \n'))
payments = float(input('how much will you pay off each month in dollars \n'))
months = int(input('how many months do you want to see the results for \n'))

monthly_rate = apr/100/12
for i in range(months):
    #calculate interest
    interest_paid = money_owed*monthly_rate
    #add in interest
    money_owed = money_owed + interest_paid
    if (money_owed - payments < 0):
        print('the last payment is', round(money_owed,2))
        print ('you paid off the loan in', i+1, 'months')
        break #this ends the loop
    #make payment
    money_owed = money_owed - payments

    print ('paid', payments, 'of which',round(interest_paid,2), 'was interest', end=' ')
    print ('now i owe', round(money_owed,2))