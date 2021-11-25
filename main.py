import re
import pandas as pd

file = open('response.html')
spsheet = pd.read_html("response.html")
print(spsheet)





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
