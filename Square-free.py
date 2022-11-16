# The code recieves an integer value and returns whether the value or number is SquareFree or not.
#An integer is called squarefree if it is not divisible by any perfect squares other than 1.

num =int(input('enter number: '))
# the list below is a container to collect squares that are factors of the number entered
s_list=[]
for i in range(2,num):
    if num%(i**2)==0:
        s_list.append(i**2)
        
if len(s_list)==0:
    print("squarefree number")
else:
    print("Not squarefree")