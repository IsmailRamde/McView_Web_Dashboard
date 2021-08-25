#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:05:21 2021

@author: ismael
"""

# Import required libraries
import plotly.express as px
import plotly.graph_objects as go




#********************************** PLOTS *************************************
###          Functions to build graphs that need to be updated.

############     Construction of the first graph          ###############
def update_figure_general(year_slider, month_slider, curve_selector, graph_selector, filtered_df):
    """
    Input :
        year_slider: recovers the selected year
        month_slider: recovers the selected month
        curve_selector: recovers the selected curve
        graph_selector: recovers the selected graph
        filtered_df: data filtered according to the user's selection
        
    Output :
        figure: graph
    """
    if graph_selector == "view1":
        if curve_selector == "all":
            figure = px.line(filtered_df, x="TimeStr", y=['PT', 'TT', 'FT', 'PCV'],
                                 hover_data={"TimeStr": "|%B %d, %Y"})
            # To enlarge the figure
            figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            # transitions allow the chart to update from one state to the next smoothly, as if it were animated
            figure.update_layout(transition_duration=500)
            
        elif curve_selector == "pt":
            figure = px.line(filtered_df, x="TimeStr", y=['PT'],
                                hover_data={"TimeStr": "|%B %d, %Y"})
            figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            figure.update_layout(transition_duration=500)
        
        elif curve_selector == "tt":
            figure = px.line(filtered_df, x="TimeStr", y=['TT'],
                                 hover_data={"TimeStr": "|%B %d, %Y"})
            figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            figure.update_layout(transition_duration=500)
    
        elif curve_selector == "ft":
                figure = px.line(filtered_df, x="TimeStr", y=['FT'],
                                 hover_data={"TimeStr": "|%B %d, %Y"})
                figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                figure.update_layout(transition_duration=500)
            
        else:
            figure = px.line(filtered_df, x="TimeStr", y=['PCV'],
                             hover_data={"TimeStr": "|%B %d, %Y"})
            figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            figure.update_layout(transition_duration=500)
    else:
        if curve_selector == "all":
            x = filtered_df["Day"]

            figure = go.Figure()
            figure.add_trace(go.Box(
                    y=filtered_df["PT"],
                    x=x,
                    name='PT',
                    marker_color='#3D9970'
                    ))
            figure.add_trace(go.Box(
                    y=filtered_df["TT"],
                    x=x,
                    name='TT',
                    marker_color='#FF4136'
                    ))
            figure.add_trace(go.Box(
                    y=filtered_df["FT"],
                    x=x,
                    name='FT',
                    marker_color='#FF851B'
                    ))
            figure.add_trace(go.Box(
                    y=filtered_df["PCV"],
                    x=x,
                    name='PCV',
                    marker_color='#8d7dff'
                    ))

            figure.update_layout(
                    xaxis=dict(title='Day', zeroline=False),
                    boxmode='group'
                    )

            figure.update_traces(orientation='v') # horizontal box plots
            figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            figure.update_layout(transition_duration=500)
            #figure.show() 
        elif curve_selector == "pt":
            x = filtered_df["Day"]

            figure = go.Figure()
            figure.add_trace(go.Box(
                    y=filtered_df["PT"],
                    x=x,
                    name='PT',
                    marker_color='#3D9970'
                    ))

            figure.update_layout(
                    xaxis=dict(title='Day', zeroline=False),
                    boxmode='group'
                    )

            figure.update_traces(orientation='v') # horizontal box plots
            figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            figure.update_layout(transition_duration=500)
            #figure.show()
        
        elif curve_selector == "tt":
            x = filtered_df["Day"]

            figure = go.Figure()
            figure.add_trace(go.Box(
                    y=filtered_df["TT"],
                    x=x,
                    name='TT',
                    marker_color='#FF4136'
                    ))

            figure.update_layout(
                    xaxis=dict(title='Day', zeroline=False),
                    boxmode='group'
                    )

            figure.update_traces(orientation='v') # horizontal box plots
            figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            figure.update_layout(transition_duration=500)
            #figure.show()
    
        elif curve_selector == "ft":
                x = filtered_df["Day"]

                figure = go.Figure()
                figure.add_trace(go.Box(
                    y=filtered_df["FT"],
                    x=x,
                    name='FT',
                    marker_color='#FF851B'
                    ))

                figure.update_layout(
                        xaxis=dict(title='Day', zeroline=False),
                        boxmode='group'
                        )

                figure.update_traces(orientation='v') # horizontal box plots
                figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                figure.update_layout(transition_duration=500)
                #figure.show()
        
        else:
            x = filtered_df["Day"]

            figure = go.Figure()
            figure.add_trace(go.Box(
                    y=filtered_df["PCV"],
                    x=x,
                    name='PCV',
                    marker_color='#8d7dff'
                    ))

            figure.update_layout(
                    xaxis=dict(title='Day', zeroline=False),
                    boxmode='group'
                    )

            figure.update_traces(orientation='v') # horizontal box plots
            figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            figure.update_layout(transition_duration=500)
            #figure.show()
#        figure = px.box(filtered_df, x="Day", y=['PT', 'TT', 'FT', 'PCV'])
#        figure.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
#        figure.show()
        
#        df = pd.DataFrame(dict(
#                f1=filtered_df["PT"],
#                f2=filtered_df["TT"],
#                f3=filtered_df["FT"],
#                f4=filtered_df["PCV"]
#                )).melt(var_name="quartilemethod")
#
#
#        figure = px.box(df, y="value", facet_col="quartilemethod", color="quartilemethod",
#                 boxmode="overlay", points='all')
#
#        figure.update_traces(quartilemethod="f1", jitter=0, col=1)
#        figure.update_traces(quartilemethod="f2", jitter=0, col=2)
#        figure.update_traces(quartilemethod="f3", jitter=0, col=3)
#        figure.update_traces(quartilemethod="f4", jitter=0, col=4)
#
#        figure.show()
    

    return figure




############     Construction of the fourth graph          ###############
def update_figure_energy_general(year_slider, month_slider, filtered_df1):
    """
    Input :
        year_slider: recovers the selected year
        month_slider: recovers the selected month
        filtered_df: data filtered according to the user's selection
        
    Output :
        figure: graph
    """
    
    figure = px.line(filtered_df1, x="TimeStr", y=['kVA','KVAR','kW'])
    # To enlarge the figure
    figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # transitions allow the chart to update from one state to the next smoothly, as if it were animated
    figure.update_layout(transition_duration=500)
    
    return figure




############     Construction of the fifth graph          ###############
def update_figure_motors_general(year_slider, month_slider, filtered_df2):
    """
    Input :
        year_slider: recovers the selected year
        month_slider: recovers the selected month
        filtered_df: data filtered according to the user's selection
        
    Output :
        figure: graph
    """

    figure = go.Figure()
    figure.add_trace(go.Bar(
            x=filtered_df2["Day"],
            y=filtered_df2["Air_Compressor"],
            name='Air Compressor',
            marker_color='indianred'
    ))
    figure.add_trace(go.Bar(
            x=filtered_df2["Day"],
            y=filtered_df2["Air_Extractor"],
            name='Air Extractor',
            marker_color='lightsalmon'
    ))
    figure.add_trace(go.Bar(
            x=filtered_df2["Day"],
            y=filtered_df2["D1_Cooling_Unit"],
            name='D1 Cooling Unit',
            marker_color='olive'
    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    figure.update_layout(barmode='group', xaxis_tickangle=-45)
    # To enlarge the figure
    figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #fig6.show()
    # transitions allow the chart to update from one state to the next smoothly, as if it were animated
    figure.update_layout(transition_duration=500)
    
    return figure