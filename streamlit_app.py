pip install Kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    # Initialize Kaggle API client and authenticate using secrets
    api = KaggleApi()
    api.set_config_value('username', st.secrets["kaggle"]["username"])
    api.set_config_value('key', st.secrets["kaggle"]["key"])
    api.authenticate()
    
    # Define the dataset and the path where files will be downloaded
    dataset = 'junyiacademy'
    path = 'https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy/data?select=Log_Problem.csv'

    # Download the dataset
    api.dataset_download_files(dataset, path=path, unzip=True)

#The dataset is now downloaded in the Streamlit environment
import streamlit as st

if st.sidebar.button('Get Data', type="primary"):
    download_dataset()
#The button will appear on a sidebar, otherwise you can use st.button

data = pd.read_csv("missile_attacks_daily.csv")
