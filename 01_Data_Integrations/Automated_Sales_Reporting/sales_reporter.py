import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO,
                    format= '%(asctime)s %(message)s',
                            handlers= [logging.FileHandler("process.log"),
                                       logging.StreamHandler()])


def ingest_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        logging.error("Error: File not found! Please check the path")
        return None


def clean_and_process(df):
    df = df.drop(axis=1, columns="Unnamed: 0")
    df['Date'] = pd.to_datetime(df['Date'])
    df["Piece"] = df["Piece"].fillna(value=0)
    df["Total_Sales"] = df["Piece"] * df["Price"]
    grand_total = df["Total_Sales"].sum()
    logging.info(grand_total)
    return df


def generate_report(df):
    category_summary = df.groupby("Product_Name")["Total_Sales"].sum()
    plt.bar(category_summary.index, category_summary.values, color='skyblue')
    plt.xlabel("Category")
    plt.ylabel("Values")
    plt.title("Category Summary")

    plt.savefig("Sales_Chart.png")

    df["Date"] = df["Date"].dt.strftime('%Y-%m-%d')
    df.to_excel("clean_report.xlsx", index=False)
    logging.info("Reporting completed: Files created")


if __name__ == "__main__":
    raw_data_path = "raw_data.xlsx"

    dataframe = ingest_data(raw_data_path)

    if dataframe is not None:
        processed_data = clean_and_process(dataframe)

        generate_report(processed_data)









