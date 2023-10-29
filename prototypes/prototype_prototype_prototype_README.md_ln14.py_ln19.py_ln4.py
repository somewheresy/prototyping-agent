def print_todo(file_path, todo):
    print(f'In file {file_path}, @TODO at line {todo[0]}: {todo[1]}')

# Usage:
# Assuming todo is a tuple where todo[0] is the line number and todo[1] is the todo text
# todo = (23, "Refactor this function")
# print_todo('./prototypes/prototype_prototype_README.md_ln14.py_ln19.py', todo)