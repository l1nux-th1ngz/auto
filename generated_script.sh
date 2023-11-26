def generate_bash_script(commands, script_name='generated_script.sh'):
    # Open the script file in write mode
    with open(script_name, 'w') as script_file:
        # Add the shebang line
        script_file.write('#!/bin/bash\n\n')

        # Add the provided commands
        for command in commands:
            script_file.write(command + '\n')

    print(f"Bash script '{script_name}' generated successfully!")

# Example usage
if __name__ == "__main__":
    # Replace these commands with your own
    custom_commands = [
        'echo "Hello, World!"',
        'ls -l',
        'mkdir example_directory',
        'cd example_directory',
        'touch new_file.txt',
    ]

    # Generate the Bash script
    generate_bash_script(custom_commands)
