import sys
import math


def read_coefficient(name, args, index):
    if index < len(args):
        try:
            return float(args[index])
        except ValueError:
            print(f"Аргумент для {name} некорректен ('{args[index]}'), введите с клавиатуры.")
    while True:
        try:
            return float(input(f"Введите коэффициент {name}: "))
        except ValueError:
            print("Ошибка: введите действительное число.")


def roots_from_t(t):
    """По неотрицательному t возвращает пару корней x = ±sqrt(t) (или [0.0])."""
    match t:
        case t if t < 0:
            return []
        case 0:
            return [0.0]
        case _:
            s = math.sqrt(t)
            return [s, -s]


def solve_biquadratic(a, b, c):
    if a == 0:
        match b:
            case 0:
                return []
            case _:
                return roots_from_t(-c / b)

    d = b * b - 4 * a * c

    match d:
        case d if d < 0:
            return []
        case 0:
            return roots_from_t(-b / (2 * a))
        case _:
            sqrt_d = math.sqrt(d)
            t1 = (-b + sqrt_d) / (2 * a)
            t2 = (-b - sqrt_d) / (2 * a)
            roots = roots_from_t(t1) + roots_from_t(t2)
            unique = []
            for r in roots:
                if r not in unique:
                    unique.append(r)
            return unique


def main():
    args = sys.argv[1:]
    a = read_coefficient("A", args, 0)
    b = read_coefficient("B", args, 1)
    c = read_coefficient("C", args, 2)

    print(f"\nУравнение: {a}*x^4 + {b}*x^2 + {c} = 0")
    roots = solve_biquadratic(a, b, c)

    if not roots:
        print("Действительных корней нет.")
    else:
        print("Действительные корни:")
        for r in roots:
            print(f"  x = {r}")


if __name__ == "__main__":
    main()