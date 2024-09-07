import importlib
import json
import os
import random
import string

project_root = os.path.dirname(os.path.abspath(__file__))


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def run_benchmark(benchmark):
    module = importlib.import_module(f'benchmarks_code.{benchmark}')

    benchmark_obj = module.Benchmark()
    meta = module.meta

    elapsed = []
    benchmark_obj.setup()
    for i in range(100):
        elapsed.append(benchmark_obj.run_once())

    with open(f'{project_root}/benchmarks_results/{benchmark}.json', 'w') as f:
        json.dump({'elapsed': elapsed, **meta}, f, indent=2)
