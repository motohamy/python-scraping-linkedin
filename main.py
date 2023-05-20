import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set your LinkedIn login credentials
email = "your_email@example.com"
password = "your_password"

# Configure the Selenium WebDriver
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# Login to LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(2)
driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("password").send_keys(Keys.RETURN)

# Search for the "Family Office group"
time.sleep(3)
driver.get("https://www.linkedin.com/search/results/groups/?keywords=family%20office")
time.sleep(3)

# Parse the search results with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
group_link = soup.find("a", class_="search-result__result-link")["href"]

# Go to the group page
driver.get(group_link)
time.sleep(3)

# Scrape the group members
members = []

# Add your own logic to navigate and scrape multiple pages
soup = BeautifulSoup(driver.page_source, 'html.parser')
members_containers = soup.find_all("div", class_="group-members__details")

for member in members_containers:
    name = member.find("span", class_="group-members__name").text.strip()
    email_elem = member.find("a", class_="group-members__email")

    if email_elem:
        email = email_elem["href"].replace("mailto:", "").strip()
    else:
        email = None

    members.append({"name": name, "email": email})

print(members)

# Close the browser
driver.quit()
