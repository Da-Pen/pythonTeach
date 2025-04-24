# WITHOUT RUNNING THE PROGRAM: what does the following program print?

class A:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def f(self, p):
        print(f"{self.x} {self.y} {self.z} {p}")

    def g(self):
        print("qwerty")

class B(A):
    def __init__(self, x, y, q):
        super().__init__(x, y, "B_Z")
        self.q = q

    def f(self, p):
        super().f(p)
        print(f"abc {self.q}")

b = B("hello", "hi", "bye")
b.g()
b.f("p")

print(isinstance(b, A))
print(issubclass(type(b), A))

