""" Python script for uploading the eCommerce Dataset to their
    respective buckets in the minIO instance.
    Needs the docker containers already deployed to work! """

from minio import Minio
from pathlib import Path

# Initialize MinIO client
minioClient = Minio('localhost:9000',
                    access_key='lWslci9JARykvqBvssFz',
                    secret_key='vVP2Xnaob6BehGitUoCI7fpBLVOsT6kHpuvwkbkk',
                    secure=False)  # Set secure to True for HTTPS

# Path to the folder containing CSV files
data_folder = Path('/Users/marcelwinterhalter/Developer/Projects/BDSP/eCommerceDataset/')

# Iterate through each file and upload
for file_path in data_folder.glob('*.csv'):
    # Extract year and month from file name (format: "2019-Nov.csv")
    year, month = file_path.stem.split('-')
    bucket_name = f"ecommerce-{year.lower()}-{month.lower()}"

    # Ensure that the bucket exists
    if not minioClient.bucket_exists(bucket_name):
        minioClient.make_bucket(bucket_name)

    # Upload the file
    object_name = file_path.name
    minioClient.fput_object(bucket_name, object_name, str(file_path))
    print(f'File {file_path.name} uploaded to bucket {bucket_name}')

print("All files uploaded.")
