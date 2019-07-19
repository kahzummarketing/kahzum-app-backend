from django.shortcuts import render
from polls.models import Choice, Question
import mysql.connector
from mysql.connector import Error
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
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
    return HttpResponse(response)
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
