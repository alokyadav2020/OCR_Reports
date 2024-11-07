from google.cloud import storage
from google.oauth2 import service_account
import streamlit as st

credentials = service_account.Credentials.from_service_account_info(st.secrets["arjun_gcs_connection"])

def create_bucket_and_folder(bucket_name:str, folder_name):
    try:
        # Initialize a Google Cloud Storage client
        client = storage.Client(project="my-project-6750-ai-2024",credentials=credentials)
        
        # Create the bucket (check if it exists first)
        # bucke_names = bucket_name.replace(" ","_")
        bucket = client.bucket(bucket_name)
        if not bucket.exists():
            bucket = client.create_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")

        # Define folder path within the bucket
        folder_path = f"{folder_name}/"

        # Create a "dummy" blob to represent the folder
        blob = bucket.blob(folder_path + ".keep")
        blob.upload_from_string("")  # Upload an empty file to create the folder

        print(f"Folder '{folder_name}' created in bucket '{bucket_name}'.")
        return f"gs://{bucket_name}/{folder_path}"
    
    except Exception as e:
        print(e)
        return None
    





import streamlit as st
from google.cloud import storage

# Initialize Google Cloud Storage client


def upload_file_to_gcs(bucket_name, folder_path, file, destination_filename):

    try:

        client = storage.Client(project="my-project-6750-ai-2024",credentials=credentials)
        # Get the bucket
        bucket = client.bucket(bucket_name)
        
        # Define the blob path within the bucket (folder + file name)
        blob_path = f"{folder_path}/{destination_filename}"
        blob = bucket.blob(blob_path)
        
        # Upload the file-like object from Streamlit without saving locally
        blob.upload_from_file(file)
        
        # st.success(f"File uploaded to gs://{bucket_name}/{blob_path}")
        print(f"File uploaded to gs://{bucket_name}/{blob_path}")
        file_url = f"gs://{bucket_name}/{blob_path}"
        return file_url

    # Streamlit file uploader
        # uploaded_file = st.file_uploader("Choose a file to upload")

        # # Form submission to upload the file to Google Cloud Storage
        # if uploaded_file is not None:
        #     bucket_name = "runsheet_tilte_ocr"
        #     folder_path = "pdf_folder"  # Folder path within the bucket
        #     destination_filename = uploaded_file.name  # Use the uploaded file's name or customize it
            
        #     # Upload the file if the upload button is clicked
        #     upload_file_to_gcs(bucket_name, folder_path, uploaded_file, destination_filename)


    except Exception as e:
        print(f"Error: {e}")
        return None



