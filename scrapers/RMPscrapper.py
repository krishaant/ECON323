from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time 
import pandas as pd
import re 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# chrome_driver_path = "/Users/krishaantpathmanathan/ECON323 final projext/chromedriver"





# creating empty dataframes
all_reviews = pd.DataFrame(columns=["Professor_ID", 
                                     "Professor_Name", 
                                     "University", 
                                     "Department", 
                                     "Quality", 
                                     "Difficulty", 
                                     "Emotion", 
                                     "Class_Name", 
                                     "Comment", 
                                     "Thumbs_Up", 
                                     "Thumbs_Down", 
                                     "Review_Date"])

# UBC is 1413
driver.get("https://www.ratemyprofessors.com/search/professors/1413?q=*")

time.sleep(5)

# Load previously saved URLs if they exist
try:
    with open("teacher_urls.txt", "r") as f:
        all_urls = f.read().splitlines()
    print(f"✅ Loaded {len(all_urls)} previously saved URLs.")
except FileNotFoundError:
    all_urls = []
    print("📂 No previous URLs found. Starting fresh.")

# Clicking show more 
for i in range(100000000):  
    try:
        # Find the 'Show More' button and click it
        show_more = driver.find_element(By.XPATH, "//button[text()='Show More']")
        driver.execute_script("arguments[0].scrollIntoView(true);", show_more)
        
        show_more.click()

        # Collect all teacher URLs from the current page
        teacher_cards = driver.find_elements(By.XPATH, "//a[starts-with(@class, 'TeacherCard__StyledTeacherCard')]")
        new_urls = [card.get_attribute("href") for card in teacher_cards]

        # Filter new URLs to exclude duplicates
        unique_new_urls = [url for url in new_urls if url not in all_urls]

        # If new URLs are found, add them to the list and save to file
        if unique_new_urls:
            all_urls.extend(unique_new_urls)  

            with open("teacher_urls.txt", "w") as f:
                for url in all_urls:
                    f.write(url + "\n")
            
    except:
        break  

# Print all collected URLs
print(all_urls)

len(all_urls)