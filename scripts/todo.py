import requests
import json
import os

MODEL = "gpt-4-32k"

def find_todos_in_file(file_path):
    todos = []
    with open(file_path, 'r') as f:
        for line_number, line in enumerate(f.readlines(), 1):
            if '@TODO' in line:
                # Prepare the payload
                payload = {
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": "Generates a suggested, expert-level completion of working python code to solve TODOs. Return all your results in .py files. DO NOT INCLUDE ANYTHING BUT EXECUTABLE PYTHON SCRIPT.\nCode context:\n" + str(f)},
                        {"role": "user", "content": f"TODO: {line}"}
                    ],
                    "temperature": 0
                }
                # Send the POST request
                response = requests.post(
                    'https://api.openai.com/v1/chat/completions',
                    headers={
                        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
                        'Content-Type': 'application/json'
                    },
                    data=json.dumps(payload)
                )
                # Extract the prototype from the response
                prototype = response.json()['choices'][0]['message']['content']
                # Ensure the /prototypes directory exists
                os.makedirs('prototypes', exist_ok=True)
                # Write the prototype to a .py file
                with open(f'prototypes/prototype_{os.path.basename(f.name)}_ln{line_number}.py', 'w') as prototype_file:
                    prototype_file.write(prototype)

                todos.append((line_number, line.strip()))

def write_todos_to_md(todos, md_file_path):
    with open(md_file_path, 'w') as f:
        for file_path, todo_list in todos.items():
            f.write(f'## {file_path}\n')
            for line_number, line in todo_list:
                f.write(f'- [ ] TODO at line {line_number}: {line}\n')
            f.write('\n')
def main():
        todos = {}
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.py') or file == 'README.md':
                    file_path = os.path.join(root, file)
                    todos_in_file = find_todos_in_file(file_path)
                    if todos_in_file:
                        todos[file_path] = todos_in_file
        write_todos_to_md(todos, 'TODO.md')
        
if __name__ == '__main__':
    main()
