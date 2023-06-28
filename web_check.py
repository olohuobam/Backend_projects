if response.status_code == 200:
    print("Request successful!")
else:
    print("Request failed with status code:", response.status_code)
    # Handle the error accordingly
