def balanced(expression):
    #your code goes here
    bruh = expression
    list = []
    list.insert(0,bruh)
    if list == []:
        list.pop(0)
    n = 0
    for i in bruh:
        if i == '(' or i == ')':
            n += 1
    if n % 2 == 0 and n > 0:
        return "True"
    elif n % 2 != 0:
        return "False"
    else:
        return "False"
    

print(balanced(input()))