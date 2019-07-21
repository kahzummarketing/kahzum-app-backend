from django.shortcuts import render
from polls.models import Choice, Question
import mysql.connector
from mysql.connector import Error
# Create your views here.
from django.http import HttpResponse
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def statistics(request, storeId):
    datatypes = ["Traffic", "Visits", "Customers", "New", "Returning", "Averagestay", "StoreID", "UpdateTime"]
    data = {}
    try:
        mydb = mysql.connector.connect(host= "kahzum.com",user= "kahzumco_testusr", password="11111", database = "kahzumco_test")
        mydb.commit()
        if mydb.is_connected():
            cursor = mydb.cursor(buffered = True)
            cursor.execute('SELECT * FROM StoreMetrics WHERE StoreID = %s' % storeId)
            rows = cursor.fetchall()
            for row in rows:
                for i in range(len(row)):
                    print("in here")
                    data[datatypes[i]]=row[i]
            jsonData = json.dumps(data, indent=4, sort_keys=True, default=str)
    except Error as e:
        jsonData = "Error while connecting to mySQL"
    return HttpResponse(jsonData)

def user(request, username):
    jsonData = username
    datatypes = [ "__id", "username", "password", "pi", "storeName"]
    data = {}
    try:
        mydb = mysql.connector.connect(host= "kahzum.com",user= "kahzumco_testusr", password="11111", database = "kahzumco_test")
        mydb.commit()
        if mydb.is_connected():
            cursor = mydb.cursor(buffered = True)
            cursor.execute('SELECT * FROM Login WHERE Username = %s' % username)
            rows = cursor.fetchall()
            
            for row in rows:
                for i in range(len(row)):
                    data[datatypes[i]]=row[i]
            #jsonData = json.dumps(data, indent=4, sort_keys=True, default=str)
    except Error as e:
        jsonData = "Error while connecting to mySQL"
    return HttpResponse(jsonData)

def traffic(request, question_id):
    
    try:
        mydb = mysql.connector.connect(host= "kahzum.com",user= "kahzumco_testusr", password="11111", database = "kahzumco_test")
        mydb.commit()
        if mydb.is_connected():
            cursor = mydb.cursor(buffered = True)
            cursor.execute('SELECT Traffic FROM StoreMetrics WHERE StoreID = %s' % question_id)
            rows = cursor.fetchone()
            q = rows
            response = "Traffic: %s devices" % q
    except Error as e:
        response = "Error while connecting to mySQL"
    return HttpResponse(response, )
def visits(request, question_id):
    
    try:
        mydb = mysql.connector.connect(host= "kahzum.com",user= "kahzumco_testusr", password="11111", database = "kahzumco_test")
        mydb.commit()
        if mydb.is_connected():
            cursor = mydb.cursor(buffered = True)
            cursor.execute('SELECT Visits FROM StoreMetrics WHERE StoreID = %s' % question_id)
            rows = cursor.fetchone()
            q = rows
            response = "Visits: %s times" % q
    except Error as e:
        response = "Error while connecting to mySQL"
    return HttpResponse(response)
def customers(request, question_id):
    
    try:
        mydb = mysql.connector.connect(host= "kahzum.com",user= "kahzumco_testusr", password="11111", database = "kahzumco_test")
        mydb.commit()
        if mydb.is_connected():
            cursor = mydb.cursor(buffered = True)
            cursor.execute('SELECT Customers FROM StoreMetrics WHERE StoreID = %s' % question_id)
            rows = cursor.fetchone()
            q = rows
            response = "Customers: %s people" % q
    except Error as e:
        response = "Error while connecting to mySQL"
    return HttpResponse(response)
def new(request, question_id):
    
    try:
        mydb = mysql.connector.connect(host= "kahzum.com",user= "kahzumco_testusr", password="11111", database = "kahzumco_test")
        mydb.commit()
        if mydb.is_connected():
            cursor = mydb.cursor(buffered = True)
            cursor.execute('SELECT New FROM StoreMetrics WHERE StoreID = %s' % question_id)
            rows = cursor.fetchone()
            q = rows
            response = "New Customers: %s people" % q
    except Error as e:
        response = "Error while connecting to mySQL"
    return HttpResponse(response)
def returning(request, question_id):
    
    try:
        mydb = mysql.connector.connect(host= "kahzum.com",user= "kahzumco_testusr", password="11111", database = "kahzumco_test")
        mydb.commit()
        if mydb.is_connected():
            cursor = mydb.cursor(buffered = True)
            cursor.execute('SELECT Returning FROM StoreMetrics WHERE StoreID = %s' % question_id)
            rows = cursor.fetchone()
            q = rows
            response = "Returning Customers: %s people" % q
    except Error as e:
        response = "Error while connecting to mySQL"
    return HttpResponse(response)
def averagestay(request, question_id):
    
    try:
        mydb = mysql.connector.connect(host= "kahzum.com",user= "kahzumco_testusr", password="11111", database = "kahzumco_test")
        mydb.commit()
        if mydb.is_connected():
            cursor = mydb.cursor(buffered = True)
            cursor.execute('SELECT Averagestay FROM StoreMetrics WHERE StoreID = %s' % question_id)
            rows = cursor.fetchone()
            q = rows
            response = "Average Stay: %s minutes" % q
    except Error as e:
        response = "Error while connecting to mySQL"
    return HttpResponse(response)
