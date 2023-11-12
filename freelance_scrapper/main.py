import requests
from bs4 import BeautifulSoup as bs


def get_content():
    # Set a valid user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Safari/537.36"
    }

    url = "https://freelance.ua/orders/web-development/"
    resp = requests.get(url, headers=headers)

    mydict = {}

    try:
        if resp.status_code == 200:
            page = bs(resp.text, "html.parser")
            # Use a more robust selector to find the desired element
            dashboard = page.find("div", class_="j-list")

            if dashboard:
                texts = page.find_all("li", class_="j-order")
                links = dashboard.select("a")

                for text, link in zip(texts, links):
                    mydict[text.get_text()] = link['href']

                print(mydict)
            else:
                print("Element not found")
        else:
            print(f"Failed to retrieve the page. Status code: {resp.status_code}")
    except Exception as exp:
        print(f"Something is wrong: {exp}")

    return mydict



