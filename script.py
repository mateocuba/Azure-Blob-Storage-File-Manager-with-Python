
from azure.storage.blob import BlobServiceClient
import os

CONN_STR = "DefaultEndpointsProtocol=https;AccountName=storageaccountmateo;AccountKey=rRJ5USQFCw9jVhe/zhmVlED1fSm/Z7paX5O17CMmXaUvgWuqcKBvjpRqUNoocBHf1mKkmXXnGQsX+AStW5T+MA==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "container1"

blob_service_client = BlobServiceClient.from_connection_string(CONN_STR)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)


def upload_file():
    file_path = input("Enter the full path of the file to upload: ").strip()
    if not os.path.isfile(file_path):
        print("❌ File does not exist.")
        return
    blob_name = os.path.basename(file_path)
    with open(file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)
    print(f"✅ Uploaded: {blob_name}")


def download_file():
    blob_name = input("Enter the blob name to download: ").strip()
    local_path = input("Enter the local path to save the file: ").strip()
    try:
        with open(local_path, "wb") as f:
            download_stream = container_client.download_blob(blob_name)
            f.write(download_stream.readall())
        print(f"✅ Downloaded to: {local_path}")
    except Exception as e:
        print(f"❌ Error: {e}")


def list_files():
    print("📄 Files in container:")
    try:
        blobs = container_client.list_blobs()
        for blob in blobs:
            print(f"- {blob.name}")
    except Exception as e:
        print(f"❌ Error: {e}")


def delete_file():
    blob_name = input("Enter the blob name to delete: ").strip()
    try:
        container_client.delete_blob(blob_name)
        print(f"🗑️ Deleted: {blob_name}")
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    while True:
        print("\n=== Azure Blob Storage Manager ===")
        print("1. Upload File")
        print("2. Download File")
        print("3. List Files")
        print("4. Delete File")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            upload_file()
        elif choice == "2":
            download_file()
        elif choice == "3":
            list_files()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()