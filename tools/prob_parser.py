import os

import requests
from bs4 import BeautifulSoup

cubes = ["red", "black", "addi"]

for cube in cubes:

    https = requests.get(
        f"https://maplestory.nexon.com/Guide/OtherProbability/cube/{cube}"
    )
    soup = BeautifulSoup(https.content, "html.parser")

    cube_option = soup.find_all("div", {"class": "cube_option"})
    cube_table = soup.find_all("table", {"class": "cube_data"})

    for option, table in zip(cube_option, cube_table):
        ul = [x.find("span") for x in option.find("ul").find_all("li")]
        filenameparam = []
        for x in ul:
            filenameparam.append(x.text.strip())
        tr = table.find("tbody").find_all("tr")

        if filenameparam[1] == "보조무기 (포스실드, 소울링 제외)":
            filenameparam[1] = "보조무기"

        tables = ["옵션1,확률1,옵션2,확률2,옵션3,확률3"]

        for td in tr:
            tds = [x.text.strip() for x in td if str(x) != "\n"]

            tables.append(",".join(tds))

        tablestext = "\n".join(tables)

        file = open(
            os.path.join(
                os.path.dirname(__file__),
                "output",
                f"{cube}&{filenameparam[0]}&{filenameparam[1]}.csv",
            ),
            "w",
            encoding="utf-8",
        )
        file.write(tablestext)
        file.close()
