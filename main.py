import ollama
import subprocess

def extract_code_blocks(text):
    code_blocks = []
    in_code_block = False
    current_block = []

    for line in text.split('\n'):
        if line.strip() == '```':
            if in_code_block:
                code_blocks.append('\n'.join(current_block))
                current_block = []
            in_code_block = not in_code_block
        elif in_code_block:
            current_block.append(line)
    print(code_blocks)
    return code_blocks

def get_code_example():
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': "Please provide a flask example related to books with Python language. There are 3 methods. GET books list, ADD a book or delete a book from the list.  Only write code and no explanation"},
    ])
    return response['message']['content']

# Function to write code blocks to a file
def write_code_to_file(code_blocks, filename="extracted_code.py"):
    with open(filename, "w") as file:
        for block in code_blocks:
            file.write(block + '\n\n')
            
def run_code_file(filename="extracted_code.py"):  # Corrected filename here
    subprocess.run(["python3", filename], check=True)

if __name__ == "__main__":
    example_text = get_code_example()  # Get the example text from ollama
    code_blocks = extract_code_blocks(example_text)  # Extract code blocks from the example text
    write_code_to_file(code_blocks)  # Write the extracted code blocks to a file
    run_code_file()  # Run the written file
