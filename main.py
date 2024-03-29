import requests
import pandas as pd
import random
# import re
# from bs4 import BeautifulSoup


link = "https://lk.rs-class.org/regbook/vessel?ln=en&a=print&fleet_id=771036"
response = requests.get(link).text.replace("<br>", "\n")
spsheet = pd.read_html(response)[0].transpose()
spsheet.columns = spsheet.iloc[0]
database = spsheet[1:].drop(labels=["General", "Type of vessel", "Building information", "Dimensions and speed", "Machinery",
            "Refrigerating plant and radio navigational equipment", "Holds, decks, passengers",
            "Hatches, Derricks, Cranes", "Capacities", "Companies related to the vessel"], axis=1)
database = database.iloc[0:0]
print(database)

# PROXIES = []


# ID = [771036, 921787, 992297, 842547, 842551, 833232]
RANGES = list(range(1220000, 2000000, 1000))
# random.shuffle(RANGES)
# print(RANGES)
for _ in RANGES:
    for id in range(_, _ + 1000):
        try:
            link = f"https://lk.rs-class.org/regbook/vessel?ln=en&a=print&fleet_id={id}"
            print(f"{link}   {len(database)}")
            response = requests.get(link).text.replace("<br>", "\n")
            spsheet = pd.read_html(response)[0].transpose()
            spsheet.columns = spsheet.iloc[0]
            spsheet = spsheet[1:].drop(labels=["General", "Type of vessel", "Building information", "Dimensions and speed", "Machinery",
                        "Refrigerating plant and radio navigational equipment", "Holds, decks, passengers",
                        "Hatches, Derricks, Cranes", "Capacities", "Companies related to the vessel"], axis=1)
            database = pd.concat([database, spsheet], ignore_index=True, axis=0)
            print(database)
        except ValueError:
            pass

    database.to_csv(f"data/database_1000000-{_ - 1000}.csv")
    # database = database.iloc[0:0]






# spsheet = dict(pd.read_html(response)[0].to_dict(orient="split")["data"])
# import PyPDF2 as ppdf
# import pandas as pd
# import tabula
# import numpy as np
#
# TOP_LEFT = [230, 114, 227, 114]
# FIELD_COORDS = {"reg_num": [0, 0, 9, 46],
#                 "imo_num": [0, 46, 9, 90],
#                 "ship_name_en": [36, 0, 45, 98]
#                 }
# reg_num = tabula.read_pdf("000.pdf", area=[np.add(FIELD_COORDS["reg_num"], TOP_LEFT).tolist(),
#                                            np.add(FIELD_COORDS["imo_num"], TOP_LEFT).tolist(),
#                                            np.add(FIELD_COORDS["ship_name_en"], TOP_LEFT).tolist()],
#                           pages="1", pandas_options={"header": None}
#                           )
# imo_num = tabula.read_pdf("000.pdf", area=np.add(FIELD_COORDS["imo_num"], TOP_LEFT).tolist(), pages="1", pandas_options={"header": None})
# ship_name_en = tabula.read_pdf("000.pdf", area=np.add(FIELD_COORDS["ship_name_en"], TOP_LEFT).tolist(), pages="1", pandas_options={"header": None})

# print(reg_num)
# print(imo_num[0][0][0])
# print(ship_name_en[0][0][0])

# file = open('000.pdf', "rb")
# input_pdf = ppdf.PdfFileReader(file)
# page = input_pdf.getPage(0)
# text = page.extractText()
# print(text)
