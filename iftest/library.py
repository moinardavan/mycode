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
if user_input == 1:
    print("Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths")
print("*****************THNAK YOU FOR SHOPPING WITH US*******************")
