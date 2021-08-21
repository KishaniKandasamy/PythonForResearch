def countWords(text):
    """Count the numbers of words occurs in a text"""
    
    text =text.lower()
    skips=[",","!",";",":","."]
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


### faster method using Counter
from collections import Counter

def countWordsFast(text):
    """Count the numbers of words occurs in a text"""
    
    text =text.lower()
    skips=[",","!",";",":","."]
    for ch in skips:
        text=text.replace(ch,"")
    
    word_counts = Counter(text.split(" ")) #count the objects index wise (if a String charwise if list each items)
    return word_counts
            
text = "I am a girl a girl lives in a village near to Col"
countWords(text)

##read a book
def read_book(title_path):
    """Read a book and return it as a String"""
    with open(title_path , "r",encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

text = read_book("./books/German/shakespeare/Romeo und Julia.txt")
len(text)
idx = text.find("name")
sampletext= text[idx : idx+1000]
sampletext
