```python
with open('./prototypes/prototype_README.md_ln14.py', 'r') as file:
    for line in file:
        if '@TODO' in line:
            print(line)
```