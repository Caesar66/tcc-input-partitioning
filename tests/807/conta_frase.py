def conta_frases(texto):
    '''conta o total de frases terminadas pela pontuacao esperada'''
    '''str->int'''
    return str.count(texto,"?")+str.count(texto,"!")+str.count(texto,".")-2*str.count(texto,"...")
