def primo(n):
    '''identifica se n  ́e primo. Int -> bool'''
    if n<=1:
        return False
    elif n==2:
        return True
    for contador in range(2,n):
        if n%contador == 0:
            return False
    return True
    
#test_cases = [
#    (174, ),
#    (5041, ),
#    (4, ),
#    (169, ),
#    (216, ),
#    (235, ),
#    (37, ),
#    (11, ),
#    (33, ),
#    (239, ),
#    (241, ),
#    (281, ),
#    (112, ),
#    (51, ),
#    (263, ),
#    (289, ),
#    (121, ),
#    (286, ),
#    (288, ),
#    (228, )
#]
#
#for test in test_cases:
#	print(f'({test[0]}, {primo(test[0])}),')
