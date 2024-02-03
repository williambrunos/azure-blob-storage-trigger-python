import azure.functions as func
import logging
from dotenv import load_dotenv
import os

load_dotenv()
AZR_CONTAINER_PATH = os.getenv("AZR_CONTAINER_PATH")
AZR_STORAGE_CONNECTION = os.getenv("AZR_STORAGE_CONNECTION")

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path=AZR_CONTAINER_PATH,
                               connection=AZR_STORAGE_CONNECTION) 
def AzrFunctionBlobTrigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")

