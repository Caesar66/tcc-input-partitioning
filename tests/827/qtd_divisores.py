def qtd_divisores(n):
    '''divisores de n. int -> int'''
    total = 0
    for contador in range(1,n+1):
        if n%contador == 0:
            total += 1
    return total
    
#test_cases = [
#    (26, ),
#    (-9, ),
#    (-4, ),
#    (-18, ),
#    (77, ),
#    (63, ),
#    (45, ),
#    (16, ),
#    (57, ),
#    (0, )
#]
#
#for test in test_cases:
#	print(f'({test[0]}, {qtd_divisores(test[0])}),')
