def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if degree == 0:
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + 'x')
        else:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)
        degree += 1

    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string

def drop_zeros(p_list):
    
    while len(p_list) != 0 and p_list[-1] == 0:
        del p_list[-1]

    return p_list

def eq_poly(p_list,q_list):
    return drop_zeros(p_list) == drop_zeros(q_list)

def eval_poly(p_list, x):
    
    sum = 0

    for degree, coeff in enumerate(p_list):
        if degree == 0:
            sum += coeff
        else:
            sum += coeff * x ** degree

    return sum

if __name__ == '__main__':
    # Task 1
    p = [2, 0, 1]
    q = [-2, 1, 0, 0, 1]

    # Task 2
    p0 = [2, 0, 1, 0]
    q0 = [0, 0, 0]

    print(eval_poly(q,-2))

