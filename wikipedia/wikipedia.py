# this is a  python program that searches anything from wikipedia
import wikipedia

# create a function to search from wikipedia
def search(to_search,number_of_sentences)-> str:
    result = wikipedia.summary(to_search,sentences = number_of_sentences)
    return result

# prompt user to enter what he wants to search
to_search = input("What do you want to search?: ")
number_of_sentences = int(input("Enter the number of the sentences you want to view: "))

# print search results
print(search(to_search,number_of_sentences))

print("Thank you for searching with our program!")