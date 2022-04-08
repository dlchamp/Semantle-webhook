from requests_html import HTMLSession
from bs4 import BeautifulSoup



def scrape_site():
    URL = 'https://semantle.novalis.org/'
    # set session and render page
    session = HTMLSession()
    r = session.get(URL)
    r.html.render(sleep=3)
    content = r.html.html

    # scrape page contents
    page = BeautifulSoup(content, 'html.parser')

    # scrape puzzle number
    paragraph = page.find('p', {'id':'similarity-story'})
    puzzle_number = int(paragraph.find('b').text) - 1

    # scrape previous day link
    panel_text = page.find('span', {'id':'nearbyYesterday'})
    link = URL + panel_text.find('a')['href']

    return puzzle_number, link

