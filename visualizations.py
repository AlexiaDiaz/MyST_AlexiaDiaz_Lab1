
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
def plot_orderbook(data_x,data_s1,data_s2,data_s3):
    '''
    Esta es la programación para representar gráficas de barras horizontales de un libro de ordenes.
    
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
    -------
    Gráfica que representa los volumes de bid, ask y total del libro de ordenes. 
    '''
    x_data=list(range(0,len(data_x)))
    fig=go.Figure()
    fig.add_trace(go.Bar(x=x_data,y=data_s1,name='Bid_Volume',width=1,marker_color='blue'))
    fig.add_trace(go.Bar(x=x_data,y=data_s2,name='Ask_Volume',width=1,marker_color='green'))
    fig.add_trace(go.Scatter(x=x_data,y=data_s3,name='Total_Volume',mode='lines',marker_color='black'))
    
    return fig
def plot_publictrades(data_x,data_y,data_y1):
    '''
    Esta es la programación para representar gráficas de barras y los precios ejecutados de operaciones públicas.
    
    Parameters
    ----------
    pt_data:dict (default:None)
        Datos de entrada de la operaciones públicas,con la siguiente estructura:
        'tiestamp': objeto tipo timestamp reconocible por maquina, e.g. pd.to_datetime()
        'price': precio de niveles
        'amount': volume de niveles
        'side': tipo de operación buy/sell
    
    Returns
    -------
    Gráfica que retorna los precios ejecutados de operaciones públicas.
    '''
        # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=data_x, y=data_y, name="traded price"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Bar(x=data_x, y=data_y1, name="volume"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text="Trades publicos"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Timestamp")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Traded Price</b> <br> BTC/USDT", secondary_y=False)
    fig.update_yaxes(title_text="<b>Volume</b> <br> BTC", secondary_y=True)

    fig.update_layout(legend_orientation='h', xaxis=dict(ticktext=list(pt_data['timestamp'])[0:499]) )

    return fig