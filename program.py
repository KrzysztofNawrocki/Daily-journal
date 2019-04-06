import journal_save_load


def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------------------')
    print('           JOURNAL APP')
    print('----------------------------------')


def run_event_loop():

    print('What do you want to do with your journal? ')
    cmd = 'anything'
    journal_name = 'default'
    journal_data = journal_save_load.load(journal_name)  # [] # list

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print(f'Sorry, we don\'t understand \'{cmd}\'')

    print('Done, goodbye!')
    journal_save_load.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for index, entry in enumerate(entries):
        print(f'* [{index+1}]: {entry}')


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal_save_load.add_entry(text, data)


# print("__file__ = " + __file__)
# print("__name__ = " + __name__)


if __name__ == '__main__':
    main()
