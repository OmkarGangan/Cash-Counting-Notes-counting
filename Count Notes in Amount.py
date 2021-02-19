# Count Total Number Of Notes required in Entered Amount.

# List to store notes
c = [2000,1000,500,200,100,50,20,10,5,2,1]        

# User entered amount stored in variable n
n = int(input("Enter Amount:"))      

# storing user entered amount in temporary variable rs
rs = n

# variable i as a counter
i=0

# creating empty list
cash = []

# finite loop while
while i<=len(c)-1:
    
    # integer of quotient stored in q i.e amount divided by cash
    q = n//c[i]        
    
    # if q>0 means that much cash is required
    if q>0:
        
        # amount - cash
        n = n-c[i]
        
        # store that cash in list
        cash.append(c[i])
        
        # set counter again to 0
        i = 0
        
        # if amount = 0 then break the while loop-stop
        if n == 0:
            break
    else:
        # increment counter
        i +=1
    
# creating dict for notes required
notes = {}
for i in cash:
    # add note in dict with count
    notes[i] = cash.count(i)

# print required output
print('*************************************')
print("To pay ₹{}/- you will require: ".format(rs))

# iterating into dict of notes
for k,v in notes.items():
    if k>=10:
        # for more than 1 notes
        if v>1:
            print("{} notes of {}".format(v,k))

        # for one note
        else:
            print("{} note of {}".format(v,k))

    else:
        # for more than 1 coins
        if v>1:
            print("{} coins of {}".format(v,k))

        # for one coin
        else:
            print("{} coin of {}".format(v,k))        
        
