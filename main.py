root_url = "https://www.americanwhitewater.org/content/River/state-summary/?state="

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':


    def running(state):
        state_url = root_url + state.strip()
        page1 = requests.get(state_url)
        soup1 = BeautifulSoup(page1.content, "html.parser")
        running = soup1.find_all('tr', class_='med river river-med0')
        for r in running:
            links = r.find_all("a")
            for link in links:
                print(link.text.strip())

    state = input("what state do you want to looks for rivers in?")


    print(running(state))

