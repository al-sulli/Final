root_url = "https://www.americanwhitewater.org/content/River/state-summary/?state="

import requests
from bs4 import BeautifulSoup

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

    import pandas as pd

    URL = "https://www.americanwhitewater.org/content/River/state-summary/?state=NC"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup.prettify())

    runnning = soup.find_all('tr', class_='med river river-med0')
    #print(runnning)


    ##this prints all of the rivers that are running in the state
    ## i need to figure out how to get the href from this result so i can get more info on the  rivers that are running

    table1 = soup.find('div', class_ ='bx--data-table-container')

    headers = []
    for i in table1.find_all('span', class_='bx--table-header-label'):
        title = i.text.strip()
        headers.append(title)


    def select_state(state):
        state_url = root_url + state.strip()
        page1 = requests.get(state_url)
        soup1 = BeautifulSoup(page1.content, "html.parser")
        running = soup1.find_all('tr', class_='med river river-med0')
        #make each entry into a list entry, is it a table
        for r in running:
            river_info = r.find_all("a")
            for y in river_info:
                p = y.text.strip()
            return(p)


    #parse


    #def river_links(ru):
     #   for r in ru:
      #      links = r.find_all("a")
       #     for link in links:
        #        link_url = link["href"]
        #    return(link_url)
    ##this find the links to each specific river, however there are unwanted links and many of them repeat

    def convert(string):
        li = list(string.split("/n"))
        return li


    state = input("what state do you want to looks for rivers in?")

    state_url = root_url + state.strip()
    page1 = requests.get(state_url)
    soup1 = BeautifulSoup(page1.content, "html.parser")
    running = soup1.find_all('tr', class_='med river river-med0')

    all_href = soup.find_all('a')
    all_href = [l['href'] for l in all_href]
    b = '\n', all_href
    bb = list(b)

    for element in bb:
        riverz = []
        if "/content/River/detail/id/" in element==True:
            riverz = riverz + element
        #print(riverz)



    #print(bb)
    print(select_state(state))
    #print(links)
    ###turn run into a list so you can clean it
    #fix functions so they return all values



    #write a function that will make the links to each states river page




    #for link in links:
    #    result1 = requests.get(f'{root}/{link}')
    #    content = result1.text
    #    soup2 = BeautifulSoup(content, 'lxml')
   # print(soup.prettify())

--------------------

URL = 'https://www.americanwhitewater.org/content/River/state-summary/?state=NC'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print('Classes of each table:')
for table in soup.find_all('table'):
    print()

table = soup.find('table', class_='sortable bx--data-table')

df = pd.DataFrame(columns=['River / section', 'Class', 'Level', 'Updated'])

for row in table.find_all('tr'):
    # Find all data for each column
    columns = row.find_all('td')
    print(columns)

    if (columns != []):
        river = columns[0].text.strip()
        class_ = columns[1].text.strip()
        level = columns[2].span.contents[0].strip('&0.')
        updated = columns[3].span.contents[0].strip('&0.')

        df = df.append(
            {'River': river, 'Class': class_, 'Level': level, 'Updated': updated}, ignore_index=True)

print(df.head)
