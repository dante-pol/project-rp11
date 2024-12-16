def validate_text(a:str, b:str, c:str):
    if not a.replace("-", "").replace(".", "").isdigit():
        return False
    
    if not b.replace("-", "").replace(".", "").isdigit():
        return False
    
    if not c.replace("-", "").replace(".", "").isdigit():
        return False
    
    return True


def calculate_area(a: float, b: float, c: float) -> float:
    import math
    
    if a > b + c or b > c + a or c > a + b:
        return None
    
    p = (a + b + c) / 2

    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return area 