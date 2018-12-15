# coding:utf8
'''
Created on 2018��11��28��

@author: samsung
'''
import pymysql
import sys

class TransferMoney(object):
    def __init__(self,conn):
        self.conn = conn
    

    def check_acct_available(self, souce_acctid):
        pass
    
    
    def has_enough_money(self, souce_acctid, money):
        pass
    
    
    def reduce_money(self, source_acctid, money):
        pass
    
    
    def add_money(self, target_acctid, money):
        pass
    
    
    def transfer(self,source_acctid,target_acctid,momey):
        try:
            self.check_acct_available(souce_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(souce_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            raise e
            self.conn.rollback()
        
if __name__=="__main__":
    souce_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    conn = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "123456aaa",
    charset = "utf8",
    db = "imooc"
    )
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(souce_acctid,target_acctid,money)
    except Exception as e:
        print(e)
        