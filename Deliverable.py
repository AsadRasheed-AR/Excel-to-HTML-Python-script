#!/usr/bin/env python
# coding: utf-8

#Import Necessary Libraries

from typing import cast
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import bs4



#Row Colors, Different Colors are used for different Levels
color_RowClass1 = '#77a8a8'
color_RowClass2 = '#eaece5'
color_RowClass3 = '#ddeedd'
color_RowClass4 = '#c0ded9'
color_RowClass5 = '#3b3a30'


#Function that is used to check if the cell value is either number or String
#Number defines the hierarchy while String means heading.
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


#Row with plus sign
#Html to generate that could expand by clicking on (+) sign.
expand_next_row = '<tr class="MDrow1 expand-next-row"><td class="MDrow1"><span class="plus-sign">+</span><span class="plus-sign" style="display: none;">–</span>'

#Row next to plus sign
expandable_row = '<tr class="expandable-row"><td class="MDrow1">'


#Function to get class name that can be used for fomatting( background color, text color exapandable )
def getClassname(number_of_dec,next_number_of_dec,cellValue):

    #Check if first cell contains number then create hierarchy of rows, If cell contain string then make heading
    if(hasNumbers(cellValue)):
        if ((number_of_dec == 0)):                                     #Whole Number
            if (number_of_dec < next_number_of_dec):
                return f'<tr class="MDrow1 RowClass2 expand-next-row" style="background-color:{color_RowClass2}" ><td class="MDrow1"><span class="plus-sign">+</span><span class="plus-sign" style="display: none;">–</span>'
            return f'<tr class="MDrow RowClass2" style="background-color:{color_RowClass2}"><td class="MDrow1">'
        elif number_of_dec == 1:                                       #One Decimel
            if (number_of_dec < next_number_of_dec):
                return f'<tr class="MDrow1 expandable-row expand-next-row RowClass3" style="display: none; background-color:{color_RowClass3}"><td class="MDrow1"><span class="plus-sign" style="display: none;">+</span><span class="plus-sign">–</span>'
            return f'<tr class="expandable-row RowClass3" style="display: none; background-color:{color_RowClass3}"><td class="MDrow1">'
        elif number_of_dec == 2:                                       #Two Decimel
            if (number_of_dec < next_number_of_dec):
                return f'<tr class="MDrow1 expandable-row expand-next-row RowClass4" style="display: none; background-color:{color_RowClass4}"><td class="MDrow1"><span class="plus-sign" style="display: none;">+</span><span class="plus-sign">–</span>'
            return f'<tr class="expandable-row RowClass4" style="display: none; background-color:{color_RowClass4}"><td class="MDrow4">'
        elif number_of_dec == 3:                                       #Three Decimel
            if (number_of_dec < next_number_of_dec):
                return f'<tr class="MDrow1 expandable-row expand-next-row RowClass5" style="display: none; color:#fff; background-color:{color_RowClass5}" ><td class="MDrow1"><span class="plus-sign" style="display: none;">+</span><span class="plus-sign">–</span>'
            return f'<tr class="expandable-row RowClass5" style="display: none; color:#fff; background-color:{color_RowClass5}"><td class="RowClass5">'
        else:
            return f'<tr class="">'
    else:                                                            #Header Row
        return f'<tr class="Header1row RowClass2" style="background-color:{color_RowClass1}"><td class="">{cellValue}'


#Read orignal html file, for embedding new table
file_path = 'example-page.html'
with open(file_path) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# soup = soup.find("table",{"class": "mainTable"})


#Input File (Excel or CSV) to parse for creating html Table.
filename = 'LstMetadataprofiltest_formatted.xlsx'

if '.csv' in filename:
    #Read csv to create html table
    df = pd.read_csv(filename,header=None,encoding = "ISO-8859-1")
elif '.xlsx' in filename:
    #Read Excel File to create html table
    df = pd.read_excel(filename,header=None,encoding= "ISO-8859-1")

df = df[[0,1,33,34,35]]         #Select the specific columns (including first column that defines the hierarchy) to create table
df = df.dropna(how='all')       #Select the empty rows
df = df.reset_index(drop=True)  #Remove the empty rows


#Choose columns with data and ignore the class column
sub_set_df_fhtml = df[[1,33,34,35]]     #Select Columns that contain data excluding first column that contains foramtting info

#Replace nan values with " "
sub_set_df_fhtml = sub_set_df_fhtml.replace(np.nan, '', regex=True)
df = df.replace(np.nan, '', regex=True)

# Create New Html Table
html = sub_set_df_fhtml.to_html(index=False,header=False)

#Create a parser to parse newly created table for adding custom classes
new_soup = BeautifulSoup(html,"html.parser")
tags = new_soup.find_all('tr',recursive=True)


#Iterate over each row of newly created table and check which class it belongs to and then make necessary changes/formatting
for num , tag in enumerate(tags):
    if (num > 0 and (num < len(tags)-1)):
        #Row Fomatting
        #print(num)
        row_class = getClassname(str(df[0][num]).count('.'),str(df[0][num+1]).count('.'),str(df[0][num]))
        tags[num] = str(tag).replace("<tr>\n<td>", row_class)
        tags[num] = BeautifulSoup(tags[num], 'lxml')
        tags[num] = tags[num].find_all('tr',recursive=True)[0]
        #print(tags[num])
    elif((num < 1)):
        #Header Formatting
        #print(num)
        row_class = getClassname(str(df[0][num]).count('.'),str(df[0][num+1]).count('.'),str(df[0][num]))
        tags[num] = str(tag).replace("<tr>", '<tr class="Headerrow RowClass1">')
        tags[num] = BeautifulSoup(tags[num], 'lxml')
        tags[num] = tags[num].find_all('tr',recursive=True)[0]
        #print(tags[num])


#remove rows from the existing table to add new rows with formatting
for tr in new_soup.find_all("tr"): 
    tr.decompose()

#Add new rows in table generated from Excel with formatting (Custom classes)
for tag in tags:
    new_soup.tbody.append(tag)

#Replace Existing table of sorce html file with the newly generated table from excel
soup.find("table",{"class": "mainTable"}).replace_with(new_soup)


#Generate Output Html File
new_html =soup.contents
new_html = soup.prettify("utf-8")

#Write changes in html file
with open("output1.html", "wb") as file:
    file.write(new_html)
