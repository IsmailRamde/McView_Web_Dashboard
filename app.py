#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 11:51:59 2021

@author: RAMDE ISMAIL
"""


# Import required libraries
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import base64
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import read_write_google_API as api
import numpy as np
import update_figure as upfig






# get relative data folder
#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.title = 'McView'
server = app.server


# Download pickle file
#urllib.request.urlretrieve(
#    "https://raw.githubusercontent.com/plotly/datasets/master/dash-sample-apps/dash-oil-and-gas/data/points.pkl",
#    DATA_PATH.joinpath("points.pkl"),
#)
#points = pickle.load(open(DATA_PATH.joinpath("points.pkl"), "rb"))


# color
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


##********************************** LOAD DATA *******************************

#    Loading of PT (Pressure), TT (Temperature Transmission), 
#    FT (Flow Transmission) and PCV (Pressure Control Valve) data.

df1_berlin = api.SortH2MDistributionData()  
df1_berlin = pd.DataFrame(df1_berlin)
df1_berlin.fillna(df1_berlin.mean(), inplace=True)
#imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
#imputer.fit_transform(df1)
#df1["TimeStr"].head
#df1["TT 8.201"]
#df1.to_excel("exemple1.xlsx", index=False)
df1_berlin.rename(columns={'PT 8.202a': 'PT', 'TT 8.201': 'TT', 'FT 8.201': 'FT', 'PCV 8.201': 'PCV'}, inplace=True)
#df1_berlin.to_excel("exemple13.xlsx", index=False)


#    Loading of the location data of the different stations.

df3 = api.Data_MAP()  
df3 = pd.DataFrame(df3)
df3.rename(columns={'Latitud': 'lat', 'Longitud': 'lon'}, inplace=True)
#df3.to_excel("exemple3.xlsx", index=False)
#df3.columns
#df3 = pd.read_excel("/home/ismael/Bureau/plotly/McView_WebDashboard/data/station_location.xlsx")


# Here we retrieve the status column and calculate for each modality the number of stations
st = df3['Status']
st = list(st)
val1 = st.count('Offline')
val2 = st.count('Not Available')
val3 = st.count('Coming Soon')
val4 = st.count('Available')


#    Loading of Energy data.

df2 = api.SortH2MEnergyData()
df2 = pd.DataFrame(df2)
#df2.to_excel("exemple5.xlsx", index=False)
#df2 = pd.read_csv(
#    "/home/ismael/Bureau/plotly/McView_WebDashboard/data/HRS_CNR_WEEK_Report_KPis_energy.csv",
#    low_memory=False,
#)



#    Loading of activation/day data.

df4 = api.SortH2MotorsData()
df4 = pd.DataFrame(df4)
df4.rename(columns={'Air Compressor': 'Air_Compressor', 
                    'D1 Cooling Unit': 'D1_Cooling_Unit', 
                    'Air Extractor': 'Air_Extractor'}, inplace=True)
df4['Air_Compressor'].replace('', '0', inplace=True)
df4['D1_Cooling_Unit'].replace('', '0', inplace=True)
df4['Air_Extractor'].replace('', '0', inplace=True)
#df4.to_excel("exemple4.xlsx", index=False)
#df4 = pd.read_csv(
#    "/home/ismael/Bureau/plotly/McView_WebDashboard/data/activation.csv",
#    low_memory=False,
#)


#******************************************************************************



#********************************** PLOTS *************************************

#fig5 = px.line(df1, x="TimeStr", y=['PT', 'TT', 'FT', 'PCV'],
#              hover_data={"TimeStr": "|%B %d, %Y"})
#fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#df1.to_excel("exemple.xlsx", index=False)

# plot Map (satellite overview)
fig1 = px.scatter_mapbox(df3, lat="lat", lon="lon", hover_name="City", hover_data=["Country", "Project"],
                        color="Status", zoom=3, height=300)
fig1.update_layout(mapbox_style="open-street-map")
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig1.show()

# station by location
fig4 = px.sunburst(df3, path=['Country', 'City', 'Project'])
fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig4.show()

# energy
#fig2 = px.line(df2, x="TimeStr", y=['kVA','KVAR','kW'])
#fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig2.show()

# activation/day
#fig6 = go.Figure()
#fig6.add_trace(go.Bar(
#    x=df4["Day"],
#    y=df4["Air_Compressor"],
#    name='Air Compressor',
#    marker_color='indianred'
#))
#fig6.add_trace(go.Bar(
#    x=df4["Day"],
#    y=df4["Air_Extractor"],
#    name='Air Extractor',
#    marker_color='lightsalmon'
#))
#fig6.add_trace(go.Bar(
#    x=df4["Day"],
#    y=df4["D1_Cooling_Unit"],
#    name='D1 Cooling Unit',
#    marker_color='olive'
#))
#
## Here we modify the tickangle of the xaxis, resulting in rotated labels.
#fig6.update_layout(barmode='group', xaxis_tickangle=-45)
#fig6.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
##fig6.show()


# McPhy logo
image_filename = "/home/ismael/Bureau/plotly/McView_WebDashboard/assets/dash-logo.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#******************************************************************************




# ***************************** CREATE APP LAYOUT *****************************
app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src='data:image/png;base64,{}'.format(encoded_image.decode()),
                            #src=app.get_asset_url("dash-logo.png"),
                            id="plotly-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H1(
                                    "McView",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "McFilling Stations Highlights", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                # Learn more button
                html.Div(
                    [
                        html.A(
                            html.Button("Learn More", id="learn-more-button"),
                            href="https://mcphy.com/en/",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        # **** The different selection options are implemented in this part ****
        html.Div(
            [
                # Station selection
                html.Div(
                    [
                        html.P("Select station:", className="control_label"),
                            dcc.Dropdown(
                                    id='station_selector',
                                    options=[
                                            {'label': 'Berlin', 'value': 'bl'},
                                            {'label': 'Bethune', 'value': 'bt'},
                                            {'label': 'Grenoble', 'value': 'gr'},
                                            {'label': 'Le Mans', 'value': 'lm'},
                                            {'label': 'Lyon', 'value': 'ly'},
                                            {'label': 'Rouen', 'value': 'rn'},
                                            {'label': 'Rostock', 'value': 'rk'},
                                            {'label': 'Rungis', 'value': 'rs'},
                                            {'label': 'Sarreguemines', 'value': 'sr'},
                                            {'label': 'Singapore', 'value': 'sp'},
                                            {'label': 'Sorigny', 'value': 'sy'},
                                            {'label': 'Valence', 'value': 'vl'},
                                            ],
                                    value='gr',
                                    className="dcc_control",
                                    ),
                        
                        html.P("Select distribution:", className="control_label"),
                        dcc.RadioItems(
                            id="distribution_selector",
                            options=[
                                {"label": "Distribution 1 ", "value": "dis1"},
                                {"label": "Distribution 2", "value": "dist2"},
                            ],
                            value="dis1",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                               
                        # Sensor selection
                        html.P("Select captor:", className="control_label"),
                        dcc.RadioItems(
                            id="captor_selector",
                            options=[
                                {"label": "captor 1 ", "value": "cap1"},
                                {"label": "captor 2", "value": "cap2"},
                                {"label": "captor 3", "value": "cap3"},
                            ],
                            value="cap1",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                                
                        # Selection of the year
                        html.P(
                            "Filter by year :",
                            className="control_label",
                        ),
                        dcc.RangeSlider(
#                            id="year_slider",
#                            min=2020,
#                            max=2021,
#                            value=[2020, 2021],
#                            className="dcc_control",
                            
                            id="year_slider",
                            min=df1_berlin['Year'].min(),
                            max=df1_berlin['Year'].max(),
                            value=[2015, 2022],
                            marks={str(Year): str(Year) for Year in df1_berlin['Year'].unique()},
                            step=None,
                            className="dcc_control",
                        ),
                                
                        # selection of the month
                        html.P(
                            "Filter by month :",
                            className="control_label",
                        ),
                        dcc.RangeSlider(
                            id="month_slider",
                            min=df1_berlin['Month'].min(),
                            max=df1_berlin['Month'].max(),
                            value=[1, 31],
                            marks={str(Month): str(Month) for Month in df1_berlin['Month'].unique()},
                            step=None,
                            className="dcc_control",
                        ),
                        
                        # selection of the day        
                        html.P(
                            "Filter by day :",
                            className="control_label",
                        ),
                        dcc.RangeSlider(
                            id="day_slider",
                            min=df1_berlin['Day'].min(),
                            max=df1_berlin['Day'].max(),
                            value=[1, 31],
                            marks={str(Day): str(Day) for Day in df1_berlin['Day'].unique()},
                            step=None,
                            className="dcc_control",
                        ),
                                
                        # Time selection
                        html.P(
                            "Filter by hour :",
                            className="control_label",
                        ),
                        dcc.RangeSlider(
                            id="hour_slider",
                            min=0,
                            max=24,
                            value=[0, 24],
                            marks={str(Hour): str(Hour) for Hour in df1_berlin['Hour'].unique()},
                            step=None,
                            className="dcc_control",
                        ),
                        
                        # Curve selection
                        html.P("Filter by curve:", className="control_label"),
                        dcc.RadioItems(
                            id="curve_selector",
                            options=[
                                {"label": "All ", "value": "all"},
                                {"label": "PT ", "value": "pt"},
                                {"label": "TT ", "value": "tt"},
                                {"label": "FT ", "value": "ft"},
                                {"label": "PCV ", "value": "pcv"}                                ,
                            ],
                            value="all",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                

                # The mini containers located at the very top of the web page
                html.Div(
                    [
                        html.Div(
                            [       
                                html.Div(
                                    [html.H6(id="station_offline"), html.P("Station Offline ")],
                                    id="offline",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="station_not_available"), html.P("Station Not Available ")],
                                    id="not_available",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="station_coming_soon"), html.P("Station Coming Soon")],
                                    id="coming_soon",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="station_available"), html.P("Station Available")],
                                    id="available",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                                    
                        # ** Change the graph on the first graphical display **
                        html.Div([
                                html.Div(
                                         [html.P("Visualization:", className="control_label"),
                                          dcc.RadioItems(
                                                  id="graph_selector",
                                                  options=[
                                                          {"label": "Viewing 1 ", "value": "view1"},
                                                          {"label": "Viewing 2", "value": "view2"},
                                                          ],
                                                          value="view1",
                                                          labelStyle={"display": "inline-block"},
                                                          className="dcc_control",
                                                          )],
                                        ),
                                
                                html.Div(
                                        [html.P("Data evolution over time", style={'textAlign': 'center'}), 
                                         dcc.Graph(id="count_graph")],
                                         id="countGraphContainer",
                                         className="pretty_container",
                                         ),
                                        
                                ],
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),


        # ****************** Second graphic display *********************
        html.Div(
            [ 
                html.Div(
                    [html.P("Satellite Overview", style={'textAlign': 'center'}), 
                     dcc.Graph(id="main_graph", figure=fig1)],
                     className="pretty_container seven columns",
                ),
                        
                # ***************** Third graphic display ********************
                html.Div(
                    [html.P("Stations by location", style={'textAlign': 'center'}), 
                     dcc.Graph(id="pie_graph", figure=fig4)],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),


        # ****************** Fourth graphic display *********************
        html.Div(
            [
                html.Div(
                    [html.P("Energy", style={'textAlign': 'center'}),
                     dcc.Graph(id="energy_graph")],
                    className="pretty_container seven columns",
                ),
                        
                # ***************** Fifth graphic display ********************
                html.Div(
                    [html.P("Activations/Day [ Current Month ]", style={'textAlign': 'center'}),
                     dcc.Graph(id="motors_graph")],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)
# *****************************************************************************






# **************************** HELPER FUNCTIONS *******************************

# Data filter function
def filter_dataframe(df, year_slider, month_slider):
    """
    Input :
        df1: PT, TT, FT and PCV data frame
        year_slider: recovers the selected year
        month_slider: recovers the selected month
        
    Output :
        filtered_df: filtered data
    """
    filtered_df = df[
            (df["Year"] > year_slider[0])
           &(df["Year"] < year_slider[1])
           &(df["Month"] > month_slider[0])
           &(df["Month"] < month_slider[1])
    ]
    return filtered_df





# **************************** CREATE CALLBACKS ******************************* 

#@app.callback(
#    Output('count_graph', 'figure'),
#    Input('month_slider', 'value'))
#def update_figure(selected_month):
#    filtered_df = df1[
#            (df1["Year"] > year_slider[0])
#           &(df1["Year"] < year_slider[1])
#    ]
##    filtered_df = df1[df1['Month'] == selected_month]
#    
#
#
#    fig = px.line(filtered_df, x='Month', y="Value")
##    fig.show()
#
#    return fig


# Callback for first graphical display
@app.callback(
    Output('count_graph', 'figure'),
    Input('year_slider', 'value'),
    Input('month_slider', 'value'),
    Input('curve_selector', 'value'),
    Input('graph_selector', 'value'),
    Input('station_selector', 'value'))

def update_figure(year_slider, month_slider, curve_selector, graph_selector, station_selector):
    """
    Input :
        year_slider: recovers the selected year
        month_slider: recovers the selected month
        curve_selector: recovers the selected curve
        graph_selector: recovers the selected graph
        station_selector: recovers the selected station
        
    Output :
        figure: graph
    """
    filtered_df_berlin = filter_dataframe(df1_berlin, year_slider, month_slider)
    
    if station_selector == 'bl':
        figure = upfig.update_figure_general(year_slider, month_slider, curve_selector, graph_selector, filtered_df_berlin)
        
    else:
        None
        
    return figure



# Callback for fourth graphical display
@app.callback(
    Output('energy_graph', 'figure'),
    Input('year_slider', 'value'),
    Input('month_slider', 'value'),
    Input('station_selector', 'value'))

def update_figure_energy(year_slider, month_slider, station_selector):
    """
    Input :
        year_slider: recovers the selected year
        month_slider: recovers the selected month
        station_selector: recovers the selected station
        
    Output :
        figure: graph
    """
    filtered_df1_berlin = filter_dataframe(df2, year_slider, month_slider)
    
    if station_selector == 'bl':
        figure = upfig.update_figure_energy_general(year_slider, month_slider, filtered_df1_berlin)
        
    else:
        None
    
    return figure



# Callback for fifth graphical display
@app.callback(
    Output('motors_graph', 'figure'),
    Input('year_slider', 'value'),
    Input('month_slider', 'value'),
    Input('station_selector', 'value'))

def update_figure_motors(year_slider, month_slider, station_selector):
    """
    Input :
        year_slider: recovers the selected year
        month_slider: recovers the selected month
        station_selector: recovers the selected station
        
    Output :
        figure: graph
    """
    filtered_df2_berlin = filter_dataframe(df4, year_slider, month_slider)
    
    if station_selector == 'bl':
        figure = upfig.update_figure_motors_general(year_slider, month_slider, filtered_df2_berlin)
        
    else:
        None
    
    return figure



#### callback for mini containers
"""
    In each of the functions we retrieve the number of stations for each 
    modality in the status column and we display them in the different 
    containers.    
"""
@app.callback(
    Output("station_offline", "children"),
    Input("aggregate_data", "data"))
def update_offline(data):
    
    return val1



@app.callback(
    Output("station_not_available", "children"),
    Input("aggregate_data", "data"))
def update_not_available(data):
    return val2



@app.callback(
    Output("station_coming_soon", "children"),
    Input("aggregate_data", "data"))
def update_coming_soon(data):
    return val3



@app.callback(
    Output("station_available", "children"),
    Input("aggregate_data", "data"))
def update_available(data):
    return val4






# ****************************** MAIN ****************************************
"""
    Allows Dash to automatically refresh the browser when we make a change to 
    our code. 
    We can disable this option with app.run_server(dev_tools_hot_reload=False)
"""
if __name__ == "__main__":
    app.run_server(debug=True)
