import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd
root_url = "https://www.americanwhitewater.org/content/River/state-summary/?state="

if __name__ == '__main__':

    URL = "https://www.americanwhitewater.org/content/River/state-summary/?state=NC"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup.prettify())

    runnning = soup.find_all('tr', class_='med river river-med0')
    #print(runnning)


    ##this prints all of the rivers that are running in the state
    ## i need to figure out how to get the href from this result so i can get more info on the  rivers that are running


    # Create a handle, page, to handle the contents of the website
    page = requests.get(URL)
    # Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    # Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')
    [len(T) for T in tr_elements[:12]]
    tr_elements = doc.xpath('//tr')
    # Create empty list
    col = []
    i = 0
    # For each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        print
        '%d:"%s"' % (i, name)
        col.append((name, []))

    for j in range(1, len(tr_elements)):
        # T is our j'th row
        T = tr_elements[j]

        # If row is not of size 10, the //tr data is not from our table
        if len(T) != 10:
            break

        # i is the index of our column
        i = 0

        # Iterate through each element of the row
        for t in T.iterchildren():
            data = t.text_content()
            # Check if row is empty
            if i > 0:
                # Convert any numerical value to integers
                try:
                    data = int(data)
                except:
                    pass
            # Append the data to the empty list of the i'th column
            col[i][1].append(data)
            # Increment i for the next column
            i += 1
    [len(C) for (title, C) in col]
    Dict = {title: column for (title, column) in col}
    df = pd.DataFrame(Dict)
    print(df)


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
    #print(select_state(state))
    #print(links)
    ###turn run into a list so you can clean it
    #fix functions so they return all values



    #write a function that will make the links to each states river page




    #for link in links:
    #    result1 = requests.get(f'{root}/{link}')
    #    content = result1.text
    #    soup2 = BeautifulSoup(content, 'lxml')
   # print(soup.prettify())
