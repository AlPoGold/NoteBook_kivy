import view.ui_console
import model.note as mnote
import model.work_with_file as wwf

notebook_list = []


def open_file():
    notebook_list_string = wwf.read()
    if notebook_list_string != []:
        view.ui_console.message_open()
        for elem in notebook_list_string:
            notebook_list.append(return_notes(elem))
        print(notebook_list)
    else:
        view.ui_console.message_empty()


def save_file():
    wwf.write(notebook_list)
    view.ui_console.message_save()


def select_by_date():
    view.ui_console.find_by_date()
    find_date = input()
    res = []
    for note in notebook_list:
        if find_date==note.get_edit_date()[:10] or find_date==note.get_creation_date()[:10]:
            if note not in res:
                res.append(note)
    if res!=[]:
        print(*res, sep='\n')
    else:
        view.ui_console.find_by_date_error()



def add_note():
    view.ui_console.message_title()
    title = input()

    view.ui_console.message_body()
    text = input()

    new_note = mnote.Note(title, text)
    notebook_list.append(new_note)
    print(new_note)


def edit_note():
    view.ui_console.message_edit()
    id_find = input()
    find_elem = False
    for elem in notebook_list:
        if elem.id == id_find:
            find_elem = True
            view.ui_console.message_edit_title()
            new_title = input()
            if new_title != "":
                elem.title = new_title
            view.ui_console.message_edit_body()

            new_body = input()

            if new_body != "":
                elem.body = new_body

            elem.set_edit_date()
    if not find_elem:
        view.ui_console.message_not_find()


def find_note():
    view.ui_console.message_find()
    find_part = input()
    result = []
    for note in notebook_list:
        for item in note.__dict__.values():
            if find_part in item and note not in result:
                result.append(note)
    for i in result:
        print(i)


def delete_note():
    view.ui_console.delete_note()
    show_notes()

    id_delete_note = input()
    flag = True
    for i in range(len(notebook_list)):
        if notebook_list[i].get_id() == id_delete_note:
            flag = False
            del notebook_list[i]
            view.ui_console.delete_note_success()
            break

    if(flag):
        view.ui_console.message_not_find()


def show_notes():
    # for elem in notebook_list:
    #     print(elem)
    answer = "\n".join(notebook_list)
    return f"{answer}"


def return_notes(note_string):
    list_attributes = note_string.split(';')
    note = mnote.Note(list_attributes[1], list_attributes[2], list_attributes[3], list_attributes[4])
    note.set_id(list_attributes[0])
    return note
