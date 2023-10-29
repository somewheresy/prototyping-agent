```python
# Open the file in read mode
with open('todo.py', 'r') as file:
    # Iterate over each line
    for line in file:
        # If '@TODO' is found in a line
        if '@TODO' in line:
            # Print that line
            print(line)
```