# core/main.py - Version 1.0
commands = {}

def register_command(name, func):
    commands[name] = func

def handle_command(command_string):
    try:
        parts = command_string.split()
        command_name = parts[0]
        args = parts[1:]

        if command_name in commands:
            return commands[command_name](*args)
        else:
            return "Invalid command."
    except IndexError:
        return "Please enter a command."

def ping():
    return "Pong!"

register_command("ping", ping)

def add(x, y):
    try:
        return int(x) + int(y)
    except ValueError:
        return "Invalid input. Please provide numbers."

register_command("add", add)

# Example usage (for testing):
#print(handle_command("ping"))
#print(handle_command("add 5 3"))
#print(handle_command("add a 3"))
#print(handle_command(""))