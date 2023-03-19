#python function that accepts a string and calculate the number of upper case letters and lower case letters
#sample string

str = "The quick Brow Fox"
lower = 0
upper = 0
for i in str:
    if(i.islower()):
            lower+=1

    elif(i.isupper()):
            upper+=1

print("the number of lower characters:", lower)
print("the number of uppercases character:", upper)


#another string
str = "Good Morning EveryOne"
lower = 0
upper = 0
for i in str:
    if(i.islower()):
            lower+=1

    elif(i.isupper()):
            upper+=1

print("the number of lower characters:", lower)
print("the number of uppercases character:", upper)


