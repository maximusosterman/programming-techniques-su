
def check_all_zeros(list):
    """Checks if all elemtnts of list are zeros

    Args:
        list (numbers): list of polynomial

    Returns:
        _type_: boolean indicating whether there are zeros in list
    """
    for element in list:
        if element != 0:
            return False

    return True



def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''

    if p_list == [] or check_all_zeros(p_list): ## If list is empty or all contains zero
        return "0"

    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if coeff == 0:
            degree += 1
            continue
        if degree == 0:
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + 'x')
        else:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)
        degree += 1

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    final_string = final_string.replace("1x", "x")
    
    return final_string

def drop_zeros(p_list):
    """Removes worthless zeros from the end of a polynomial

    Args:
        list (numbers): list of polynomial

    Returns:
        _type_: Polynomial without zeros at the end of the polynomial
    """
    
    while len(p_list) != 0 and p_list[-1] == 0:
        del p_list[-1]

    return p_list

def eq_poly(p_list,q_list):
    """Checks equallity between two polynomials

    Args:
        p_list (numbers): list of polynomial
        q_list (numbers): list of polynomial

    Returns:
        _type_: boolen in which the polynomials are equal or not
    """
    return drop_zeros(p_list) == drop_zeros(q_list)

def eval_poly(p_list, x):

    """Evaluates polynomials when plugging in a value of x

    Args:
        p_list (numbers): list of polynomial
        x (number): value of x which will determine the sum the polynomial

    Returns:
        _type_: the sum of the polynomial
    """
    
    sum = 0

    for degree, coeff in enumerate(p_list):
        if degree == 0:
            sum += coeff # This to avoid the constant to be powered by the 0
        else:
            sum += coeff * x ** degree

    return sum

def neg_poly(p_list):

    """Negates the polynomial

    Args:
        p_list (numbers): list of polynomial

    Returns:
        _type_: Negated polynomial
    """
    
    p_list = p_list.copy()

    for i in range(len(p_list)):
        p_list[i] *= -1

    return p_list
    

def add_poly(p_list,q_list):
    """Adds two polynoms 

    Args:
        p_list (numbers): list of polynom
        q_list (numbers): list of polynom

    Returns:
        _type_: New polynom which is a sum of the two inputs
    """
    
    new_poly = []

    for i in range(max(len(p_list), len(q_list))):

        if i < len(p_list) and i < len(q_list):
            new_poly.append(p_list[i] + q_list[i])

        elif i < len(p_list):
            new_poly.append(p_list[i])
        elif i < len(q_list):
            new_poly.append(q_list[i])

    return new_poly



def sub_poly(p_list,q_list):
    """Subtracts two polynoms from each other. 

    Args:
        p_list (numbers): List of polynomial
        q_list (_type_): List of polynomial

    Returns:
        _type_: Subtracted polynomial 
    """
    return add_poly(p_list, neg_poly(q_list))

if __name__ == '__main__':
    
    # Task 1
    p = [2, 0, 1]
    q = [-2, 1, 0, 0, 1]

    # Task 2
    p0 = [2, 0, 1, 0]
    q0 = [0, 0, 0]

    print(check_all_zeros([0,0,0,0]))