# import all libraries
from selenium.webdriver import ChromeOptions
import pandas as pd
import time
from all_functions import *

def process():
    options =ChromeOptions()
    # options.headless =True
    driver = Chrome(executable_path="H://web_scrap/driver/chromedriver.exe")
    # Read the Excel file data
    input_file = pd.read_excel('Amazon_scraping.xlsx', engine="openpyxl")
    result = []
    start_time=time.time()
    for index, row in input_file.iterrows():
        asin = str(row["Asin"])
        country = str(row["country"])
        url = f"https://www.amazon.{country}/dp/{asin}"
        data = get_data(url, driver)
        if (index+1)%100==0:
            time_taken=time.time()-start_time
            print(f"Time taken to 100 processed rows:{time_taken}")
            start_time =time.time()  # time for after completing each round of 100 urls
        if data:
            result.append(data)
        if len(result) == 100:  # get scrape data of minimum 100 URL
            break
    # Scraped data represent in the JSON file
    make_json_file_of_scraped_data(result)
    # Connect MySQL database amd dump data into database
    load_data_into_mysql(result)

if __name__ == "__main__":
    process()
