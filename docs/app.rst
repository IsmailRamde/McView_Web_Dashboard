app module
==========



The *app.py* module is the main script of our Dash application. This script is composed of two parts : the **layout** (app.layout) and the **Dash Callbacks**. 
It also contains package loads and imports of other modules that are necessary for the application to work, several independent commands (loading and preprocessing of data, etc.) and several functions.

* **app.layout** describes what the application looks like and is a hierarchical tree of components. the dash_html_components library provides classes for all HTML and keyword arguments describing HTML attributes such as style, className, and id. the dash_core_components library generates higher level components such as controls and graphics. 

* The **callback function** allows to update the *output* component on the page (the HTML div) each time the value of the *input* component (the text zone) is modified.



.. py:function:: filter_dataframe(df1, year_slider, month_slider)

   :param df1: the data frame containing PT (Pressure), TT (Temperature Transmission), FT (Flow Transmission) and PCV 			(Pressure Control Valve) data.
		This data set has been loaded in the top part of the code.

   :param year_slider: recovers the selected year
   
   :param month_slider: recovers the selected month

   :return: filtered_df (filtered data).



The inputs and outputs of following functions are retrieved in the decorator **@app.callback**. 
   
.. py:function:: update_figure(year_slider, month_slider, curve_selector, graphe_selector, station_selector)

   In this function we use two functions. The first one is the **filter_dataframe** function to filter the data according to the user's selection. And the second one is the **update_figure_general** function implemented in another script (*update_figure.py*). This allows us to simplify our main script (*app.py*).

   :param year_slider: which retrieves the selected year
   :param month_slider: which retrieves the selected month
   :param curve_selector: which retrieves the selected curve
   :param graphe_selector: which retrieves the selected graph
   :param station_selector: which retrieves the selected station
        
   :return: figure (graph of data evolution over time)
   
   
.. py:function:: update_figure_energy(year_slider, month_slider, station_selector)
   
   Here we also use the **filter_dataframe** function and the **update_figure_energy_general** function, another function implemented in the *update_figure.py* script.
   
   :param year_slider: which retrieves the selected year
   :param month_slider: which retrieves the selected month
   :param station_selector: which retrieves the selected station
        
   :return: figure (graph of energy consumption)


.. py:function:: update_figure_motors(year_slider, month_slider, station_selector)

   As the two previous functions, we use the **filter_dataframe** function and the **update_figure_motors_general** function contained in the *update_figure.py* script.
   
   :param year_slider: which retrieves the selected year
   :param month_slider: which retrieves the selected month
   :param station_selector: which retrieves the selected station
        
   :return: figure (barplot graph of motors)


.. py:function:: update_offline(data)

   :param data: data of stations status
   
   :return: value (number of offline stations)
   
   
.. py:function:: update_not_available(data)

   :param data: data of stations status
   
   :return: value (number of not available stations)
   
   
.. py:function:: update_coming_soon(data)

   :param data: data of stations status
   
   :return: value (number of coming soon stations)


.. py:function:: update_available(data)

   :param data: data of stations status
   
   :return: value (number of available stations)
