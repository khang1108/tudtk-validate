from sympy import oo, solve, symbols, sympify, Matrix, diff

def gradient(func, vars):
    """
    A function to compute the gradient of a given function with respect to its variables.

    Args:
        func (sympy expression): The function for which to compute the gradient.
        vars (list): A list of sympy symbols representing the variables.
    """

    gradient = [diff(func, var) for var in vars]
    return Matrix(gradient)

def gradient2(func, vars):
    """
    A function to compute the Hessian matrix of a given function with respect to its variables.

    Args:
        func (sympy expression): The function for which to compute the Hessian matrix.
        vars (list): A list of sympy symbols representing the variables.
    """

    hessian = []
    for var_x in vars:
        hessian_col = []
        for var_y in vars:
            hessian_ele = diff(diff(func, var_x), var_y)
            hessian_col.append(hessian_ele)
        hessian.append(hessian_col)
    return Matrix(hessian)

def evaluate_convexity(func, vars):
    """
    A function to check if a given function is convex based on its Hessian matrix.

    Args:
        func (sympy expression): The function to check for convexity.
        vars (list): A list of sympy symbols representing the variables.
    """

    hessian_matrix = gradient2(func, vars)
    raw_eigenvalues = hessian_matrix.eigenvals()
    eigenvalues = [float(eigenvalue.evalf().as_real_imag()[0]) for eigenvalue in raw_eigenvalues.keys()]

    print("Eigenvalues of the Hessian Matrix: ", eigenvalues)

    is_positive_definite = all(eigenvalue > 1e-10 for eigenvalue in eigenvalues)
    is_negative_definite = all(eigenvalue < -1e-10 for eigenvalue in eigenvalues)

    if is_positive_definite:
        return {"strictly": True, "status": "convex"}
    elif is_negative_definite:
        return {"strictly": True, "status": "concave"}
    else:
        return {"strictly": False, "status": "neither convex nor concave"}
    
def find_global_max_min(func, vars):
    """
    A function to find the global maximum and minimum of a given function.

    Args:
        func (sympy expression): The function for which to find the global maximum and minimum.
        vars (list): A list of sympy symbols representing the variables.
    """

    critical_points = []
    gradient_vector = gradient(func, vars)

    # Solve for critical points where the gradient is zero
    critical_points = solve(gradient_vector, vars, dict=True)
    
    if not critical_points:
        print("Hàm số không có điểm dừng. Không có cực trị hữu hạn.")
        return -oo, oo

    # Evaluate the function at critical points
    critical_values = [func.subs(point) for point in critical_points]

    # Find global maximum and minimum
    global_max = max(critical_values)
    global_min = min(critical_values)

    return global_max, global_min

if __name__ == "__main__":
    n = int(input("Enter the number of variables: "))

    variables = symbols(' '.join([f'x{i}' for i in range(1, n + 1)]))

    raw_function = input("Enter the function in terms of the variables (e.g., x1**2 + x2**2): ")

    function = sympify(raw_function)

    hessian_matrix = gradient2(function, variables)
    print("Hessian Matrix: ", hessian_matrix)

    convexity_result = evaluate_convexity(function, variables)
    global_max, global_min = find_global_max_min(function, variables)

    if convexity_result["strictly"]:
        print(f"The function is {convexity_result['status']}.")
        print(f"Global Maximum: {global_max}")
        print(f"Global Minimum: {global_min}")
    else:
        print("The function is not strictly convex or concave.")

    