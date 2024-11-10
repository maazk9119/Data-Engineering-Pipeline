from pipHelper import Datasource

def main():
    print("Data processing pipeline has been started.")
    datasource = Datasource().InitalizeData()

    for table, config in datasource.datasets.items():
        print(f"The dataset name is:{table}")
    
    print("Data processing completed and loaded into the database.")

if __name__ == "__main__":
    main()