#this problem blown my mind i use long time to figure out how to solve it but i can't 
"""
this is what i did
n = int(input())
print(n)
month = [i+1 for i in range(12) if i % 2 == 0]
print(month)
insect = [x*n for x in month]
print(insect)

#and it still incorrect way though ToT
"""
######################################################################################################################################
"""
this is what it should look like to get the right answer i should just type that thing from it explanation that it said 
'The formula to calculate the number of insects after N months will be: count*2ᴺ, where count is the initial number of insects.'
this is what i got when i asked chatgpt 'new_list = [expression for item in iterable if condition]'
"""
######################################################################################################################################

n = input()
insect = [n*(2**i) for i in range(12)]
print(insect)