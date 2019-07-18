def compute(string):
<<<<<<< HEAD
    """Perform simple arithmetic based on string input.
    
    Example: '5 + 7' -> 12
    """
    values = string.split(' ')
    num0 = int(values[0])
    num1 = int(values[2])
    operator = values[1]
    if operator == '+':
        return num0 + num1
    elif operator == '-':
    	return num0 - num1
    else:
    	raise ValueError('Unknown operator!')
=======
	values = string.split(' ')
	num0 = int(values[0])
  	num1 = int(values[2])
	operator = values[1]
	if operator == '+':
		return num0 + num1
	elif operator == '-':
		return num0 - num1
	else:
		msg = f'Unknown operator: "{operator}"'
		msg += 'Choose from "+" and "-"'
		raise ValueError(msg)
>>>>>>> better-error
