import urllib.request
import time
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

def get_HTML(url):
    request = urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    raw_HTML = response.read()

    soup_HTML = BeautifulSoup(raw_HTML, features = 'html5lib')
    
    return soup_HTML


def get_chapter(HTML):
    chapter = ''

    for div in HTML.findAll('div', attrs = {'class': 'innerContent fr-view', 'id': 'chapterContent'}):
        chapter = div

    print('Parsed: ' + url)

    return str(chapter)


def get_next_url(HTML, url):
    next_url = ''

    for a in HTML.findAll('a', attrs = {'class': 'btn btn-lg btn-link'}, href = True):
        next_url = a['href']

    if next_url in url:
        return None
    
    return next_url



url = input("Enter the URL of the first chapter to parse: ")
delay = float(input("Enter the delay time between each parsing: "))
filename = input("Enter the name for the parsed file: ")
parsed = ''

while url != None:
    time.sleep(delay)
    HTML = get_HTML(url)
    next_url = get_next_url(HTML, url)

    parsed += get_chapter(HTML)

    url = next_url

parsed = '<html><body>' + parsed + '</body></html>'

f = open('./parsing_result/' + filename + '.html','w')
f.write(parsed)
f.close()

print('Parsing done')
print('(•_•)')
print('( •_•)>⌐■-■')
print('(⌐■_■)')
