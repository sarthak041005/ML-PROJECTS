# import pyjokes
#  MY FIRST PYTHON PROGRAM
#   THAT WAS MY PROGRAM
# n=int(input("enter a number "))
# for i in range(1,11):
#     print(n*i)
# a=30
# b=6
# c=a+b
# print(b)
# b+=3
# print(b)
# d = 30.52
# t = type(d)
# print (t)
# a = input("enter number 1 ")
# c = int(a)
# b = input("enter number 2 ")
# d = int(b)
# print("number a is:",c)
# print("number b is:",d)
# print("sum is:", c + d)
# name= "sarthak"
# print(name)
# f = len(name)
# print(f)
# nameshort = name[0:4]  #start from index 0 and end at 3
# nameshort2 = name[-4:-1]  #start from last index amd move in reverse till 4th index
# print(nameshort)
# print(nameshort2)
# character1 = name[4]  #prints the 5th index value 
# print(character1)
# word = "amazing"
# print(word[0: :3])
# name7 = "abcdefghijklmnopqrstuvwxyz"
# print(name7[1: ])
# okay = "sarthakpareek"
# print(len(okay))
# print(okay.endswith("eekh"))
# print(okay.capitalize())
# print(okay.startswith("sa")) 
# "HELLO".lower() 
# abcd  = "mit \t moradabad"
# print(abcd)
# a = "sarthak pareek"
# index = a.find("pareek")
# print(index)
# s = "hello world"
# replaced_string = s.replace("world", "Python")
# print(replaced_string)
# a = "mit moradabad is shitty\n but manageable"
# print(a)
# name = input("enter your name\t")

# print(f"good morning\t{name}")
# abcd = int(input("enter your marks"))
# print(f"sarthak scored {abcd} marks in python")

# sart = float(input("enter the average"))
# print(f"the average is {sart} for royal enfield hunter350" )
# letter = ' '  'dear <|name|> ,  you are selected! <|date|>'''

# print(letter. replace("|name|" , "sarthak").replace("<|date|>" , "18 august"))
# name = "sarthak pareek"
# print(name.find("pa"))
# print(name.replace("pareek" , "agarwal")) 
# language = ["pyhton", "html" , "css" , "js"]
# print(language) 
# print(language[0])
# print(language[0:3])
# language[0] = "java"
# print(language)
# l1 = [8,6,2,3,5,7]
# l1.append(9)
# l1.pop(5)
# print(l1)
# l1.reverse()
# print(l1)
# l1.sort()
# print(l1)
# l1.append(4.7)
# print(l1)
# l1.remove(5)
# print(l1)
# l1.insert(3,2)
# print(l1) 
# print(l1.pop(3))
# a=(1,)
# print(type(a))
# a=(1,7,2,False,"sarthak")
# print(a)
# a = (1,3,5,5,3,7,9)
# no = a.count(5)
# print(no)
# a = (1,3,2,3,4,5,6,7)
# abcd = a.index(4)
# print(abcd)
# a = (1,2,3,4)

# repeat= a*3
# print(repeat)
# a = (1,2,3,4)
# print(len(a))
# abcd = (1,2,3,4,5,6,7,8,9)
# sliced = abcd[1:7]
# print(sliced)
# fruits = []
# f1 = input("enter first fruit")
# fruits.append(f1)
# f2 = input("enter 2nd fruit")
# fruits.append(f2)
# f3 = input("enter 3rd fruit")
# fruits.append(f3)
# f4 = input("enter 4th fruit")
# fruits.append(f4)
# print(fruits)
# marks = []
# m1 = int(input("enter 1st student marks"))
# marks.append(m1)
# m2 = int(input("enter 1st student marks"))
# marks.append(m2)
# m3 = int(input("enter 1st student marks"))

# marks.append(m3)
# m4 = int(input("enter 1st student marks"))
# marks.append(m4)
# m5 = int(input("enter 1st student marks"))
# marks.append(m5)
# m6 = int(input("enter 1st student marks"))
# marks.append(m6)
# marks.sort()
# print(marks)
# l = [1,2,3,4]
# print(sum(l))
# a = (7,0,8,0,0,9)
# n = a.count(0)
# print(n)
# marks = {
#     "harry" : 100,
#     "sarthak" : 97,
#     "ananya" : 65
    
#     }
# # print(marks, type(marks))
# # print(marks["harry"],marks["sarthak"])
# # print(marks.items())
# # print(marks.keys())
# # print(marks.values())
# marks.update({"harry" : 99 , "saksham" : 94})
# print(marks)
# print(marks.get("saksham"))
# d = {}
# print(type(d))
# e = {1,2,3,3,4,5}
# print(e)
# a = set()
# a.add(1)
# a.add(2)
# print(a)
# s = {1,2,3,4,5,6}
# print(len(s))
# s.remove(3)
# print(s)
# s1 = {1,2,3,4,5,6}
# s2 = {3,4,5,6,7,8}
# print(s1.union(s2))
# print(s1.intersection(s2))
# translate = { "namaste" : "hello",
#              "bike" : "motorcycle"
# }
# word = input("enter the word you want\n")
# print(translate[word])
# s = set()
# n = int(input("enter number"))
# s.add(n)
# n = int(input("enter number"))
# s.add(n)
# n = int(input("enter number"))
# s.add(n)
# n = int(input("enter number"))
# s.add(n)
# n = int(input("enter number"))
# s.add(n)
# n = int(input("enter number"))
# s.add(n)
# n = int(input("enter number"))
# s.add(n)
# n = int(input("enter number"))
# s.add(n)
# print(s)
# s = set()
# s.add(18)
# s.add("18")
# print(s)
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s)) # the value is 2 because in python it checks numerical value which is true for 20==20.0
# print(s)
# s = {} # it is not a set. its a dictionary
# print(type(s))
# language = {
#     "sarthak": "english",
#     "ananya":"french",
#     "raj":"spanish"
# }
# print(language)
# d={}

# name = input("enter your name")
# lang = input("enter your lang")
# d.update({name:lang})
# name = input("enter your name")
# lang = input("enter your lang")
# d.update({name:lang})
# name = input("enter your name")
# lang = input("enter your lang")
# d.update({name:lang})
# name = input("enter your name")
# lang = input("enter your lang")
# d.update({name:lang})
# print(d)
# a = int(input("enter a nmber"))
# if (a>18):
#     print("valid age")
# else:
#     print("invalid")
# a = int(input("enter 1st number"))
# a2 = int(input("enter 2nd number"))
# a3= int(input("enter 3rd number"))
# a4 = int(input("enter 4th number"))
# if(a>a2 and a>a3 and a>a4):
#     print("gratest number is", a)
# elif( a2>a and a2>a3 and a2>a4):
#      print("gratest number is", a2)
# elif(a3>a and a3> a2 and a3>a4):
#      print("greatest number is ", a3)
# else:
#      print("greatest number is", a4)
# marks1= int(input("enter marks for 1st subject"))
# marks2= int(input("enter marks for 2nd subject"))
# marks3= int(input("enter marks for 3rd subject"))
# total_percentage= (marks1+marks2+marks3)/300 *100
# if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("passed", total_percentage)
# else:
#     print("failed",total_percentage)
# p1="Make a lot of money"
# p2="buy now"
# p3= "subscribe this"
# p4= "click this"
# message = input("enter your message")
# if(p1 in message or p2 in message or p3 in message or p4 in message):
#     print("this is a scam")
# else:
#     print(message)
# username= input("enter your username")
# if(len(username)<=10):
#     print("atleast 10 characters required for username")
# else:
# #     print("your username is", username)
# l1= ["a", "b", "c", "d", "e"]
# name= input("enter your name")
# if(name in l1):
#     print("name is in the list")
# else:
#     print("name is not in the list")
#Loops:-
# for i in range(1,100):
#     print(i)
# i=2
# while(i<6):
#     print(i)
#     i+=1
# i=0
# while(i<5):
#     print("harry")
#     i=i+1
# l=[1, "sarthak", False, 3.14]
# i=0
# while(i<len(l)+1):
#     print(l[i])
#     i+=1
# l=[1,4,2,7,0]
# for item in l:
#     print(item)
# for i in range(0,15):
#     print(i)
# for i in range(0,100,5):
#     print(i)
# l=[1,3,4,5,3,9]
# print(l)
# s = "harry"
# for i in s:
#     print(a)
# l=[1,2,3,4,5]
# for item in l:
#     print(item)
# else:
#     print("done")
# for i in range(10):
#     if(i==4):
#         continue
#     print(i)
# def func1():
#     print('good day')
# n = int(input("enter a number"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n * i}")
# n= int(input("enter a number"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")
# l=["harry", "Sarthak", "rahul","sachin"]
# for name in l:
#     if(name.startswith("s" and "S")):
#         print(f"hello {name}")
# n = int(input("enter a number"))
# i=1
# i+=1
# while(i<11):
#     print(f"{n}*{i}={n*i}")
# n = int(input("enter a number"))
# for i in range(2,n):
#     if(n%i)==0:
#         print("number is  not prime")
#     else:
#         print("number is prime")
# n= int(input("enter a number"))
# for i in range(2,n):
#     if(i%n)==0:
#         print("not prime")
#     else:
#         print("prime")
# n=int(input("enter a number"))
# for i in range(2,n):
#     if(n%i)==0:
#         print("not prime")
#         break
# else:
#     print("number is prime")
# n=int(input("enter a number"))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)
#factorial:
# n=int(input("enter a number"))
# product=1
# for i in range(1,n+1):
#     product =product*i
#     print(f"the product of {n} is{product}")
#numpy
#WORKING ON SMALL DATASET average
# tempratures=[12,23,14,34,21]
# total=0
# for temp in tempratures:
#     total+=temp
# average=total/len(tempratures)
# print(average)
