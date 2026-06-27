# Python Script to Validate Your Results When Solving the Applied Math Final Exam

This is a simple project I made to validate my results while solving the **Applied Math Final Exam** at **Ho Chi Minh University of Science - VNUHCM** using Python and SymPy.

# Overview

Here is the structure of the final exam:

```text
Question 1: Evaluate the convexity of the given function.
	In this question, you will be given a multivariable function and asked to evaluate its convexity using matrix methods, then find the global maximum or minimum if one exists.

    Solution:
    	1: Find the gradient ∇f of the function
        2: Find the Hessian matrix
        3: Use the Hessian matrix and solve |H - Iλ| = 0 to find the eigenvalues
        4: Check all eigenvalues:
            - If all of them are greater than 0 -> strictly convex
            - If all of them are greater than or equal to 0 -> convex
            - If all of them are less than 0 -> strictly concave
            - If all of them are less than or equal to 0 -> concave
        5: Solve ∇f = 0 to find the critical point
```
#### Validate Question 1

```shell
python convex_global_max_min.py
```

You will be asked to enter the `number of variables` and the `function` (for example: `3*x**2`, `2*y**2`, etc.).
