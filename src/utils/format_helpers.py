def replace_comma_with_dot(value):
    return round(float(value.replace(",", ".")), 3)

def put_missing_commas(value):
    if isinstance(value, int): 
        value = str(value)
    
    if not isinstance(value, float) and ',' not in value:
        return value[:2] + ',' + value[2:]
    return value

def replace_percentage(value):
    value = value.replace("%", "")
    value = value.replace(",", ".")
    return round(float(value), 2)