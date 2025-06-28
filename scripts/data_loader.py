import pandas as pd;
import os;

def load_data():
    try:
        processed = os.path.join("data","processed","car_data.csv")
        raw = os.path.join("data","raw","car_data.csv")
        
        if os.path.exists(processed):
            print("Loading processed dataset...")
            return pd.read_csv(processed)
        
        if (os.path.exists(raw)):
            print("Loading raw dataset")
            df = pd.read_csv(raw)
            df = process_dataset(df)

            os.makedirs(os.path.dirname(processed), exist_ok = True)

            df.to_csv(processed, index = False)
            return df
    except FileNotFoundError as err:
        raise err("Neither Files were found.\nCheck data folder and ensure at least raw dir and the raw data set is inside it")
    


def process_dataset(df):
    try:
        df = df.rename(columns={'Price ($)': 'Price', 'Dealer_No ': 'Dealer_No'})
        ## Preencher valores ausentes com a média da coluna
        df['Annual Income'].fillna(df['Annual Income'].mean(), inplace=True)
        df['Price'].fillna(df['Price'].mean(), inplace=True)

        # Preencher valores ausentes com strings
        df['Customer Name'].fillna("John Doe", inplace=True)
        df['Gender'].fillna("Unknown", inplace=True)
        df['Dealer_Name'].fillna("Unknown Dealer", inplace=True)
        df['Company'].fillna("Unknown Company", inplace=True)
        df['Model'].fillna("Unknown Model", inplace=True)
        df['Engine'].fillna("Unknown Engine", inplace=True)
        df['Transmission'].fillna("Manual", inplace=True)
        df['Color'].fillna("Unknown Color", inplace=True)
        df['Dealer_No'].fillna("Unknown Dealer No", inplace=True)
        df['Body Style'].fillna("Unknown Body Style", inplace=True)
        df['Dealer_Region'].fillna("Unknown Dealer Region", inplace=True)

        print("Data prepared successfully")
        return df
    except Exception as err:
        print(f"Unexpected error: ${err}")
        raise;