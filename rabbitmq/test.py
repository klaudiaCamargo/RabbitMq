class Foo(object):
    def __init__(self):
        self.file = open("test.txt", "w")

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.file.close()

    def writer(self):
        print("Function...")
        self.file.write("qualquer coisa")

if __name__ == "__main__":
    with Foo() as f:
        f.writer()