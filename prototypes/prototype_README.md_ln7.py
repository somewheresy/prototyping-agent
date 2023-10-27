# Here is an example script that reads a file and prints its content.

```python
# Open the file in read mode
with open('./README.md', 'r') as file:
    # Read the content of the file
    content = file.read()

# Print the content of the file
print(content)
```