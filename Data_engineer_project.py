from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

# Webscrapping the data
url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
data = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
for row in soup.find_all('tbody')[3].find_all('tr')[1:]:
    cols = row.find_all('td')
    name = cols[1].find_all('a')[-1].getText()
    market_cap = cols[2].getText()
    data = data.append({"Name":name, "Market Cap (US$ Billion)":market_cap[:-1]}, ignore_index=True)
data.to_json('bank_market_cap_1.json')

# Extracting more data using an API
url = "http://api.exchangeratesapi.io/v1/latest?access_key=3b8b965b7ce5a1af4daf6fd8828ef8cb"  #Make sure to change ******* to your API key.
response = requests.get(url)
data = response.json()

df = pd.DataFrame(columns=["Currency", "Rate"])
dictrates = data.get("rates")
for currency in dictrates:
    rate = dictrates.get(currency)
    df = df.append({"Currency": currency, "Rate": rate}, ignore_index=True)
df = df.set_index("Currency")
df.to_csv('exchange_rates_1.csv')

# Extract bank and market cap data from the JSON file bank_market_cap.json
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe

columns=['Name','Market Cap (US$ Billion)']
def extract():
    # Write your code here
    data = pd.DataFrame(columns = columns)
    data = data.append(extract_from_json("bank_market_cap_1.json"), ignore_index = True)
    return data

df = pd.read_csv("exchange_rates.csv", index_col = 0)
exchange_rate = float(df.loc["GBP"].values)

# Transform the market cap currency using the exchange rate data
def transform(data):
    data['Market Cap (US$ Billion)'] = round(data["Market Cap (US$ Billion)"] * exchange_rate, 3)
    data.rename(columns = {'Market Cap (US$ Billion)':'Market Cap (GBP$ Billion)'}, inplace=True)
    return data

# Load the transformed data into a seperate CSV
def load(data):
    data.to_csv("bank_market_cap_gbp.csv")

def log(message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y' # Hour-Minute-Second-Monthname-Day-Year.
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("dealership_logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')

def ETL_pipeline():
    log("ETL Job Started")

    log("Extract phase Started")
    extracted_data = extract()
    log("Extract phase Ended")

    log("Transform phase Started")
    transformed_data = transform(extracted_data)
    log("Transform phase Ended")

    log("Load phase Started")
    load(transformed_data)

ETL_pipeline()
