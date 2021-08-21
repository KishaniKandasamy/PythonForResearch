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
