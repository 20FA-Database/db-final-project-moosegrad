"""
    @author Colin Grad
    @date 12/7/2020
    *mySql search

"""
#import
import mysql.connector
from mysql.connector import errorcode
import sys
#def for menu

# r= reviews w = reviewer s = supplement_Brand b = brand

#code 
try:
    cm_connection = mysql.connector.connect(user="cm_user", password="pyuser5134", host="127.0.0.1", database="Supplement_Reviews")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalide credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print("Cannot connect to database:", err)
else:
    print("Success")
    supp_cursor = cm_connection.cursor()
    start = True
    while start == True:
        print("""
******Menu******
A. View Tables //
B. View Data in Table //
C. Add Review to Table //
D. Remove Review Ferom Table 
E. Describe a Table //
F. View Reviews by Brand/Stars //
G. View Supplement Info //
Q. To quit //
            """)
        choice = input("Enter the Letter of your Choice: ")
        print()
        if choice == "A" or choice == "a": #view tables
            print("-----Tables-----")
            supp_query = ("SHOW tables;")
            try:
                supp_cursor.execute(supp_query)
                for row in supp_cursor.fetchall():
                    print("{}".format(row[0]))
            except mysql.connector.Error as err:
                print("Error: {}".format(err))
        
        elif choice == "B" or choice == "b": #view data of tables
            viewStart = True
            while viewStart == True:
                print("""
    1. Reviewer
    2. Reviews
    3. Supplement_Brand
    4. Supplements
    5. To Exit to Main Menu
                """)
                viewTable = input("Pick a table to View: ")
                if viewTable == "1":
                    supp_query = ("SELECT * FROM Reviewer;")
                    print("ReviewerID Firstname LastName")
                    try:
                        supp_cursor.execute(supp_query)
                        for row in supp_cursor.fetchall():
                            print("{}          {}     {}".format(row[0],row[1],row[2]))
                    except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                elif viewTable == "2":
                    supp_query = ("SELECT * FROM Reviews;")
                    print("ReviewID SuppID BrandID ReviewerID Stars")
                    try:
                        supp_cursor.execute(supp_query)
                        for row in supp_cursor.fetchall():
                            print("{}        {}      {}       {}          {}".format(row[0],row[1],row[2],row[3],row[4]))
                    except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                elif viewTable == "3": 
                    supp_query = ("SELECT * FROM Supplement_Brand;")
                    print("BrandID BrandName   Location")
                    try:
                        supp_cursor.execute(supp_query)
                        for row in supp_cursor.fetchall():
                            print("{}       {}      {}".format(row[0],row[1],row[2]))
                    except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                elif viewTable == "4":
                    supp_query = ("SELECT * FROM Supplements;")
                    print("SuppID BrandID  SuppName       SuppType")
                    try:
                        supp_cursor.execute(supp_query)
                        for row in supp_cursor.fetchall():
                            print("{}      {}        {}        {}".format(row[0],row[1],row[2],row[3]))
                    except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                elif viewTable == "5":
                     viewStart = False
                else:
                    print("That was not a valid Option")
            
        elif choice == "C" or choice == "c": #add data to table
            addStart = True
            goAhead = True
            while addStart == True:
                supp_query = ("SELECT MAX(ReviewID) FROM Reviews;")
                supp_cursor.execute(supp_query)
                for row in supp_cursor.fetchall():
                    print("Last Review Number = {}".format(row[0]))
                rID = input("Enter a RviewID one higher then Listed above ")
                print("""
    1. for Outlift by Nutrex
    2. for WheyISo by nutrex
    3. for MesoMorph by First Phorm
    4. for Iso Whey by First Phorm
    5. for Pre-Aminos by Rule 1
    6. for Natural Whey by Rule 1
    7. for Spazmatic by Tim Muller
    8. for Pump Plus by Tim Muller
    9. for Savage AF by Dynamic
    10. for Natty Whey by Dynamic""")
                sID = input("Enter Supplement ID: ")
                dropStart = True
                print("""
    1. For Nutrex
    2. for First Phorm
    3. Rule 1
    4. Tim Muller
    5. Dynamic""")
                bID = input("Enter Brand ID: ")
                reID = input("Enter your reviewerID: ")
                st = input("Enter Start 1-5: ")
                supp_query = ("INSERT INTO Reviews(ReviewID, SuppID, BrandID, ReviewerID, Stars) Values (%s, %s, %s, %s, %s);")
                try:
                    supp_cursor.execute(supp_query,[rID, sID, bID, reID, st])
                    cm_connection.commit()
                except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                addStart = False
        elif choice == "D" or choice == "d": #remove data in table
            dropStart = True
            while dropStart == True:
                supp_query = ("Select * From Reviews;")
                try:
                    supp_cursor.execute(supp_query)
                    print("ReviewID")
                    for row in supp_cursor.fetchall():
                        print("{}   {}  {}  {}  {}".format(row[0],row[1],row[2],row[3],row[4]))
                except mysql.connector.Error as err:
                    print("Error: {}".format(err))
                dropChoice = input("Enter 'Q' to quit or Enter ReviewID to drop: ")
                if dropChoice == "q":
                    dropStart = False
                else:
                    supp_query = ("DELETE FROM Reviews WHERE ReviewID = %s LIMIT 1;")
                    try:
                        supp_cursor.execute(supp_query,[dropChoice])
                        cm_connection.commit()
                        print("Dropped Review" + dropChoice)
                    except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                    
        elif choice == "E" or choice == "e": #desc table
            print("""
    1. Reviewer
    2. Reviews
    3. Supplement-Brand
    4. Supplements
    5. to Exit to Main Menu
                """)
            descStart = True
            while descStart == True:
                tableChoice = input("Pick a table to Describe: ")
                if tableChoice == "1":
                    supp_query = ("desc Reviewer;")
                elif tableChoice == "2":
                    supp_query = ("desc Reviews;")
                elif tableChoice == "3":
                    supp_query = ("desc Supplement_Brand;")
                elif tableChoice == "4":
                    supp_query = ("desc Supplements;")
                elif tableChoice == "5":
                    descStart = False
                else:
                    print("That was not a valid Option")
                try:
                    supp_cursor.execute(supp_query)
                    for row in supp_cursor.fetchall():
                        print("{}".format(row[0]))
                except mysql.connector.Error as err:
                        print("Error: {}".format(err))
        elif choice =="F" or choice == "f": #by Brand
            brandStart = True
            while brandStart == True:
                print("""
    1. Sort By Brand
    2. Sort By Stars
    3. Search by Both
    4. To Exit to main Menu """)
                sBS = input("Enter Choice: ")
                if sBS == "1":
                    
                    print("""
        Sort Reviews By Brand
        1. For Nutrex
        2. for First Phorm
        3. Rule 1
        4. Tim Muller
        5. Dynamic
        6. to Exit to Main Menu""")
                    brandChoice = input("Enter a brand To Review")
                    if brandChoice == "1":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 1;")
                    elif brandChoice == "2":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 2;")     
                    elif brandChoice == "3":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 3;")
                    elif brandChoice == "4":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 4;")
                    elif brandChoice == "5":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 5;")
                    elif brandChoice == "6":
                        brandStart = False
                    else:
                        print("Invalide Choice!")
                    try:
                        supp_cursor.execute(supp_query)
                        for row in supp_cursor.fetchall():
                            print("{}       {}          {} ".format(row[0],row[1],row[2]))
                    except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                elif sBS == "2":
                    numStars = input("Enter Number of Stars 1-5: ")
                    supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.Stars = %s;")
                    try:
                        supp_cursor.execute(supp_query,[numStars])
                        for row in supp_cursor.fetchall():
                            print("{}       {}          {} ".format(row[0],row[1],row[2]))
                    except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                elif sBS == "3":
                    print("""
        Sort Reviews By Brand
        1. For Nutrex
        2. for First Phorm
        3. Rule 1
        4. Tim Muller
        5. Dynamic
        6. to Exit to Main Menu""")
                    brandChoice = input("Enter a brand To Review: ")
                    starsNum = input("Enter Number of Stars 1-5: ")
                    if brandChoice == "1":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 1 AND r.Stars = %s;")
                    elif brandChoice == "2":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 2 AND r.Stars = %s;")     
                    elif brandChoice == "3":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 3 AND r.Stars = %s;")
                    elif brandChoice == "4":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 4 AND r.Stars = %s;")
                    elif brandChoice == "5":
                        supp_query = ("SELECT b.BrandName, s.SuppName, r.Stars FROM Reviews AS r INNER JOIN Supplement_Brand as b ON r.BrandID = b.BrandID INNER JOIN Supplements AS s ON r.SuppID = s.SuppID WHERE r.BrandID = 5 AND r.Stars = %s;")
                    elif brandChoice == "6":
                        brandStart = False
                    else:
                        print("Invalide Choice!")
                    try:
                        supp_cursor.execute(supp_query,[starsNum])
                        for row in supp_cursor.fetchall():
                            print("{}       {}          {} ".format(row[0],row[1],row[2]))
                    except mysql.connector.Error as err:
                        print("Error: {}".format(err))
                elif sBS == "4":
                    brandStart = False
                else:
                    print("Invalid Input")
                    
                
        elif choice == "G" or choice == "g": #view Supplement info
            vpStart = True
            while vpStart == True:
                print("""

        1. for Outlift
        2. for WheyISo
        3. for MesoMorph
        4. for Iso Whey
        5. for Pre-Aminos
        6. for Natural Whey
        7. for Spazmatic
        8. for Pump Plus
        9. for Savage AF
        10. for Natty Whey
        11. To exit to Main Menu""") 
                suppChoice = input("Enter Supplement Choice: ")
                if suppChoice == "1":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 1;")
                elif suppChoice == "2":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 2;")
                elif suppChoice == "3":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 3;")
                elif suppChoice == "4":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 4;")
                elif suppChoice == "5":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 5;")
                elif suppChoice == "6":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 6;")
                elif suppChoice == "7":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 7;")
                elif suppChoice == "8":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 8;")
                elif suppChoice == "9":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 9;")
                elif suppChoice == "10":
                    supp_query = ("Select s.SuppName, b.BrandName, s.SuppType, AVG(r.Stars) From Supplements AS s INNER JOIN Supplement_Brand AS b ON s.BrandID = b.BrandID INNER JOIN Reviews AS r ON s.SuppID = r.SuppID WHERE s.SuppID = 10;")
                elif suppChoice == "11":
                    vpStart = False
                try:
                    supp_cursor.execute(supp_query)
                    print("SuppName    BrandName   SuppType    Avg Stars")
                    for row in supp_cursor.fetchall():
                        print("{}     {}     {}   {} ".format(row[0],row[1],row[2],row[3]))
                except mysql.connector.Error as err:
                    print("Error: {}".format(err))
                    
        elif choice == "Q" or choice == "q": #quit
            start=False
            sys.exit
        else:
            print("That is not a valid option try again!")
    supp_cursor.close()
    cm_connection.close()

