from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
from flask import Flask, jsonify


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "c:/Users/aa11717/Documents/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():

# A. NASA Mars News - Visit NASA Mars New Site
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    #print(response)
    soup = BeautifulSoup(response.text, 'html.parser')  

    # Mars New Title:
    content_titles = soup.find_all('div', class_="content_title")
    news_title = []

    for titles in content_titles:
            # Identify and return title of listing
            if (titles.a):
                if (titles.a.text):
                    news_title.append(titles.text)

    #print(news_title[0])
    news_title = news_title[0]
    news_title = news_title.replace('\n', '')
    news_title = [(news_title)]
#    print(news_title)

    # Mars New Paragraph Description of Story:
    news_para = soup.find_all('div', class_="rollover_description_inner")
    news_desc = []

    for result in news_para:
        news_desc.append(result.text)
    #    title = result.find('div', class_="rollover_description_inner")
    #print(news_desc)
    news_desc = news_desc[0]
    news_desc = news_desc.replace('\n', '')
    news_desc = [(news_desc)]
#    print(news_desc)



# B. JPL Mars Space Images - Featured Image
    browser = init_browser()
    # executable_path = {"executable_path": "c:/Users/aa11717/Documents/chromedriver"}
    # browser = Browser("chrome", **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    browser.click_link_by_partial_text('FULL IMAGE')

    time.sleep(2)

    browser.click_link_by_partial_text('more info')

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_image = soup.find("figure", class_="lede")
    #print(mars_image)
    mars_featured_image = mars_image.find("img", class_="main_image")
    mars_link = mars_featured_image["src"]
    featured_image_link = ["https://www.jpl.nasa.gov" + (mars_link)]
    #print(featured_image_link)
    browser.quit


# C. Mars Weather
    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

    response = requests.get(url)
    #print(response)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
    tw_mar_weather = soup.find_all('div', class_="js-tweet-text-container")
    #print(results)

    sol = []
    for tweets in tw_mar_weather:
        sols = tweets.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
        sol.append(sols)
        
    mars_weather = sol[0]
    #print(mars_weather)

# D. Mars Facts - PANDAS
    # URL of page to be scraped
    url = 'https://space-facts.com/mars/'
    response = requests.get(url)
    #print(response)

    tables = pd.read_html(url)
    tables

    #type(tables)

    marsfacts_df = tables[0]
    marsfacts_df.columns = ['Mars Planet Fact', 'Planet Description']
    marsfacts_df.set_index('Mars Planet Fact', inplace=True)
    marsfacts_df

    marsfacts_html_table = marsfacts_df.to_html()
    mars_facts = marsfacts_html_table.replace('\n', '')
    mars_facts
    # marsfacts_df.to_html('table.html')
    print(marsfacts_df)
#    get_ipython().system('explorer table.html')


# E. Mars Hemispheres

    # URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Retrieve page with the requests module
    response = requests.get(url)
    #print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    hemispheres = soup.find_all('div', class_='item')

    hemisphere_title = []
    hemisphere_url_list = []
    for h in hemispheres:
        h_title = h.find('h3').text
        hemisphere_title.append(h_title)
        h_url = h.find('a')['href']
        hemisphere_url_list.append(h_url)

    #print(hemisphere_title)
    #print(hemisphere_url_list)

    #Use splinter to visit the pages and pull the images
    browser = init_browser()
    # executable_path = {"executable_path": "c:/Users/aa11717/Documents/chromedriver"}
    # browser = Browser("chrome", **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    hemisphere_image_urls =[]

    for i in hemisphere_title:
        #print(i)
        #for hem_title in hemisphere_title:
        browser.click_link_by_partial_text(i)
        browser.click_link_by_partial_text('Open')
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        #soup = BeautifulSoup(response.text, 'html.parser')

        #hem1 = soup.find('div', class_="container")
        cerberus_title = soup.find('h2', class_="title").text
        #print(cerberus_title)

        cerberus_image = soup.find('img', class_="wide-image")
        #print(cerberus_image)
        cerberus_link = cerberus_image['src']

        # Store data in a dictionary
        hemisphere_image_urls.append({
            "title": cerberus_title,
            "img_url": "https://astrogeology.usgs.gov" + (cerberus_link)})

        #print(cerberus_title, cerberus_link)
        print(hemisphere_image_urls)

        browser.click_link_by_partial_text('Close')
        
        time.sleep(3)
        
        browser.click_link_by_partial_text("Back")

    #print(hemisphere_image_urls)

    # Close the browser after scraping
    browser.quit()

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title[0],
        "news_desc": news_desc[0],
        "featured_link": featured_image_link,
        "mars_weather": mars_weather,
        "mars_facts": mars_facts,
        "mars_hemispheres": hemisphere_image_urls
    }

    # Return results
    #print(mars_data)
    return mars_data
#    return (mars_data, tables)

# init_browser()    
# print(scrape())