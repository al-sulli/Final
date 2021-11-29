
if __name__ == '__main__':
    import requests
    from bs4 import BeautifulSoup

    URL = "https://www.americanwhitewater.org/content/River/state-summary/?state=NC"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())

    results = soup.find_all("span", class_="river_extra river-section")
    print(results)
    ## this finds the  names of all  the  rivers, not needed

    runnning = soup.find_all('tr', class_='med river river-med0')
    print(runnning)

    for result in runnning:
        link = result.find_all('a', href = True)
        updated = result.find_all('td', class_="right")
        river_name =  result.find_all('span', class_='river_extra river-section')
    print(link)
    print(updated)
    print(river_name)

    ##this prints all of the rivers that are running in the state
    ## i need to figure out how to get the href from this result so i can get more info on the  rivers that are running

    for r in runnning:
       links = r.find_all("a")
       for link in links:
            print(link.text.strip())

    for r in runnning:
        links = r.find_all("a")
        for link in links:
            link_url = link["href"]
            print(link_url)
    ##this find the links to each specific river, however there are unwanted links and many of them repeat

    states = ["AK","NC","TN","MN"]

    root = 'https://www.americanwhitewater.org/content/River/state-summary/?state='
    req = ''
    for page in states :
        req = req+ (root + str(page) + '/')
    print(req)


    #write a function that will make the links to each states river page

    #links = [link['href'] for link in runnning.find('a', href=True)]



    #for link in links:
    #    result1 = requests.get(f'{root}/{link}')
    #    content = result1.text
    #    soup2 = BeautifulSoup(content, 'lxml')
   # print(soup.prettify())
