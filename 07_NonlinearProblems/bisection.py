
import numpy


def residual(x):
    raise RuntimeError("Please insert residual definition within `residual()`")
    #
    # REMOVE THE CALL TO `raise()` ABOVE. ADD RESIDUAL DEFINITION HERE.
    #
    return F

def solve_bisection(x_min, x_max, max_it, user_residual):
    """
    Approximates a root x, of F(x) = 0 bounded
    between xmin <= x <= x_max within.

    Input:
        x_min: float
            Left value of interval.
        x_max: float
            Right value of interval.
        max_it: int
            Maximum number of allowed iterations.
        user_residual: Callable Python function.
            Function to evaluate the nonlinear residual F(x).

    Output:
        x_star: float
            The approximate solution of F(x) = 0.
        it: int
            The number of iterations required to solve F(x) = 0.
    """
    x_lower = x_min
    x_upper = x_max

    # Check if root contained within [x_lower, x_upper]
    # This requires F(x) changes sign
    if numpy.sign(user_residual(x_lower)) == numpy.sign(user_residual(x_upper)):
        raise ValueError("The root is not contained between [`x_min`, `x_max`]")

    it = 1

    while it <= max_it:
        x_star = (x_lower + x_upper)/2.0 # Get midpoint
        F_star = user_residual(x_star)

        print('%1.6d'%it, '%+1.16e'%x_star, '%+1.16e'%F_star)

        F_lower = user_residual(x_lower)
        if F_lower * F_star < 0.0:
            #
            # ADD CODE HERE TO UPDATE INTERVAL TO SEARCH
            #
        elif F_lower * F_star > 0.0:
            #
            # ADD CODE HERE TO UPDATE INTERVAL TO SEARCH
            #
        else: # F(x_star) == 0
            print('[Converged] F(x_star) == 0.0')
            break

        if it == max_it:
            print('[Diverged] it == max_it')
            break

        if (x_upper - x_lower)/2.0 < 1.0e-32:
            print('[Converged] interval is small')
            break

        #
        # ADD STOPPING CONDITIONS HERE
        #

        it += 1

    return x_star, it


x, iterations = solve_bisection(1.0, 2.0, 10000, residual)
print("x =", "%+1.16e"%x, "iterations", iterations)
