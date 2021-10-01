import requests
from bs4 import BeautifulSoup

places = {}
list = []
countries = []


def cases_per_capita():
    link = "https://www.worldometers.info/coronavirus/#main_table"

    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")

    x = soup.find_all("div", class_="maincounter-number")
    print("total Covid19 cases : " + x[0].text.strip())

    table = soup.find("table")

    for i in table.find_all("tr")[1:]:
        td = i.find_all("td")
        if td[1] and td[10].text != "":
            list.append(float(td[10].text.replace(",", "")))
            places[td[1].text] = td[10].text
    list.sort(reverse=True)

    for i in list:
        for key in places.keys():
            if float(places[key].replace(",", "")) == i:
                if key not in countries:
                    countries.append(key)
    return countries, places


def convert_to_html_table():
    table = []
    places.pop("World")
    table.append("<table border=\"1\" style=\"width: 100%\">")
    table.append("<tr><td><h2>Countries</h2></td><td><h2>New cases per capita</h2></td></tr>")
    for key, value in places.items():
        table.append("<tr><td>" + str(key) + "</td><td>" + str(value) + "</td></tr>")
    table.append("</table>")

    return table


def html_table_to_html_file():
    my_list = convert_to_html_table()
    with open('html_table.html', 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)


if __name__ == "__main__":
    countries, deaths = cases_per_capita()
    html_table_to_html_file()
