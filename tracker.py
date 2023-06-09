"""
This module is a command-line interface that can help users to track expenses and generate reports.
"""
import sys
from transaction import Transaction

HELP = '''Options:
     0. quit
     1. show categories
     2. add category
     3. modify category
     4. show transactions
     5. add transaction
     6. delete transaction
     7. summarize transactions by date
     8. summarize transactions by month
     9. summarize transactions by year
     10. summarize transactions by category
     11. print this menu
'''


def print_usage():
    '''Print an explanation of how to use this command.'''
    print(HELP)


def process_args(tracker, arglist):
    '''Examine args and make appropriate calls to Transaction class.'''
    if arglist == []:
        print_usage()
    elif arglist[0] == "0":
        return
    elif arglist[0] == "1":
        rows = tracker.show_categories()
        if len(rows) == 0:
            print("No categories found.")
        else:
            print("Categories:")
            for row in rows:
                print(f"{row[0]}. {row[1]}")
    elif arglist[0] == "2" and len(arglist) == 1:
        print("The format should be '2 category_name'")
    elif arglist[0] == "2":
        tracker.add_category(arglist[1])
    elif arglist[0] == "3":
        tracker.modify_category(arglist[1], arglist[2])
    elif arglist[0] == "5":
        if len(arglist) < 5:
            print("Not enough arguments for 'add transaction'")
            print_usage()
        else:
            try:
                tracker.add_transaction(arglist[1], arglist[2],
                                        float(arglist[3]), int(arglist[4]))
                print("Transaction added successfully.")
            except ValueError as exception:
                print("An error occurred while adding the transaction.")
                print(str(exception))
    elif arglist[0] == "6":
        if len(arglist) < 2:
            print("Not enough arguments for 'delete transaction'")
            print_usage()
        else:
            tracker.delete_transaction(arglist[1])
    elif arglist[0] in ['4', '7', '8', '9', '10']:
        action = {
            '4': tracker.show_transactions,
            '7': tracker.summarize_transactions_by_date,
            '8': tracker.summarize_transactions_by_month,
            '9': tracker.summarize_transactions_by_year,
            '10': tracker.summarize_transactions_by_category,
        }

        results = action[arglist[0]]()
        if results:
            for row in results:
                print(row)
        else:
            print('empty')
    elif arglist[0] == "11":
        print_usage()
    else:
        print(arglist, "is not implemented")
        print_usage()


def main():
    '''Read the command args and process them.'''
    tracker = Transaction()

    if len(sys.argv) == 1:
        # They didn't pass any arguments, so prompt for them in a loop
        # so prompt for them in a loop
        print_usage()
        args = []
        while args != ['0']:
            args = input("Enter an option: ").split(' ')
            process_args(tracker, args)
            print('-' * 40 + '\n' * 3)
    else:
        # Read the args and process them
        args = sys.argv[1:]
        process_args(tracker, args)
        print('-' * 40 + '\n' * 3)


if __name__ == '__main__':
    main()
