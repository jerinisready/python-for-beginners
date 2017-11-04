##### Python For CEK

1. List Touple Set Dict String - and manipulating functions

###### PRINT
``` print "Hello, Python
```
###### INITIALIZATION
``` a = 10
```
 # int()
```b = '10'
```
# str()
```c = []
```
      # list()
```d = {}
  ```
        # set()
```e = ()
```
      # touple()
```f = a,b,c, b>c
```
     # set()
```print a == b
```


```a = b = 10
```
```print a == b
```

```a = 10
```
```b = 10
```
```print a == b
```
    #Reason



```sum = a + b ```
```print sum ```
```diff = a - b ```
```diff sum ```
```product = a * b ```
```print product ```
```quotient = a//b ```
```print quotient```
```desimal = a/b```
```print desimal```
```remainder = a % b```
```print remainder```


```a = 100```
```b = 43```
```a += b```
```print a```
```a -= b```
```print a```
```a *= b```
```print a```
```a /= b```
```print a```
```a %= b```
```print a```




##### '\' as Escape Charector
###### FIND THE OUTPUT!
```print(" Did you know that 'word' is a word?")```
```print('Did you know that " word " is a word?')```
```print(' Did you know that \'word\' is a word?')```
```print(" Did you know that \"word\" is a word ?")```


```print('A\nB\nC')````
```print('D\tE\tF')```
```print('W X\b Y Z')
```
        # so what if we want to print a '\'?
```print('I just wanna try how to print a \\ ?') ```
```print " \n ", " \t ", " \" ", " \' ", " \\ ", " \/ ", " \b ", " \d ", " \D ", " \w ", " \W "
```


###### Format String

```print "His name is %s and his age is %d! he paid Rs. %.4f \/-" % ('Arun', 28, 256.2932384 )
```
```print "His name is {} and his age is {}! he paid Rs. {} \/-".format('Arun', 28, 256.2932384 )
```
```name, age, donation = 'Arjun' , 30, 295.234423
```
```print "His name is {} and his age is {}! he paid Rs. {} \/-".format( name, age, donation )
```

```print "His name is {name} and his age is {age}! he paid Rs. {donation} \/-".format( name, age, donation )
```
```print "His name is {0} and his age is {2}! he paid Rs. {1} \/-".format( name,  donation, age )
```

```data_set = {'name':name, 'age': age, 'payment':donation}
```
```print "His name is {0['name']} and his age is {0['age']}! he paid Rs. {0['payment']} \/-".format( data_set )
```



###### KEYBOARD INTERACTIONS

> *Program 1*

```print()
input_data = input('Enter Limit? ')
try:
    size_of_array = int(input_data)
    array = []
except Exception as e:
    print "Failed to convert data! {e} ".format(e)
    sys.exit(9)

for _ in range(size_of_array):
    array.append(input())
print "-"*20
print "\n => ".join(array)
```

> *Program 2*

```a = " 1 + ( 3 % 2 ) "           # note that its a string
print type(a)
print eval(a)
```

```b = " ( 1 or ( 0 and 1 ) or 0 or (1 and 1)) "
print type(b)
print eval(b)
```
> *VERY SIMPLEST EVER CALCULATOR is using USING PYTHON! [in one line]*
print eval( input() )


##### PYTHON RESERVED WORDS
* and 	          | Boolean And Operation
* assert 	        | For testing Purpose
* break 	        | to break a control flow from if condition or loop
* class 	        | defining a class
* continue        | stop current iteration of loop and skip iteration
* def 	          | defining a function
* del 	          | delete an object
* elif 	          | else if condition: tag
* else 	          | else condition tag
* except          | try catch block tag
* exec 	          | execute ython script or file
* finally 	      | try catch tag
* for             | loop tag
* from 	          | tag to import files or packages
* global          | declare variables as global
* if 	            | if tag
* import 	        | tag to import files or packages
* in 	            | check weather an object is in a list or set
* is 	            | check weather the id's are same?
* lambda          | declare an inline function
* not 	          | negate anything
* or 	            | logiucal or
* pass 	          | leave an empty block as it is
* print 	        | print to starnderd output or file
* raise           | call an exception
* return 	        | return control flow to caller
* try 	          | try cache tag
* while           | looping tag



###### LIST
```mylist = ['a','f','e','Shamly','Manu', 34, -21, False, None, 3.14]

mylist[5]
mylist[-2]
mylist[5:-2]
mylist[1:-1:2]
mylist.index('Shamly')
mylist.append([123,2534,324])
mylist.extend(['abc','def','ghi'])
mylist.sort()
mylist.insert(3,"Hello world!")
mylist.remove("Shamly")
mylist.push(2,"Rocker")
mylist.pop(5)
mylist.reverse()
mylist.count()

'a' in mylist


del mylist[3]
sorted(mylist, [function])
len(mylist)

mylist = [(634, True), None, ['hello','', None, 'world'], {}]
mylist[1][1][0]
mylist[-2]
mylist[5:-2]
```

```stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack
stack.pop()
stack.pop()
stack
```

###### TOUPLE
```mytouple = ('abc', 123, 0, None)
mytouple[-2]
mytouple[2:-2]

mytouple =  123, None, True, "ABCDEF"
mytouple[-2]
mytouple[2:-2]
```



###### SET
```myset = set('abc', 123, 0, None)
myset_dup  = set('abcd', 123, 425, "Hello World")

print myset
print myset
print myset         # EACH TIME ORDER CHANGES, NO DEFINIT#E ORDER
print myset

myset.union(myset_dup)
myset.intersection(myset_dup)
myset.diff(myset_dup)
```


###### DICT
```mydict = {
    'name'      : 'Johny',
    'class'     : 'LKG B',
    'roll no'   : 2,
    'present'   : True,
    'marks'     :{
                    'english' : 43,
                    'malyalam' : 46,
                    'maths' : 50,
                }
    'internals' : [10, 10, 9]    
}

print mydict
```
### If feels interesting; check out, an immutable object inside mutable object or vice versa are modfyable

###### STRING
a = "Hello" + " " + "World!" + " " + " The crazzy fox " + "quicklly jumped over " + " llazy Dogs! "
print(a)
"wor" in a
"acb" not in a


a[5]
a[-2]
a[5:-2]
a[1:-1:2]

print a.capitialise()
print a.center(50,'-')
print a.find("ll")
print a.index('z')
print a.isalnum()
print a.isalpha()
print a. isdigit()
print a. islower()
print a.upper()
print a.lower()
print a.title()


###### PYTHON BUILTIN USEFUL FUNCTION FOR UNIQUE HANDLING
>Lambda, filter, reduce and map


###### LAMBDA
sub = lambda x,y: x-y if x > y else y-x

print sub(5,3)
equivalent to :

def sum(x,y)
    if x > y:
        return x-y
    else:
        return y-x


###### MAP - if we want to do a perticular function to all elements in the iterative list
> result_list = map( function, list )

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)

print F


###### FILTER - if we want to do create a new list with elements which satisfy a particular condition
> result_list = filter( function, list )

ages = 24,18,17,42,23,10,5,16,9,40    
youth = filter(lambda x : 18< x and x <36, ages)
print youth


internal_marks = (10,25,36,20,42)
external_marks = (19,23,72,94,68)
extra_marks = (2,5,4,3,3)

passed = filter(lambda x, y, z : (x + y + z) > 45, internal_marks, external_marks, extra_marks )
