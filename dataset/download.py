import os
import json
import requests

from dataset.download_gcp import authenticate_implicit_with_adc, download_blob

def download_dataset_from_json ():
    """Parses datasets.json and downloads all the datasets listed in the file to their respective filepaths."""

    # read in json file
    f = open('datasets.json')
    data = json.load(f)

    # google authentication step needed if we are downloading data from google storage bucket.
    # print(data['datasets'][0])
    authenticate_implicit_with_adc(data['datasets'][0]['project_name'])

    # iterate over datasets in .json file
    for i, dataset in enumerate(data['datasets']):
        bucket_name = dataset['bucket_name']
        blob_name = dataset['blob_name']
        destination_file_name = dataset['destination_file_name']

        # create dir for dataset to be stored in
        destination_file_path = '/'.join(destination_file_name.split('/')[:-1])
        if not os.path.exists(destination_file_path):
            os.makedirs(destination_file_path)

        # make google storage api call to download the blob to our dir
        download_blob(bucket_name, blob_name, destination_file_name, data['datasets'][0]['project_name'])

def download_public_data_from_url ():
    # read in json file
    f = open('datasets.json')
    data = json.load(f)

    if not os.path.exists('datasets'):
        os.makedirs('datasets')

    # iterate over datasets in .json file
    for i, dataset in enumerate(data['public_datasets']):
        name = dataset['name']
        url = dataset['url']
        response = requests.get(url)
        open(name, "wb").write(response.content)

        os.replace(name, "datasets/{}".format(name))

download_dataset_from_json ()