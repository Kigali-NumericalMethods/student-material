
import numpy


def residual(x):
    raise RuntimeError("Please insert residual definition within `residual()`")
    #
    # REMOVE THE CALL TO `raise()` ABOVE. ADD RESIDUAL DEFINITION HERE.
    #
    F = # ADD CODE HERE

    return F

def jacobian(x):
    raise RuntimeError("Please insert Jacobian definition within `jacobian()`")
    #
    # REMOVE THE CALL TO `raise()` ABOVE. ADD JACOBIAN DEFINITION HERE.
    #
    J = # ADD CODE HERE
    return J


def solve_newton(x0, max_it, user_residual, user_jacobian):
    """
    Approximates a root x, of F(x) = 0 using an initial guess x0

    Input:
        x0: float
            Intial guess for x.
        max_it: int
            Maximum number of allowed iterations.
        user_residual: Callable Python function.
            Function to evaluate the nonlinear residual F(x).
        user_jacobian: Callable Python function.
            Function to evaluate the Jacobian of F(x).

    Output:
        x_star: float
            The approximate solution of F(x) = 0.
        it: int
            The number of iterations required to solve F(x) = 0.
    """

    it = 1
    x_star = x0

    while it <= max_it:

        F_star = user_residual(x_star)
        J_star = user_jacobian(x_star)

        print('%1.6d'%it, '%+1.16e'%x_star, '%+1.16e'%F_star)

        delta_x = -F_star / J_star

        x_star = x_star + delta_x

        if it == max_it:
            print('[Diverged] it == max_it')
            break

        #
        # ADD STOPPING CONDITIONS HERE
        #


        it += 1

    return x_star, it


x0 = 8.0
x, iterations = solve_newton(x0, 7000, residual, jacobian)
print("x =", "%+1.16e"%x, "iterations", iterations)
