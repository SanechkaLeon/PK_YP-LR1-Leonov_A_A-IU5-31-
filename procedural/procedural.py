import sys
import math


def read_coefficient(name, args, index):
    """
    Возвращает коэффициент: сначала пытается взять из аргументов командной строки,
    если аргумента нет или он некорректен — запрашивает с клавиатуры до корректного ввода.
    """
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


def solve_biquadratic(a, b, c):
    """
    Решает биквадратное уравнение a*x^4 + b*x^2 + c = 0.
    Возвращает список действительных корней (без дубликатов).
    """
    if a == 0:
        if b == 0:
            return []
        t = -c / b
        if t < 0:
            return []
        if t == 0:
            return [0.0]
        return [math.sqrt(t), -math.sqrt(t)]

    d = b * b - 4 * a * c

    if d < 0:
        return []

    if d == 0:
        t = -b / (2 * a)
        if t < 0:
            return []
        if t == 0:
            return [0.0]
        return [math.sqrt(t), -math.sqrt(t)]

    sqrt_d = math.sqrt(d)
    t1 = (-b + sqrt_d) / (2 * a)
    t2 = (-b - sqrt_d) / (2 * a)

    roots = []
    for t in (t1, t2):
        if t > 0:
            roots.extend([math.sqrt(t), -math.sqrt(t)])
        elif t == 0:
            roots.append(0.0)

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