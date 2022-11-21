from lexer import analizador as analyzer
from AnalizadorParser import prueba

class funtions:
    def __init__(self,syntax):
        self.ListTokens = []
        analyzer.input(syntax)

    def saveTokens(self):
        while True:
            tok = analyzer.token()
            if not tok: 
                break
            self.ListTokens.append(tok)
    
    def getTokens(self):
        result = ''
        for i in self.ListTokens:
            result+=str(i)+'\n'
            
        return result
    

def validateParser(sintax):
        concat=''
        for items in prueba(sintax):
            concat += items+'\n'
        
        return concat