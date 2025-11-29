import math
from strands import tool

@tool
def calculator_tool(expression: str) -> str:
    """
    Realiza cálculos matemáticos (ex: '2 * 5', 'sqrt(144)').
    """
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names.update({"abs": abs, "round": round})
    
    try:
        code = compile(expression, "<string>", "eval")
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Uso de '{name}' não permitido.")
        
        result = eval(code, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Erro ao calcular: {str(e)}"