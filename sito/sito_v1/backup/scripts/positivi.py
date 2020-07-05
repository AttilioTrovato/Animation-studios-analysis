import chart_studio.plotly as py
import plotly
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')


# Create a trace
trace = go.Scatter(
    x = df['data'],
    y = df['totale_positivi'],
   
    
)

data = [trace]

layout = go.Layout(
        xaxis=dict(
            title='Data',
            
        ),
        yaxis=dict(
            title='Totale positivi',
            
        ),
        margin=go.layout.Margin(
        l=0, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=0, #top margin
        )
	
    )
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig,filename='../html/positivi.html',config={'displayModeBar': False})
