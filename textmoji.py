def text_to_emoji(text):
    a=[]
    for i in text:
        j=ord(chr(i))+128000
        a.append(chr(j))
    final=''.join(a)
    return(final)
    
    
def emoji_to_text(emoji_sequence):
    a=[]
    for i in emoji_sequence:
        j=ord(i)-128000
        a.append(chr(j))
    final=''.join(a)
    return final

