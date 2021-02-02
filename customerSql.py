import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gamz"
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

def addCustomers():
    quitter = "no"
    while quitter != "yes":
        name = input("Enter name: ")
        address = input("Enter address: ")
        mycursor.execute("SELECT COUNT(*) FROM customers WHERE address LIKE \"{}\" AND name LIKE \"{}\";".format(address, name))
        myresult = mycursor.fetchall()
        for row in myresult:
            if (row[0] == 0):
                query = "INSERT INTO customers (name, address) VALUES(%s, %s);"
                val = (name, address)

                mycursor.execute(query, val)
                mydb.commit()
                
                mycursor.execute("SELECT * FROM CUSTOMERS ORDER BY id DESC LIMIT 1;")
                myresultShow = mycursor.fetchall()
                for row in myresultShow:
                    print(row)
            else:
                print("This customer already exist")
                print()
        quitter = input("Do you want to quit to main? Type \"yes\" to quit: ")
   
def updateCustomers():
    quitter = "no"
    while quitter != "yes":
        idNo = input("Enter ID: ")
        try:
            idNo = int(idNo)
            mycursor.execute("SELECT COUNT(*) FROM customers WHERE id = {};".format(idNo))
            myresult = mycursor.fetchall()
            for row in myresult:
                if (row[0] == 0):
                    print("Customer does not exist")
                    print()
                else:
                    mycursor.execute("SELECT * FROM customers WHERE id = {};".format(idNo))
                    myresultShow = mycursor.fetchall()
                    for row in myresultShow:
                        print(row)
                    print("Updating this customer")
                    name = input("Enter new name: ")
                    address = input("Enter new address: ")
                    changeConfirm = input("Save changes? Type \"yes\" to save changes: ")
                    if changeConfirm == "yes":
                        mycursor.execute("UPDATE customers SET name = \"{}\", address = \"{}\" WHERE id = {};".format(name, address, idNo))
                        mycursor.execute("SELECT * FROM customers WHERE id = {};".format(idNo))
                        myresultShow = mycursor.fetchall()
                        for row in myresultShow:
                            print(row)
                            print()
                        mydb.commit()
                        print("Customer updated")
                    else:
                        print("Update cancelled")
                    print()
        except ValueError:
            print("Invalid input")
        quitter = input("Do you want to quit to main? Type \"yes\" to quit: ")

def removeCustomers():
    quitter = "no"
    while quitter != "yes":
        idNo = input("Enter ID: ")
        try:
            idNo = int(idNo)
            mycursor.execute("SELECT COUNT(*) FROM customers WHERE id = {};".format(idNo))
            myresult = mycursor.fetchall()
            for row in myresult:
                if (row[0] == 0):
                    print("Customer does not exist")
                    print()
                else:
                    mycursor.execute("SELECT * FROM customers WHERE id = {};".format(idNo))
                    myresultShow = mycursor.fetchall()
                    for row in myresultShow:
                        print(row)
                        
                    answer = input("Do you wish to remove this customer? Type yes for remove, no for not remove: ")
                    if (answer == "yes"):
                        mycursor.execute("DELETE FROM customers WHERE id = {};".format(idNo))
                        mydb.commit()
                        print("Customer removed")
                        print()
                    elif (answer == "no"):
                        print("Removal cancelled")
                        print()
                    else:
                        print("Invalid input, removal cancelled")
        except ValueError:
            print("Invalid input")
        quitter = input("Do you want to quit to main? Type \"yes\" to quit: ")
        
while True:
    answer = input("Enter command \n\"add\" for adding new customer \n\"remove\" to remove customers, \n\"update\" to update new customers, \n\"none\" for exiting\n->  ")
    if (answer == "update"):
        updateCustomers()
    elif (answer == "remove"):
        removeCustomers()
    elif (answer == "add"):
        addCustomers()
    elif (answer == "none"):
        break
    else:
        print("Invalid input")
        print()

