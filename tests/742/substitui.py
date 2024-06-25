def substitui(s,x,i):
    if i<0 or i>= len(s):
        return "i inválido"
    return s[:i] + x + s[i+1:]
