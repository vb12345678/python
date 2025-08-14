expenses = []
#for i in range(7):#creates a for loop running from 0-6
num_exspenses = int(input("enter # of expenses:"))#asks the user for the number of expenses they have
for i in range(num_exspenses):#runs the for loop based on the users expenses
    expenses.append(float(input("enter an expense:")))#adds item to the expenses list from the user



total = sum(expenses)#this uses the built in function sum in python instead of using a loop to calculate the values

print ('you spent $',total, sep='')#using the comma instead of the plus sign which also works in python and no conversion needed for sum.sep rovides a seperator

#a more efficient way of creating the expense function
#we can use a range function to generate a sequenc of numbers