def filtra_pares(a):
    """Retorna uma nova tupla apenas com os valores pares da tupla que é a entrada;
    tupla->tupla"""
    if a[0]%2==0 and a[1]%2!=0 and a[2]%2!=0 and a[3]%2!=0:
        return (a[1])
    elif a[0]%2!=0 and a[1]%2==0 and a[2]%2!=0 and a[3]%2!=0:
        return (a[2])
    elif a[0]%2!=0 and a[1]%2!=0 and a[2]%2==0 and a[3]%2!=0:
        return (a[4])
    elif a[0]%2!=0 and a[1]%2!=0 and a[2]%2!=0 and a[3]%2==0:
        return a[4]
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2!=0 and a[3]%2!=0:
        return (a[1],a[2])
    elif a[0]%2==0 and a[1]%2!=0 and a[2]%2==0 and a[3]%2!=0:
        return (a[1],a[3])
    elif a[0]%2==0 and a[1]%2!=0 and a[2]%2!=0 and a[3]%2==0:
        return (a[1],a[4])
    elif a[0]%2!=0 and a[1]%2==0 and a[2]%2==0 and a[3]%2!=0:
        return (a[2],a[3])
    elif a[0]%2!=0 and a[1]%2==0 and a[2]%2!=0 and a[3]%2==0:
        return (a[2],a[4])
    elif a[0]%2!=0 and a[1]%2!=0 and a[2]%2==0 and a[3]%2==0:
        return (a[3],a[4])
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2==0 and a[3]%2!=0:
        return (a[1],a[2],a[3])
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2!=0 and a[3]%2==0:
        return (a[1],a[2],a[4])
    elif a[0]%2==0 and a[1]%2!=0 and a[2]%2==0 and a[3]%2==0:
        return (a[1],a[3],a[4])
    elif a[0]%2!=0 and a[1]%2==0 and a[2]%2==0 and a[3]%2==0:
        return (a[2],a[3],a[4])
    elif a[0]%2==0 and a[1]%2==0 and a[2]%2==0 and a[3]%2==0:
        return a
    else:
        return ()
