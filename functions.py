
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import numpy

def OrderBook_Metrics(data_ob):  
    '''
    Esta es la programación para calcular las metricas de un libro de órdenes en un periodo 
    particular de tiempo. 

    Parameters 
    ----------
    data:dict (default:None)
        Datos de entrada del libro de ordenes, diccionario con la siguiente estructura:
        'tiestamp': objeto tipo timestamp reconocible por maquina, e.g. pd.to_datetime()
        'bid_size':volume de niveles bid
        'bid': precio de niveles bid
        'ask': precio de niveles ask
        'ask_size':volume de niveles ask

    Returns
    --------
    r_data:dict
        Diccionario con las metricas calculas:
        'Median Time of OrderBook'
        'Spread'
        'Midprice'
        'No. Price Levels'
        'Bid Volume'
        'Ask Volume'
        'Total Volume'
        'OrderBook Imbalance'
        'Weighted-MidPrice'
        'VWAP'
    '''
    
        # -- Median Time of OrderBook Update
    ob_ts = list(data_ob.keys())
    l_ts = [pd.to_datetime(i_ts) for i_ts in ob_ts] 
    ob_m1 = numpy.median([l_ts[n_ts+1]-l_ts[n_ts] for n_ts in range(0,len(l_ts)-1)]).total_seconds()*1000
        
        # -- Spread
    ob_m2= [data_ob[ob_ts[i]]['ask'][0]-data_ob[ob_ts[i]]['bid'][0] for i in range(0,len(ob_ts))]
        
        # -- Midprice
    ob_m3= [(data_ob[ob_ts[i]]['ask'][0]+data_ob[ob_ts[i]]['bid'][0])*0.5 for i in range(0,len(ob_ts))]
        
        # -- No. Price Levels
    ob_m4 = [data_ob[i_ts].shape[0] for i_ts in ob_ts]
        
        # -- Bid_Volume
    ob_m5 = [numpy.round(data_ob[i_ts]['bid_size'].sum(),6) for i_ts in ob_ts]
        
        # -- Ask_Volume
    ob_m6 = [numpy.round(data_ob[i_ts]['ask_size'].sum(),6) for i_ts in ob_ts]
        
        #-- Total_Volume
    ob_m7 = [numpy.round(data_ob[i_ts]['bid_size'].sum()+data_ob[i_ts]['ask_size'].sum(),6) for i_ts in ob_ts]

        # -- OrderBook Imbalance (im)
    ob_m8 = [(ob_m5[i_ts]/(ob_m5[i_ts]+ob_m6[i_ts])) for i_ts in range(0,len(ob_ts))] 

        # -- Weighted-MidPrice (im*midprice) 
    ob_m9 = [(ob_m8[i_ts]*ob_m3[i_ts]) for i_ts in range(0,len(ob_ts))]

        # -- VWAP (Volume-Weight Average Price)
    ob_m10 = [((data_ob[ob_ts[i]]['bid']*data_ob[ob_ts[i]]['bid_size'])+
                     (data_ob[ob_ts[i]]['ask']*data_ob[ob_ts[i]]['ask_size'])/
                     (data_ob[ob_ts[i]]['ask_size']+data_ob[ob_ts[i]]['bid_size']))
                     for i in range(0,len(ob_ts))] 
        
        # -- OHLCV: Open, High, Low, Close, Volume (Quoted Volume) --> midprice 
    ob_m11= {'open': ob_m3[0],'high':max(ob_m3),'low':min(ob_m3),'close':ob_m3[-1]}
    
        # Statistics (Median, Variance, Skewness, Kurtosis)
    ob_m12= {'median': numpy.median(ob_m8),'variance':numpy.var(ob_m8),'skewness':skew(ob_m8),'kurtosis':kurtosis(ob_m8)}
   
    r_data={'Median_ts_ob': ob_m1,'Spread':ob_m2,'Mid_Price':ob_m3,'No.Price Levels':ob_m4,'Bid_Volume':ob_m5,
            'Ask_Volume':ob_m6,'Total_Volume':ob_m7,'OrderBook Imbalance':ob_m8,'Weighted-MidPrice':ob_m9,'VWAP':ob_m10,
           'OHLCV_Midprice':ob_m11,'Statistics_Weighted-MidPrice':ob_m12} 
    
    return r_data

def publictrades_metrics(pt_data):
    '''
    Esta es la programación para calcular las metricas de operaciones públicas en un periodo 
    particular de tiempo.    
    
    Parameters
    ----------
    pt_data:dict (default:None)
        Datos de entrada de la operaciones públicas,con la siguiente estructura:
        'tiestamp': objeto tipo timestamp reconocible por maquina, e.g. pd.to_datetime()
        'price': precio de niveles
        'amount': volume de niveles
        'side': tipo de operación buy/sell
        
    Return
    ------
    r_data:dict
        Diccionario con las métricas calculadas:
        'Buy Trade Count'
        'Sell Trade Count'
        'Total Trade Count'
        'Difference in Trade Count'
        'Sell Volume'
        'Buy Volume'
        'Total Volume'
        'Difference in Volume'
        'OHLCV_Difference_in_volume':  Open, High, Low, Close, Volume
        'Statistics_Difference_in_volume:Median': Variance, Skewness, Kurtosis
    '''
    # Data
    #pt_data.index = pd.to_datetime(pt_data['timestamp'])
    
    ## Quantity of trades per period
    
    # -- Buy Trade Count
    
    n_pt_data_m1=pt_data[pt_data.side == 'buy'].resample('60T').count()
    pt_m1 = n_pt_data_m1.iloc[:,[3]]
    
     # -- Sell Trade Count
    n_pt_data_m2=pt_data[pt_data.side == 'sell'].resample('60T').count()
    pt_m2 = n_pt_data_m2.iloc[:,[3]]
    
     # -- Total Trade Count
    pt_m3 = pt_data['side'].resample('60T').count()
    
     # -- Difference in Trade Count
    pt_m4 = pt_m1 - pt_m2
    
    ## Quantity of Buy-side,Sell-side and Total trades per period
    
    # -- Sell Volume
    v_pt_data_m5=pt_data[pt_data.side == 'sell'].resample('60T').sum()
    pt_m5 = v_pt_data_m5.iloc[:,1]

    # -- Buy Volume
    v_pt_data_m6=pt_data[pt_data.side == 'buy'].resample('60T').sum()
    pt_m6 = v_pt_data_m6.iloc[:,1]

    # -- Total Volume
    pt_m7 = pt_data['amount'].resample('60T').sum()

    # -- Difference in Volume (Buy-Sell)
    pt_m8 = pt_m6-pt_m5
    
    # -- OHLCV: Open, High, Low, Close, Volume (Trated Volume) --> pt_m8 
    pt_m9= {'open': pt_m8[0],'high':max(pt_m8),'low':min(pt_m8),'close':pt_m8[-1]}
    
        # Statistics (Median, Variance, Skewness, Kurtosis)
    pt_m10= {'median': numpy.median(pt_m8),'variance':numpy.var(pt_m8),'skewness':skew(pt_m8),'kurtosis':kurtosis(pt_m8)}
    
    
    r_data={'Buy Trade Count':pt_m1,'Sell Trade Count':pt_m2,'Total Trade Count':pt_m3,'Difference in Trade Count':pt_m4,
                    'Sell Volume':pt_m5,'Buy Volume':pt_m6,'Total Volume':pt_m7,'Difference in Volume':pt_m8,'OHLCV_Difference_in_volume':pt_m9,'Statistics_Difference_in_volume':pt_m10}
    
    return r_data
    