# python function to summ of all the numbers in list


def num(l):
   total_sum= 0
   for x in l:
      total_sum = total_sum + x
   return total_sum
my_list = [3, 5, 7, 9 ,1, 4, 2, 5]
print("sum of my_list", num(my_list))