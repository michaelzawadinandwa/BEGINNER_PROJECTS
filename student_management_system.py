class Student:
    def __init__(self, name: str, age: int, marks: list = None):
        self.name = name
        self.age = int(age)
        self.marks = list(marks) if marks is not None else []

    def add_mark(self, mark: float):
        if not (0 <= mark <= 100):
            raise ValueError("mark must be between 0 and 100")
        self.marks.append(float(mark))

    def average(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def grade(self) -> str:
        avg = self.average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age}, avg={self.average():.2f}, grade={self.grade()!r})"


def main():
    s1 = Student("Alice", 20, [95, 87, 92])
    s2 = Student("Bob", 19, [65, 70, 58])
    s3 = Student("Charlie", 21, [])

    for s in (s1, s2, s3):
        print(f"{s.name}: age={s.age}, average={s.average():.2f}, grade={s.grade()}")


if __name__ == "__main__":
    main()
        