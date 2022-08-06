from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import json
import mysql.connector

# Declare a function for scrape the data from the URL
def get_data(url: str, driver: Chrome):
    data = {}
    # check the URL has an Error  is 404 or not
    try:
        driver.get(url)
    except AttributeError:
        print(f"{url} not available")
    soup = BeautifulSoup(driver.page_source, 'lxml', multi_valued_attributes=None)   # Parse the HTML documents
    image_url =None
    prod_title = None
    price =None
    prod_detail=None
    product_details_list = []
    try:
        prod_title = soup.find(id="productTitle")
        image_url = soup.find(id="imgBlkFront")
        price = soup.find(class_="a-size-base a-color-price a-color-price")
        prod_detail = soup.find("ul", class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list")
    except AttributeError:
        pass
    # put the data in the dictionary when all variable are not None
    if prod_title and image_url and price and prod_detail:
        data['Title'] = prod_title.string
        data['image_url'] = image_url.attrs.get("src")
        data['product_price'] =price.string
        for detail in prod_detail:
            product_details_list.append(detail.get_text(strip=True))
        data['product_details'] ="".join(product_details_list)
    return data  # return the dictionary

def load_data_into_mysql(list_data):
    # ------- Establish a MySQL connection -------
    my_database = mysql.connector.connect(host="localhost", user="root", password="password", db="assignment")
    # Get the cursor, which is used to traverse the database, line by line
    my_cursor = my_database.cursor()
    # Create the INSERT INTO sql query
    query = "insert into amazon_scrape(product title, product image url, product price, product details)" \
            "values(%s,%s,%s,%s)"
    # Assign values:
    values =[tuple(data.values()) for data in list_data]
    # Execute sql Query
    my_cursor.executemany(query, values)
    # Close the cursor, Commit the transaction and Close the database connection
    my_cursor.close()
    my_database.commit()
    my_database.close()
    print("Data load in MySQL database table successfully.")

def make_json_file_of_scraped_data(data_list):
    json_data = {}
    with open("Amazon_scrape_data.json", "w") as scrape_file:
        for dict_item in range(len(data_list)):
            json_data[dict_item] = data_list[dict_item]
        json.dump(json_data, scrape_file, indent=4)
