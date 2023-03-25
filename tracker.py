import sys
from transaction import Transaction



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



if __name__ == '__main__':
    main()
