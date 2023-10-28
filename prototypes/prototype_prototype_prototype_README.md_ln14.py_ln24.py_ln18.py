```python
import os

# Traverse all directories starting from the current directory
for root, dirs, files in os.walk("."):
    for file in files:
        # Check if the file extension is .py
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                # Iterate over each line
                for line_no, line in enumerate(f, start=1):
                    # If the line contains @TODO, print the file path, line number, and the line itself
                    if '@TODO' in line:
                        print(f'File: {file_path}, Line: {line_no}, Content: {line.strip()}')
```