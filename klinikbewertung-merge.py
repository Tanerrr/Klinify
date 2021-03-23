from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("/Users/MEHMET/Downloads/chromedriver")

klinikliste = ["https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-augenklinik-dr-hoffmann-braunschweig/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-marienstift-braunschweig/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-kliniken-herzogin-elisabeth-braunschweig/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-goettingen/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-tiefenbrunn-rosdorf/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-friederikenstift-hannover/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-annastift-hannover/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-drk-clementinenhaus-hannover/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-sophien-klinik-hannover/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-grossburgwedel/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-lehrte/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-lindenbrunn-coppenbruegge/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-hameln/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-kreis-und-stadtkrankenhaus-alfeld/bewertungen?allbew#more",
"https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-hildesheim/bewertungen?allbew#more"]



names=[] #List to name of the hospitals
ratings=[] #List to rating of the product
reviews=[] #List to reviews of hospitals
departments=[] #List to departments of reviews
dates=[] #List to dates of reviews
titles=[] #List to titles of reviews


x=0
for x in klinikliste:
    url = x
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    name = driver.find_element_by_tag_name("h1").text
    time.sleep(3)
    try:
        driver.find_element_by_id("ez-accept-all").click()
    except:
        print("no cookies")
    time.sleep(3)

    for i in soup.find_all("article", attrs={"class":"bewertung"}):
        names.append(name)
        title = i.find("h2")
        titles.append(title.text)
        date = i.find("time")
        dates.append(date.text)
        department = i.find("a", href=True)
        departments.append(department.text)
        review = i.find("p").text.split("\n")
        reviews.append(review)
        rating = i.find("section", attrs={"class":"rating"}).text.split("\n")
        ratings.append(rating)
    # for i in soup.find_all("section", attrs={"class":"rating"}):
    #     rating = i.find("img")
    #     ratings.append(rating["class"])

df = pd.DataFrame({'Name':names, 'Department':departments, 'Date':dates, 'Title':titles, 'Review':reviews, 'Rating':ratings}) 
df.to_csv('kliniks_reviews9.csv', index=False, encoding='utf-8')

# print(names)
# print(dates)
# print(ratings)
# print(titles)
# print(reviews)