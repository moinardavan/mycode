#!/usr/bin/env python3

# a list of books

books = ["Harry Potter","Hobbit & Lord of the Rings","Chronicles of Narni","Indiana Jones","Batman:The Killing Joke"]

print("welcome to our virutal library; please pick a book from list elow::\n")

for i, item in enumerate(books, start=1):
    print(i,item)

print()
user_input=int(input())
if user_input > len(books):
    print("Please pick number from the given list")
else:
    print("You Picked:",books[user_input-1],",Great choice!!")

print("*****************THNAK YOU FOR SHOPPING WITH US*******************")
