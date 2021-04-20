import json
import pprint
from csv_parser import parse_csv
from utils import is_float


if __name__ == "__main__":
    
    raw_data = parse_csv('data.csv')
    
    profit_dict_key = 'Profit (in millions)'

    # filter function is checking to see whether the profit represents a number
    valid_data = list(filter(lambda x: is_float(x[profit_dict_key]) == True, raw_data))
    
    # top 20
    top_sorted = sorted(valid_data, key=lambda x: float(x[profit_dict_key]), reverse=True)[:20]


    print(len(raw_data))
    print(len(valid_data))
    pprint.pprint(top_sorted, indent=1)


    # outputs data2.json with valid data
    with open('data2.json', 'w') as out_file:
        json.dump(valid_data, out_file, indent=2)
