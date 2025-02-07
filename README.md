# Short course on Numerical Methods

Date: Jan 27 - Feb 07, 2025

Instructor: Dave May

## Overview

Numerical methods are ubiquitous in science. From pocket calculators, to using Google Maps, to modelling the dynamics of the atomsphere, oceans, planetary interiors and the universe we find applications of numerical methods.

In this course you will learn the foundational building blocks of numerical methods, going from how numbers are represented inside a computer, to how functions can be approximated, to how to obtain approximate _numerical_ solutions to ODEs and PDEs.

## Format and Philosophy

This is not a 100% theory class. Being proficient in numerical methods requires knowledge of the theory, along with pracical skiils to implement a numerical method into a piece of code which executes an algorithm. Numerical methods is not a "spectator sport" - you have to do it (code it) yourself to be good in numerical methods.

To facilitate the theory and practical aspects, most topics will be taught with the following structure

- **Theory session** (blackboard)
- **"Do-It-Yourself" (DIY)** coding session in which you implement the algorithms learned and apply them to a problem set. You will do the coding live in lectures - and I will assist you.
- **"Do-It-Using-Packages"** Many algorithms we will learn about already exist within Python packages. With the theory understood and having implemented them yourself, you will have a deep insight into how, when and why these algoritms work. You will then learn how to use the same algorithms from existing Python packages (these will generally be much more efficient than the algorithms we implemented ourselves). Often this part of a lecture will be a short walk through, followed by some exercises (usually repeating earlier problem sets but using a standard Python package).


## Topic schedule (tentative)

* Programming basics in Python (datatypes, arrays, plotting)
* Taylor series, function approximation, derivative approximation
* Interpolation in 1D
* Regression in 1D
* Errors, round-off, finite precision
* Numerical stability, ill conditioning
* Linear algebra (vectors, matrices, solvers)
* Solving non-linear problems (scalar and systems)
* Integration in 1D
* Solving Ordinary Differential Equations | scalar, systems


## Assessment

* Homweork (60%)
	- There will be three homeworks due on
		- Feb 01, 2025
		- Feb 06, 2025
		- Feb 11, 2025		
* Final exam (40%)
	- Feb 14, 2025 (time and location to be determined by C. Meriaux)

* The problem sets provided during lectures will constitute a large component of the homeworks issued.

## Electronic references

Below are five online references which are incredibly useful. I will refer to them via the name shown in quotes throughout lectures, or in problem sets.

1. "PyNumMeth"
	* Python Programming And Numerical Methods: A Guide For Engineers And Scientists
	* https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/Index.html
	* Python

2. "FNC" 
	* Fundamentals of Numerical Computation
	* https://fncbook.com  
	* Julia (Book link also contains Python example code)

3. "NumMeth_Sullivan"
	* Numerical Methods - An Inquiry-Based Approach With Python
	* https://numericalmethodssullivan.github.io  
	* Python

4. "NumMeth_LeMesurier"
	* Introduction to Numerical Methods and Analysis with Julia
	* https://lemesurierb.people.charleston.edu/introduction-to-numerical-methods-and-analysis-julia  
	* Julia

5. "NumMeth_Young"
	* Introduction to Numerical Methods and Matlab Programming for Engineers
	* http://www.ohiouniversityfaculty.com/youngt/IntNumMeth  
	* Matlab 



## Listing of problem sets

* Problem set 1: `01_PythonIntro/part_1/problem_set_1.pdf`
* Problem set 2: `01_PythonIntro/part_2/problem_set_2.pdf`
* Problem set 3 (function approx.): `02_FuncAndFuncDerivApproximation/problem_set_3.pdf`
* Problem set 4 (derivative function approx.): `02_FuncAndFuncDerivApproximation/problem_set_4.pdf`
* Problem set 5 (interpolation): `03_Interp/problem_set_5.pdf`
* Problem set 6 (regression): `04_Regression/problem_set_6.pdf`
* Problem set 7 (linear algebra): `06_LinearAlgebra/problem_set_7.pdf`
* Problem set 8 (nonlinear problems): `07_NonlinearProblems/problem_set_8.pdf`
* Problem set 9 (numerical integration): `08_Integration/problem_set_9.odf`
* Problem set 10 (ordinary differential equations): `09_ODEs/problem_set_10.pdf`

## Listing of homeworks

* Homework 1: `homework/numerical_methods_hw01.pdf`
* Homework 2: `homework/numerical_methods_hw02.pdf`
* Homework 3: `homework/numerical_methods_hw03.pdf`
