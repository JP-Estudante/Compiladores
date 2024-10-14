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

delimiters = {' ','=',';','{','}','[',']'}
operators = {'=', '+', '-', '*', '/'}


def is_reserved_keyword(str):
    if str in reserved_keywords:
       return True 
    return False


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return []
    except IOError:
        print(f"Erro: Não foi possível ler o arquivo '{file_path}'.")
        return []


def analyze_line(lines):
    tokens = [] # Lista com os tokens
    token = ""
    
    for line in lines:
        for char in line:
            if char in delimiters or char in operators:
                if token:
                    tokens.append(token)
                    token = ""
            token += char
        return tokens
            
file_path = "io/input.niko"
lines = read_file(file_path)
print(analyze_line(lines))