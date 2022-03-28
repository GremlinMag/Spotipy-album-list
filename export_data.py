import json
import pandas

def export_to_json(data, output):
    json_string = json.dumps(data)                      # convert data to json format
    with open(output, 'w') as outfile:                  # open file
        json.dump(json_string, outfile)                 # save file

def export_to_excel(data, output):
    df1 = pandas.DataFrame(data, columns=['name'])      # convert data to xls format
    df1.to_excel(output)                                # save file

def export_to_csv(data, output):
    df1 = pandas.DataFrame(data, columns=['name'])      # convert data to csv format
    df1.to_csv(output)                                  # save file
