import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class ToDoList:

    columns = {
        'todo': {},
        'in_progress': {},
        'done': {},
    }
    index = {
        'todo': 1,
        'in_progress': 1,
        'done': 1,
    }

    def __init__(self):
        self.exit = False
        # TODO load json

    def add_item(self):
        clear_screen()
        print('# Adding item')
        print('1/T : To Do')
        print('2/P : In Progress')
        print('3/D : Done')
        column = input('Choose column: ')
        # Set actual column name
        if column in '1tT':
            column = 'todo'
        elif column in '2pP':
            column = 'in_progress'
        elif column in '3dD':
            column = 'done'
        else:
            print('No such column, dumbass!\n')
            return
        value = input('Enter value: ')
        self.columns[column][self.index[column]] = value
        self.index[column] += 1

    def remove_item(self):
        print('Removing item')
        input('Press Enter')

    def edit_item(self):
        print('Editing item')
        input('Press Enter')

    def print_list(self):
        clear_screen()
        for i in range(20):
            print('=', end='')
        print()
        for column, col_items in self.columns.items():
            print(column)
            if len(column) > 0:
                for item in col_items:
                    print(f'# {item}: {col_items[item]}')
        for i in range(20):
            print('=', end='')
        print()

    def run(self):
        while not self.exit:
            print('1/A : Add item')
            print('2/R : Remove item')
            print('3/E : Edit item')
            print('0/X : Exit')
            action = input('Choose action: ')
            if action in '0xX':
                self.exit = True
            elif action in '1aA':
                self.add_item()
            elif action in '2rR':
                self.remove_item()
            elif action in '3eE':
                self.edit_item()
            else:
                print('Action unavailable!\n')
            self.print_list()


if __name__ == '__main__':
    clear_screen()
    to_do_list = ToDoList()
    to_do_list.run()
