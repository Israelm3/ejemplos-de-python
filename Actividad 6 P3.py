# GENERAR EXCEL

import pandas as pd

#create dataframe
df_marks = pd.DataFrame({
    'Nombre': ['Luis', 'Andrea', 'Miguel', 'Samir'],
    'Química': [68, 74, 77, 78],
    'Álgebra': [84, 56, 73, 69],
    'Geometría': [78, 88, 82, 87]
})

#Create excel
writer = pd.ExcelWriter('Puntajes.xlsx')

#Write dataframe to excel
df_marks.to_excel(writer)

#save
writer.close()

print("Archivo excel creado correctamente...")
