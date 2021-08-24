# Meta Profile Doc

This Repository contains python script that can be used to generate HTML of Meta data using either xlsx or csv file.

## Dependencies:

- beautifulsoup4
- numpy
- pandas
- argparse

## How to run the code:

### Necessary Files To Run The Project:
The project requires three files to run successfully, A Meta Profile Doc html template (`example-page.html`) file, Input Excel file (`LstMetadataprofiltest_formatted.xlsx`) of Meta data and Excel to HTML converter (`MetaProfileDoc.py`). 

- HTML File : example-page.html -> Meta Profile Doc template.
- LstMetadataprofiltest_formatted.xlsx -> Input Data sheet for Meta data.
- MetaProfileDoc.py -> Python script for Excel to Html Parsing.

## Run Command

```
python MetaProfileDoc.py -html example-page.html -excel LstMetadataprofiltest_formatted.xlsx -config 0,1,33,34,35
```
Where 0,1,33,34,35 are the required columns, You can pass required column's numbers as comma delimited numbers but 0 is 
mandatory column because it contains information regarding formatting of rows

## XLSX Formatting Guide:

- The First column should only contain numbers (digits) and decimal points (.). 
- There are two rules , If a row belongs to list then it should contain some class indication in first column (Information) in Excel file such as (12.1) to be a part of the list, or if it is a heading (heading only contains string in first column not numbers) then it should be before the list.
- There should be no heading between list items, because it will discontinue the list, The heading should be before the starting of the list.

## Example Format:

- Below given is an example to define hierarchy, Same format should be used to create table correctly. In the example below 'x' represents row number. However script only check decimal points to format rows accordingly.

```
heading
x (list start contains plus sign)
x.x (list item one)
x.x (list item two with plus sign because it contains one child)
x.x.x (child of list item two)
```

# Other Output.html Information
## Row Colors Formatting:
- In Python script, Following colors are used for different levels of hierarchy(Rows).
    - color_RowClass1 = '#77a8a8' , Header Row. This color code is used for headings '#77a8a8'.
    - color_RowClass2 = '#eaece5' , Parent Row(In Excel file, First cell without decimal). This color code is used '#eaece5'.
    - color_RowClass3 = '#ddeedd' , In Excel file, First cell with One Decimel. This color code is used '#eaece5'.
    - color_RowClass4 = '#c0ded9' , In Excel file, First cell with Two Decimel. This color code is used '#c0ded9'.
    - color_RowClass5 = '#3b3a30' , In Excel file, First cell with Three Decimel. This color code is used '#3b3a30'.