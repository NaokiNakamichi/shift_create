import numpy as np, pandas as pd
from pulp import *
from ortoolpy import addvars, addbinvars
import random
import datetime
import openpyxl
import jpholiday
from openpyxl.styles import PatternFill


class Shift:
    def __init__(self,name):
        self.shift = pd.read_excel(name,sheet_name='Shift',index_col=0)
        self.manage = pd.read_excel(name,sheet_name='Manage',index_col=0)
        self.member = pd.read_excel(name,sheet_name='Member',index_col=0)
        self.member = self.member.T
        self.detail = pd.read_excel(name,sheet_name='Detail',index_col=0)

        print(self.shift)

        # 従業員数と月の日数
        days, number_employee = self.shift.shape[0], self.shift.shape[1]

        # 日付の配列、従業員の名前の配列
        date,employee = self.shift.index, self.shift.columns

        # 変数の追加
        # self.shift['V_need_dif'] = addvars(days)         # 必要人数に達していない時のペナルティ変数
        # self.shift['V_gender_rate'] = addvars(days)      # 女性が少ない時のペナルティ
        # self.shift['V_experience'] = addvars(days)       # 新人だけになった時のペナルティ
        # self.shift['need'] = self.manage.need            # 必要人数

        # 足りない人が入れば終了
        # shortage = []
        # for index,r in self.shift[employee].iterrows():
        #     if sum(r) < int(self.shift.at[index,'need']):
        #         shortage.append(index)
        # if shortage:
        #     raise ValueError(day + '日足りません')


    def return_data(self):
        return self.shift, self.manage, self.member, self.detail
