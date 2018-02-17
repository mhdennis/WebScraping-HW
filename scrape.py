
# coding: utf-8




#Import BeautifulSoup and splinter 
from bs4 import BeautifulSoup
from splinter import Browser 
import time 
import pandas as pd
from selenium import webdriver





def init_browser()
    executable_path = {'executable_path':'/Users/mayadennis/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser

    mars_data = {}






    #Visit NASA Mars News URL
    mars = "https://mars.nasa.gov/news/"
    browser.visit(mars)





# Scrape for Most Recent Article
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    article = soup.find("div", class_ = "list_text")
    news_p = article.find("div", class_= "article_teaser_body").text
    news_title = article.find("div", class_="content_title").text
    news_date = article.find("div",class_="list_date").text

    #Add data above into dictionary 
    mars_data["news_date"] = news_date
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_p





    #JPL Mars Space Images 
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)








    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image_html = browser.html
    img_soup = BeautifulSoup(image_html, 'html.parser')
    main_img = img_soup.find('img', class_='main_image')
    split_img = main_img.get('src')
    featured_img = "https://www.jpl.nasa.gov" + split_img

    mars_data["featured_img"] = featured_img










    #Mars Weather 
    mars_twitter = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_twitter)





    html = browser.html
    twitter_soup = BeautifulSoup(html, 'html.parser')





    mars_tweet = twitter_soup.find('div', class_="js-tweet-text-container")




    mars_weather = mars_tweet.find('p', 'tweet-text').get_text()
    mars_weather

    mars_data["mars_weather"] = mars_weather

    df_mars_facts = pd.read_html("https://space-facts.com/mars/")
    df_mars_facts = df_mars_facts[0]
    df_mars_facts.rename_axis({0:"Mars Facts", 1:"Data"}, axis=1, inplace=True)
    html_table = df_mars_facts.to_html
    df_mars_facts.to_html('table.html')

    mars_data["mars_table"] = html_table


    #Mars Hemispheres 
    astrogeology_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(astrogeology_url)



    import time 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres=[]





    for i in range (4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
        img_url = 'https://astrogeology.usgs.gov'+ partial
        dictionary={"title":img_title,"img_url":img_url}
        hemispheres.append(dictionary)
        browser.back()

    mars_data["hemispheres"] = hemispheres

    return mars_data 





print(hemispheres)

