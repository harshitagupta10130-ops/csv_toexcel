import pandas as pd
import argparse
import logging
import os
from utilis import clean_data

#setup logging
logging.basicConfig(filename = "app.log",level=logging.INFO)

def convert_csv_to_excel(input_file,output_file):
    try:
        if not os.path.exists(input_file):
            logging.error("File not found")
            print("File not found!")
            return
        print("Reading csv...")
        df = pd.read_csv(input_file)

        print("Cleaning data...")
        df = clean_data(df)

        print("Converting to excel..")
        df.to_excel(output_file,engine="openpyxl",index=False)

        print("Done!")
        logging.info("Conversion Successful")
    except Exception as e:
        logging.error(str(e))
        print("Error",e)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="CSV to Excel converter")
    parser.add_argument("input",help="Input csv file")
    parser.add_argument("output",help="output excel file")
    args = parser.parse_args()
    convert_csv_to_excel(args.input,args.output)