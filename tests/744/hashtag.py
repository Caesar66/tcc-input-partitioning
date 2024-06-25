def hashtag(string):
    pos = len(string)//2
    return "#" + string[:pos] + "#" + string[pos:] + "#"
