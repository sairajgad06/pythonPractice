zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'aeiou':
      print (char, end='')

print()

numbers = (34,54,67,21,78,97,45,44,80,19)
total = 1
for num in numbers:
   total*=num
print ("Total =", total)

print()
 
numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
   if num%2 == 0:
      print (num)