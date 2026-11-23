import sys
import math


class BiquadraticEquation:
    """Биквадратное уравнение a*x^4 + b*x^2 + c = 0."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def _read_coefficient(name, args, index):
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

    @classmethod
    def from_input(cls, args):
        a = cls._read_coefficient("A", args, 0)
        b = cls._read_coefficient("B", args, 1)
        c = cls._read_coefficient("C", args, 2)
        return cls(a, b, c)

    def discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        a, b, c = self.a, self.b, self.c

        if a == 0:
            if b == 0:
                return []
            t = -c / b
            if t < 0:
                return []
            if t == 0:
                return [0.0]
            return [math.sqrt(t), -math.sqrt(t)]

        d = self.discriminant()
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

    def __str__(self):
        return f"{self.a}*x^4 + {self.b}*x^2 + {self.c} = 0"


def main():
    eq = BiquadraticEquation.from_input(sys.argv[1:])
    print(f"\nУравнение: {eq}")

    roots = eq.solve()
    if not roots:
        print("Действительных корней нет.")
    else:
        print("Действительные корни:")
        for r in roots:
            print(f"  x = {r}")


if __name__ == "__main__":
    main()