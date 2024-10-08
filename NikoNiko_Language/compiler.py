file_path = "io/input.niko"

keywords = [
    "mein",         # Marca o início do programa `main`
    "modoru",       # Retorna um valor `return`
    "hyouji",       # Imprime o texto `printf`
    "nyuuryoku",    # Lê o texto de entrada `scanf`
    "moshi",        # Início de uma estrutura condicional `if`
    "sore igai",    # Alternativa na estrutura condicional `else`
    "kurikaeshi",   # Início de uma estrutura de repetição `for`
    "kokoromiru",   # Início de uma estrutura de repetição `while`
    
    # Regras de formação: Letras (a-z, A-Z) e números (0-9), não começando com número
    "seisuu",       # Representa números inteiros `int`
    "shousuu",      # Representa números decimais `float`
    "mojiretsu",    # Representa sequências de caracteres `char`
    "shingi",       # Representa valores verdadeiro/falso `bolean`
    "mu",           # Representa uma função que não retorna valor `void`
    "nuru"          # Representa um valor nulo `nuru`
    "shin"          # Representa o valor verdadeiro `true`
    "gi"            # Representa o valor falso `false`
    
    # Operadores Lógicos 
    "katsu" # Representa o `&&`
    "mata wa" # Representa o `||`
    "dewa nai" # Representa a `!`
]

def is_keyword(str):
    if str in keywords:
       return True 
    return False

# Lendo o arquivo linha por linha
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # strip() remove espaços em branco extras e quebras de linha
        if 
            print(word)
             
print(is_keyword('men'))