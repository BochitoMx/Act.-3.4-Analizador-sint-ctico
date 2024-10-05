import ply.lex as lex

tokens = [
    'IDENTIFICADOR', 'NUMERO', 'PARENTESIS_APERTURA', 'PARENTESIS_CIERRE',
    'LLAVE_APERTURA', 'LLAVE_CIERRE', 'PUNTOYCOMA', 'ASIGNAR', 
    'SUMA', 'RESTA', 'MULT', 'DIV', 'CADENA', 'VARIABLE'
]

reservadas = {
    'if': 'IF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE', 'return': 'RETURN',
    'programa': 'PROGRAMA', 'int': 'INT', 'float': 'FLOAT', 'char': 'CHAR', 'void': 'VOID',
    'switch': 'SWITCH', 'case': 'CASE', 'break': 'BREAK', 'default': 'DEFAULT', 'do': 'DO',
    'continue': 'CONTINUE', 'static': 'STATIC', 'const': 'CONST', 'struct': 'STRUCT',
    'typedef': 'TYPEDEF', 'union': 'UNION', 'enum': 'ENUM', 'signed': 'SIGNED',
    'unsigned': 'UNSIGNED', 'sizeof': 'SIZEOF', 'long': 'LONG', 'short': 'SHORT',
    'main': 'MAIN', 'read': 'READ', 'end': 'END', 'print': 'PRINT', 'printf': 'PRINTF',
    'la': 'LA', 'do': 'DO'
}

tokens = tokens + list(reservadas.values())


t_ASIGNAR = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PUNTOYCOMA = r';'
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CIERRE = r'\)'
t_LLAVE_APERTURA = r'\{'
t_LLAVE_CIERRE = r'\}'
t_CADENA = r'\".*?\"'

t_ignore = ' \t'

def t_VARIABLE(t):
    r'[a-dA-D]'
    t.value = t.value.lower() 
    return t

# Regla para identificadores
def t_IDENTIFICADOR(t):
    r'[e-zE-Z_][a-zA-Z_0-9]*' 
    t.value = t.value.lower() 
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')  
    return t

# Regla para números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value) 
    return t

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()


def analizar_codigo(codigo):
    lexer.input(codigo)
    resultado = []

    for token in lexer:
        fila = {
            'token': token.value,
            'palabra_reservada': 'X' if token.type in reservadas.values() else '',
            'identificador': 'X' if token.type == 'IDENTIFICADOR' else '',
            'variable': 'X' if token.type == 'VARIABLE' else '',
            'cadena': 'X' if token.type == 'CADENA' else '',
            'numero': 'X' if token.type == 'NUMERO' else '',
            'simbolo': 'X' if token.type in ['PARENTESIS_APERTURA', 'PARENTESIS_CIERRE', 'LLAVE_APERTURA', 'LLAVE_CIERRE', 'PUNTOYCOMA', 'ASIGNAR', 'SUMA', 'RESTA', 'MULT', 'DIV'] else '',
            'tipo': 'Operador' if token.type in ['SUMA', 'RESTA', 'MULT', 'DIV'] else 'Condicional' if token.type == 'IF' else 'Otro'
        }
        resultado.append(fila)
    
    return resultado