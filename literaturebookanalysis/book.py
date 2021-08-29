import os
import pandas as pd
import matplotlib.pyplot as plt

def countWords(text):
    """Count the numbers of words occurs in a text"""
    
    text =text.lower()
    skips=[",",".",";",":","'",'"']
    for ch in skips:
        text=text.replace(ch,"")
    
    word_counts = {}
    for word in text.split(" "):
        if(word in word_counts):
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
            
text = "I am a girl a girl lives in a village near to col"
countWords(text)


from collections import Counter

def countWordsFast(text):
    """Count the numbers of words occurs in a text"""
    
    text =text.lower()
    skips=[",","!",";",":",".",]
    for ch in skips:
        text=text.replace(ch,"")
    
    word_counts = Counter(text.split(" ")) #count the objects index wise (if a String charwise if list each items)
    return word_counts
            
text = "I am a girl a girl lives in a village near to Col"
countWords(text)


def read_book(title_path):
    """Read a book and return it as a String"""
    with open(title_path , "r",encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

text = read_book("./books/English/shakespeare/Romeo and Juliet.txt")
len(text)
idx = text.find("What's in a name?")
sampletext= text[idx : idx+1000]
sampletext


def word_stats(word_counts):
    """count number of unique words and frequencies"""
    num_uniqueword = len(word_counts)
    count=word_counts.values()
    return (num_uniqueword, count)


text = read_book("./books/English/shakespeare/Romeo and Juliet.txt")
word_counts = countWords(text)
(num_uniqueword, count) = word_stats(word_counts)
print(num_uniqueword, sum(count))

book_dir ="./books"

stats=pd.DataFrame(columns =("language","author","title","length","unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir+"/"+language):
        for title in os.listdir(book_dir+"/"+language+"/"+author):
            inputfile= book_dir+"/"+language+"/"+author+"/"+title
            #print(inputfile)
            text = read_book(inputfile)
            word_counts=countWords(text)
            (num_uniqueword, count) = word_stats(word_counts)
            stats.loc[title_num]=language, author.capitalize(), title.replace(".txt",""), sum(count), num_uniqueword
            title_num += 1


stats.head()
stats.tail()

#plt.plot(stats.length,stats.unique,"bo")
#plt.loglog(stats.length,stats.unique,"bo")

plt.figure(figsize=(10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length,subset.unique,"o", label="English", color="crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length,subset.unique,"o", label="French", color="forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length,subset.unique,"o", label="German", color="blue")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length,subset.unique,"o", label="Portuguese", color="orange")
plt.legend()
plt.xlabel(" Book Length ")
plt.ylabel(" Number of unique words")
plt.savefig("Lang_plot.pdf")
