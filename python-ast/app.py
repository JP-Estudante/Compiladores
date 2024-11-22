import ast
from graphviz import Digraph

# Função para gerar a árvore de execução
def generate_execution_tree(node, graph, parent_id=None):
    node_id = str(id(node))  # Identificador único para cada nó
    
    if isinstance(node, ast.Assign):
        graph.node(node_id, "Assign: =")
        if parent_id:
            graph.edge(parent_id, node_id)
        
        # Lado esquerdo (identificador)
        for target in node.targets:
            generate_execution_tree(target, graph, node_id)
        
        # Lado direito (expressão)
        generate_execution_tree(node.value, graph, node_id)
    
    elif isinstance(node, ast.BinOp):
        op_map = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/"}
        op_label = op_map[type(node.op)]
        graph.node(node_id, op_label)
        if parent_id:
            graph.edge(parent_id, node_id)
        
        # Operandos esquerdo e direito
        generate_execution_tree(node.left, graph, node_id)
        generate_execution_tree(node.right, graph, node_id)
    
    elif isinstance(node, ast.Name):
        graph.node(node_id, f"Identifier: {node.id}")
        if parent_id:
            graph.edge(parent_id, node_id)
    
    elif isinstance(node, ast.Constant):
        graph.node(node_id, f"Number: {node.value}")
        if parent_id:
            graph.edge(parent_id, node_id)

# Função principal para criar a visualização
def visualize_expression(expression):
    try:
        # Parse da expressão para gerar a árvore sintática
        tree = ast.parse(expression, mode='exec')
        
        # Criar um gráfico com Graphviz
        graph = Digraph(format='png')
        graph.attr(rankdir="TB")  # Orientação de cima para baixo
        
        # Gerar nós para a árvore
        for node in tree.body:
            generate_execution_tree(node, graph)
        
        # Renderizar o gráfico
        graph.render("execution_tree", view=True)  # Salva e abre a árvore como um arquivo
    except Exception as e:
        print(f"Erro ao gerar a árvore: {e}")

# Testar com a expressão do exemplo
expression = "a = 3 + 4 * 2"
visualize_expression(expression)
