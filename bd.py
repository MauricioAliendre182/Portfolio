import pymysql

def get_information():
    return pymysql.connect(host="Maps182.mysql.pythonanywhere-services.com",
                          user="Maps182",
                          password="M@ps182Register",
                          db="Registration")