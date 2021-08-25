#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:52:27 2021

@author: ismael
"""

# Import required libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
import pandas as pd
import requests
import numpy as np


####################### Google API Credentials #######################
gc = gspread.service_account(filename="stage-mcphy-4523d4f594b4.json")      # Open API Google Project Credentials.

#-----------------------------------------------------------------------------------------------------------------------# 



####################### Global Variables #######################
global sh

#-----------------------------------------------------------------------------------------------------------------------# 



####################### Functions ####################### 

def Insert_DF_inGsheets(gSheetKey,gsheetindex,df):        # Function for write inside GSpread Sheet.   
    """
    Input :
        gSheetKey: Google spread Sheet key
        gsheetindex: Google spread Sheet index
        df: Data Frame
        
    Output :
        nothing
        """
    global sh
    sh = gc.open_by_key(gSheetKey)              # sh = Google spread Sheet.
    Name = sh.get_worksheet(gsheetindex)        #-> 0 - first sheet, 1 - second sheet etc.
    your_dataframe = pd.DataFrame(df)           # Create Variable Type Data Frame. 
    set_with_dataframe(Name, your_dataframe)    #-> THIS EXPORTS YOUR DATAFRAME TO THE GOOGLE SHEET (Tab Name, DataFrame).


def openDF(gSheetKey,index):                    # Function for Open a Table Database from Server.
    """
    Input :
        gSheetKey: Google spread Sheet key
        index: Index value 
        
    Output :
        data frame
        """
    global sh
    sh = gc.open_by_key(gSheetKey)              # sh = Google spread Sheet. 
    Name = sh.get_worksheet(index)              # Name = open Tab x Depending of index value. ( 0 - first sheet,   1 - second sheet etc.).	
    Table = Name.get_all_records()              # Table = values of all Cells.
    dfRead = pd.DataFrame(Table)                # Convert table to DataFrame Type.
    return dfRead                               # Return DataFrame.



def SortH2MDistributionData():
    """
    Input :
        nothing
        
    Output :
        data frame
        """
    Tableau = openDF('1R_Ovf6fv3xLOvO9C1OOCi8vHn8m1JjpyH8ytzuu-tc4',0)

    PTdf = Tableau.loc[Tableau['Month'] == 'PT 8.202a']
    PTdf.drop('TagId', axis=1, inplace=True)
    PTdf.drop('Hour', axis=1, inplace=True)
    PTdf.drop('Year', axis=1, inplace=True)
    PTdf.drop('Day', axis=1, inplace=True)
    PTdf.drop('Month', axis=1, inplace=True)
	#print(PTdf)

    FTdf = Tableau.loc[Tableau['Month'] == 'FT 8.201']
    FTdf.drop('TagId', axis=1, inplace=True)
    FTdf.drop('Hour', axis=1, inplace=True)
    FTdf.drop('Year', axis=1, inplace=True)
    FTdf.drop('Day', axis=1, inplace=True)
    FTdf.drop('Month', axis=1, inplace=True)
	#print(FTdf)

    PCVdf = Tableau.loc[Tableau['Month'] == 'PCV 8.201']
    PCVdf.drop('TagId', axis=1, inplace=True)
    PCVdf.drop('Hour', axis=1, inplace=True)
    PCVdf.drop('Year', axis=1, inplace=True)
    PCVdf.drop('Day', axis=1, inplace=True)
    PCVdf.drop('Month', axis=1, inplace=True)
	#print(PCVdf)

    TTdf = Tableau.loc[Tableau['Month'] == 'TT 8.201']
    TTdf.drop('TagId', axis=1, inplace=True)
    TTdf.drop('Hour', axis=1, inplace=True)
    TTdf.drop('Year', axis=1, inplace=True)
    TTdf.drop('Day', axis=1, inplace=True)
    TTdf.drop('Month', axis=1, inplace=True)
	#print(TTdf)


    DFMerge1 = pd.merge(PTdf,TTdf, on='TimeStr', how='outer', suffixes=('_PTdf','_TTdf'))
    DFMerge2 = pd.merge(DFMerge1,FTdf, on='TimeStr', how='outer', suffixes=('','_FTdf'))
    DFMerge3 = pd.merge(DFMerge2,PCVdf, on='TimeStr', how='outer', suffixes=('','_PCVdf'))
    DFMerge3.TimeStr = pd.to_datetime(DFMerge3.TimeStr)
    DFMerge3 = DFMerge3.sort_values('TimeStr')
    DFMerge3['TimeStr'] = DFMerge3['TimeStr'].dt.tz_localize(None)
    DFMerge3.rename(columns = {'Value_PTdf': 'PT 8.202a', 'Value_TTdf': 'TT 8.201', 'Value': 'FT 8.201', 'Value_PCVdf': 'PCV 8.201'}, inplace = True)
    DFMerge3['Hour'] = DFMerge3.TimeStr.dt.hour
    DFMerge3['Month'] = DFMerge3.TimeStr.dt.month
    DFMerge3['Day'] = DFMerge3.TimeStr.dt.day
    DFMerge3['Year'] = DFMerge3.TimeStr.dt.year
    custom_sort = ['TimeStr','Year','Month', 'Day', 'Hour', 'PT 8.202a', 'TT 8.201', 'FT 8.201', 'PCV 8.201']
    DFMerge3 = DFMerge3[custom_sort]



    return DFMerge3
	#DFMerge3.to_excel('X:\Ismail\TestAcommodation.xlsx', index=False)
	


def SortH2MEnergyData():
    """
    Input :
        nothing
        
    Output :
        data frame
        """
    Tableau = openDF('1R_Ovf6fv3xLOvO9C1OOCi8vHn8m1JjpyH8ytzuu-tc4',1)

    Energy_APPdf = Tableau.loc[Tableau['Month'] == 'IDC_Energie_Apparente']
    Energy_APPdf.drop('TagId', axis=1, inplace=True)
    Energy_APPdf.drop('Hour', axis=1, inplace=True)
    Energy_APPdf.drop('Year', axis=1, inplace=True)
    Energy_APPdf.drop('Day', axis=1, inplace=True)
    Energy_APPdf.drop('Month', axis=1, inplace=True)

    Energy_Reactdf = Tableau.loc[Tableau['Month'] == 'IDC_Energy_ReActivePower_Inst']
    Energy_Reactdf.drop('TagId', axis=1, inplace=True)
    Energy_Reactdf.drop('Hour', axis=1, inplace=True)
    Energy_Reactdf.drop('Year', axis=1, inplace=True)
    Energy_Reactdf.drop('Day', axis=1, inplace=True)
    Energy_Reactdf.drop('Month', axis=1, inplace=True)

    Energy_Activedf = Tableau.loc[Tableau['Month'] == 'IDC_Energy_ActivePower_Inst']
    Energy_Activedf.drop('TagId', axis=1, inplace=True)
    Energy_Activedf.drop('Hour', axis=1, inplace=True)
    Energy_Activedf.drop('Year', axis=1, inplace=True)
    Energy_Activedf.drop('Day', axis=1, inplace=True)
    Energy_Activedf.drop('Month', axis=1, inplace=True)


    DFMerge1 = pd.merge(Energy_APPdf,Energy_Reactdf, on='TimeStr', how='outer', suffixes=('_EnergyApp','_EnergyReact'))
    DFMerge3 = pd.merge(DFMerge1,Energy_Activedf, on='TimeStr', how='outer', suffixes=('','_EnergyAct'))
    DFMerge3.TimeStr = pd.to_datetime(DFMerge3.TimeStr)
    DFMerge3 = DFMerge3.sort_values('TimeStr')
    DFMerge3['TimeStr'] = DFMerge3['TimeStr'].dt.tz_localize(None)
    DFMerge3.rename(columns = {'Value_EnergyApp': 'kVA', 'Value_EnergyReact': 'KVAR', 'Value': 'kW'}, inplace = True)
    DFMerge3['Hour'] = DFMerge3.TimeStr.dt.hour
    DFMerge3['Month'] = DFMerge3.TimeStr.dt.month
    DFMerge3['Day'] = DFMerge3.TimeStr.dt.day
    DFMerge3['Year'] = DFMerge3.TimeStr.dt.year
    custom_sort = ['TimeStr','Year','Month', 'Day', 'Hour', 'kVA', 'KVAR', 'kW']
    DFMerge3 = DFMerge3[custom_sort]

    return DFMerge3
	#DFMerge3.to_excel('X:\Ismail\TestAcommodation.xlsx', index=False)




def SortH2MotorsData():
    """
    Input :
        nothing
        
    Output :
        data frame
        """
    Tableau = openDF('1R_Ovf6fv3xLOvO9C1OOCi8vHn8m1JjpyH8ytzuu-tc4',2)

    Air_compdf = Tableau.loc[Tableau['Month'] == 'Air Compressor ONOFF']
    Air_compdf.drop('TagId', axis=1, inplace=True)
    Air_compdf.drop('Hour', axis=1, inplace=True)
    Air_compdf.drop('Year', axis=1, inplace=True)
    Air_compdf.drop('Day', axis=1, inplace=True)
    Air_compdf.drop('Month', axis=1, inplace=True)

    D1Cooling_unitdf = Tableau.loc[Tableau['Month'] == 'D1 Cooling Unit ONOFF']
    D1Cooling_unitdf.drop('TagId', axis=1, inplace=True)
    D1Cooling_unitdf.drop('Hour', axis=1, inplace=True)
    D1Cooling_unitdf.drop('Year', axis=1, inplace=True)
    D1Cooling_unitdf.drop('Day', axis=1, inplace=True)
    D1Cooling_unitdf.drop('Month', axis=1, inplace=True)

    Air_extractordf = Tableau.loc[Tableau['Month'] == 'Air Extractor ONOFF']
    Air_extractordf.drop('TagId', axis=1, inplace=True)
    Air_extractordf.drop('Hour', axis=1, inplace=True)
    Air_extractordf.drop('Year', axis=1, inplace=True)
    Air_extractordf.drop('Day', axis=1, inplace=True)
    Air_extractordf.drop('Month', axis=1, inplace=True)


    DFMerge1 = pd.merge(Air_compdf,D1Cooling_unitdf, on='TimeStr', how='outer', suffixes=('_AirComp','_D1Cooling'))
    DFMerge3 = pd.merge(DFMerge1,Air_extractordf, on='TimeStr', how='outer', suffixes=('','_AirExtract'))
    DFMerge3.TimeStr = pd.to_datetime(DFMerge3.TimeStr)
    DFMerge3 = DFMerge3.sort_values('TimeStr')
    DFMerge3['TimeStr'] = DFMerge3['TimeStr'].dt.tz_localize(None)
    DFMerge3.rename(columns = {'Value_AirComp': 'Air Compressor', 'Value_D1Cooling': 'D1 Cooling Unit', 'Value': 'Air Extractor'}, inplace = True)
    DFMerge3['Hour'] = DFMerge3.TimeStr.dt.hour
    DFMerge3['Month'] = DFMerge3.TimeStr.dt.month
    DFMerge3['Day'] = DFMerge3.TimeStr.dt.day
    DFMerge3['Year'] = DFMerge3.TimeStr.dt.year
    custom_sort = ['TimeStr','Year','Month', 'Day', 'Hour', 'Air Compressor', 'D1 Cooling Unit', 'Air Extractor']
    DFMerge3 = DFMerge3[custom_sort]

    return DFMerge3
	#DFMerge3.to_excel('X:\Ismail\TestAcommodation.xlsx', index=False)



def Data_MAP():
    """
    Input :
        nothing
        
    Output :
        nothing
        """
    TableauMap = openDF('1q1Rpj8GCWCoOElwYp_QCzqG84FQooP8gb-rRZcqnb_g',0)
    return TableauMap


#-----------------------------------------------------------------------------------------------------------------------# 




#DfH2M = SortH2MDistributionData()
#print(DfH2M)
#DfH2M.columns
#
#
#DfMap = Data_MAP()
#print(DfMap)
#DfMap.columns

#dff = SortH2MotorsData()
#print(dff)
#dff.columns



#-----------------------------------------------------------------------------------------------------------------------# 



#Tableau = openDF('1R_Ovf6fv3xLOvO9C1OOCi8vHn8m1JjpyH8ytzuu-tc4',0)          # Tableau = Function to Open a DF (GoogleSheetsAPIKEY,Tab#).
#
#MAPTable = openDF('1q1Rpj8GCWCoOElwYp_QCzqG84FQooP8gb-rRZcqnb_g',0)
#MAPTable.rename(columns={'Latitud ': 'lat', 'Longitud': 'lon'}, inplace=True)
#MAPTable.to_excel('test.xlsx')
#
#MAPTable = pd.DataFrame(MAPTable)
#MAPTable.columns
#print (MAPTable.columns)
#print(Tableau)                                                              # Print Data Frame.