import requests
from bs4 import BeautifulSoup

# Send a GET request to the forum website
response = requests.get("https://gsmarthub.com/")

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the thread elements
threads = soup.find_all("div", class_="post-body")

# Extract the title, author, date, and content
for thread in threads:
    title = thread.find("h2", class_="entry-title").text.strip()
    author = thread.find("span", class_="author-name").text.strip()
    date = thread.find("span", class_="entry-date").text.strip()
    content = thread.find("div", class_="entry-content").text.strip()

    print("Title:", title)
    print("Author:", author)
    print("Date:", date)
    print("Content:", content)
    print("--------------------")



# second file
import csv
import requests
from bs4 import BeautifulSoup

# Send a GET request to the news website
response = requests.get("https://www.example.com/news")

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the headlines and summaries
headlines = soup.find_all("h2", class_="headline")
summaries = soup.find_all("p", class_="summary")

# Write the data to a CSV file
with open("news_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Headline", "Summary"])  # Write the header row

    # Write the extracted data row by row
    for headline, summary in zip(headlines, summaries):
        writer.writerow([headline.text.strip(), summary.text.strip()])

print("Data extraction complete.")



# 3rd file Gathering Forum Thread Titles, Authors, Dates, and Content:
import requests
from bs4 import BeautifulSoup

# Send a GET request to the forum website
response = requests.get("https://www.example.com/forum")

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the forum thread elements
threads = soup.find_all("div", class_="thread")

# Extract the title, author, date, and content
for thread in threads:
    title = thread.find("h3", class_="title").text.strip()
    author = thread.find("span", class_="author").text.strip()
    date = thread.find("span", class_="date").text.strip()
    content = thread.find("div", class_="content").text.strip()

    print("Title:", title)
    print("Author:", author)
    print("Date:", date)
    print("Content:", content)
    print("--------------------")

