import urllib.request
import time
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7' # noqa
}


def get_HTML(url):
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    raw_HTML = response.read
    soup_HTML = BeautifulSoup(raw_HTML, features='html5lib')
    return soup_HTML


def get_chapter(HTML):
    raw_chapter = ''
    title = HTML.find('title').text

    for div in HTML.findAll('div', attrs={'class': 'fr-view'}):
        if len(div) > len(raw_chapter):
            raw_chapter = div

    chapter = str(raw_chapter).replace('Previous Chapter', '').replace('Next Chapter', '') # noqa

    return '<h4>' + title + chapter + '</h4>' + '<br>'


def get_next_url(html_content):
    next_url = ''

    for a in html_content.findAll('a', attrs={'class': 'btn btn-link'}, href=True): # noqa
        next_url = a['href']

    return 'https://www.wuxiaworld.com' + next_url


url = input("Enter the URL of the first chapter to parse: ")
delay = int(input("Enter the delay time between each parsing: "))
parsed = ''
prev_url = ''
count = 1

while True:
    try:
        time.sleep(delay)
        html_content = get_HTML(url)
        next_url = get_next_url(html_content)
        parsed += get_chapter(html_content)
        if prev_url == next_url:
            break
        prev_url = url
        url = next_url

        print(str(count) + ' chapters parsed')
        count += 1
    except Exception:
        break


parsed = '<html><body>' + parsed + '</body></html>'

f = open('wuxiaworld_result.html', 'w')
f.write(parsed)
f.close()

print("Parsing done")
