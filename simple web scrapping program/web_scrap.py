#This is main python script for the program.
# First, lets import the libraries.
import requests
from bs4 import BeautifulSoup

# creating th function for scrap
def scrap():

    # enter url of the webpage:
    url = 'https://vimukthigw.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    print(title)
    print(text)
    print(link)
    print(soup)

# if statement for program
if __name__ == '__main__':
    scrap()



