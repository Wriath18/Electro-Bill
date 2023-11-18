import mysql.connector
from datetime import date
from datetime import datetime
db=mysql.connector.connect(host='localhost',user='root',password='Sanidhya',database='Gada_Electronics')
cur=db.cursor()

#all functions are here
def intro():
    print("  ____           _         _____ _           _                   _")
    print(" / ___| __ _  __| | __ _  | ____| | ___  ___| |_ _ __ ___  _ __ (_) ___ ___ ")
    print("| |  _ / _` |/ _` |/ _` | |  _| | |/ _ \/ __| __| '__/ _ \| '_ \| |/ __/ __|")
    print("| |_| | (_| | (_| | (_| | | |___| |  __/ (__| |_| | | (_) | | | | | (__\__ \\")
    print(" \____|\__,_|\__,_|\__,_| |_____|_|\___|\___|\__|_|  \___/|_| |_|_|\___|___/")


def outro():
    print(" _____ _                 _")
    print("|_   _| |__   __ _ _ __ | | __  _   _  ___  _   _")
    print("  | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | |")
    print("  | | | | | | (_| | | | |   <  | |_| | (_) | |_| |")
    print("  |_| |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_|")
    print("                                |___/")
    
    
def cont():
    Continue = input("Back to Main menu ? (y/n)")
    if Continue == 'y':
        menu()
    elif Continue == 'n':
        thankyou = outro()
        print(thankyou)
    else:
        thankyou = outro()
        print(thankyou)


#main menu funciton
def menu():
    print('1. Stock')
    print('2. Purchase')
    print('3. View Sales')
    print('4. Stop Program')

    choice = int(input('Enter your Choice - '))
    if choice == 1:
        display_Stock()
    elif choice==2:
        details()
        buy()
        sql()
        bill()
        cont()
    elif choice==3:
        view_details()
        
    elif choice == 4:
        thankyou = outro()
        print(thankyou)
    else:
        print('Enter valid choice')
        menu()


#Function to display stock
def display_Stock():
    print('1. For Display Stock')
    print('2. For Editing Stock')
    z=('Code, Type, Name, Brand, Quantity, Price/Piece')
    choice = int(input("Enter your Choice - "))
    if choice == 1:
        print('1. Specific Product (By Type)')
        print('2. Display Whole Stock')
        stock_choice = int(input("Enter your Choice - "))
        if stock_choice == 1:
            print('1. T.V.')
            print('2. Mobile')
            print('3. A.C.')
            print('4. Watch')

            display_choice = int(input('Enter the type of product you want to see - '))
            if display_choice==1:
                print()
                cur.execute("SELECT P_Code,Name,Brand,Quantity,Priceperpiece FROM Stock WHERE Type='T.V.'")
                dataa=cur.fetchall()
                print('list of items')
                print(z)
                for row in dataa:
                    print(row)
                    print('\n')
                cont()
            
            elif display_choice==2:
                print()
                cur.execute("SELECT P_Code,Name,Brand,Quantity,Priceperpiece FROM Stock WHERE Type='Mobile'")
                dataa=cur.fetchall()
                print('list of items')
                print(z)
                for row in dataa:
                    print(row)
                    print('\n')
                cont()
            
            elif display_choice==3:
                print()
                cur.execute("SELECT P_Code,Name,Brand,Quantity,Priceperpiece FROM Stock WHERE Type='A.C.'")
                dataa=cur.fetchall()
                print('list of items')
                print(z)
                for row in dataa:
                    print(row)
                    print('\n')
                cont()

            elif display_choice==4:
                print()
                cur.execute("SELECT P_Code,Name,Brand,Quantity,Priceperpiece FROM Stock WHERE Type='Watch'")
                dataa=cur.fetchall()
                print('list of items')
                print(z)
                for row in dataa:
                    print(row)
                    print('\n')
                cont()


        if stock_choice==2:
            print()
            cur.execute('SELECT P_Code,Name,Brand,Quantity,Priceperpiece FROM Stock')
            data = cur.fetchall()
            print('List Of items')
            print(z)
            for row in data:
                print(row)
                print('\n')
            cont()
    elif choice==2:
        edit_stock()
        cont()

    else:
        print('Enter valid choice')
        display_Stock()
  
        
#Stock Edit Function
def edit_stock():
    print('1. Update Stock\n')
    print('2. Delete An Item \n')
    print('3. Add An item\n')
    print('3. Back to Main Menu\n')

    edit_choice = int(input('Enter your choice - '))
    
    if edit_choice == 1:
        update_stock()
    elif edit_choice == 2:
        delete_stock_item()
    elif edit_choice == 3:
        add_stock_item()
    elif edit_choice == 4:
        menu()
    else:
        print('Enter valid choice')
        edit_stock()
        

#Stock Update Function
def update_stock():
    try:
        p_code = int(input("Enter the product code - "))
        print('1. Quantity')
        print('2. Price')

        update = int(input('Enter your choice - '))

        if update == 1:
            new_quantity = int(input('Enter the new quantity - '))
            print()
            cur.execute("UPDATE Stock SET Quantity = {} WHERE P_Code = {}".format(new_quantity, p_code))
            print("Updates was sucessful")
            db.commit()

        elif update == 2:
            new_price = int(input('Enter the new price (Per peice - '))
            print()
            cur.execute("UPDATE Stock SET Priceperpiece = {} WHERE P_Code = {}".format(new_price, p_code))
            print('Update was sucessesful')
            db.commit()
        else:
            print('Enter valid choice')
            update_stock()
    except:
        print('there was some error ')
        print('try again')
        update_stock()


#Delete Stock Function
def delete_stock_item():
    try:
        p_code = int(input('Enter the product code - '))
        print()
        cur.execute('SELECT * FROM Stock WHERE P_Code = {}'.format(p_code))
        data = cur.fetchall()
        print('The Following Items will be removed from the Stock database')
        for row in data:
            print(row)

        sure = input('Are your Sure you want to delete this item ? (y/n) - ')
        if sure[0] == 'y':
            print()
            cur.execute('DELETE FROM Stock WHERE P_Code = {}'.format(p_code))
            print('The Item was Deleted\n')
            db.commit()
            cont()
        elif sure[0] == 'n':
            print('Process has been canceled .. \n')
            cont()
        else:
            print('Enter valid choice')
            delete_stock_item()
    except:
        print('there was some error')
        print('try again')
        delete_stock_item()


#Add Item to stock
def add_stock_item():
    choice = input('Do you want to add an item ? (y/n) - ')
    try:
        if choice == 'y':
            p_code = int(input("Enter the product Code - \n"))
            print("1. T.V.")
            print('2. Mobile')
            print('3. A.C.')
            print('4. Watch')
            type_ch = int(input("Choose the Product type - "))
            if type_ch == 1:
                p_type = "T.V."
            elif type_ch == 2:
                p_type = "Mobile"
            elif type_ch == 3:
                p_type = "A.C."
            elif type_ch == 4:
                p_type = "Watch"
            name = input("Enter the Name of the Product - ")
            brand = input("Enter the Brand Name - ")
            Quantity = int(input("Enter the Quantity - "))
            Price = int(input("Enter the Price (Per peice) - "))
            
            print()
            cur.execute("INSERT INTO Stock (P_Code, Type, Name, Brand, Quantity, Priceperpiece) Values ('{}', '{}', '{}', '{}', '{}', '{}')".format(p_code, p_type, name, brand, Quantity, Price))
            print("The addition was sucessesful\n")
            db.commit()
        elif choice=='n':
            pass
        else:
            print('Enter y or n')
            add_stock_item()
    except:
        print('There was some error')
        print('try again')
        add_stock_item()


#Customer Details (while buying) function
def details():
    global name
    def num():
        global pnum
        pnum=int(input('Enter phone number of customer- '))
        if len(str(pnum))<10 or len(str(pnum))>10:
            print('Enter 10 digit phone number ')
            num()
    try:
        name=input('Enter name of customer- ')
        num()
    except:
        print('Enter integer value in phone number')
        details()
      

#Buy Function
def buy():
    global quantity
    global pcode
    pcode=int(input('input product code- '))
    quantity=int(input('input quantity of product- '))
    items[pcode]=quantity
    def contin():
        cont=input('Do you want to continue buying (y/n)- ')
        if cont=='y':
            buy()
        elif cont=='n':
            cart()
        else:
            print('Enter y or n')
            contin()
    contin()


#Items in cart 
def cart():
    change=input('Do you want to add or remove products you have bought (y/n)- ')
    if change=='y':
        pcode=int(input('input product code- '))
        quantity=int(input('input new quantity of product- '))
        items.update({pcode:quantity})
    elif change=='n':
        pass
    else:
        print('Enter y or n')
        cart()
   
        
#Table Updatation
def sql():
    global amount
    items_count=sum(items.values())
    pcode=str(items)
    amount=0
    for i in items.keys():
        a=items[i]
        cur.execute('SELECT Priceperpiece FROM Stock WHERE P_Code={}'.format(i))
        ab=cur.fetchall()
        pr=ab[0]
        price=int(pr[0])
        total=price*a
        amount=amount+total
    dat=date.today()
    now=datetime.now()
    tim=now.strftime('%H:%M:%S')    
    attrib='INSERT INTO Sale (date, time, Name, phoneno, item_count, pcode_pquantity, amount) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    value=(dat, tim, name, pnum, items_count, pcode, amount)
    cur.execute(attrib, value)
    db.commit()
    print('sale table updated')
    print()

    for i in items.keys():
        b=items[i]
        cur.execute('SELECT Quantity FROM Stock WHERE P_Code={}'.format(i))
        ac=cur.fetchall()
        pc=ac[0]
        old_quan=int(pc[0])
        new_quan=old_quan-b
        cur.execute("UPDATE Stock SET Quantity = {} WHERE P_Code = {}".format(new_quan, i))
        db.commit()


#Bill Generate Function
def bill():
    print('Your bill is-')
    print('NAME- ',name)
    print('Phone No.- ',pnum)
    for i in items.keys():
        cur.execute('SELECT Name, Brand, Priceperpiece FROM Stock WHERE P_code ={}'.format(i))
        bil=cur.fetchall()
        bil2=bil[0]
        print('PRODUCT- ',bil2[0])
        print('BRAND- ', bil2[1])
        print('Quantity- ',items[i])
        print('Price/Piece- ', bil2[2])
    print('TOTAL AMOUNT- ', amount)


#View Customer details 
def view_details():
    print('1. View Sales Record')
    print('2. View Customer Details')
    x=('Date, Name, PhoneNo, Items, Product&Quan., Amount')    
    try:
        details_choice=int(input('Enter your Choice-') )
        if details_choice==1:
            cur.execute('SELECT date, Name, phoneno, item_count, pcode_pquantity, amount FROM Sale')
            data=cur.fetchall()
            print(x)
            for row in data:
                print(row)
                print()
        elif details_choice==2:
            cust_dat()
        else:
            print('Enter Valid Choice')
            view_details()
    except:
        print('There was some error')
        view_details()
    cont()


#View customer data by request
def cust_dat():
    print('1. View by Phone Number')
    print('2. View by Name')
    x=('Date, Name, PhoneNo, Items, Product&Quan., Amount')
    choice_3=int(input('Enter your choice- '))
    if choice_3==1:
        c_phone=int(input("Enter Customer Phone Number- "))
        cur.execute('SELECT date, Name, phoneno, item_count, pcode_pquantity, amount FROM Sale WHERE phoneno= {}'.format(c_phone))
        data=cur.fetchall()
        print(x)
        print()
        for row in data:
            print(row)
            print()
        else:
            print('No record with this Phone number')
    elif choice_3==2:
        c_name=input('Enter customer name- ')
        cur.execute('SELECT date, Name, phoneno, item_count, pcode_pquantity, amount FROM Sale')
        dat=cur.fetchall()
        print(x)
        print()
        for i in dat:
            j=i[1]
            if j==c_name:
                print(i)
        else:
            print('No record with this name')
    else:
        print('Wrong choice entered')
        print()
        print('Try again')
        cust_dat()


#main code is here
if db.is_connected():
    result = intro()
    print(result)

items={}

menu()


