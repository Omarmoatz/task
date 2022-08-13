#firstSetOfTasks
------------------------
#Create a Boolean variable named x
#1- x=true
# Create an integer variable named y
#2- y=5
# Create a float variable named z
#3- z=2.7
# Create a string variable names s
#4- s='ziad'
#Convert the int variable to float
#5- float(y)
#Can we convert the str to int ?  =>>yes;incase of reciving number as a string as in input() function
# Create a list of numbers from 1 to 5
#7- num=[1,2,3,4,5]
#Create a tuple from 10 to 15
#8- tuple=(10,11,12,13,14,15)
# Convert the list to tuple
#numTuple=tuple(num)
# Create a dict of 3 values
dic={"product" : "oil" , "price" : 70 , "id" : "6642"}
# Can we use semi colon ; with python ? =>> yes for example if we want to sperate two or more commands
# Python is interpreted or compiled ?   =>>interpreted
# What is the differences between low level & high level =>> low level is used mostly in H.w related like machine luanguage and it is hard to understand from human prespictive while high level luanguages in the other hand is almost human luangue realy easy to understand and it useses an interpreter to translte the lines into machine luangue
# What is the differences between low level & high leve  =>> "=" is used to assign value to a varible ;while "==" is used to check whether the value of two value are equaltive 
# What do we mean by using != >> "means not equal" 
#What is the operator precedence =>>Multipication,Division,Addition,Subtraction
#Create a variable x with value of 10 
x=10
#Increase x value by 15 using assignment operators
x+=15
#Divide the x value by 5 using assignment operators
x/=5
#Multiply the x value by 10 using assignment operator
x*=10
#Get module of x on 3 using assignment operators
x%=3
#Using python print the module of 11 to 4
print(11%4)
# Print the exponent of 2,3
print(2**3)
#Divide 11 by 3 using python division
print(11/3)
#Can we divide 11 by 3 and get an integer number ? = >>yes if we use '//'
print(11//3)
#Check if 10 is bigger than 15 or not
print(10>15)
#If 10 is not bigger than15 print x is smaller than 15
if 10 < 15 :
	print("x is smaller than 15")
#In which cases we will use all >> if we want to check more than two condition on some statement;while all codition shall be true
#What is the differences between all , and >> and is used to check two conditions at the most;both of them should be true ;while all is used to check on set of coditions ;all of them should be true
#What is the differences between any , or  >> or is used to check two codintions at the most ;one of them at least should be ture; while any checks on multible conditions at least one of them should be ture
#If we need all the conditions to be true we will use …. >> 'all'
#What is the differences between if , elif >> if is used in the begining of statement while elif is used in the middle of statement and if is immandantory while elif is not  and elif can occur more then one time in the condition while if only occures once
#What is the differences between elif else >> elif is used in the middle of the condition while else is used in the end of it ; elif could occur more than one time in a single condition while else cann't
#Can we use more than one elif >> yes
#Can we use more than one else >> no
#write s simple ternary operator >> print("helloWorld") if code==ture else print("erorrFound")
#in elif , python will check all the conditions no matter what ? >>python will check elif statements by order until one of them is ture ;else it preform else statment
#in elif we use else for ... ? >> none of them works as a defult statement
#if we have this list [2,4,6,8,10] :
#○ check to see if 4 in this list or not 
list=[2,4,6,8,10]
for num in list:
	if num == 4:
		return "found"
	else:
		continue
	 if return != "found"
        return -1


#○ check to see if 4 and 6 in this list on not
list=[2,4,6,8,10]
for num in list:
        if num == 4 && 6:
                return "found"
        else:
                continue
	if return != "found"
	return -1


#○ check to see if 3 or 6 in this list
list=[2,4,6,8,10]
for num in list:
        if num == 3 or 6:
                return "found"
        else:
                continue
        if return != "found"
        return -1

#○ check to see if 2 , 4 and 5 in this list 
list=[2,4,6,8,10]
for num in list:
        if num == all ([4,2,5]):
                return "found"
        else:
                continue
        if return != "found"
        return -1

