```python
import random

def add_random_numbers(num_numbers=10):
    total = 0
    for _ in range(num_numbers):
        total += random.randint(1, 100)
    return total

print(add_random_numbers())
```