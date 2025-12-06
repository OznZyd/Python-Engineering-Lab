import pandas
import pandas as pd


def load_data(file_path):

    column_names = [f"{i}" for i in range(30)]
    column_names[0] = "Time"
    column_names[1] = "Category"
    column_names[2] = "Sub-Category"
    column_names[3] = "Zone"
    column_names[4] = "Marc Code"
    column_names[5] = "Pick Number"
    column_names[6] = "Description_1"
    column_names[7] = "Barcode Number"
    column_names[8] = "Divert Status"

    data_file = pd.read_csv(file_path, sep=",", header=None, names= column_names, engine="python", on_bad_lines='skip')

    return data_file

if __name__ == "__main__":
    file_road = "row_data_V2.txt"
    coming_data= load_data(file_road)
    print(coming_data.head())






