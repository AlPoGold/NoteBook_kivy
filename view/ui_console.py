import view.text
import view.methods


def main_menu():
    view.methods.printmenu(view.text.start_menu)
def message_error_input():
    view.methods.printmessage(view.text.error_input)

def message_action():
    view.methods.printmessage(view.text.request_action)

def message_exit():
    view.methods.printmessage(view.text.exit_message)

def message_title():
    view.methods.printmessage(view.text.title)

def message_body():
    view.methods.printmessage(view.text.body)


def message_find():
    view.methods.printmessage(view.text.find_message)
    
    
def message_open():
    view.methods.printmessage(view.text.open_message)
    
    
def message_save():
    view.methods.printmessage(view.text.save_message)
    
    
def message_empty():
    view.methods.printmessage(view.text.empty_message)
    
def message_edit():
    view.methods.printmessage(view.text.edit_message)
    
def message_edit_title():
    view.methods.printmessage(view.text.edit_message_title)    

def message_edit_body():
    view.methods.printmessage(view.text.edit_message_body)


def message_not_find():
    view.methods.printmessage(view.text.not_find)

def delete_note():
    view.methods.printmessage(view.text.delete_message)

def delete_note_success():
    view.methods.printmessage(view.text.delete_success)


def find_by_date():
    view.methods.printmessage(view.text.find_by_date)


def find_by_date_error():
    view.methods.printmessage(view.text.not_find_date)

def find_by_date_wrong_date():
    view.methods.printmessage(view.text.wrong_date)

