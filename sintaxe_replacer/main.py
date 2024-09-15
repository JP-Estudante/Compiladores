import os

def lerEntrada(path):
    read_lines = []
    
    with open(path, 'r') as file:
        for line in file:
            read_line = line.rstrip()
            
            read_lines.append(read_line)
        return read_lines

def remove_includes(code_lines):
    processed_lines = []

    for line in code_lines:
        if '#include' not in line: 
            processed_lines.append(line)
            
    return processed_lines

def semicolons_remove(code_lines):
    processed_lines = []
    
    for line in code_lines:
        processed_line = line.rstrip(';')
        
        processed_lines.append(processed_line)
        
    return processed_lines

def brackets_remove(code_lines):
    pilha = []
    processed_lines = []
    
    for line in code_lines:

        while '{' in line:
            push(pilha, '{')
            line = line.replace('{', '', 1)  # Remove o primeiro '{' encontrado

        while '}' in line:
            pop(pilha)
            line = line.replace('}', '', 1)  # Remove o primeiro '}' encontrado
        
        processed_lines.append(line)  # Adiciona a linha processada
    
    if (is_empty(pilha)): # Verifica se a pilha esta vazia
        return processed_lines
    else:
        raise IndexError("pilha não vazia, chave aberta que não foi fechada")

def create_output(code_lines, path):
    for line in code_lines:
        file = open(path, 'a')
        file.write('\n')
        file.write(line)
    file.close()

def is_file_empty(path):
    try:
        with open(path, 'r') as file:
            # Tenta ler o primeiro caractere
            return file.read(1) == ''
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{path}' não encontrado.")

  
# FUNÇÕES DA PILHA
def push(pilha, item):
    pilha.append(item)
    
def pop(pilha):
    if not pilha:
        raise IndexError("pop em uma pilha vazia")
    else:
        pilha.pop()

def size(pilha):
    return len(pilha)

def is_empty(pilha):
    return len(pilha) == 0

def main():
    input_path = "sintaxe_replacer/execution/input.txt"
    output_path = "sintaxe_replacer/execution/output.txt"
    pure_lines = lerEntrada(input_path) # Recebe o codigo não formatado para o python
    no_includes = remove_includes(pure_lines) # remove os `#includes` 
    no_semicolon_lines = semicolons_remove(no_includes) # remove do codigo os `;`
    formatted_lines = brackets_remove(no_semicolon_lines) # remove as `{}`
    
    print("\nENTRADA:")
    for pure_line in pure_lines:
        print(pure_line)
    
    # Saida
    if is_file_empty(output_path):
        create_output(formatted_lines, output_path)
    else:
        file = open(output_path, 'w')
        file.write('')
        create_output(formatted_lines, output_path)
             
if __name__ == "__main__":
    main()
    