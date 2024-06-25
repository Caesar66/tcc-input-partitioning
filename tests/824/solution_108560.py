def uppCons(frase):
    l=0
    s=""
    c="aeiou"
    while l<len(frase):
        if frase[l] in c:
            s=s+frase[l]
        else:
            s=s+frase[l].upper()
        l=l+1
    return s