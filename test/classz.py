#!/usr/bin/python
#  -*- coding: utf-8 -*- 
'''
@Copyright © 2017 sanbo Inc. All rights reserved.
@Description: todo
@Version: 1.0
@Create: 2017年1月7日 下午3:58:38 
@Author: sanbo
'''

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary



if __name__ == '__main__':
    "创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
    "创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print "Total Employee %d" % Employee.empCount
