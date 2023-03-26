import sys
from transaction_br1 import Transaction



def print_usage():
    '''Print an explanation of how to use this command.'''
    print('''Options:
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
''')


    
def process_args(tracker, arglist):
    '''Examine args and make appropriate calls to Transaction class.'''
    if arglist == []:
        print_usage()
    elif arglist[0] == "0":
        return
    elif arglist[0] == "1":
        tracker.show_categories()
    elif arglist[0] == "2":
        tracker.add_category(arglist[1])
    elif arglist[0] == "3":
        tracker.modify_category(arglist[1], arglist[2])
    elif arglist[0] == "4":
        for transaction in tracker.show_transactions():
             print(transaction)
    elif arglist[0] == "5":
        tracker.add_transaction(arglist[1], arglist[2], arglist[3], arglist[4])
    elif arglist[0] == "6":
        tracker.delete_transaction(arglist[1])
    
        '''Don't forget to add other features from 7-10'''
    
    
    
    
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
        #so prompt for them in a loop
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
