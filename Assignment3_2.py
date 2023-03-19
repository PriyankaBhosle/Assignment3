#Python program reverse a string

def reverse(str):
   str1 = "  "
   for i in str:
         str1 = i + str1
   return str1
str = "pkonb1234"

print("The original string :", str)
print("The reverse string :", reverse(str))    