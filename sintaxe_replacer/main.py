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

def remover_semicolons(code_lines):
    processed_lines = []
    
    for line in code_lines:
        processed_line = line.rstrip(';')
        
        processed_lines.append(processed_line)
        
    return processed_lines

def remover_brackets(code_lines):
    pilha = []
    processed_lines = []
    
    for line in code_lines:
        if '{' in line: 
            push(pilha, '{') # Adiciona na pilha, pois encontrou `{`
            processed_line = line.rstrip('{') # Remove do codigo o `{`
            processed_lines.append(processed_line) # Adiciona na lista a linha, já formatada
        elif '}' in line:
            pop(pilha) # Remove da pilha, pois encontrou `}`
            processed_line = line.rstrip('}') # Remove do codigo o `}`
            processed_lines.append(processed_line) # Adiciona na lista a linha, já formatada
        else:
            processed_lines.append(line) # Adiciona na lista a linha, já formatada   
             
    return processed_lines

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

def main():
    input_path = "sintaxe_replacer/execution/input.txt"
    output_path = "sintaxe_replacer/execution/output.txt"
    pure_lines = lerEntrada(input_path) # Recebe o codigo não formatado para o python
    no_includes = remove_includes(pure_lines) # remove os `#includes` 
    no_semicolon_lines = remover_semicolons(no_includes) # remove do codigo os `;`
    formatted_lines = remover_brackets(no_semicolon_lines) # remove as `{}`
    
    
    print("\nENTRADA:")
    for pure_line in pure_lines:
        print(pure_line)
    
    # Saida
    for formatted_line in formatted_lines:
        file = open(output_path, 'a')
        file.write('\n')
        file.write(formatted_line)
    file.close()
        
if __name__ == "__main__":
    main()
    