import ply.yacc as yacc
from lexer import tokens

def p_programa(p):
    '''programa : PROGRAMA IDENTIFICADOR PARENTESIS_APERTURA PARENTESIS_CIERRE LLAVE_APERTURA declaraciones LLAVE_CIERRE'''
    p[0] = "Programa correcto"

def p_declaraciones(p):
    '''declaraciones : declaraciones declaracion
                     | declaracion'''
    p[0] = p[1]  

def p_declaracion(p):
    '''declaracion : tipo IDENTIFICADOR PUNTOYCOMA
                   | declaracion_variable'''
    p[0] = p[1]  

def p_declaracion_variable(p):
    '''declaracion_variable : IDENTIFICADOR ASIGNAR expresion PUNTOYCOMA'''
    p[0] = p[1]

def p_instruccion(p):
    '''instruccion : READ IDENTIFICADOR PUNTOYCOMA
                   | PRINTF CADENA PUNTOYCOMA
                   | IDENTIFICADOR ASIGNAR expresion PUNTOYCOMA
                   | END PUNTOYCOMA
                   | WHILE PARENTESIS_APERTURA expresion PARENTESIS_CIERRE LLAVE_APERTURA declaraciones LLAVE_CIERRE'''
    p[0] = p[1]  

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR'''
    p[0] = p[1]  

def p_expresion(p):
    '''expresion : expresion SUMA termino
                 | expresion RESTA termino
                 | termino'''
    p[0] = p[1]  

def p_termino(p):
    '''termino : termino MULT factor
               | termino DIV factor
               | factor'''
    p[0] = p[1] 

def p_factor(p):
    '''factor : PARENTESIS_APERTURA expresion PARENTESIS_CIERRE
              | NUMERO
              | IDENTIFICADOR'''
    p[0] = p[1]  


def p_error(p):
    if p:
        error_message = f"Error de sintaxis cerca del token '{p.value}' en la línea {p.lineno}, columna {p.lexpos}."
        raise SyntaxError(error_message)
    else:
        raise SyntaxError("Error de sintaxis: fin inesperado de entrada.")


parser = yacc.yacc()


def analizar_sintaxis(codigo):
    try:
        result = parser.parse(codigo)
        return "La sintaxis ingresada está correctamente estructurada" if result else "Error de sintaxis"
    except SyntaxError as e:
        return str(e)