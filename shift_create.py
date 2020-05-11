import numpy as np, pandas as pd
from pulp import *
from ortoolpy import addvars, addbinvars
import random
import datetime
import openpyxl
import jpholiday
from openpyxl.styles import PatternFill


class Shift:
    def __init__(self):
        pass

class GetExcelData:
    def __init__(self,name):
        self.shift = pd.read_excel(name,sheet_name='Shift',index_col=0)
        self.manage = pd.read_excel(name,sheet_name='Manage',index_col=0)
        self.member = pd.read_excel(name,sheet_name='Member',index_col=0)
        self.member = self.member.T
        self.detail = pd.read_excel(name,sheet_name='Detail',index_col=0)

    def return_data(self):

        return self.shift, self.manage, self.member, self.detail


class ShiftCheck:
    def __init__(self):
        shortage = []
        for index,r in shift[employee].iterrows():
            if sum(r) < int(shift.at[index,'need']):
                shortage.append(index)
        if shortage:
            day = ''
            for i in shortage:
                day += (str(i) + '日足りません')
                print(day)
            sys.exit()
