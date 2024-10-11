from pyparsing import line


file_path = "io/input.niko"

# Dicionário de palavras-chave e seus equivalentes em Python
reserved_keywords = {
    "mein": "main",             # Marca o início do programa `main`
    "modoru": "return",         # Retorna um valor `return`
    "hyouji": "print",          # Imprime o texto `print`
    "nyuuryoku": "input",       # Lê o texto de entrada `input`
    "moshi": "if",              # Início de uma estrutura condicional `if`
    "sore igai": "else",        # Alternativa na estrutura condicional `else`
    "kurikaeshi": "for",        # Início de uma estrutura de repetição `for`
    "kokoromiru": "while",      # Início de uma estrutura de repetição `while`

    # Tipos de dados
    "seisuu": "int",            # Representa números inteiros `int`
    "shousuu": "float",         # Representa números decimais `float`
    "mojiretsu": "str",         # Representa sequências de caracteres `str`
    "shingi": "bool",           # Representa valores verdadeiro/falso `bool`
    # "mu": "None",               # Representa uma função que não retorna valor `None`
    # "nuru": "None",             # Representa um valor nulo `None`
    "shin": "True",             # Representa o valor verdadeiro `True`
    "gi": "False",              # Representa o valor falso `False`

    # Operadores Lógicos
    "katsu": "and",             # Representa o operador lógico `and`
    "mata wa": "or",            # Representa o operador lógico `or`
    "dewa nai": "not"           # Representa o operador lógico `not`
}

lines = []

def is_reserved_keyword(str):
    if str in reserved_keywords:
       return True 
    return False


with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line.strip()
        lines.append(line)

for line in lines:
        print(line) 