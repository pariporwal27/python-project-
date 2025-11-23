# python-project -
#Pet a Cat Cafe Management System

# Overview

The code is written in Python language and manages a pet cafe. Core functionalities of the system include customer management, event reservations, ordering from the menu and billing , pet adoptions, and donations for pet care . The application uses MySQL at the backend for database purposes and a command-line interface for user interaction.

# Features 

The features of the project includes :

1. Reservation Functionality where user can select date and time, choose decor option according to their requirement .
2. Allow the user to view menus of cakes, milkshakes, and ice cream and later create a bill with discounts applied for various price ranges 
3. Facilitate the adoption of pets by listing available pets and updating records if a pet is adopted  .
4. keep record  of donations for pet care at the café along with the donor's details in a file.


# Technologies/Tools Used

1. Python 3 with mysql.connector 
2. PrettyTable 
3. MySQL database 
4. SQL queries 
5. Modules : mysql.connector, prettytable
6. func1 as reservation system, func2 menu & billing, func3 as adoption system and func4 as donation system.
7. Database Tables: customer, decor, cake (menu), milkshake(menu), icecream(menu) , data (pet), donation

# Steps to install and run your Pet a Cat <3 Cafe project :

1. Install Required Software :
Visual Studio Code
GitHub Desktop
Python 3.x
Git 
2. Clone Repository with GitHub Desktop
3. Open GitHub Desktop and sign in to your GitHub account.
4. clone your project repository to a local folder.
5. Open Project in VS Code
6. In GitHub Desktop, select your repository and click "Open in Visual Studio Code".
7. VS Code will load your project files
8. In VS Code, select Python interpreter .
9. Install required Python modules  ( mysql-connector-python, prettytable) using the terminal:
pip install mysql-connector-python prettytable
10. Run the Project and interact with the program.
11. commit and push from GitHub Desktop.

# Instruction for testing 

Confirm the database and tables exist with sample data for menu and pets.
Run the Python script and check the welcome message and options display.

# Test the key functions:

1. Register new customer and verify in table customer of the database named catcafe.
2. Make a reservation and check if the data is inserted in decor table.
3. Order from menu and check bill calculations and discount application.
4. Adopt a pet and verify removal of the adopted pet from data table.
5. Make a donation and confirm record is inserted in donation table .

# Screenshots of output and changes in database 

1. making reservation and registering new user 
   <img width="991" height="496" alt="image" src="https://github.com/user-attachments/assets/e40d62f3-5513-477c-9cf6-c55a74ed96b1" />

   changes in decor table
   <img width="1083" height="250" alt="image" src="https://github.com/user-attachments/assets/464d086a-5dd3-4065-8b0d-a76ba162c81d" />

   changes in customer table
   <img width="1257" height="242" alt="image" src="https://github.com/user-attachments/assets/cd668805-18e7-4ab2-938c-61d3bc3b5139" />

   
2. ordering and billing
   <img width="1293" height="920" alt="image" src="https://github.com/user-attachments/assets/beffdc47-d1c8-4115-96bd-cefc36825d06" />
   <img width="1276" height="450" alt="image" src="https://github.com/user-attachments/assets/5f562792-aa87-4269-9223-04bc02346b56" />

3. adopting pet
   <img width="1275" height="510" alt="image" src="https://github.com/user-attachments/assets/5634d0ab-2597-48ea-acb6-da97bd2b9092" />

   changes in data table
   <img width="1168" height="261" alt="image" src="https://github.com/user-attachments/assets/1e7dd99c-82fe-4dfa-8e62-08219b28ebf1" />

4. making donation
   <img width="1273" height="335" alt="image" src="https://github.com/user-attachments/assets/b4b81f22-1a5a-4d78-9128-0754ecbbf2d1" />

   changes in donation table
   <img width="1154" height="224" alt="image" src="https://github.com/user-attachments/assets/dac05132-ce50-48b3-9fae-7750b4d4d8c7" />





