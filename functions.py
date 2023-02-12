FILEPATH = "todos.txt"

FREEZING_POINT = 0

BOILING_POINT = 100


def get_todos(filepath=FILEPATH):
    """Get the items in the file as a list """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the given list to a file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def get_state(temperature):
    """a function that takes the given Celsius
     temperature of water and returns whether it is
     solid, liquid, or gas"""

    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"
