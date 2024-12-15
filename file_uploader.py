import requests

def upload_file(file_path: str, url: str = "https://gunfire.icu/api"):
    """
    Uploads a file to the specified URL.
    
    :param file_path: The path of the file to upload.
    :param url: The URL where the file will be uploaded (default is "https://gunfire.icu/api").
    :return: The file URL if the upload is successful, or None if it fails.
    """
    with open(file_path, "rb") as file_to_upload:
        files = {
            "filetoupload": file_to_upload
        }

        try:
            response = requests.post(url, files=files)
            
            # Print the response
            if response.status_code == 200:
                print("Upload Successful!")
                return response.json().get("fileUrl")
            else:
                print(f"Failed to upload. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None
