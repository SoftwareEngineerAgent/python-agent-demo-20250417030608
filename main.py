```python
# main.py
import os
import openai
import pytest  # While imported, it might not be directly used here, but is a dependency of the project

# Load API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_code(prompt):
    """
    Generates Python code using OpenAI's GPT-3 model.

    Args:
        prompt (str): The prompt to guide the code generation.

    Returns:
        str: The generated Python code.  Returns None if there is an error.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another suitable engine
            prompt=prompt,
            max_tokens=200,  # Adjust as needed
            n=1,
            stop=None,
            temperature=0.7, # Adjust for desired randomness
        )

        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred during code generation: {e}")
        return None


def main():
    """
    Main function to orchestrate the AI agent and code generation process.
    """
    print("Starting the AI agent demo...")

    # Define a prompt for code generation
    prompt = """
    # Python program to calculate the factorial of a number.

    def factorial(n):
    """
    # Generate the code
    generated_code = generate_code(prompt)

    if generated_code:
        print("\nGenerated Code:\n")
        print(generated_code)

        # Option to save the generated code to a file (e.g., generated_script.py)
        try:
            with open("generated_script.py", "w") as f:
                f.write(generated_code)
            print("\nGenerated code saved to generated_script.py")
        except Exception as e:
            print(f"Error saving code to file: {e}")
    else:
        print("Failed to generate code.")

    print("\nDemo completed.")


if __name__ == "__main__":
    main()
```