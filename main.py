import requests
from bs4 import BeautifulSoup
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




    def select_state(state):
        state_url = root_url + state.strip()
        page1 = requests.get(state_url)
        soup1 = BeautifulSoup(page1.content, "html.parser")
        running = soup1.find_all('tr', class_='med river river-med0')
        for r in running:
            river_info = r.find_all("a")
            for y in river_info:
                print(y.text.strip())


    #parse

    def river_links(ru):
        for r in ru:
            links = r.find_all("a")
            for link in links:
                link_url = link["href"]
                return(link_url)
    ##this find the links to each specific river, however there are unwanted links and many of them repeat

    state = input("what state do you want to looks for rivers in?")

    state_url = root_url + state.strip()
    page1 = requests.get(state_url)
    soup1 = BeautifulSoup(page1.content, "html.parser")
    running = soup1.find_all('tr', class_='med river river-med0')



    #print(select_state(state))
    run = river_links(running)
    ###turn run into a list so you can clean it

    y = []
    for element in list:
        if "javascript:dialoghelper" in element == False:
            y.append(element)



    #write a function that will make the links to each states river page




    #for link in links:
    #    result1 = requests.get(f'{root}/{link}')
    #    content = result1.text
    #    soup2 = BeautifulSoup(content, 'lxml')
   # print(soup.prettify())
