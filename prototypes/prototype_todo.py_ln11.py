# Here is the completion of the TODO in the python code

```python
with open('./scripts/todo.py', 'r') as file:
    for line in file:
        if '@TODO' in line:
            print(line)
```

This script will open the file 'todo.py' in read mode and iterate over each line. If '@TODO' is found in a line, it will print that line.