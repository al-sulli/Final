
if __name__ == '__main__':
    import requests
    from bs4 import BeautifulSoup

    URL = "https://www.americanwhitewater.org/content/River/state-summary/?state=AK"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup.prettify())

    results = soup.find_all("span", class_="river_extra river-section")
    #print(results)
    river_class =soup.find_all("td", class_="right")
    #find if its running
    #print(river_class)

    root = 'https://www.americanwhitewater.org'
    #write a function that will make the links to each states river page

    links = [link['href'] for link in soup.find_all('a', href=True)]
    #print(links)
    for link in links:
        result1 = requests.get(f'{root}/{link}')
        content = result1.text
        soup2 = BeautifulSoup(content, 'lxml')
    print(soup.prettify())

    runable_hmm = soup2.find_all("span", class_="bx--tag__label")
    print(runable_hmm)