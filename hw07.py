# Author: Your Name / your_email
# Date: 2024-09-01
# Assignment Name: hw07


import time
import numpy as np
import matplotlib.pyplot as plt

def p1(func, y0, tspan, n_steps, method):
    """
    # Implement the function to solve the ODE y' = f(t, y) 
    # using the specified method (euler, midpoint, rk4)
    # 
    # @param func: The function f(t, y).
    # @param y0: The initial condition y(0).
    # @param tspan: The time span [t0, tf].
    # @param n_steps: The number of time steps to take.
    # @param method: The method to use to solve the ODE.
    # @return: The solution array to the ODE at each time step.
    """

    # YOUR CODE HERE. Euler method is implemented for an example. Implement the other methods.

    h = (tspan[1] - tspan[0]) / n_steps
    t = np.linspace(tspan[0], tspan[1], n_steps + 1)
    y = np.zeros(n_steps + 1)
    y[0] = y0

    if method == 'euler':
        for i in range(n_steps):
            y[i + 1] = y[i] + h * func(t[i], y[i])
    elif method == 'midpoint':
        # your code for midpoint method here
        pass
    elif method == 'rk4':
        # your code for Runge Kutta 4th order method here.
        pass
    else:
        raise ValueError("Invalid method. Choose 'euler', 'midpoint', or 'rk4'.")

    return y

def p2():
    """
    # Test the implemented methods on the ODE
    # y' = t(y - t sin(t)) with initial condition y(0) = 1 over the interval
    #  [0, 1], [0, 3], and [0, 5] with variable step lengths. 
    # 
    # Plot the solution y(t) over the interval for various step sizes h. And plot the 
    # exact solution y(t) = t sin(t) + cos(t) over the same interval.
    #
    # Use the commands below to test the implemented methods:
    #
    #> p2('euler');
    #> p2('midpoint');
    #> p2('rk4');
    #
    # Observe the solution and error plots for the numerical solutions with different step sizes.
    # Write your observations in the comments. 

    # Your comment here (e.g, how does the error change with step size and the time span, etc.): 
    # 
    # 
    # 
    #
    #  
    """

    def f(t, y):
        return t * (y - t * np.sin(t))

    tf_values = [1, 3, 5]
    _, axs = plt.subplots(2, len(tf_values), figsize=(15, 10))

    for tf in tf_values:
        tspan = [0, tf]
        y0 = 1
        hs = np.array( [1e-1, 1e-1 * 10/11, 1e-1*4/5, 1e-1*0.72,
                         1e-1*0.64, 1e-1*1/2, 1e-1*2/5, 1e-1*0.32] )
        n_steps = np.array(  [int((tf - tspan[0]) / h) for h in hs] )
        error = np.zeros(len(n_steps))

        for i, n in enumerate(n_steps):
            t = np.linspace(tspan[0], tspan[1], n + 1)
            y_exact = t * np.sin(t) + np.cos(t)
            y_num = p1(f, y0, tspan, n, 'rk4')
            error[i] = np.max(np.abs(y_num - y_exact))

            axs[0, tf_values.index(tf)].plot(t, y_num, label=f'h = {hs[i]:.2e}')

        axs[1, tf_values.index(tf)].loglog(hs, error, 'g-d', label='error vs. n_steps')
        axs[1, tf_values.index(tf)].loglog(hs, error[0] * hs **4/ hs[0] ** 4, 'ro--',
                            linewidth=1, markersize=2, label='4th order convergence')
        axs[1, tf_values.index(tf)].loglog(hs, error[0] * hs **3/ hs[0] ** 3, 'bo--',
                            linewidth=1, markersize=2,  label='3rd order convergence')
        axs[1, tf_values.index(tf)].loglog(hs, error[0] * hs **2/ hs[0] ** 2, 'mo--',
                            linewidth=1,  markersize=2, label='2nd order convergence')
        axs[1, tf_values.index(tf)].loglog(hs, error[0] * hs **1/ hs[0] ** 1, 'ko--',
                            linewidth=1,  markersize=2,  label='1st order convergence')
        axs[0, tf_values.index(tf)].plot(t, y_exact, '--', label='Exact Solution', linewidth=2)
        axs[0, tf_values.index(tf)].set_title(f'numerical and exact solutions on [0, {tf}]')
        axs[0, tf_values.index(tf)].legend()
        axs[0, tf_values.index(tf)].set_xlabel('t')
        axs[0, tf_values.index(tf)].set_ylabel('y')

        axs[1, tf_values.index(tf)].set_title(f'max error vs step sizes for solution on [0, {tf}]')
        axs[1, tf_values.index(tf)].legend()
        axs[1, tf_values.index(tf)].set_xlabel('h')
        axs[1, tf_values.index(tf)].set_ylabel('Error')

    plt.tight_layout()
    plt.show()

def p3():
    """
    # For 6630 ONLY
    # First implement the 3/8 rule for Runge Kutta method.
    # 
    # The implementation should be done in the function rk4_38_rule below. 
    # It is a subfunction which can only be called within p3 method.
    #
    # Then run p3() and compare the results with the 4th order Runge Kutta method. 
    # 
    # Write your observations in the comments. 
    #
    # Your comment here (e.g, how does the error change with step size and the time span, 
    # is there a clear difference in the running time and error
    #  (you may need to run a few times to conclude), etc.): 
    # 
    #
    #
    #
    #
    """
    def rk4_38_rule(func, y0, tspan, n_steps):
        h = (tspan[1] - tspan[0]) / n_steps
        t = np.linspace(tspan[0], tspan[1], n_steps + 1)
        y = np.zeros(n_steps + 1)
        y[0] = y0

        # your code here.

        return y

    def f(t, y):
        return t * (y - t * np.sin(t))

    tf_values = [3, 5, 7]
    _, axs = plt.subplots(2, len(tf_values), figsize=(15, 10))

    for tf in tf_values:
        t0 = 0
        y0 = 1
        hs = 0.1 / 2 ** np.array([1, 2, 3, 4, 5, 6, 7, 8])
        error_rk4 = np.zeros(len(hs))
        error_rk4_38 = np.zeros(len(hs))
        runtime_rk4 = np.zeros(len(hs))
        runtime_rk4_38 = np.zeros(len(hs))

        for i, h in enumerate(hs):
            n_steps = int((tf - t0) / h)
            t = np.linspace(t0, tf, n_steps + 1)
            y_exact = t * np.sin(t) + np.cos(t)

            time_start = time.time()

            for _ in range(20):
                y_rk4 = p1(f, y0, [t0, tf], n_steps, 'rk4')
            time_end = time.time()
            runtime_rk4[i] = (time_end - time_start) / 20

            time_start = time.time()
            for _ in range(20):
                y_rk4_38 = rk4_38_rule(f, y0, [t0, tf], n_steps)
            time_end = time.time()

            runtime_rk4_38[i] = (time_end - time_start) / 20

            error_rk4[i] = np.max(np.abs(y_exact - y_rk4))
            error_rk4_38[i] = np.max(np.abs(y_exact - y_rk4_38))

        axs[0, tf_values.index(tf)].loglog(hs, error_rk4, 'b-d',
                                label='Max error vs step size (RK4)',
                                linewidth=1, markersize=5)
        axs[0, tf_values.index(tf)].loglog(hs, error_rk4_38, 'g-o',
                                label='Max error vs step size (3/8 Rule)',
                                linewidth=1, markersize=5)
        axs[0, tf_values.index(tf)].set_title(f'Max error vs step size on [0, {tf}]')
        axs[0, tf_values.index(tf)].legend()
        axs[0, tf_values.index(tf)].set_xlabel('h')
        axs[0, tf_values.index(tf)].set_ylabel('Error')

        axs[1, tf_values.index(tf)].loglog(hs, runtime_rk4, 'b-d',
                                label='run time of RK4', linewidth=1, markersize=5)
        axs[1, tf_values.index(tf)].loglog(hs, runtime_rk4_38, 'g-o',
                                label='run time of 3/8 Rule', linewidth=1, markersize=5)

        axs[1, tf_values.index(tf)].set_title(f'Runtime vs. step size on [0, {tf}]')
        axs[1, tf_values.index(tf)].legend()
        axs[1, tf_values.index(tf)].set_xlabel('h')
        axs[1, tf_values.index(tf)].set_ylabel('Run time')

    plt.tight_layout()
    plt.show()
    
