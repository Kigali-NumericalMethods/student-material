## Problem set 2

1. Create an `ndarray` representing the following vector
$$
    \mathbf x = (1.0, 1.1, 1.0, 0.0, 33.0 ).
$$
	* Write code which evaluates $\mathbf y = \mathbf x + 16.0$.

	* Write code which evaluates the following expression
$$
    \alpha = \sqrt{\sum_{i=1}^5 \sqrt{x_i}}
$$
	Print the answer in expoential notation showing 6 digits after the decimal point.

2. Write a Python function which takes $N$ as an input, computes the factorial of $N$ and returns the result.
	* Test your function using
  		- $N = 7$
  		- $N = 0$
  		- $N = -2$
	* Write a better version of your factorial function which checks that $n$ is an integer, and that $n >= 0$. In the event that $n$ is not valid for use in your factorial function, force your function to report an appropriate error.

3. Consider the following mathematical function (from Problem set 1)
$$
  f(x) = \frac{\exp(x)}{ (\cos(x))^3 + (\sin(x))^3 }
$$
Write a Python function which evaluates $f(x)$ and returns the result. Make your Python function work with NumPy's `ndarray` objects. That is, the input should be an `ndarray` and the output should be an `ndarray`.



4. You are given two vectors, $\mathbf x \in \mathbb R^N, \mathbf y \in \mathbb R^N$  
Write a Python function which evaluates the $l_2$ error between two vectors via:
$$
    E = \sqrt{ \frac{1}{N} \sum_{i=1}^N (x_i - y_i)^2 }.
$$
Your function should have two arguments $\mathbf x, \mathbf y$ and return $E$.

	* Test your function using the vectors
$$
    x = (1.00012, 3.003, 7.0023 ),
$$
$$
    x_e = (1.0, 3.0, 7.0 ).
$$

