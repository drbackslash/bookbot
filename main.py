def read():
    #This is getting the text of the book and outputting as a string
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


#word count is just returning the length of the split string
def word_count(book):
    return len(book.split())


#this function will take teh string, and convert all to lowercase
def lowercase(book):
    lowered_string = book.lower()
    return lowered_string

#removing non alphabet characters from string
def remove_non_alpha(text):
    return ''.join([c for c in text if c.isalpha()])

#this function will take the lower string as an input and return 
#a dictionary output of all the occurances of the letters
def dictionary(lowercase_book):
    my_dict = {}
    for i in lowercase_book:
        if i in my_dict:
           my_dict[i] += 1
        else:
           my_dict[i] = 1
    return my_dict 


#this is for sorting purposes only
def dict_to_list(input):
    list = []
    for char, count in input.items():
        char_dict = {"char": char, "num": count}
        list.append(char_dict)
    return list

def sort_dict(dict):
    return dict["num"]

#Here, i am defining "Main" which is whatever the assignment is at the time
def main():
    count = word_count(read())
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")

    #this is reading the book, converting to lowercase, and removing non alpha in one line
    output = remove_non_alpha(lowercase(read()))
    
    #this takes the string above and turns into a dictionary
    letter_dict = dictionary(output)
    #this turns the dictionary into a lis of dictionaries for sorting
    letter_list = dict_to_list(letter_dict)
    #this sorts by biggest number first to smallest
    letter_list.sort(reverse=True, key=sort_dict)
    #this will be for printing the report
    for i in letter_list:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
    print("--- End report ---")



main()