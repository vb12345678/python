empty =[]#empty list 
words = ['lol','idk','tbh']#list of strings
num = [5,10,15]#a list of numbers
mixed = [5,'sdk',1.5]#a list of mixed items
lists = [['a','b','c'],['d','e','f']]#a list of lists,index numbering for the list starts at 0
acronyms = ['lol','idk','smh','tbh','bfn']
acronyms.remove ('bfn')# this removes the last item from the acronyms list
#del acronyms[4]#this deletes the fourth item from the acronyms list
if 1 in [1,2,3,4,5]:#this checks for a specific item in the list-keyword in.
    print ('true')
acronyms = ['lol','idk','smh','tbh']    
word = 'bfn'
if word in acronyms:#now using the key word in to check for a string
    print (word + 'is in the list')
else:
    print (word + 'is not in the list')    
for acronym in acronyms:#this for loop prints all the items in the acronyms list individually using acronym as a loop variable
    print (acronym)#python programing is very big on indenting for its structure    