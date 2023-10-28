```python
import os

def find_todos():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    for line_no, line in enumerate(f, start=1):
                        if '@TODO' in line:
                            print(f'File: {os.path.join(root, file)}')
                            print(f'Line Number: {line_no}')
                            print(f'Line: {line.strip()}')

if __name__ == "__main__":
    find_todos()
```
This script uses `os.walk` to traverse all directories starting from the current directory. For each file, it checks if the file extension is `.py` (indicating a Python file). If it is, it opens the file and iterates over each line. If the line contains `@TODO`, it prints the file path, line number, and the line itself.