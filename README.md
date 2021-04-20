# Highest Profit

## General JSON Structure

    [
        {
            year: Int
            Rank: Int
            Company: String
            Revenue: Float
            Profit: Float
        },
        ...
    ]

### PART 1

    - print total initial rows
    - print rows after all invalid 'profit' rows removed

I approached this project by first converting the csv data to a list of dictionaries using the built in python 'csv' library, and from there I had data which could easily be transformed.

Using the list of dictionaries, I removed the invalid data using a filter function that checks whether the value for the value in the 'Profit' column represented a number.

eg:
```python 
valid_data = list(filter(lambda x: is_float(x[profit_dict_key]) == True, raw_data))
```
Printed output of `valid_data` is 25500

### PART 2

    - output valid rows into data2.json file
    - order rows based on profit value, and print top 20 rows 

Using the filtered data I used the built in python'json' library to output the 'data2.json' file

I then sorted the filtered data by profit from highest to lowest using the sorted function, and saved the first 20

eg:
```python
top_sorted = sorted(valid_data, key=lambda x: x[profit_dict_key], reverse=True)[:20]
```
printed output of `top_sorted` data is 25131

### PART 3

    - Think about how you may do this using SQL

Given the format of the data given, I could consider making a single table for the data, calling it FinancialData, with the primary key being the index of the list. If additional company information was given, I would make 'Company' into a separate table, along with the additional company information.

Given a singular table with the data, I'd use the following query to fetch the top 20 companies.

eg:
```SQL
SELECT TOP 20
FROM FinancialData
ORDER BY Profit DESC
```
