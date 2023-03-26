import pymysql

def get_information():
    return pymysql.connect(host="Maps182.mysql.pythonanywhere-services.com",
                          user="Maps182",
                          password="M@ps18244Registration",
                          db="Maps182$Registration")