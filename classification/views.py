import pymysql
import ipaddress

from django.shortcuts import render
from django.http import HttpResponse

class CIDRClassification():
    def __init__(self):
        pass

    # A group query
    def SearchAgroup(self, request, IP):
        addr = ipaddress.ip_address(IP)
        re_type = None

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='cidr', passwd='123456789', db='CIDRSystem')
        cursor = conn.cursor()

        sql = "SELECT * FROM A_group"
        cursor.execute(sql)

        group_row = cursor.fetchall()
        for line in group_row:
            ip_cidr = ipaddress.IPv4Network(line[2], strict=False)
            if addr in ip_cidr:
                return HttpResponse(line[1])
            else:
                return HttpResponse(None)

	# B group query
    def SearchBgroup(self, request, IP):
        addr = ipaddress.ip_address(IP)
        re_type = None

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='cidr', passwd='123456789', db='CIDRSystem')
        cursor = conn.cursor()

        sql = "SELECT * FROM B_group"
        cursor.execute(sql)

        group_row = cursor.fetchall()
        for line in group_row:
            ip_cidr = ipaddress.IPv4Network(line[2], strict=False)
            if addr in ip_cidr:
                return HttpResponse(line[1])
            else:
                return HttpResponse(None)
