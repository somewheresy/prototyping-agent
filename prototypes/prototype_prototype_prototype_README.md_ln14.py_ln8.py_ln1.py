```python
with open('./prototypes/prototype_prototype_README.md_ln14.py_ln8.py', 'r') as file:
    lines = file.readlines()
    todo_lines = [line for line in lines if '@TODO' in line]
```