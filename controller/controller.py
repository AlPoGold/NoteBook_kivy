import view
import controller.commands as commands
import view.ui_console


def start():
    flag = True
    while(flag):
        view.ui_console.main_menu()
        view.ui_console.message_action()
        user_input = input()
        if user_input == '1':
            commands.open_file()
        elif user_input == '2':
            commands.show_notes()
        elif user_input == '3':
            commands.find_note()
        elif user_input == '4':
            commands.add_note()
        elif user_input == '5':
            commands.edit_note()
        elif user_input == '6':
            commands.delete_note()
        elif user_input == '7':
            commands.save_file()
        elif user_input == '8':
            commands.select_by_date()
        elif user_input == '9':
            flag = False
            view.ui_console.message_exit()
        else:
            view.ui_console.message_error_input()


