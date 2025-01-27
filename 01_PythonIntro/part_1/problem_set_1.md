## Problem set 1

1. Store the value 1 as a real number in a variable $x$, and the value 2 as a real number in a variable $y$. Calculate $x + y$ and store the result in $z$. Print the value of $z$ in scientific notation and display the first 8 digits after the decimal point.  

2. Print the value of $\sqrt{\pi}$ to 4 digits after the decimal point. Use `math.pi` for $\pi$.

3. Consider the following mathematical function
$$
  f(x) = \frac{\exp(x)}{ (\cos(x))^3 + (\sin(x))^3 }
$$
	* Write a Python script which assigns as a value of $\pi/4$ to variable $z$, and then evaluates $f(z)$. Use `math.pi` for $\pi$.

4. Write a python script which computes the factorial of a number $N$. Compare the answer from your code using `math.factorial()`.
Test your code using
	* $N = 7$
	* $N = 0$

5. Given an integer $n > 0$, we wish to compute the value of $z$ given by
$$
    z = \sum_{i=1}^n i^2.
$$
	* Use an `if-else` conditional to check the value of $n$. If $n > 0$ and $n$ is an integer, compute $z$, otherwise report an error using `raise` with either `TypeError()` if $n$ is not an integer and `ValueError()` if $n$ is an integer but it is $<= 0$.
	* Test your code using
  		- $n$ = 1 ($z = 1$)
  		- $n$ = 3 ($z = 1 + 4 + 9 = 14$)
  		- $n$ = 3.3 (Error)
  		- $n$ = -3 (Error)
