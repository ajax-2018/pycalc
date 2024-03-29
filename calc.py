def compute(string):
    """Perform simple arithmetic based on string input.
    Supports all basic operators and floats.
    
    Example: '5 + 7' -> 12
    """
    values = string.split(' ')
    num0 = float(values[0])
    num1 = float(values[2])
    operator = values[1]
    if operator == '+':
        return num0 + num1
    elif operator == '-':
    	return num0 - num1
    elif operator == '*':
    	return num0 * num1
    else:
	msg = f'Unknown operator: "{operator}"\n'
	msg += 'Choose from "+" and "-".'
	raise ValueError(msg)
