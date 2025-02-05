
import numpy

#
# Configure numpy to return nicely formatted values for arrays
#
numpy.set_printoptions(sign="+",formatter={'float': '{: 1.16e}'.format})

def residual_sys(x):
    F = numpy.zeros(3) # Initialize an empty vector of length 3 [DONT CHANGE THIS]

    raise RuntimeError("Please insert residual definition within `residual()`")
    #
    # REMOVE THE CALL TO `raise()` ABOVE. ADD RESIDUAL DEFINITION HERE.
    #

    F[0] = # ADD CODE HERE
    F[1] = # ADD CODE HERE
    F[2] = # ADD CODE HERE
    return F

def jacobian_sys(x):
    J = numpy.zeros((3, 3)) # Initialize an empty matrix of size 3x3 [DONT CHANGE THIS]

    raise RuntimeError("Please insert Jacobian definition within `jacobian()`")
    #
    # REMOVE THE CALL TO `raise()` ABOVE. ADD JACOBIAN DEFINITION HERE.
    #

    J[0, 0] = # ADD CODE HERE
    J[0, 1] = # ADD CODE HERE
    J[0, 2] = # ADD CODE HERE

    J[1, 0] = # ADD CODE HERE
    J[1, 1] = # ADD CODE HERE
    J[1, 2] = # ADD CODE HERE

    J[2, 0] = # ADD CODE HERE
    J[2, 1] = # ADD CODE HERE
    J[2, 2] = # ADD CODE HERE

    return J

def solve_newton_sys(x0, max_it, user_residual, user_jacobian):
    """
    Approximates a root x, of the vector function F(x) = 0
    using an initial guess x0.

    Input:
        x0: numpy.ndarray, shape = (3, )
            Intial guess for x.
        max_it: int
            Maximum number of allowed iterations.
        user_residual: Callable Python function.
            Function to evaluate the nonlinear residual F(x).
        user_jacobian: Callable Python function.
            Function to evaluate the Jacobian of F(x).

    Output:
        x_star: numpy.ndarray, shape = (3, )
            The approximate solution of F(x) = 0.
        it: int
            The number of iterations required to solve F(x) = 0.
    """

    it = 1
    x_star = numpy.copy(x0)

    while it <= max_it:

        F_star = user_residual(x_star)
        J_star = user_jacobian(x_star)

        F_star_norm = numpy.linalg.norm(F_star)

        print('%1.6d'%it, x_star, '|| %1.16e ||_2'%F_star_norm)

        delta_x = - numpy.linalg.solve(J_star, F_star)

        x_star = x_star + delta_x

        if it == max_it:
            print('[Diverged] it == max_it')
            break

        #
        # ADD STOPPING CONDITION HERE
        #

        it += 1

    return x_star, it


x0 = numpy.zeros(3)
x, iterations = solve_newton_sys(x0, 7000, residual_sys, jacobian_sys)
print("x =", x, "iterations", iterations)
