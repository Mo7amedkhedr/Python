import sys

def script_with_command():
   
    script_name = sys.argv[0]
    print(f"Script name: {script_name}")

    
    arguments = sys.argv[1:]
    if arguments:
        print(f"Arguments passed {len(arguments)} : ")
        for index, arg in enumerate(arguments, start=1):
            print(f"Argument {index}: {arg}")
    else:
        print("No arguments passed.")


script_with_command()
