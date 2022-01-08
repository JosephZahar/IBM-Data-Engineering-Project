# IBM-Data-Engineering-Project
<p align="justify">
We will apply foundational Python skills by implementing different techniques to collect and work with data. Playing the role of a Data Engineer and extract data from multiple file formats, transform it into specific datatypes, and then load it into a single source for analysis. We will also implement webscraping and extracting data with APIs to gather informations from new data sources. This project aims to collect large datasets from multiple sources and transform them into one primary source, and web scraping to gain valuable business insights all with the use of Python. The final product of this project aims to retrieve a dataset of the largest bank in the world along with their market capitalisation in $ and transforming it to British Pound by extracting currency rating using an API an finally load our new dataset into a new file.
</p>

## Raw data 1: Extract Data Using Web Scraping
<p align="justify">
The wikipedia webpage https://en.wikipedia.org/wiki/List_of_largest_banks provides information about largest banks in the world by various parameters. We will first scrape the data from the table 'By market capitalization' and store it in a JSON file for future analysis.
</p>
<p align="center">
<img width="562" alt="Screen Shot 2022-01-08 at 2 40 33 AM" src="https://user-images.githubusercontent.com/70657426/148624164-403ad767-52b0-401a-8d3d-2d5f311aa7d2.png">
</p>

## Raw data 2: Extract Data Using API
Using ExchangeRate-API we will extract currency exchange rate data. 
<p align="center">
<img width="910" alt="getapi" src="https://user-images.githubusercontent.com/70657426/148624412-4aba4eff-fbdd-4ef8-8804-4c17b2ff6462.png">
</p>

## Create an ETL pipeline
In this final part we will create and run an ETL process, extract bank and market cap data from the JSON file bank_market_cap.json, transform the market cap currency to GBP using the exchange rate data and load the transformed data into a seperate CSV.
<p align="center">
<img width="394" alt="Screen Shot 2022-01-08 at 2 48 26 AM" src="https://user-images.githubusercontent.com/70657426/148624490-9692260e-ef30-432c-a273-4d4c1ff2acb6.png">
</p>
