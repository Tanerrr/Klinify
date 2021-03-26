from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/MEHMET/Downloads/chromedriver")

url = "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-augenklinik-dr-hoffmann-braunschweig"
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

# klinikliste = ["https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-augenklinik-dr-hoffmann-braunschweig",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-marienstift-braunschweig",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-kliniken-herzogin-elisabeth-braunschweig",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-goettingen",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-tiefenbrunn-rosdorf",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-friederikenstift-hannover",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-annastift-hannover",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-drk-clementinenhaus-hannover",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-sophien-klinik-hannover",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-grossburgwedel",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-lehrte",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-lindenbrunn-coppenbruegge",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-hameln",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-kreis-und-stadtkrankenhaus-alfeld",
# "https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-krankenhaus-hildesheim"]

# print(klinikliste[1])

names=[] #List to name of the hospitals
ratings=[] #List to rating of the product
reviews=[] #List to reviews of hospitals
departments=[] #List to departments of reviews
dates=[] #List to dates of reviews
titles=[] #List to titles of reviews

for i in soup.find_all("article", attrs={"class":"bewertung"}):
    title = i.find("h2")
    titles.append(title.text)
    date = i.find("time")
    dates.append(date.text)
    department = i.find("a", href=True)
    departments.append(department.text)
    review = i.find("p")
    reviews.append(review.text)
    #rating = i.find("section", attrs={"class":"rating"})
    #ratings.append(rating.text)
for i in soup.find_all("section", attrs={"class":"rating"}):
    rating = i.find("img")
    ratings.append(rating["class"])

df = pd.DataFrame({'Department':departments, 'Date':dates, 'Title':titles, 'Review':reviews}) 
df.to_csv('klinik1_reviews.csv', index=False, encoding='utf-8')

# print(departments)
# print(dates)
# print(ratings)
# print(titles)
# print(reviews)

# i=0
# for i in klinikliste:
#     url = i
#     driver.get(url)
#     name = driver.find_element_by_tag_name("h1").text
#     names.append(name)
# # content = driver.page_source
# # soup = BeautifulSoup(content, 'html.parser')


            
# for a in soup.findAll('article', attrs={'class':'js-klinik-row standard'}):
#     name = a.find('a',href=True)
#     names.append(name.text)
#     adres = a.find('section', attrs={'class': 'content'})
#     adresses.append(adres.text)
#     rating = EC.presence_of_element_located(
#             (By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[2]/article[7]/section[2]/dl/dd[1]/img"))
#     ratings.append(rating)

# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('article', attrs={'class':'js-klinik-row standard'}):
#name = a.find('article', attrs={'class':'js-klinik-row standard'})
# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    
# prices.append(price.text)
# ratings.append(rating.text) 

# print(names)

# df = pd.DataFrame({'Name':names}) 
# df.to_csv('klinik1.csv', index=False, encoding='utf-8')