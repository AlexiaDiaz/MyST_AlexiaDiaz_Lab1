
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio 1. Metricas                                                                    -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: Alexia Marisol Díaz Verduzco                                                                -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: https://github.com/AlexiaDiaz/MyST_AlexiaDiaz_Lab1.git                                                                 -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import data as dt
import functions as fn
import visualizations as vs

data_ob=dt.ob_data
pt_data=dt.pt_data

print("La cantidad total de libros de libros de ordenes es",fn(OrderBook_Metrics(data_ob)['Median_ts_ob']))