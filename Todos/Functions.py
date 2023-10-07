def open_read(filepath="todos_run.txt"):
    """
    open todos text file and read its content
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        return (todos_local)

def open_write(todos_arg, filepath="todos_run.txt"):
    """ open todos text file and change its content"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)