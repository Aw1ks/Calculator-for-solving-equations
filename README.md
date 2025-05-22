# Calculator-for-solving-equations
This project provides a Python script that solves systems of equations (specifically, equations in terms of `x` and `y`) and visualizes the solutions by plotting them on a graph using `numpy`, `matplotlib`, and `sympy`.
## How to install
This project uses the following libraries:
*   [numpy](https://numpy.org/): For numerical computations and array handling.
*   [matplotlib](https://matplotlib.org/): For creating plots and visualizations.
*   [sympy](https://www.sympy.org/en/index.html): For symbolic mathematics, equation solving, and simplification.
To install the necessary dependencies, you can use `pip`:
```
pip install numpy matplotlib sympy
```
## How to use
1.  **Prepare your equations:**
    *   The script expects a list of equations where `x` and `y` are the variables.
    *   Ensure the equations are in a format that `sympy` can understand (e.g., `y**2 + x**2 - 9`).
    *   Modify the `equations` list within the `main()` function to include the equations you want to solve and plot.
2.  **Run the script:**
    ```bash
    python your_script_name.py  # Replace your_script_name.py with the actual file name
    ```
    The script will:
    *   Solve each equation for `y` in terms of `x`.
    *   Generate a plot displaying the solutions for each equation within a specified range.
    *   Handle cases where an equation has no solution for `y` or contains unknown variables.
## Example
The `main()` function in the provided code includes an example set of equations:
```
def main():
    y, x = symbols(['y', 'x'])
    equations = [(y2 + x2 - 9), (y - x**2 + 2)]
    solve_and_plot(equations)
```
This example will solve and plot the following equations:
*   `y**2 + x**2 - 9 = 0` (a circle)
*   `y - x**2 + 2 = 0` (a parabola)
