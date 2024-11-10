from etl import (extract, transform, load)

"""
Datasource class has responsibilty to manage selected Portal e.g Data.gov
"""
class Datasource:
    
    """
    Initialzing the selected datasets into DSA format
    Args:
        self: Instance level implementation
    Return: current instance of Datasource 
    """
    def initalize_datasets(self):
        self.datasets = {
        "ReportCardEnrollment": {
            "url": "https://data.wa.gov/api/views/m644-2j5h/rows.csv?accessType=DOWNLOAD",
            "columns_to_delete": [
                "American_Indian","Asian","Black","Hispanic","Native_Hawaiian",
                "Two_or_More_Races","White","English","Fooster_Care","Migrant",
                "Military_Parent","Section_504","Students_with_Disability",
                "Non-English_Language_Learners","Non-Foster_Care","Non_Migrant",
                "Non_Military_Parent","Non_Section_504","Students_without_Disability",
                "DateAsOf"
            ]
        },
        "SchoolNeighborhoodPovertyEstimates": {
            "url": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10bd90462ec14a53bab1827bc8f533c9/csv?layers=1",
            "columns_to_delete": [
                "X",
                "Y",
                "OBJECTID",
                "NCESSCH"
            ]
        }}
        return self
    
    def execute_etl_process(self, table, config):
        #step 1 Extract from Datasource
        df = extract.get_dataframe(config['url'])
        #step 2 Transform data
        df_transformed = transform.apply_defined_transformation(df, config)
        #step 3 load data
        load.load_data_to_sqlitedb(table, df)