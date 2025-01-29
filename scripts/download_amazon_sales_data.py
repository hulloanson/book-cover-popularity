import os
import requests
from tqdm import tqdm

def download_amazon():

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "data")
    output_file = os.path.join(output_dir, "amazon-sales-rank-data-for-print-and-kindle-books.zip")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    if os.path.exists(output_file):
        print(f"{output_file} already exists. Skipping download.")
    else:
        url = "https://www.kaggle.com/api/v1/datasets/download/ucffool/amazon-sales-rank-data-for-print-and-kindle-books"
        
        with requests.get(url, stream=True, allow_redirects=True) as response:
            if response.status_code == 200:
                total_size = int(response.headers.get('content-length', 0))
                block_size = 1024  # 1 KB

                with open(output_file, "wb") as file, tqdm(
                    total=total_size, unit='B', unit_scale=True, desc="Downloading"
                ) as progress_bar:
                    for chunk in response.iter_content(chunk_size=block_size):
                        file.write(chunk)
                        progress_bar.update(len(chunk))

                print(f"File downloaded successfully as {output_file}")
            else:
                print(f"Failed to download file. Status code: {response.status_code}")