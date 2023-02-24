
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
        print('Adding item')
        print('[T]o Do', 'In [P]rogress', '[D]one', sep='\n')
        column = input('Choose column: ')
        # Set actual column name
        if column in 'tT':
            column = 'todo'
        elif column in 'pP':
            column = 'in_progress'
        elif column in 'dD':
            column = 'done'
        else:
            print('No such column, dumbass!\n')
            return
        value = input('Enter value: ')
        self.columns[column][self.index[column]] = value
        self.index[column] += 1

    def remove_item(self):
        print('Removing item')
        pass

    def edit_item(self):
        print('Editing item')
        pass

    def print_list(self):
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
    to_do_list = ToDoList()
    to_do_list.run()
