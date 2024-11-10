from pipHelper import Datasource

def main():
    print("Data processing pipeline has been started.")
    datasource = Datasource().InitalizeData()

    for index, (table, config) in enumerate(datasource.datasets.items(), start=1):
        print(f"No.{index}: The dataset name is: {table}")
        print(f"The setup configurations are:{config}")


    
    print("Data processing completed and loaded into the database.")

if __name__ == "__main__":
    main()