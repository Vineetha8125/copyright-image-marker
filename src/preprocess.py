# src/preprocess.py

import pandas as pd

def preprocess_csv(csv_path):
    df = pd.read_csv(csv_path)

    # Extract registration number from "Registration Number / Date"
    df['Registration Number'] = df['Registration Number / Date'].str.extract(r'(VA\d{10})')

    # Lowercase and strip title and claimant for better matching
    df['Clean Title'] = df['Title'].astype(str).str.lower().str.strip()
    df['Clean Claimant'] = df['Copyright Claimant'].astype(str).str.lower().str.strip()

    # Return processed dataframe
    return df[['Registration Number', 'Clean Title', 'Clean Claimant', 'Title']]
