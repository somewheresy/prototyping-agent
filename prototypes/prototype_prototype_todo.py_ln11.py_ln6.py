```python
with open('./prototypes/prototype_todo.py_ln11.py', 'r') as file:
    for line in file:
        if '@TODO' in line:
            print(line)
```