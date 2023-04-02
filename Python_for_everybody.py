# I am going to work through this introduction to Python:
# "Python for everybody": https://www.py4e.com/book
#print("hello world")    #this is a statement that outputs to terminal
#print(type(4.0))        #outputs the value type
#my_age=40               #assigns a value to a variable
#print("my age is",my_age)
#print((2+3-1)/2*4**2)   #operators in an expression. note that division(/) creates a floating point
#print(6//3)             #division (//) uses floored division
#print(7//3)             #quotient
#print(7%3)              #remainder
#first='100'
#second='200'
#print(first+second)
#name=input('What is your name?\n')  #Input from user in terminal - press Enter. \n new line
#print("Your name is",name)
#degC=input('What is the temperature in Celcius?\n')
#degF=int(degC)*9/5+32
#print('That temperature converted to farrenheit is -',degF,'degF')
#print(type(1))
#print(type(1.0))
#print(type('word'))
#print(type(True))
#x=11
#print(x>0 and x<10)
#print(x!=11 or x>11)
#x=69
#if x>0:                     # Conditional execution
#    print('x is p ositive')
#elif x==0:
#    print('x has no value')
#else:
#    print('x is negative')
#try:                        # Catching exceptions
#    degC=input('What is the temperature in Celcius?\n')
#    degF=int(degC)*9/5+32
#    print(degF,'degF')
#except:
#    print('Please enter a numbeer')
#try:                #Exercise grade an input score with exception catching
#    user_str=input('Please enter a score between 0.0 and 1.0:\n')
#    user_score=float(user_str)
#    if user_score>1.0 or user_score<0.0:
#         print('Bad score')
#     elif user_score>=0.9:
#         print('Grade:A')
#     elif user_score>=0.8:
#         print('Grade: B')
#     elif user_score>=0.7:
#         print('Grade: C')
#     elif user_score>=0.6:
#         print('Grade: D')
#     else:
#         print('Grade: F')    
# except:
#     print('Bad score')
#print(len('Elephant'))
#print(max('A word'))
#import math
#print(math.sin(1))
# import random
# for i in range(10):
#     x=random.random()
#     print(x)
# t=[3,6,9,12,15,18]
# print(random.choice(t))
# def MyFirstFunction():
#     print('What a great function')
# MyFirstFunction()
# def IJustAdd(a,b):
#     output=a+b
#     return output
# x=IJustAdd(3,5)
# print(x)
# Define a function for the previous scoring program
# user_str=input('Please enter a score between 0.0 and 1.0:\n')
# user_flt=float(user_str)
# def computegrade(user_score):
#     try:
#         if user_score>1.0 or user_score<0.0:
#             print('Bad score')
#         elif user_score>=0.9:
#             print('Grade:A')
#         elif user_score>=0.8:
#             print('Grade: B')
#         elif user_score>=0.7:
#             print('Grade: C')
#         elif user_score>=0.6:
#             print('Grade: D')
#         else:
#             print('Grade: F')    
#     except:
#         print('Bad score')    
# computegrade(user_flt)
# n=5                   #While Loop program
# while n>0:
#     print(n)
#     n=n-1
# print('blastoff!')
# n=5                     #Loop with break
# while True:
#     print(n)
#     n=n-1
#     if n==0:
#         break
# print('blastoff!')
# n=5                     #Loop with continue
# while True:
#     print(n)
#     n=n-1
#     if n>0:
#         continue
#     print('blastoff!')
#     break
# friends = ['Joseph','Glen','Sally']         #For Loop. friends is set and friend is iteration variable
# for friend in friends:
#     print('Happy New Year:', friend)
# print('Done')
# count=0                             #Note we dont use the iteration variable here.
# for intervar in [3,41,12,9,74,15]:
#     count=count+1
# print('Count: ',count)
# total=0
# for intervar in [3,41,12,9,74,15]:
#     total=total+intervar
# print('Total is: ',total)
# print(sum([3,41,12,9,74,15]))       #does the same thing
# print(len([3,41,12,9,74,15]))       #does the same thing
# largest=None
# for intervar in [3,41,12,9,74,15]:
#     if largest==None or intervar>largest:
#         largest=intervar
#     print(intervar,largest)
# print('Largest is: ',largest)
# print(max([3,41,12,9,74,15]))
# def minimum(values):                #same but practicing defining a function.
#     smallest=None
#     for value in values:
#         if smallest==None or value<smallest:
#             smallest=value
#     return smallest
# print(minimum([3,41,12,9,74,15]))
# user_input=[]
# user_input=user_input + [4]
# print(user_input)
# Excercise:
# user_input=None         #will be  string
# user_number=0           #integer
# user_list=[]            #list
# while user_input != 'done':
#     try:
#         user_input=(input('Please enter number or done:'))
#         if user_input=='done':
#             break
#         user_number=int(user_input)
#         user_list=user_list+[user_number]
#     except:
#         print('Error. Type integer or done')
# print('Total is',sum(user_list))
# print('Count is',len(user_list))
# print('Average is',sum(user_list)/len(user_list))
# Execise:
# user_input=input('Input a list if numbers: ')
# def minimum(values):               
#     smallest=None
#     for value in values:
#         if smallest==None or value<smallest:
#             smallest=value
#     return smallest
# user_list=list(map(int,user_input.split(',')))
# print('The minimum is: ', minimum(user_list))
# fruit='banana'              # Indexing starts at 0
# type(fruit)
# first=fruit[0]
# print(first)
# last=fruit[-1]
# print(last)
# index=0
# fruit='banana'
# while index < len(fruit):
#     letter=fruit[index]
#     print(letter)
#     index=index+1
# fruit='banana'
# intervar=-1
# while intervar >= -len(fruit):
#     letter=fruit[intervar]
#     print(letter)
#     intervar=intervar-1
# fruit='apple'
# for char in fruit:
#     print(char)
# s='Monty Python'
# print(s[0:5])           #: creates a slice from first char to second-1 char.
# print(s[6:12])
# print(s[:3])
# print(s[3:])
# print(type(s[:]))
# greeting='Hello World'
# new_greeting='J'+greeting[1:]
# print(new_greeting)
# def count(word,letter):
#     count=-0
#     for char in word:
#         if char == letter:
#           count=count+1
#     return count
# print(count('pineapple','p'))
# print('a' in 'banana')          # in is a boolean operator
# print('pineapple'<'banana')     # letters are in alphabetical order. note: upper case first
# stuff='Hello World'
# print(type(stuff))      #A string is an object - inc data and methods
# print(dir(stuff))       #dir lists the methods available for an object
# list=[0,1,2,3]
# print(type(list))
# print(dir(list))
# word='banana'
# print(word.upper())       #Method call with string
# numbers=[0,1,2,3,3]
# help(list.count)          #Method call with list
# print(numbers.count(3))
# line='Have a nice day'
# print(line.lower().startswith('h'))     #Multiple method calls
# print(line.count('ve'))
# # Exercise: Parsing strings
# data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# atpos=data.find('@')
# print(atpos)
# sppos=data.find(' ',atpos)
# print(sppos)
# host=data[atpos+1:sppos]        #slice the string
# print(host)
# camels=42
# print('I have spotted %d camels.'%camels)       #the format operator
# dogs=4.2
# print('I have spotted %g dogs'%dogs)
# print('%d dogs with %d hats and %d balls'%(3,2,1))
# print('in %d years I have spotted %g %s.' % (3,0.1,'camels'))
# str = 'X-DSPAM-Confidence:0.8475'
# copos=str.find(':')
# number=float(str[copos+1:])
# print(number)
# fhand=open('mbox.txt')        #it does not open the data - only the file handle
# print(fhand)
# stuff='X\nY'            #\n creates a new line
# print(stuff)
# print(len(stuff))       #\n is a single character
# fhand = open('mbox-short.txt')
# count=0
# for line in fhand:          #the for loop reads, counts and then discards each line - little memory)
#     count=count+1
# print('Line count: ',count)         #each line in the txt file is a value (string) in a list
# fhand = open('mbox-short.txt')
# inp=fhand.read()            #the entire contents of the file are read into variable inp
# print(len(inp))
# print(inp[:20])
# It is good to read the contents of a file into a variable to put it in the RAM and not exhaust the use of the file
# fhand=open('mbox-short.txt')
# print(len(fhand.read()))
# print(len(fhand.read()))
# fhand=open('mbox-short.txt')        #prints lines that start with From
# for line in fhand:
#     line=line.rstrip()              # strips white spaces including invisible new line character
#     if line.startswith('From:'):     # For interesting lines
#         print(line)                  # Process our interesting line:

# fhand=open('mbox-short.txt')        #Same idea but different structure
# for line in fhand:
#     line=line.rstrip()                  # strips white spaces including invisible new line character
#     if not line.startswith('From:'):     # Skip uninteresting lines:
#         continue
#     print(line)                          # Process our interesting line:
# fhand=open('mbox-short.txt')            #search for string
# for line in fhand:
#     line=line.rstrip()
#     if line.find('uct.ac.za')==-1: continue
#     print(line)
# fname=input('Please enter the name of file: ')  #search for subject in user defined file
# try:
#     fhand=open(fname) 
# except:
#     print('File cannot be opene:', fname)
#     exit()                                  #gracefully exits the program.
# count=0       
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count +1
# print('There were', count, 'subject lines in', fname)
# fout=open('output.txt','w')     # Lets write to a new file!
# print(fout)                     # Print the new file handle
# line1="this heres the wattle,\n"
# fout.write(line1)
# line2="the emblem of our land,\n"
# fout.write(line2)
# fout.close()                    # Close it write to disk
# fout=open('output.txt')
# print(fout.read())
# EXERCISE
# filename=input("Please enter filename: ")
# fhand=open(filename)
# text=fhand.read()
# capitalized=text.upper()
# print(capitalized)
#  EXERCISE
# filename=input("Please enter filename: ")
# fhand=open(filename)
# count=0
# total=0.0
# for line in fhand:
#     line=line.rstrip()
#     if line.find("X-DSPAM-Confidence:")>= 0:
#         count=count+1
#         poschar=line.find("X-DSPAM-Confidence:")
#         posnum=poschar+len("X-DSPAM-Confidence:")
#         total=total+float(line[posnum+1:posnum+7])
# print("Count is:",count)
# print("Total is:",total)
# print ("Average is: ",total/count)
#  EXERCISE
# try:
#     filename=input("Type name of file: ")
#     if filename == "na na boo boo":
#         print("NA NA BOO BOO TO YOU!")
#     fhand=open(filename)
#     count=0
#     for line in fhand:
#         if line.startswith("Subject"):
#             count=count+1
#     print("There were ",count,"subject lines in ",filename)
# except:
#     print("File cannot be opened: ",filename)
#8 - LISTS
# numbers=[17,125]
# for i in range(len(numbers)):
#     numbers[i]=numbers[i]*2
# print(numbers)
# print(len([1,5,3,"g",[3,4,5]])) #list can include different types and nested lists
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
# print(a*3)
# t=['a','b','c','d','e','f']
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# t[1:3]=['x','y']
# print(t)
# t=['g','d','e','u','o']
# g=t.sort()
# print(g)            #Doesnt work! it modifies the list but returns nothing.
# print('what about now ',t)
# t=['g','d','e','u','o']
# x=t.pop(3)            #Remove from list and return.
# print(x)
# print(t)
# t=['g','d','e','u','o']
# del t[1]                #Remove from list
# print(t)
# t=['g','d','e','u','o']
# t.remove('o')             #When you know the element and not the index.
# print(t)
# t=['g','d','e','u','o']
# del t[1:3]
# print(t)
# nums=[3,41,12,9,74,15]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# numlist=list()
# while True:
#     inp=input('Enter a number: ')
#     if inp=='done': break
#     value=float(inp)
#     numlist.append(value)
# average=sum(numlist)/len(numlist)
# print('AVerage: ', average)
# s='spam'
# t=list(s)
# print(t)
# s=('Pining for the fjords')
# t=s.split()                       #Split automatically assumes ' '
# print(t)
# s='spam-spam-spam'
# print(s.split('-'))                 #Split can use defined delimiter
# t=['Pining', 'for', 'the', 'fjords']
# print(' '.join(t))                  #Join as to be invoked on the delimiter
# fhand=open('mbox-short.txt')
# for line in fhand:
#     line=line.rstrip()
#     if not line.startswith('From '): continue
#     words=line.split()
#     print(words[2])
# a='banana'
# b='banana'
# print(a is b)           #True because Python only created one object
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)           #False because Python created two objects
# a=[1,2,3]
# b=a                       #The object (list) has more than one reference.
# print(a is b)
# b[0]=17                   #changes made to one alias affect another
# print(a)
# def delete_head(t):         #t is aliased to the letters object
#     del t[0]
#     print(t)                #note that t does not exist outside of this function
# letters=['a','b','c']
# delete_head(letters)
# print(letters)
# t1=[1,2]
# t2=t1.append(3)             #remember append does not return a value
# print(t1)
# print(t2)                   #returne None
# t3=t1+[3]
# print(t3)
# t2 is t3
# def tail(t):
#     return t[1:]
# letters=['a','b','c']
# rest=tail(letters)
# print(rest)
#Exercise Chop
# numbers = [1,2,3,4,5,6,7,8,9]
# def chop(user_list):      #If a function modifies a parameter the caller sees the change
#     del user_list[0]
#     del user_list[-1]
# x=chop(numbers)
# print(numbers)
# print(x)            #the function chop returns None
#Exercise Middle
# numbers = [1,2,3,4,5,6,7,8,9]
# def middle(user_list):      #Function does not modify the parameter
#     return user_list[1:-1] 
# print(numbers)
# newlist=middle(numbers)
# print(newlist)
# print(numbers)
#Exercise on copying
# t=[9,8,7,6,56,34,26,99]
# print(t)
# print(t.sort())         #sort() returns None but modifies paramter object.
# print(t)                # shows that object was modified.
# t=[9,8,7,6,56,34,26,99]
# copy=t[:]                   #Make a copy to avoid modification of the object.
# print(copy.sort())
# print(t)
# print(copy)
# Debugging exercise
# fhand=open('mbox-short.txt')    #Print day of week - 3rd word in From line.
# for line in fhand:
#     words=line.split()
# #    print('debug: ',words)            #bug tracking
#     if words == []: continue
#     if words[0] != 'From': continue
#     print(words[2])
# fhand=open('mbox-short.txt')    #Print day of week - 3rd word in From line.
# for line in fhand:
#     words=line.split()
# #    print('debug: ',words)            #bug tracking
#     if words == [] or words[0] != 'From': continue
#     print(words[2])
#Exercise 8.16-4: list all unique words
# unique_words = []
# fhand = open('romeo.txt')
# for line in fhand:
#     words = line.split()
#     for word in words:
#         matches = 0
#         for unique_word in unique_words:
#             if word == unique_word:
#                 matches = matches+1
#         if matches == 0:
#             # print('debug: ', unique_words)
#             # print('debug: ', words)
#             # print('debug: ', word)
#             unique_words.append(word)
# unique_words.sort()
# print(unique_words)
#Exercise 8.16-5: list all email senders and total count
# count=0
# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:'): continue
#     if line.startswith('From'):
#         words = line.split()
#         print(words[1])
#         count=count+1
# print('Count: ',count)
#Exercise 8.16-5: list all email senders and total count
# user_input = 0
# user_list = []
# while user_input != 'done':
#     user_input = input('Enter a number and done when finished: ')
#     if user_input == 'done': break
#     try:            # Guardian code
#         user_float = float(user_input)
#     except:
#         print('Not a number')
#         continue
#     user_list.append(user_float)
# print(user_list)
# def maximum(user_input):
#     maximum = user_input[0]
#     for number in user_input:
#         if number > maximum:
#             maximum = number
#     return maximum
# calc_max = maximum(user_list)
# print('Max is: ',calc_max)
# def minimum(user_input):
#     minimum = user_input[0]
#     for number in user_input:
#         if number < minimum:
#             minimum = number
#     return minimum
# calc_min = minimum(user_list)
# print('Min is: ',calc_min)
#9 - DICTIONARIES
# eng2sp = dict()
# print(eng2sp)
# eng2sp['one']='uno'
# print(eng2sp)
# eng2sp={'one':'uno', 'two':'dos', 'three':'tres'}
# print(eng2sp)   #not order of items in a dictionary are unpredictable.
# print(eng2sp['two'])
# print(len(eng2sp))      #the number of key-value pairs
# print('one' in eng2sp)  #tests if it exists as a key (but not a value)
# print('uno' in eng2sp) 
# print(eng2sp.values())
# vals = list(eng2sp.values())
# print('uno' in vals)
#
# word='brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c]+1
# print(d)
#
# counts = {'chuck':1,'annie':42,'jan':100}
# print(counts.get('jan',0))
# print(counts.get('tim',0))      #return the specified default value if key does not exist
# 
# word = 'brontosaurus'
# d = dict()
# for c in word:
#     d[c] = d.get(c,0)+1         #more succint than the above code.
# print(d)
#
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('Filename does not exist')
#     exit()
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
# print(counts)

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     print(key,counts[key])

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key,counts[key])

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# first = list(counts.keys())
# print(first)
# first.sort()
# print(first)
# for key in first:
#     print(key, counts[key])

#ADVANCED TEXT PARSING
# import string

# fname = input('Enter the file name: ')
# try:
#     fhand=open(fname)
# except:
#     print('Filename does not exist: ',fname)
#     exit()
# counts=dict()
# for line in fhand:
#     line = line.strip()     #removes the invisible new line character
#     line = line.translate(line.maketrans('','',string.punctuation)) # removes punctuation
#     line = line.lower()     #makes all lower case
#     words = line.split()    #makes a list of words
#     for word in words:      #makes a dictionary that counts the frequency of words
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)

#  9.7 EXERCISE 2 - quantity of emails sent on each day of week
# counts=dict()
# fhand=open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:'): continue       #guardian code
#     if line.startswith('From'):
#         words = line.split()
#         # if words[2] in counts:
#         #     counts[words[2]] += 1
#         # else:
#         #     counts[words[2]] = 1
#         counts[words[2]] = counts.get(words[2],0) + 1
# print(counts)

# #  9.7 EXERCISE 3 - quantity of emails sent from each person
# counts=dict()
# fhand=open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From:'): continue       #guardian code
#     if line.startswith('From'):
#         words = line.split()
#         counts[words[1]] = counts.get(words[1],0) + 1
# print(counts)

#  9.7 EXERCISE 4 - who sent the most emails
# fname = input('Enter filename: ')
# try:
#     fhand=open(fname)
# except:
#     print('File name not found: ',fname)
#     exit()
# counts=dict()
# for line in fhand:
#     if line.startswith('From:'): continue       #guardian code
#     if line.startswith('From'):                 #counter keys=author values=quantity
#         words = line.split()
#         counts[words[1]] = counts.get(words[1],0) + 1
# def maximum(user_list):         #returns maximum number from a lsit
#     max_num = user_list[0]
#     for number in user_list:
#         if number > max_num:
#             max_num = number
#     return max_num
# max_emails = maximum(list(counts.values()))     #max quantity from counts list
# for key in counts:          #prints author and quantity if they have max quantity
#     if counts[key] == max_emails:
#         print(key, counts[key])

#  9.7 EXERCISE 5 - how many emails from each domain:
# fhand=open('mbox-short.txt')
# counts=dict()
# for line in fhand:
#     if line.startswith('From:'): continue       #guardian code
#     if line.startswith('From'):                 #counter keys=author values=quantity
#         words = line.split()
#         author = words[1]
#         pos_start=author.find('@')+1
#         domain=author[pos_start:]               #slices out the domain
#         counts[domain] = counts.get(domain,0) + 1
# print(counts)

# CHAPTER 10 - TUPLES
# t = 'a','b','c','d','e'
# print(t)
# print(type(t))
# t = ('a','b','c','d','e')           # You can add a bracket for the code to look better.
# print(t)
# print(type(t))
# x=tuple()           # to create an empty tuple
# print(x)
# y=tuple('lupins')
# print(y)
# print(y[1:3])       # you can slice a tuple
# y[1] = 'o'          # error! you cannot modify a tuple.
#... remembering the difference between string, list, dictionary and tuple.
# word = 'funny'
# print(word)
# word[1] = 'o'         # error! string does not support item assignment
# dictionary = {'apple':'good','doctor':'away'}  # dictionaries
# print(dictionary)
# print(type(dictionary))
# print(dictionary['apple'])
# print(dictionary.values())
# print(dictionary.keys())
# list_example = [1,2,'h',69,'what?']         # Lists
# print(list_example)
# print(type(list_example))
# print(list_example[1])
# t = ('a','b','c','d','e')  
# #So I cannot modify an element of a tuple... 
# #but I can re-assign the variable to a new tuple referencing the old tuple.
# t = ('A',) + t[1:]          
# print(t)





