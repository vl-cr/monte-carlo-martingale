import time

class timeit:
    def __init__(self, print_str: str = 'Execution time'):
        self.print_str = print_str

    def __enter__(self):
        self.start = time.perf_counter()
        
    def __exit__(self, *args, **kwargs):
        end = time.perf_counter()
        print(f"{self.print_str}: {int(end - self.start)} s.")
