# Python Script to Validate Your Results when Solving Final Exam of Applied Math

It's just a simple project that I made to validate my results when I solved the **Final Exam of Applied Math** at **Ho Chi Minh University of Science  - VNUHCM** using Python and Sympy. 

# Overview

Here is the matrix of final exam

```text
Question 1: Evaluate convexity of the given function.
	In this question, you will be given a multi-variables function and required to evaluate its convexity using Matrix knowledge and find the global maximum or minimum if have. 

    Solution:
    	1: find the ∇ of the function
        2: find the Hessian matrix
        3: Using Hessian matrix |H - Iλ| = 0 to find eigenvalues
        4: Check all eigenvalues:
            - If all of them are greater than 0 -> strictly convex
            - If all of them are greater or equal to 0 -> semi-strictly convex
            - If all of them are lower than 0 -> strictly convae
            - If all of them are lower or equal to 0 -> semi-strictly convae
        5: Solve ∇f = 0 to find the critical point
```
#### Validate Question 1

```shell
python convex_global_max_min.py
```