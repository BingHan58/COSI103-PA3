# COSI103-PA3

***** PA03 Introduction *****

Transaction.py is an Object-Relational Mapping (ORM) module that interacts with the tracker.db database.

The ORM will map SQL rows with the schema
(id, date, description, amount, category_id)
to Python Dictionaries as follows:
{id:1, date:'2022-03-28', description:'Grocery shopping', amount: 100.00, category_id:1}
In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database named tracker.db
The class Transaction provides various methods for accessing and manipulating data, including getting ,adding and modifying categories, adding and deleting transactions, and summarizing transactions by date, month, year, or category etc.

In addition, the ORM includes a method run_query() that connects to the database, executes a query with parameters, fetches the rows, and closes the connection. The method catches and ignores any errors that may occur during the database interaction.


***** Pylint Script *****
```
pylint transaction.py
```

***** run pytest  *****
```
pytest -v
```
```
============================================================== test session starts ==============================================================
platform darwin -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
cachedir: .pytest_cache
rootdir: /Users/icey/Desktop/COSI103-PA3-5
plugins: anyio-3.6.2
collected 11 items                                                                                                                              

test_transaction.py::test_show_categories PASSED                                                                                          [  9%]
test_transaction.py::test_add_category PASSED                                                                                             [ 18%]
test_transaction.py::test_modify_category PASSED                                                                                          [ 27%]
test_transaction.py::test_show_transactions_empty PASSED                                                                                  [ 36%]
test_transaction.py::test_show_transactions_nonempty PASSED                                                                               [ 45%]
test_transaction.py::test_add_show_transaction PASSED                                                                                     [ 54%]
test_transaction.py::test_add_delete_show_transaction PASSED                                                                              [ 63%]
test_transaction.py::test_summarize_transactions_by_date PASSED                                                                           [ 72%]
test_transaction.py::test_summarize_transactions_by_month PASSED                                                                          [ 81%]
test_transaction.py::test_summarize_transactions_by_year PASSED                                                                           [ 90%]
test_transaction.py::test_summarize_transactions_by_category PASSED                                                                       [100%]

============================================================== 11 passed in 0.13s ===============================================================
```

***** How to run tracker *****
```
python3 tracker.py
```
If the user enter 0, the program will quit
If the user eneter 1, the program will show all categories
```
Enter an option: 1
Categories:
1. food
2. snake
3. fruit
```
If the user enter 2, the program will add a category
```
Enter an option: 2 food
Enter an option: 2 snake
Enter an option: 2 fruit
```
If the user enter 3, the program will modify category
```
Enter an option: 3 food veg

Enter an option: 1
Categories:
1. veg
2. snake
3. fruit
```
If the user enter 4, the program will show transactions
```
Enter an option: 4
(1, '2022-03-28', 'Food', 103.0, 2)
(2, '2022-03-28', 'Grocery', 78.87, 1)
(3, '2022-03-28', 'Grocery', 12.53, 1)
(4, '2022-04-09', 'Food', 67.23, 2)
(5, '2022-05-21', 'Coffee', 353.2, 3)
(6, '2022-05-12', 'Sanke', 13.45, 4)
(7, '2023-12-12', 'Snake', 45.22, 4)
(8, '2023-12-12', 'Coffee', 42.1, 3)
```
If the user enter 5, the program will add transaction
```

Enter an option: 5 2022-03-28 Food 103 2 
Transaction added successfully.
----------------------------------------

Enter an option: 5 2022-03-28 Grocery 178.87 1
Transaction added successfully.
----------------------------------------

Enter an option: 5 2022-03-28 Grocery 12.53 1
Transaction added successfully.
----------------------------------------

Enter an option: 5 2022-04-09 Food 67.23 2     
Transaction added successfully.
----------------------------------------

Enter an option: 5 2022-05-21 Coffee 353.2 3
Transaction added successfully.
----------------------------------------

Enter an option: 5 2022-05-12 Sanke 13.45 4 
Transaction added successfully.
----------------------------------------

Enter an option: 5 2023-12-12 Snake 45.22 4 
Transaction added successfully.
----------------------------------------

Enter an option: 5 2023-12-12 Coffee 42.1 3
Transaction added successfully.


Enter an option: 4
(1, '2022-03-28', 'Food', 103.0, 2)
(2, '2022-03-28', 'Grocery', 78.87, 1)
(3, '2022-03-28', 'Grocery', 12.53, 1)
(4, '2022-04-09', 'Food', 67.23, 2)
(5, '2022-05-21', 'Coffee', 353.2, 3)
(6, '2022-05-12', 'Sanke', 13.45, 4)
(7, '2023-12-12', 'Snake', 45.22, 4)
(8, '2023-12-12', 'Coffee', 42.1, 3)
```
If the user enter 6, the program will delete transaction
```
Enter an option: 4
(1, '2022-03-28', 'Food', 103.0, 2)
(2, '2022-03-28', 'Grocery', 78.87, 1)
(3, '2022-03-28', 'Grocery', 12.53, 1)
(4, '2022-04-09', 'Food', 67.23, 2)
(5, '2022-05-21', 'Coffee', 353.2, 3)
(6, '2022-05-12', 'Sanke', 13.45, 4)
(7, '2023-12-12', 'Snake', 45.22, 4)
(8, '2023-12-12', 'Coffee', 42.1, 3)

Enter an option: 6 1

Enter an option: 6 6

Enter an option: 4
(2, '2022-03-28', 'Grocery', 78.87, 1)
(3, '2022-03-28', 'Grocery', 12.53, 1)
(4, '2022-04-09', 'Food', 67.23, 2)
(5, '2022-05-21', 'Coffee', 353.2, 3)
(7, '2023-12-12', 'Snake', 45.22, 4)
(8, '2023-12-12', 'Coffee', 42.1, 3)
```
If the user enter 7, the program will summarize transactions by date
```
Enter an option: 4
(2, '2022-03-28', 'Grocery', 78.87, 1)
(3, '2022-03-28', 'Grocery', 12.53, 1)
(4, '2022-04-09', 'Food', 67.23, 2)
(5, '2022-05-21', 'Coffee', 353.2, 3)
(7, '2023-12-12', 'Snake', 45.22, 4)
(8, '2023-12-12', 'Coffee', 42.1, 3)

Enter an option: 7
('2022-03-28', 91.4)
('2022-04-09', 67.23)
('2022-05-21', 353.2)
('2023-12-12', 87.32)
```
If the user enter 8, the program will summarize transactions by month
```
Enter an option: 4
(2, '2022-03-28', 'Grocery', 78.87, 1)
(3, '2022-03-28', 'Grocery', 12.53, 1)
(4, '2022-04-09', 'Food', 67.23, 2)
(5, '2022-05-21', 'Coffee', 353.2, 3)
(7, '2023-12-12', 'Snake', 45.22, 4)
(8, '2023-12-12', 'Coffee', 42.1, 3)

Enter an option: 8
('2022-03', 91.4)
('2022-04', 67.23)
('2022-05', 353.2)
('2023-12', 87.32)
```
If the user eneter 9, the program will summarize transactions by month
```
Enter an option: 4
(2, '2022-03-28', 'Grocery', 78.87, 1)
(3, '2022-03-28', 'Grocery', 12.53, 1)
(4, '2022-04-09', 'Food', 67.23, 2)
(5, '2022-05-21', 'Coffee', 353.2, 3)
(7, '2023-12-12', 'Snake', 45.22, 4)
(8, '2023-12-12', 'Coffee', 42.1, 3)

Enter an option: 9
('2022', 511.83)
('2023', 87.32)
```
If the user enter 10, the program will summarize transactions by category
```

Enter an option: 4 
(1, '2022-03-28', 'carwash', 44.0, 2)
(2, '2022-03-28', 'food', 34.22, 1)
(3, '2022-05-21', 'Coffee', 353.2, 3)
(4, '2023-12-12', 'Snacks', 45.22, 1)
----------------------------------------


Enter an option: 10
[('Food', 79.44), ('Car', 44.0), ('Drink', 353.2)]


```

If the user eneter 11, the program will print this menu
```
Enter an option: 11
Options:
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
```     

***** PA03 Assignment Introduction *****

PA03 - finance tracker - using SQL, pytest, and pylint

Motivation
Many software projects use SQLite to manage their data and this problem set will give you the experience of building such an app.  Another important process in software engineering is the design of automated tests.  This assignment will ask you to develop a suite of tests for your app. There are other database and testing frameworks, but they are all similar in principle and this assignment will expose you to the core concepts and skills you'll need.


Learning Objectives -
* to write SQL queries to perform the CRUD operations (Create, Read, Update, Delete) and aggregation(with SQLite3)
* to develop automated testing (with pytest)

Steps:
1) create a git repository to contain the pa03 code, which you then push to github
2) add all members of the team as collaborators
3) create a Python class Transaction in a new file transaction.py which will store financial transactions with the fields. 
It should have an __init__ method where you pass in the filename for the database to be used (e.g. tracker.db) 
and each transaction should have the following fields stored in a SQL table called transactions.

'item #',
'amount',
'category',
'date',
'description'

It should be similar to the Todolist ORM from Lesson 19 in class. It will allow the user to read and update the database as need.
The transaction class should not do any printing!! 

Create a file tracker.py which offers the user the following options and makes calls to the Transaction class to update the database.

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

The tracker.py program should not have any SQL calls and should be similar is structure to the todo2.py program from Lesson19

Testing with pytest -- 
create a file, test_transaction.py, and addtests to it for each method in the Transaction class. 
It is a good idea to add a test each time you implement a feature. 
You are testing the Transaction class, not the tracker.py user interface code.

Linting with pylint --
Use pylint with transactions.py and tracker.py and eliminate all of the style errors that it flags. Try to get 100% compliance.

Collaborating with github -- 
regularly commit your changes and push them to github, every team member should push some changes of their own. I suggest you have each person implement a few of the options in tracker.py and everyone collaborate on the operations needed for the ORM transaction.py

Creating a transcript - 
create a transcript of your session as you demonstrate each of the features you have implemented. 
create a README.md file which describes your app and contains 
* a script of you running pylint, and 
* then running pytest, and 
* then running tracker.py and demonstrating all of the features you added

Try to make sure that everyone gets to work on some substantial part of the project.
 
What to upload to mastery.cs.brandeis.edu (programs)
* a link to your github
* a reflection where you state what you did personally on the project 
(you should put your name in the comments of each method you personally write....). 
We can use the "blame" feature in the github repository to see what each person did, but its easier if you just tell us!
