def write_bash_script():
    filename = input("Enter the name of the bash script: ")
    command = input("Enter the command to be written in the bash script: ")

    with open(filename, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write(command + "\n")

write_bash_script()
