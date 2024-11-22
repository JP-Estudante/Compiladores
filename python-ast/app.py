import ast

# Função para verificar a validade de um nó na árvore sintática
def is_valid_node(node):
    if isinstance(node, ast.Assign):  # Atribuição
        return is_valid_node(node.value)
    
    elif isinstance(node, ast.BinOp):  # Operação Binária
        if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            left_valid = is_valid_node(node.left)
            right_valid = is_valid_node(node.right)
            return left_valid and right_valid
        return False
    
    elif isinstance(node, ast.Constant):  # Número
        return True
    
    elif isinstance(node, ast.Name):  # Identificador
        return True
    
    elif isinstance(node, ast.Expr):  # Expressão Raiz
        return is_valid_node(node.value)
    
    elif isinstance(node, ast.UnaryOp):  # Operação Unária
        if isinstance(node.op, (ast.UAdd, ast.USub)):
            return is_valid_node(node.operand)
        return False
    
    return False

# Função principal para verificar a expressão
def check_expression(expression):
    try:
        # Verifica se há uma atribuição
        if '=' not in expression:
            return False
        
        identifier, expr = expression.split("=", 1)
        identifier = identifier.strip()
        expr = expr.strip()
        
        # Gera a árvore sintática abstrata
        tree = ast.parse(expr, mode='eval') # Não sera tratada como instrução 
        assign_node = ast.Assign(targets=[ast.Name(id=identifier, ctx=ast.Store())], value=tree.body) # Simula um atribuição de valor em Python
        return is_valid_node(assign_node)
    
    except SyntaxError:
        return False

# Exemplos de uso
expressions = [
    "a = 3 + 4 * 2",  # Deve ser aceita
]

for expr in expressions:
    result = check_expression(expr)
    status = "Aceita" if result else "Não Aceita"
    print(f"Expressão: '{expr}' -> {status}")