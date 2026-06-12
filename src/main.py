def add(a, b, c=0):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return "error"
        
    if not all(0 <= x <= 10 for x in (a, b, c)):
        return -2

    return a + b + c
