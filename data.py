
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
# Library
import json
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats import kurtosis
import plotly.graph_objects as go

# Opening JSONfile
f = open('orderbooks_05jul21.json')

#Returns JSON object as a dictionary
orderbooks_data = json.load(f)
ob_data = orderbooks_data['bitfinex']

#Drop None Keys
ob_data= {i_key : i_value for i_key,i_value in ob_data.items() if i_value is not None}

#Convert to dataframe  and rearange columns
ob_data={i_ob:pd.DataFrame(ob_data[i_ob])[['bid_size','bid','ask','ask_size']]
        if ob_data[i_ob] is not None else None for i_ob in list(ob_data.keys())}

# Read CSV
pt_data=pd.read_csv('btcusdt_binance.csv',header=0)
pt_data.drop('index', inplace=True, axis=1)
pt_data.index = pd.to_datetime(pt_data['timestamp'])