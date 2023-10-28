```python
import os

def find_todos(file_path):
    todos = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file_path, 1):
            if '@TODO' in line:
                todos.append((line_number, line.strip()))
    return todos

def main():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                todos = find_todos(file_path)
                for todo in todos:
                    print(f'In file {file_path}, @TODO at line {todo[0]}: {todo[1]}')

if __name__ == '__main__':
    main()
```