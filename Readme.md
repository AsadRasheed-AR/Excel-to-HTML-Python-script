# Excel To HTML Parser

## This Repository contains python script that can be used to generate HTML table using either xlsx or csv file.

#### Note: It is recommended to use xlsx file for generating tables in order to avoid encoding issues.


## File paths:

- In python script, On Line no 64 'file_path' variable is used where "HTML" file path can be entered. See the example below:
```
file_path = 'example-page.html'
```
In this example, python script will use HTML file named 'example-page.html'

- In python script, On Line no 69 'filename' variable is used where "Excel or Csv" file path can be entered. See the example below:
```
filename = 'LstMetadataprofiltest_formatted.xlsx'
```
In this example, python script will use Excel file named 'LstMetadataprofiltest_formatted.xlsx'

## Row Colors Formatting:
- In Python script, Following colors are used for different levels of hierarchy(Rows).
    - color_RowClass1 = '#77a8a8' , Header Row. This color code is used for headings '#77a8a8'.
    - color_RowClass2 = '#eaece5' , Parent Row(In Excel file, First cell without decimal). This color code is used '#eaece5'.
    - color_RowClass3 = '#ddeedd' , In Excel file, First cell with One Decimel. This color code is used '#eaece5'.
    - color_RowClass4 = '#c0ded9' , In Excel file, First cell with Two Decimel. This color code is used '#c0ded9'.
    - color_RowClass5 = '#3b3a30' , In Excel file, First cell with Three Decimel. This color code is used '#3b3a30'.

## Requirements:
- The First column should only contain numbers (digits) and decimal points (.). 
- There are two rules , If a row belongs to list then it should contain some class indication in first column (Information) in Excel file such as (12.1) to be a part of the list, or if it is a heading (heading only contains string in first column not numbers) then it should be before the list.
- There should be no heading between list items, because it will discontinue the list, The heading should be before the starting of the list.

## Example Of Format:

- Below given is an example to define hierarchy, Same format should be used to create table correctly. In the example below 'x' represents row number. However script only check decimal points to format rows accordingly.

```
heading
x (list start contains plus sign)
x.x (list item one)
x.x (list item two with plus sign because it contains one child)
x.x.x (child of list item two)
```

## Necessary Files To Run The Project:

#### Note: The project requires three files to run successfully, First one is the html file in which the python script will add table. Second one is the Excel or CSV file which python script will use to generate table and the third one is the python script file itself which contains the code for parsing Excel file into Html. An Example related to this repository is given below:

- HTML File : example-page.html -> python scrip will use this file and add the newly generated table into this file.
- LstMetadataprofiltest_formatted.xlsx -> Python script will use this file to generate table and then replace the newly generated table in the html file.
- Deliverable.py -> Python script which contains the code for Excel to Html Parsing.

## Requirements (Dependencies):

- python==3.8.3
- beautifulsoup4==4.9.1
- numpy==1.18.5
- pandas==1.0.5
- argparse==1.1
- sys==3.8.3

## How to run the code:

#### Note: If the html and excel file is in the same directory then only the name of the files can be used instead of complete path, For Example,

```
python Deliverable.py -html example-page.html -excel LstMetadataprofiltest_formatted.xlsx -config 0,1,33,34,35
```
#### Where 0,1,33,34,35 are the required columns, You can pass required column's numbers as comma delimited numbers but 0 is mandatory column because it contains information regarding formatting of rows

#### Note: If the html and excel file is not in the same directory then complete path for the files should provide to run the script, For Example,

```
python Deliverable.py --html E:\<path to html file>\example-page.html --excel E:\<path to excel file>\LstMetadataprofiltest_formatted.xlsx
```

#### 'LstMetadataprofiltest_formatted.xlsx' (Excel File) can be used as a reference to generate tables correctly, However 'LstMetadataprofiltest.csv' contains same data but some errors that should be avoided. You can compare both files to see the difference.