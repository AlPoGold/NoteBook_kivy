
PATH = r"C:\Users\Админ\PycharmProjects\NB_kivy\files\notebook.csv"

def read(path=PATH):
    with open(path, 'r') as file:
        notebook = [line.strip() for line in file.readlines()]
        return notebook


def write(notebook, path=PATH):
    with open(path, 'w') as file:
        for elem in notebook:
            file.write(elem.to_string())
            file.write('\n')


