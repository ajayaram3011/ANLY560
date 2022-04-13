# Assignment -1 => Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def unique():
    # Getting input from the user
    num_seq = input("Write a sequence of number:").split(',')
    # checking for uniqueness
    i = 0
    dup = 0
    for i in range(len(num_seq)-1):
        if num_seq[i] == num_seq[i+1]:
            dup += (i+1)
        i += 1

    if dup != 0:
        print(f"Sequence you have entered is:{num_seq} the entered sequence has got Duplicates")
    else:
        print(f"Sequence you have entered is:{num_seq} the entered sequence has no Duplicates")

# calling the unique function
# unique()

# Assignment -2 => Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.

def occurrences ():
    num_list = input("Please enter the integer lists (hint: sequence of number seperated by comma):").split(",")
    count_19 = 0
    count_5 =0

    for i in range(len(num_list)):
        if int(num_list[i]) == 19:
            count_19 += 1
        elif int(num_list[i]) == 5:
            count_5 += 1


    if count_5 == 3 and count_19 == 2:
        print ("the entered sequence has 2 occurences of 19 and 3 occurrences of 5")
    elif count_5 > 3 and count_19 >2:
        print ("the entered sequence has more than 2 occurences of 19 and 3 occurrences of 5")
    elif count_5 < 3 and count_19 < 2:
        print("the entered sequence has fewer occurences of 19 and  5")

# occurrences()

# Assignment -3 => Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.

def powof4test(x):
    if x > pow(4,4) and x % 34 == 4:
        print("the entered number is greater than 4^4 and mod of 34 as well")
    else:
        print("the entered integer is nither greater than 4^4 and nor mod of 34")

powof4test(922)

# Assignment -4 ==> Write a Python program to get the top stories from Google news.
import bs4
from bs4 import BeautifulSoup as gogl
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

gogl_page=gogl(xml_page,"xml")
news_list=gogl_page.findAll("item")

# Printing the top 10 news
for i in range(1,10):
  print(news_list[i].title.text)
  print(news_list[i].link.text)
  print(news_list[i].pubDate.text)
  print("-"*60)