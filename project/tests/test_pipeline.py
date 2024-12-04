from fixtures import(execute_pipeline, delete_output_filePath)
import os    

def test_output_file_Exist(execute_pipeline):
    #Ensure the file created
    file_path = "./data/UnequalGroundsDB.db"
    
    #Assert
    assert os.path.exists(file_path), (
        "Output file is not created by Advance Data Engineering pipeline")

def test_output_file_NotExist(delete_output_filePath):
    # Ensure the file does not exist
    file_path = "./data/UnequalGroundsDB.db"
    
    #Assert
    assert not os.path.exists(file_path), (
        "Output file is already Exist")