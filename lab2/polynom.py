
def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''

    if p_list == [] or all(element == 0 for element in p_list):
        return 0

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

def neg_poly(p_list):
    
    p_list = p_list.copy()

    for i in range(len(p_list)):
        p_list[i] *= -1

    return p_list
    

def add_poly(p_list,q_list):
    
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
    return add_poly(p_list, neg_poly(q_list))

if __name__ == '__main__':
    # Task 1
    p = [2, 0, 1]
    q = [-2, 1, 0, 0, 1]

    # Task 2
    p0 = [2, 0, 1, 0]
    q0 = [0, 0, 0]

    # print(add_poly(p, q))

    print(poly_to_string(p))

