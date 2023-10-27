# Project Overview

This project is designed to automatically generate Python code prototypes to solve TODOs in a codebase. It uses OpenAI's GPT-4 model to generate the prototypes. The project is structured as a Python script that can be run locally or as a GitHub Action.

@TODO: Test the feature and provide a Python program which creates a diagram for the program

## File Structure

- `scripts/todo.py`: This is the main script that scans the codebase for TODOs, generates prototypes for each TODO, and writes a markdown file with all the TODOs.
- `run.py`: This script is a simple runner for `todo.py`.
- `.github/workflows/generate_prototypes_from_TODO.yml`: This is a GitHub Action workflow that runs `todo.py` whenever there's a push to the main branch.

## How It Works

1. The script scans the entire codebase for files ending in `.ts` or named `README.md`.
2. For each file, it looks for lines containing `@TODO`.
3. For each TODO, it sends a POST request to OpenAI's API with the TODO as the prompt.
4. The response from the API is written to a new Python file in the prototypes directory.
5. All the TODOs are written to a markdown file named `TODO.md`.

## Running the Script

To run the script locally, you need to have Python installed. You can run the script using the command:

`python run.py`


## GitHub Action

The GitHub Action is set up to run on every push to the main branch. It checks out the code, sets up Python, installs the necessary dependencies, and runs `todo.py`.

## Environment Variables

The script requires the OPENAI_API_KEY environment variable to be set. This is the API key for OpenAI's API. The Github Action pulls it from Github Secrets.

`export OPENAI_API_KEY=<your_API_key_here>`

## Output

The script generates a markdown file named `TODO.md` with all the TODOs in the codebase. For each TODO, it also generates a Python file in the prototypes directory with a suggested solution.

## Code Snippets

The main function of the script is in `scripts/todo.py`:
