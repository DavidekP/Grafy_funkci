import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import functions as fn


def ensure_images_dir():
    os.makedirs("images", exist_ok=True)


def find_min_max(x, y):
    """Vrátí (x_min, y_min, x_max, y_max) pomocí NumPy."""
    i_min = np.argmin(y)
    i_max = np.argmax(y)
    return x[i_min], y[i_min], x[i_max], y[i_max]


def plot_single(name, x, y, title, filename):
    plt.figure(figsize=(9, 5))
    plt.plot(x, y, label=name)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Možnost C: vyznačení minima a maxima
    x_min, y_min, x_max, y_max = find_min_max(x, y)
    plt.scatter([x_min, x_max], [y_min, y_max], zorder=3)
    plt.annotate(
        f"min = ({x_min:.2f}, {y_min:.2f})",
        (x_min, y_min),
        textcoords="offset points",
        xytext=(10, 10),
    )
    plt.annotate(
        f"max = ({x_max:.2f}, {y_max:.2f})",
        (x_max, y_max),
        textcoords="offset points",
        xytext=(10, -15),
    )

    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close()


def main():
    ensure_images_dir()

    # x hodnoty: -10 až 10, alespoň 1000 bodů
    x = np.linspace(-10, 10, 1000)

    # Parametry (proměnné, ne natvrdo ve funkcích)
    lin_params = dict(a=1.5, b=-2.0)
    quad_params = dict(a=0.5, b=1.0, c=-3.0)
    sin_params = dict(k=1.0, amplitude=2.0, phase=0.0)
    exp_params = dict(a=0.2)
    rec_params = dict(a=5.0)

    available = {
        "linear": (
            "Lineární funkce",
            lambda t: fn.linear(t, **lin_params),
            "images/linear.png",
        ),
        "quadratic": (
            "Kvadratická funkce",
            lambda t: fn.quadratic(t, **quad_params),
            "images/quadratic.png",
        ),
        "sin": (
            "Sinusová funkce",
            lambda t: fn.sine(t, **sin_params),
            "images/sin.png",
        ),
        "exp": (
            "Exponenciální funkce",
            lambda t: fn.exponential(t, **exp_params),
            "images/exponential.png",
        ),
        "reciprocal": (
            "Reciproční funkce",
            lambda t: fn.reciprocal(t, **rec_params),
            "images/reciprocal.png",
        ),
    }

    # Možnost A: uživatel zvolí funkci
    # - bez argumentu vykreslí vše
    # - s argumentem vykreslí jen zvolenou
    args = sys.argv[1:]
    if len(args) == 1:
        key = args[0].lower()
        if key not in available:
            print("Neznámá funkce:", key)
            print("Dostupné:", ", ".join(available.keys()))
            sys.exit(1)

        title, f, filename = available[key]
        y = f(x)
        plot_single(key, x, y, title, filename)
        print(f"Uloženo: {filename}")
    else:
        # Vykreslení všech funkcí do samostatných souborů
        for key, (title, f, filename) in available.items():
            y = f(x)
            plot_single(key, x, y, title, filename)
            print(f"Uloženo: {filename}")

    # Kombinovaný graf (minimálně 3 funkce)
    plt.figure(figsize=(10, 6))
    plt.plot(x, fn.linear(x, **lin_params), label="linear", color="tab:blue")
    plt.plot(
        x,
        fn.quadratic(x, **quad_params),
        label="quadratic",
        color="tab:orange",
    )
    plt.plot(x, fn.sine(x, **sin_params), label="sin", color="tab:green")
    plt.title("Kombinovaný graf: linear + quadratic + sin")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/multiple_functions.png", dpi=200)
    plt.close()
    print("Uloženo: images/multiple_functions.png")

    # Experimentování: ukázka změny intervalu + parametru pro sin
    x2 = np.linspace(-20, 20, 1000)  # změna intervalu
    sin_params_exp = dict(k=2.0, amplitude=2.0, phase=0.0)  # změna parametru k
    y2 = fn.sine(x2, **sin_params_exp)
    plot_single(
        "sin",
        x2,
        y2,
        "Experiment: sin s k=2 na intervalu <-20, 20>",
        "images/experiment_sin.png",
    )
    print("Uloženo: images/experiment_sin.png")


if __name__ == "__main__":
    main()