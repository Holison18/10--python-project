# this is a  python program that searches anything from wikipedia
from bs4 import BeautifulSoup
import wikipedia

# create a function to search from wikipedia
def search(to_search,number_of_sentences):
    try:
        result = wikipedia.summary(to_search, sentences=number_of_sentences, auto_suggest=False)
        soup = BeautifulSoup(result,features="html.parser")
        lis = soup.find_all('li')
        for item in lis:
            print(item.text)
    except wikipedia.exceptions.WikipediaException as e:
        print(f"An Error occurred: {e}")

# prompt user to enter what he wants to search
to_search = input("What do you want to search?: ")
number_of_sentences = int(input("Enter the number of the sentences you want to view: "))

# print search results
search(to_search,number_of_sentences)

print("Thank you for searching with our program!")