
import math
import numpy
import matplotlib.pyplot as plt

def ivp_solve_euler(t0, t1, y0, dt):
    """
    Solve an ODE using Forward Euler.

    Input:
        t0: float
            Start time
        t1: float
            End time
        y0: float
            Value of y(time=t0)
        dt: float
            Time step

    Output:
        thist: numpy.ndarray, shape = (nsteps, )
            time for each time step taken.
        yhist: numpy.ndarray, shape = (nsteps, )
            y_approximate at all time steps.
        yehist: numpy.ndarray, shape = (nsteps, )
            y_exact at all time steps.
    """

    nsteps = int((t1 - t0)/dt) + 1

    thist = numpy.zeros(nsteps)
    yhist = numpy.zeros(nsteps)
    yehist = numpy.zeros(nsteps)

    time = t0
    y = y0

    # Define the exact solution
    y_exact = 0.1 * math.cos(4.0 * time) + 0.2 * math.sin(4.0 * time) + 2.9 * math.exp(-2.0 * time)

    thist[0] = time
    yhist[0] = y
    yehist[0] = y_exact

    for step in range(1, nsteps):

        f = # ADD CODE HERE

        y = y + dt * f  # Perform the Euler step
        time += dt      # Update time

        y_exact = 0.1 * math.cos(4.0 * time) + 0.2*math.sin(4.0 * time) + 2.9 * math.exp(-2.0 * time)

        # Record the time, y and the exact value for y
        thist[step] = time
        yhist[step] = y
        yehist[step] = y_exact

    return thist, yhist, yehist


# ==========================================================

dt = 0.1 # Time step

# Call the solver
t, y, y_exact = ivp_solve_euler(0.0, 8.0, 3.0, dt)

# Report the error at t1 = 8.0
print('error at final time', '%1.8e'%math.fabs(y[-1] - ye[-1]))

# Make a simple plot
plt.plot(t, y, label='forward-Euler')
plt.plot(t, y_exact, label='exact')
plt.legend()
plt.show()
