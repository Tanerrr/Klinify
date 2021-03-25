from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd


df = pd.read_excel('Klinikliste.xlsx')

driver = webdriver.Chrome(executable_path="/Applications/chromedriver")


def scrap_daten(url):
    driver.get(url)
    driver.maximize_window()

    ''' Exit from Google's Agree verification '''
    try:
        WebDriverWait(driver, 2).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe")))
        agree = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="introAgreeButton"]/span/span')))
        agree.click()
    except:
        pass

    sleep(3)

    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')
    name = soup.find(
        'div', {'class': 'section-hero-header-title-top-container'})
    name = name.h1.text.strip()
    # print(name)
    stern = soup.find(
        'span', {'class': 'section-star-display'})
    stern = stern.text.strip()
    # print(stern)
    kommantare_zahl = soup.find(
        'button', {'class': 'widget-pane-link'})
    kommantare_zahl = int(kommantare_zahl.text.strip().split()[0])
    # print(kommantare_zahl)
    adresse = soup.find_all(
        'div', {'class': 'ugiz4pqJLAG__primary-text gm2-body-2'})

    if adresse[0].text.strip().split()[0] == 'COVID-19':
        adresse = adresse[1].text.strip()
    else:
        adresse = adresse[0].text.strip()

    try:
        Kommentare = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button.widget-pane-link"))

        )
        Kommentare.click()
    except:
        print('Quiting Point 3')
        driver.quit()

    div_num = 1
    schleife = 0
    kliniks = []

    sleep(5)

    while True:

        schleife += 1

        scrollable_div = driver.find_element_by_css_selector(
            'div.section-layout.section-scrollbox.scrollable-y.scrollable-show'
        )
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight',
            scrollable_div
        )

        sleep(3)

        source = driver.page_source
        soup = BeautifulSoup(source, 'lxml')

        komments = soup.find_all(
            'div', {'class': 'section-review ripple-container gm2-body-2'})  #  section-review-content

        if len(komments) >= kommantare_zahl or schleife > 70:
            break
        else:
            continue
    sleep(5)

    for div_num in range(1, kommantare_zahl * 3, 3):

        try:
            Click_More = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[9]/div[{div_num}]/div/div[3]/div[3]/jsl/button"))
            )
            Click_More.click()
        except:
            pass

    sleep(10)
    source = driver.page_source
    soups = BeautifulSoup(source, 'lxml')

    komments = soups.find_all(
        'div', {'class': 'section-review ripple-container gm2-body-2'})

    for komment in komments:

        datum = komment.find(
            'span', {'class': 'section-review-publish-date'})

        datum = datum.text.strip()
        # print(datum)

        komment_stern = komment.find(
            'span', {'class': 'section-review-stars'})
        komment_stern = int(komment_stern["aria-label"].strip().split()[0])
        # print("kommen stern ist : ", komment_stern)

        try:
            komment_text = komment.find(
                'span', {'class': 'section-review-text'}).text.strip()
            # print(komment_text)
        except:
            komment_text = ' '

        try:
            like = komment.find(
                'span', {'class': 'section-review-thumbs-up-count'}).text.strip()
        except:
            like = 0

        einzelne = {
            'Name': name,
            'AVG - Sterne': stern,
            'Zahl der Kommentaren': kommantare_zahl,
            'Adresse': adresse,
            'Sterne': komment_stern,
            'Kommentare': komment_text,
            'Datum': datum,
            'Likes': like
        }

        kliniks.append(einzelne)

    print(kliniks)

    return kliniks, name


def get_data(links):
    kliniks = links.to_list()
    while len(kliniks) > 0:
        try:
            einzelne_klinik, names = scrap_daten(kliniks[0])
            data_frame = pd.DataFrame(einzelne_klinik)
            data_frame.to_csv(f'csvs/{names}.csv', index=False)
            # wenn die Daten Erfolgreich bekommen wurde, geht nachste Klinik weiter.
            del kliniks[0]
        except:  #  wenn die Daten der Klinik nicht bekommen wurde, werde es wieder versuchen.
            continue
    print('daten wurden bekommen')
    quit()


get_data(df['Link Google Maps'])
