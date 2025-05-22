import numpy as np
import matplotlib.pyplot as plt
from sympy import *


def solve_and_plot(equations, x_range=(-10, 10), num_points=400):
    try:
        x, y = symbols('x y')
        plt.figure()  

        for equation in equations:
            solutions = solve(equation, y)

            if not solutions:
                print(f"Уравнение {equation} не имеет решений относительно y.")
                continue  

            x_values = np.linspace(x_range[0], x_range[1], num_points)

            for sol in solutions:
                try:
                    y_val = lambdify(x, sol, modules=['numpy'])
                    y_values = y_val(x_values)
                    plt.plot(x_values, y_values, label=f'{equation} - Solution: {sol}') 
                except NameError:
                    print(f"уравнение {sol} имеет неизвестные переменные.")

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Решение систем уравнений')  
        plt.grid(True)
        plt.legend()
        plt.show()

    except NameError:
        print("Уравнение должно содержать переменные x и y.")


def main():
    y, x = symbols(['y', 'x'])
    equations = [(y**2 + x**2 - 9), (y - x**2 + 2)]  

    if not isinstance(equations, (list, tuple)):
        equations = [equations] 

    solve_and_plot(equations)


if __name__ == "__main__":
    main()