def le_grafo(path):
    
    with open(path, 'r') as f:
        
        linhas = f.readlines()
        for linha in linhas:
        
            if (linha.split(' ')[0] == 'c' or linha.split(' ')[0] == ' '):
                continue
            
        print(linha)
        