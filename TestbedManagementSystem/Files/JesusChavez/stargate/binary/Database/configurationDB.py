import pymysql
class configurationDB:

    def __init__(self):
        self.__connect = set()
        self.__connection = set()
     
    def isset(self):
        return self in locals()
            
        
    def connect(self):
        self.__connection = pymysql.connect(host="earth.cs.utep.edu", user = "aquiroz10", passwd="cs4311", db="aquiroz10")
        return self.__connection