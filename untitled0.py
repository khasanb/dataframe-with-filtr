# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YRnFHBx9S63tIgWGd3pQHMIkx0DwKPed
"""

import pandas as pd
baza={
    "FISH":["Alijonov Sarvar", "Alijonova Xilola", "Aliyev Ali", "Ariya Stark", "Jon Snov", "Umarova Salima", "Xatamov Jonibek", "Xatamova Malika", "Shokirov Sardor", "Deynarias Targariyan" ],
    "Yoshi":["15", "10", "17", "15","11", "13","12", "17","16", "25"    ],
    "Jinsi":["erkak", "ayol", "erkak", "ayol","erkak", "ayol","erkak", "ayol","erkak", "ayol",   ],
    "Maktabi":["22-makta", "22-maktab", "55-makta", "55-maktab", "22-makta", "22-maktab","22-makta", "22-maktab","65-makta", "65-maktab",   ],
    "Manzili":["Farg'ona shahar", "Farg'ona shahar", "Andijon shahar", "Andijon shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Farg'ona shahar", "Namangan shahar",  "Namangan shahar" ],
    "Tel raqami":["90 000 11 10", "90 000 11 22","99 000 33 11", "99 000 33 20", "95 000 44 17", "95 000 44 25", "90 000 55 19", "90 000 55 30", "91 000 77 55", "91 000 77 88",  ]
}
db=pd.DataFrame(baza)
print(db)
filtr=db[db["Manzili"]=="Andijon shahar"]
print(filtr)
filtr=db[(db["Jinsi"]=="ayol") & (db["Yoshi"]<"15")]
print(filtr)

filtr=db[(db["Jinsi"]=="erkak") & (db["Yoshi"]<"15")]
print(filtr)