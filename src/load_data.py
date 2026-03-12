import pandas as pd
from sqlalchemy import create_engine

columns = [
    "transaction_id", "price", "date", "postcode",
    "property_type", "new_build", "tenure",
    "paon", "saon", "street", "locality",
    "town", "district", "county",
    "ppd_category", "record_status"
]

print("Loading CSV...")
df = pd.read_csv(
    "data/Jan_26.csv",
    header=None,        # file has no header row, so tell pandas to treat the first row as data
    names=columns,   # but replace it with our cleaner names
    skiprows=1       # skip that empty row 0
)

print(f"Loaded {len(df):,} rows")
print(df.head())
print(df.columns.tolist())  # let's print all column names to verify

engine = create_engine("sqlite:///data/house_prices.db")
df.to_sql("transactions", engine, if_exists="replace", index=False)
print("Done! Database saved to data/house_prices.db")