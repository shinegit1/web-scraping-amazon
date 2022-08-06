Task Description : In this main.py file, we scrape a minimum hundred URLs.
The URL will be in format of"https://www.amazon.{country}/dp/{asin}".The country code and Asin parameters are in
the CSV file https://docs.google.com/spreadsheets/d/1BZSPhk1LDrx8ytywMHWVpCqbm8URTxTJrIRkD7PnGTM/edit?usp=sharing.
The CSV file contains 1000 rows. Use Selenium or bs4 to Scarpe the following details from the page.
1. Product Title
2. Product Image URL
3. Price of the Product
4. Product Details

Program description:
1. In main.py file, imported all required python packages and all_functions.py python file and using
2. The process() method work as root method for using chromedriver, read Amazon_scraping.xlsx file data, make url link
[www.amazon.{country_code}/dp/{Asin} ] then call other functions such as
3. The get_data() method use for fatch the data from the URL link, and then prepare a list of scraped data.
4. The make_json_file_for_scraped_data() method use for create a json file and dump list data in the file.
5. At the end, The load_data_into_mysql() method use for connecting with Mysql DB table and dump all data into database.


Requirements : {
Python : 3.10,
Pandas : 1.4.3,
selenium : 4.3.0,
beautifulsoup4 : 4.11.1,
}
