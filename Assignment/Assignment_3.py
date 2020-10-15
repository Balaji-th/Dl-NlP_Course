#--------------------------------------------------
#  Assignment-3 program-1
#--------------------------------------------------
def my_reduce(func,seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first,i)
    return first

def do_sum(x1,x2):
    return x1+x2
def do_mul(x1,x2):
    return x1*x2
print(my_reduce(do_mul, [1,2,3,4]))

#--------------------------------------------------
#  Assignment-3 program-2
#--------------------------------------------------
def my_filter(func,my_list):
    result=[]
    for x in my_list:
        if func(x):
            result.append(x)
    return result

def ispositive(x):
    if x<=0:
        return False
    else:
        return True
print(str(my_filter(ispositive,[0,1,-2,3,4,5])))

#--------------------------------------------------
#  Assignment-3 program-3
#--------------------------------------------------
word = 'ACADGILD'
list_word = list(word)
print(list_word)

list1 = ['x','y','z']
new_list=[]
for i in list1:
    for j in range(1,5):
        new_list.append(i*j)
print(new_list)

list2 = [2,3,4]
result1 = [[item+num] for item in list2 for num in range(0,4)]
print(result1)

list2 = [2,3,4,5]
result2 = [[item+num for item in list2] for num in range(0,4)]
print(result2)

list3 = [1,2,3]
result3 = [(b,a) for a in list3 for b in list3]
print(result3)