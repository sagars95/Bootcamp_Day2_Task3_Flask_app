#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database = "emplpoyees", user = "bootcamp", password = "bootcamp", host = "192.168.21.57", port = "3306")
print ("Opened database successfully");

cur = conn.cursor()

#cur.execute("INSERT INTO emp (fname,lname,email,pnumber,country,current_city)\
      #VALUES (?,?,?,?,?,?,?)");


conn.commit()
print ("Records created successfully");
conn.close()