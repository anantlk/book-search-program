import urllib2
from bs4 import BeautifulSoup
import re

book_author_name=[]
book_title_name=[]
books={}

genres=["692.Best_Science_Books_Non_Fiction_Only","11.Best_Crime_Mystery_Books","21580.Geeky_Techy_Books_","453.Best_Philosophical_Literature","135.Best_Horror_Novels","19534.Funny_as_Hell_"]

print("Enter the category:")
category=raw_input()

print("\nFetching data for You...")
category=category.lower()
for genre in genres:
	if(re.search(category,genre.lower())): 
		query=genre
		break
	
page=urllib2.urlopen("https://www.goodreads.com/list/show/"+genre)
page=BeautifulSoup(page,"html.parser")
book_name_list=page.find_all('a',class_="bookTitle")
for title in book_name_list:
	book_title_name.append(title.find('span',attrs={"itemprop":"name"}).string)
book_author_list=page.find_all('a',class_="authorName")
for author in book_author_list:
	book_author_name.append(author.find('span',attrs={"itemprop":"name"}).string)
	

books[category]=[]
for pos in range(0,5):
	books[category].append(	{"name":str(book_title_name[pos].string),"author":str(book_author_name[pos].string)})

print("\n")
rank=1
for bk in books[category]:
	print(str(rank)+".Name:"),
	print(bk["name"])
	print("  Author:"),
	print(bk["author"])
	print("\n")
	rank+=1

