read\_write\_google\_API module
===============================


This script is used to establish the connection to the Google cloud via an API. It also contains functions used to write in the Google spread Sheet, to open a database of tables from the Server and to structure our different data frame.



.. py:function:: Insert_DF_inGsheets(gSheetKey,gsheetindex,df)

   This function allows to write in the Google spread sheet.

   :param gSheetKey: Google spread Sheet key
   :param gsheetindex: Google spread Sheet index (0 - first sheet, 1 - second sheet etc)
   :param df: Data Frame

   :return: Do not return but export the dataframe to the Google Sheet.



.. py:function:: openDF(gSheetKey,index)

   openDF function allows to open a Table Database from Server.

   :param gSheetKey: Google spread Sheet key
   :param index: Index value ( 0 - first sheet,   1 - second sheet etc.)

   :return: Data Frame 
   
   
   
.. py:function:: SortH2MDistributionData()

   This function allows us to structure the data according to our needs in the web application for the construction of the first graph.
   The function takes nothing as input but uses the **openDF** function.

   :return: It returns the Data Frame in the following form: 
   **| Date | Year | Month | Day | Time | PT | TT | FT | PCV |**


   
   
.. py:function:: SortH2MEnergyData()

   :return: Data Frame in the following form:
   **| TimeStr | Year | Month | Day | Hour | kVA | KVAR | kW |**
   
   
   
.. py:function:: SortH2MotorsData()

   :return: Data Frame in the following form:
   **| TimeStr | Year | Month | Day | Hour | Air_Compressor | D1_Cooling_Unit |**
   


   
.. py:function:: Data_MAP()

   The Data_MAP function takes nothing as input but uses **openDF** function.
   It retrieves the location data of McPhy stations and their current status. This data is used in the satellite overview presentation.
   
   :return: It returns the Map Tableau in the following form:
   **| Latitud | Longitud | Country | City | Project | Status | Status Value |**
   



