import sympy as sp

def differentiate(expression, variable):
    x = sp.symbols(variable)
    expr = sp.sympify(expression)
    derivative = sp.diff(expr, x)
    return derivative

def integrate(expression, variable):
    x = sp.symbols(variable)
    expr = sp.sympify(expression)
    integral = sp.integrate(expr, x)
    return integral

if __name__ == "__main__":
    expression = input("Enter the mathematical expression:  ")
    variable = input("Enter the variable to differentiate or integrate with respect to:  ")

    derivative = differentiate(expression, variable)
    integral = integrate(expression, variable)

    print("Derivative:", derivative)
    print("Integral:", integral) 
    