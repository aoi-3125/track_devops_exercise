def add(a, b, c=0):
    try:

        ab = a + b
        result = int(ab) + int(c)
        return result
    except:
        return "error"
