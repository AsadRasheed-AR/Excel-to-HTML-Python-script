#!/usr/bin/env python
# coding: utf-8

# In[265]:


import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import bs4


# In[266]:


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


# In[267]:


#Row with plus sign
expand_next_row = '<tr class="MDrow1 expand-next-row"><td class="MDrow1"><span class="plus-sign">+</span><span class="plus-sign" style="display: none;">–</span>'
#Row next to plus sign
expandable_row = '<tr class="expandable-row"><td class="MDrow1">'


# In[268]:


def getClassname(number_of_dec,next_number_of_dec,cellValue):
#     try:
#         val = float(cellValue)
    if(hasNumbers(cellValue)):
        if ((number_of_dec == 0)):                                     #Whole Number
            if (number_of_dec < next_number_of_dec):
                return '<tr class="MDrow1 RowClass2 expand-next-row"><td class="MDrow1"><span class="plus-sign">+</span><span class="plus-sign" style="display: none;">–</span>'
            return '<tr class="MDrow RowClass2"><td class="MDrow1">'
        elif number_of_dec == 1:                                       #One Decimel
            if (number_of_dec < next_number_of_dec):
                return '<tr class="MDrow1 expandable-row expand-next-row RowClass3" style="display: none;"><td class="MDrow1"><span class="plus-sign" style="display: none;">+</span><span class="plus-sign">–</span>'
            return '<tr class="expandable-row RowClass3" style="display: none;"><td class="MDrow1">'
        elif number_of_dec == 2:                                       #Two Decimel
            if (number_of_dec < next_number_of_dec):
                return '<tr class="MDrow1 expandable-row expand-next-row RowClass4" style="display: none;"><td class="MDrow1"><span class="plus-sign" style="display: none;">+</span><span class="plus-sign">–</span>'
            return '<tr class="expandable-row RowClass4" style="display: none;"><td class="MDrow4">'
        elif number_of_dec == 3:                                       #Three Decimel
            if (number_of_dec < next_number_of_dec):
                return '<tr class="MDrow1 expandable-row expand-next-row RowClass5" style="display: none;"><td class="MDrow1"><span class="plus-sign" style="display: none;">+</span><span class="plus-sign">–</span>'
            return '<tr class="expandable-row RowClass5" style="display: none;"><td class="RowClass5">'
        else:
            return '<tr class="">'
    else:                                                            #Header Row
        return f'<tr class="Header1row RowClass2"><td class="Header1row">{cellValue}'


# #Function to determine the type of row
# def getClassname(number_of_dec,next_number_of_dec,cellValue):  
#     try:
#         val = float(cellValue)
#         if (number_of_dec < next_number_of_dec):
#             print("Adding plus sign")
#             return ('<tr class="MDrow1 RowClass2 expand-next-row"><td class="MDrow1"><span class="plus-sign" style="display: inline-block;">+</span><span class="plus-sign" style="display: none;">–</span>')
#         elif (number_of_dec == next_number_of_dec):
#             print("Adding expandable")
#             return('<tr class="expandable-row" style="display: table-row;"><td class="MDrow1">')
#         else:
#             print("normal")
#             return '<tr class="MDrow1 RowClass2"><td>'
#     except: #Header Row
#         return f'<tr class="Header1row RowClass1"><td class="Header1row">{cellValue}'


# In[269]:


#Read orignal html file, for embedding new table
file_path = 'example-page.html'
with open(file_path) as fp:
    soup = BeautifulSoup(fp, 'html.parser')


# In[270]:


#orignal html
soup.table


# In[271]:


#Read csv to create html table
df = pd.read_csv('LstMetadataprofiltest.csv',header=None,encoding = "ISO-8859-1")
df = df[[0,1,33,34,35]]
df = df.dropna(how='all')
df = df.reset_index(drop=True)
df.head(10)


# In[272]:


#Choose columns with data and ignore the class column
sub_set_df_fhtml = df[[1,33,34,35]]
sub_set_df_fhtml.head(10)


# In[273]:


len(sub_set_df_fhtml[1])


# In[274]:


#Replace nan values with " "
sub_set_df_fhtml = sub_set_df_fhtml.replace(np.nan, '', regex=True)
sub_set_df_fhtml.head(10)


# In[275]:


# New Html Table
html = sub_set_df_fhtml.to_html(index=False,header=False)
html


# In[276]:


#Create a parser to parse newly created table for adding custom classes
new_soup = BeautifulSoup(html,"html.parser")
tags = new_soup.find_all('tr',recursive=True)


# In[277]:


new_soup


# In[278]:


#Iterate over each row and check which class it belongs to and then make necessary changes
for num , tag in enumerate(tags):
    if (num > 0 and (num < len(tags)-1)):
        print(num)
        row_class = getClassname(str(df[0][num]).count('.'),str(df[0][num+1]).count('.'),str(df[0][num]))
        tags[num] = str(tag).replace("<tr>\n<td>", row_class)
        tags[num] = BeautifulSoup(tags[num], 'lxml')
        tags[num] = tags[num].find_all('tr',recursive=True)[0]
        print(tags[num])
    elif((num < 1)):
        #Header
        print(num)
        row_class = getClassname(str(df[0][num]).count('.'),str(df[0][num+1]).count('.'),str(df[0][num]))
        tags[num] = str(tag).replace("<tr>", '<tr class="Headerrow RowClass1">')
        tags[num] = BeautifulSoup(tags[num], 'lxml')
        tags[num] = tags[num].find_all('tr',recursive=True)[0]
        print(tags[num])


# In[279]:


#remove rows to add new rows with modifications
for tr in new_soup.find_all("tr"): 
    tr.decompose()


# In[280]:


#Add new rows in table with modifications (Custom classes)
for tag in tags:
    new_soup.tbody.append(tag)


# In[281]:


new_soup.tbody


# In[282]:


#remove rows to add new rows with modifications
for tr in soup.find_all("tr"): 
    tr.decompose()


# In[283]:


#Add new rows in table with modifications (Custom classes)
for tag in tags:
    soup.tbody.append(tag)


# In[284]:


soup.tbody


# In[285]:


#Generate Output Html File
new_html =soup.contents
new_html = soup.prettify("utf-8")
with open("output1.html", "wb") as file:
    file.write(new_html)


# In[286]:


hasNumbers('2.1')


# In[ ]:




