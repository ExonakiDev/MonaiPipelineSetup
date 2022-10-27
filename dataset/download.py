import os
import json

from utils.download_gcp import download_blob, authenticate_implicit_with_adc
# from utils.parse_json import parse_dataset_json_file

def download_dataset_from_json ():
    """Parses datasets.json and downloads all the datasets listed in the file to their respective filepaths."""

    # google authentication step needed if we are downloading data from google storage bucket.
    authenticate_implicit_with_adc("fluid-tangent-363120")

    # read in json file
    f = open('datasets.json')
    data = json.load(f)

    # iterate over datasets in .json file
    for i, dataset in enumerate(data['datasets']):
        bucket_name = dataset['bucket_name']
        blob_name = dataset['blob_name']
        destination_file_name = dataset['destination_file_name']

        # create dir for dataset to be stored in
        destination_file_path = '/'.join(destination_file_name.split('/')[:-1])
        os.makedirs(destination_file_path)

        # make google storage api call to download the blob to our dir
        download_blob(bucket_name, blob_name, destination_file_name, "fluid-tangent-363120")

download_dataset_from_json()

