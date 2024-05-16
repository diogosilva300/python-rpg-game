from os import system
import sys

class ShowMessage():
    def __init__(self, message):
        print(message)

class GameMenu:
    col_selected = 0
    row_selected = 0
    menu = ["Status", "Inventory", "Fight", "Rest", "Exit"]
    confirm = ["Yes", "No"]
    menus = {"menu" : menu, "confirm" : confirm}
    active_menu = None

    @classmethod
    def add_menu(classe, key, value):
        classe.menus.update({key : value})

    @classmethod
    def show_menu(classe):
        system('cls')
        print(classe.row_selected, classe.col_selected)
        col = []
        max_row_length = 0
        header = []

        for k in classe.menus.keys():
            header.append(str(k).capitalize())
        ShowMessage('{:<15}{:15}{:<15}'.format(*header))

        for v in classe.menus.values():
            col.append(v)

        for i in col:
            max_row_length = len(i) if max_row_length < len(i) else max_row_length

        for i in range(max_row_length):
            row = []
            for x in range(len(col)):
                if isinstance(col[x], list):
                    if i < len(col[x]):
                        if classe.row_selected == i and classe.col_selected == x:
                            row.append("> " + str(col[x][i]) + " <")
                        else:
                            row.append(" " + str(col[x][i]) + "")
                    else:
                        row.append("")
                if isinstance(col[x], dict):
                    row.append(str(list(col[x].items())[i][0]).capitalize() + ": " +str(list(col[x].items())[i][1]))
                else:
                    row += ""
            ShowMessage('{:<15}{:15}{:<15}'.format(*row))

    @classmethod
    def up(classe):
        if classe.row_selected == len(list(classe.menus.values())[classe.col_selected]) - len(list(classe.menus.values())[classe.col_selected]):
            return
        classe.row_selected -= 1
        classe.show_menu()

    @classmethod
    def down(classe):
        if classe.row_selected == len(list(classe.menus.values())[classe.col_selected]) - 1:
            return
        classe.row_selected += 1
        classe.show_menu()
    
    @classmethod
    def left(classe):
        if classe.col_selected == len(list(classe.menus.keys())) - len(list(classe.menus.keys())):
            return
        if classe.row_selected > len(list(classe.menus.values())[classe.col_selected - 1]) - 1:
            classe.row_selected = len(list(classe.menus.values())[classe.col_selected - 1]) - 1
        classe.col_selected -= 1
        classe.show_menu()

    @classmethod
    def right(classe):
        if classe.col_selected == len(list(classe.menus.keys())) - 1:
            return
        if classe.row_selected > len(list(classe.menus.values())[classe.col_selected + 1]) - 1:
            classe.row_selected = len(list(classe.menus.values())[classe.col_selected + 1]) - 1
        classe.col_selected += 1
        classe.show_menu()

    @classmethod
    def done(classe):
        system('cls')
        ShowMessage(list(classe.menus.items())[classe.col_selected][1][classe.row_selected]);
        if classe.col_selected == 0 and classe.row_selected == len(list(classe.menus.items())[classe.col_selected][1][classe.row_selected]):
            sys.exit()