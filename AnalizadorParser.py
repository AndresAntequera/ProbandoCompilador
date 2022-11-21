from sys import stdin
from lexer import tokens,analizador

precedence = (
    ('right','IGUAL'),
    ('right','IGUALQUE'),
    ('left','MAYQUE','MENQUE'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('left','PARIZQ','PARDER'),
    ('left','LLAVIZQ','LLAVDER')
    )

nombres = {}

def p_init(t):
    'init : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]
    
def p_instrucciones_instruccion(t):
    'instrucciones : instruccion'
    t[0] = [t[1]]
    
def p_instruccion(t):
    '''instruccion : imprimir_instr
                   | asignacion_instr
                   | if_instr
                   | while_instr    
    '''
    t[0] = t[1]
    
def p_if(t):
    '''if_instr : IF PARIZQ expresion_logica PARDER LLAVIZQ statement LLAVDER'''
    print(t[3])
    if(t[3]):
        t[0] = t[6]
 
def p_statement(t):
    '''statement : imprimir_instr
                 |  if_instr
                 |  expresion
                 |  while_instr
    '''
    t[0] = t[1]
    print(t[0])
    
def p_while(t):
    '''while_instr : WHILE PARIZQ expresion_logica PARDER LLAVIZQ statement LLAVDER'''
    while(t[3]):
        t[0] = t[6]
        
def p_asignacion(t):
    'asignacion_instr : ID IGUAL expresion PTCOMA'
    nombres[t[1]] = t[3] 
    
def p_asignacion_tipo(t):
    '''expresion : ENTERO
                 |  DECIMAL
                 |  STRING                 
    '''
    t[0] = t[1]
    
def p_expresion_id(t):
    '''expresion : ID'''
    t[0] = nombres[t[1]]
    
def p_print(t):
    '''imprimir_instr : PRINT PARIZQ expresion PARDER PTCOMA'''
    t[0] = t[3]
    
def p_expresion_logica(t):
    ''' expresion_logica : expresion MENQUE expresion
                         | expresion MAYQUE expresion
                         | expresion IGUALQUE expresion
                         | expresion NIGUALQUE expresion
                         | expresion MENIGUAL expresion
                         | expresion MAYIGUAL expresion
    '''
    if t[2] == '<':t[0] = t[1] < t[3]
    elif t[2] == '>':t[0] = t[1] > t[3]
    elif t[2] == '==':t[0] = t[1] == t[3]
    elif t[2] == '!=':t[0] = t[1] != t[3]
    elif t[2] == '<=':t[0] = t[1] <= t[3]
    elif t[2] == '>=':t[0] = t[1] >= t[3]
    
def p_expresion_logica_group(t):
    '''expresion_logica : PARIZQ expresion_logica PARDER'''
    t[0] = t[2]    

def p_expresion_logica_group(t):
    '''expresion_logica : PARIZQ expresion_logica PARDER MENQUE PARIZQ expresion_logica PARDER
                        | PARIZQ expresion_logica PARDER MAYQUE PARIZQ expresion_logica PARDER
                        | PARIZQ expresion_logica PARDER IGUALQUE PARIZQ expresion_logica PARDER
                        | PARIZQ expresion_logica PARDER NIGUALQUE PARIZQ expresion_logica PARDER
                        | PARIZQ expresion_logica PARDER MAYIGUAL PARIZQ expresion_logica PARDER
                        | PARIZQ expresion_logica PARDER MENIGUAL PARIZQ expresion_logica PARDER
    '''
    if t[4] == '<':t[0] = t[2] < t[5]
    elif t[4] == '>': t[0] = t[2] > t[5]
    elif t[4] == '==': t[0] = t[2] is t[5]
    elif t[4] == '!=': t[0] = t[2] != t[5]
    elif t[4] == '<=': t[0] = t[2] <= t[5]
    elif t[4] == '>=': t[0] = t[2] >= t[5]
    
def p_expresion_operador_logico(t):
    '''expresion_logica : PARIZQ expresion_logica PARDER AND PARIZQ expresion_logica PARDER
                        | PARIZQ expresion_logica PARDER OR PARIZQ expresion_logica PARDER
                        | expresion_logica AND expresion_logica
                        | expresion_logica OR expresion_logica
    '''
    if t[4] == '^': t[0] = t[2] and t[5]
    elif t[4] == '~': t[0] = t[2] or t[5]
    elif t[2] == '~': t[0] = t[1] or t[3]
    elif t[2] == '~': t[0] = t[1] or t[3]
    
def p_expresion_operaciones(t):
    '''expresion : expresion MAS expresion
                 | expresion MENOS expresion
                 | expresion POR expresion
                 | expresion DIVIDIDO expresion
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

def p_error(t):
    global resultadoGramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(t.type),str(t.value))
    else:
        resultado = "Error sintactico {}".format(t)        
    
    resultadoGramatica.append(resultado)

import ply.yacc as yacc
parser = yacc.yacc()

resultadoGramatica = []

def prueba(data):
    resultadoGramatica.clear()
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultadoGramatica.append(str(gram)) 
    
    return resultadoGramatica            

# text = '''
# x¬:2[;
# anota(x)[;
# siempreQue(x:¬¬:2){anota(°xd°)[;
# }
# '''

# for i in prueba(text):
#     print(i)