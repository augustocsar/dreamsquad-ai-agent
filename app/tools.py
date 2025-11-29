import math
from strands import tool

@tool
def calculator_tool(expression: str) -> str:
    """
    Realiza cálculos matemáticos baseados em uma expressão numérica.
    Útil para responder perguntas como "quanto é 1234 * 5678" ou raízes quadradas.
    
    Args:
        expression (str): A expressão matemática a ser calculada (ex: "1234 * 5678", "sqrt(144)").
    
    Returns:
        str: O resultado do cálculo ou uma mensagem de erro.
    """
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names.update({"abs": abs, "round": round})
    
    try:
        # AVISO: Em produção real, use bibliotecas como numexpr para segurança total.
        # Para o teste, eval com globais restritos é aceitável.
        code = compile(expression, "<string>", "eval")
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Uso de '{name}' não permitido.")
        
        result = eval(code, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Erro ao calcular: {str(e)}"