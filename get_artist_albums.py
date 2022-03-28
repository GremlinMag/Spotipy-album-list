import sys
from data import get_data
from export_data import export_to_json, export_to_excel, export_to_csv
import pandas as pd

if __name__ == "__main__":
    albums = get_data(sys.argv[1])                                                  # get names of albums from spotify api
    sys.argv[2] = sys.argv[2].lower()                                               # translate value to lowercase

    try:
        output_filename = sys.argv[3]                                               # check the existence of the parameter 3
    except IndexError:
        sys.argv[1] = sys.argv[1].lower()                                           # translate value to lowercase
        sys.argv[1] = "".join(c for c in sys.argv[1] if c not in "\/:*?<>|")        # delete dangerous characters (windows will throw an error
                                                                                    # with an incorrect name if any of them are present in string)
        output_filename = sys.argv[1]+'.'+sys.argv[2]                               # concatenate strings to make file name

    match sys.argv[2]:                                                              # check extension and chose right option
        case "csv": export_to_csv(albums, output_filename)
        case "xlsx": export_to_excel(albums, output_filename)
        case "json": export_to_json(albums, output_filename)
        case "raw": print(albums)