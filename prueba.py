from functionalities import funtions
from AnalizadorParser import prueba

data = '''
2 + (1.1)
°xd°
duranteQue
anota
siempreQue(){
    anota(°xd°)[;
}
desde
cuandoNo 
x ¬: °diego°
x ¬: 2
'''

sintaxis1=funtions(data)
sintaxis1.saveTokens()
# print(sintaxis1.getTokens())

data = '''
x ¬: 2[;
anota(x)[;

'''

for i in prueba(data):
    print(i)

