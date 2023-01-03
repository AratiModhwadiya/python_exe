"""dict1={
    "color":"black",
    "brand":"abc",
    "price":2000,
    "status":True,
    "l1":["abc",1,True],
    "t1":("ab",2,False)
}
print(dict1)
a=dict1["color"]
b=dict1.get("l1")
k=dict1.keys()
v=dict1.values()
print(a)
print(b)
print(k)
print(v)
dict1["color"]="purple"
print(dict1)
i=dict1.items()
print(i)
if "brand" in dict1:
    print("yes")
if "color" not in dict1:
    print("abc")
else:
    print("no")
dict1.update({"brand":"xyz"})
print(dict1)
dict1.pop("brand")
print(dict1)
dict1.popitem()
print(dict1)
del dict1["color"]
print(dict1)
for x in dict1.values():
    print(x)
for x in dict1.keys():
    print(x)
for x in dict1.items():
    print(x)
x=dict1.copy()
print(dict1)
x=dict(dict1)
print(dict1)
dict2={
    "d1":{
    1:"a",
    2:"b"
},
    "d2":{
        3:"4",
        "color":"black"
    },
}
print(dict2)

dct1={
    "color":"black",
    "brand":"abc",
}
dct2={
    "price":2000,
    "status":True,
}
dct3={
    "l1":["abc",1,True],
    "t1":("ab",2,False)
}
dct={
    "dct1":dct1,
    "dct2":dct2,
    "dct3":dct3
}
print(dct)

dict1.update({"color":"red"})
print(dict1)
g=dict1.get("l1")
print(g)
#dictionary can be added into list
di={"ab":1,"bh":2}
list1=[]
d=dict1.copy()
list1.append(d)
print(list1)

#List can be added in dictionary
d1={
    1:2020,
    2:False,
    "l1":[1,6,True,"abc"]
}
print(d1)

#FUNCTIONS
def my_f():
    print("hello")
my_f()

def my_fun(name):
    print(f"are you from{name}")
my_fun("paris")




def a_function(string):
    "hello from hello"
    return len(string)
print("length of function is:(",a_function("hello"))
print("length of python",a_function("from"))


def add(sum1=a,sum2=b):
    return (sum1+sum2)
print("sum of a and b is",add(4,5))

def maxmin(num1,num2):
     return (num1*num2)
print("maxmin is",maxmin(9,6))

def addn():
    return

a=int(input("enter number a"))
b=int(input("enter number b"))
def max() :
    if a>=b:
        print("a is bigger",a)
    if a==b:
        print(a,"is equal to ",b)
    else:
        print("b is bigger")
max()


#Lambda Function

l=lambda a,b,c:a+b+c
print(l(1,2,4))
list3=[]
a=int(input("enter 3 numbers:"))
for i in range(a):
    list3.append(a)
    func=lambda i:a
    print(func(list3))

lst=[1,2,3,4,"hello",True]
for x in lst:
    print(x)

i=5
while i<=6:
    print(i)
    i=+1

import re

s = '''geeks.forgeeks
hello./[mbchdj78367489}\.(findall,search,split,sum,finditer)
fdeshello jhokf , '''

match = re.search(r'.', s)
match1 = re.search(r'mbchd',s)#for printing escap sequence character
print(match1)
print(match)

match = re.search(r'\.', s)
print(match)"""

"""lst=[]
for i in range(0,5):
    no = int(input('Enter value-{}: '.format(i+1)))
    lst.append(no)
min_no = lst[0]
max_no = lst[0]
for no in range(len(lst)):
    if lst[no] <= min_no:
        min_no = lst[no]
    elif lst[no] >= max_no:
        max_no = lst[no]
        print('Max No. is: {}'.format(max_no))
        print('Min No. is: {}'.format(min_no))"""





"""em=input("email you want")
pattern =r"(^[a-zA-z0-9_+.-]+@[a-zA-z0-9_+.-]+.[a-zA-z0-9.-]+$)"
print(re.match(pattern,em))"""

"""no1=input("enter second number")
pattern =r"(^[0-9]+[0-9]+[0-9]+$)"
print(re.match(pattern,no))

print("no is:{}".format(no))
print(f'no is:{no},second no is:{no1}')"""
import re
no=input("number you want")
pattern=('[6-9][0-9]{9}$')
print=(re.match(pattern,no))

