# Excel To HTML Parser

## This Repository contains python script that can be used to generate HTML table using either xlsx or csv file.

### Note: It is recommended to use xlsx file for generating tables in order to avoid encoding issues.


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

## 'LstMetadataprofiltest_formatted.xlsx' (Excel File) can be used as a reference to generate tables correctly, However 'LstMetadataprofiltest.csv' contains same data but some errors that should be avoided. You can compare both files to see the difference.