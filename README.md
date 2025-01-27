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
* Errors, round-off, finite precision
* Interpolation and Integration in 1D
* Linear algebra I (vectors, matrices, special case solvers)
* Linear algebra II (LU factorization, sparsity, sparse LU)
* Numerical stability, ill conditioning
* Root finding
* Solving systems of nonlinear equations
* Regression, interpolation in 2D
* Solving Ordinary Differential Equations | scalar, systems
* Solving Partial Differential Equations (finite difference for linear, nonlinear problems)


## Assessment

* To be determined.

* Completing the problem sets provided during lectures will constitute the homework component of your assessment for this course.

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
