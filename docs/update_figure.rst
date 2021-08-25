update_figure
=============


In this script three functions are implemented, namely *update_figure_general*, *update_figure_energy_general* and *update_figure_motors_general*.
It was created in order to make the main *app.py* script less busy and more fluid. 
It is imported into the *app.py* script with the following command: **import update_figure as upfig**
As an example, *upfig.update_figure_general([parameters])* allows to use the *update_figure_general* function in the *app.py* script.

Translated with www.DeepL.com/Translator (free version)


.. py:function:: update_figure_general(year_slider, month_slider, curve_selector, graph_selector, filtered_df)

   :param year_slider: retrieves the selected year
   :param month_slider: retrieves the selected month
   :param curve_selector: retrieves the selected curve
   :param graphe_selector: retrieves the selected graph
   :param filtered_df: data filtered according to the user's selection.
        
   :return: figure (graph)


.. py:function:: update_figure_energy_general(year_slider, month_slider, filtered_df1)

   :param year_slider: retrieves the selected year
   :param month_slider: retrieves the selected month
   :param filtered_df: filtered_df: data filtered according to the user's selection
        
   :return: figure (graph)
   


.. py:function:: update_figure_motors_general(year_slider, month_slider, station_selector)

      :param year_slider: retrieves the selected year
   :param month_slider: retrieves the selected month
   :param filtered_df: filtered_df: data filtered according to the user's selection
        
   :return: figure (graph)


