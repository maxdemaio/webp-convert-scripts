import os
import sys

def delete_files(folder_path, files_to_delete):
    # Loop through the list of files and delete those that exist in the folder
    for file_name in files_to_delete:
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f'{file_name} has been deleted.')
            except Exception as e:
                print(f'Error deleting {file_name}: {e}')
        else:
            print(f'{file_name} does not exist in the folder.')

def main():
    # Check if the directory argument was provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <directory_path>")
        sys.exit(1)

    # Get the directory path from the command-line argument
    folder_path = sys.argv[1]

    # Check if the provided path is a valid directory
    if not os.path.isdir(folder_path):
        print(f"The provided path '{folder_path}' is not a valid directory.")
        sys.exit(1)

    # Dummy list for files_to_delete
    files_to_delete = ['Header-EastWestNorthSouth.png', 'applications-history.png', 'J69Jfm1sSw7fIAhEevhp1kc06o.png', 'L4cnQaIbnyucN4Km4ueeNNL4Dg.jpg', 'Zv4GggkgicRCuXYly7wkSAIoo.jpg', 'job-queue-go-users.png', 'cloud-limits-header.png', 'uk2pkbR1r5GKdqZtXeXthkSBus.jpg', 'shed-light.png', '7dGbw11p9ewjrAWqZPnIMZoqPI.jpg', 'i9q9Ov492ktNm8JSTwqybze0.png', '1MkTm8uVCuvwnoJKPJpBE3Nv5Z0.jpg', 'job-queue-go-default-account.png', 'saas-awards-thumbnail.png', '1RunhJs2IqPDYDxmDifVtMfjTcI.jpg', 'header-love-about-nats.png', '9VwI70aX6FwNidHlbDudZA9MAm8.jpg', 'wMCrZBTFsmHy4saKkB078Cs2I5w.jpg', 'teWta2i0zFXBJhFoPzX0ZpoJaM.png', 'byon.png', 'cloud-connection-graph.png', '8GXu8H0IKSNibRM1iLhI3SeEJ0.png', 'nats-and-kafka-compared-header.png', 'FRsvZey28q3OsI9wHwrKm3QddY.png', 'jPPBfsdozsFxQxWtAYe8jdYkZ4.png', 'kafka-vs-nats-compared-1.png', 'kbuPl0csYYNdYUpHfs4JriRGeQ.png', 'cobHDygvkHzZeGgkqLmkGqKEzbs.jpg', 'job-queue-go-architecture.png', 'cloud-user-management.png', 'nvSe1KiRJ0jwVVKPuM3CMI6LwRo.png', 'Forklift-header-v2.png', 'kv-bucket-viewer.png', 'autonomous-cars.jpg', 'nats-and-pathway-arch.png', 'applications.png', 'http-nats.jpg', 'kafka-vs-nats-compared-2.png', 'GvnQCPKEqBYFPnhITsNXLxehF0.jpg', 'XNG32jZ74kVQK0vUfP0Si9wv32Y.jpg', 'gbqdnVEeRzQa6khOcbeBFSFDNA8.jpg', '9r7p7CxfjirKVmVYJIoxYpOZw7E.png', 'request-many-chunks-small.png', 'dataframed-edge-computing.png', 'FKV09TJ8AnLqrhDArKDBJFMHfE.png', 'LPw5qDSI4VzSuLYDIJS0HBxT91E.png', 'KNkqAlyd6L79D5RP0IUpCqLsQU.png', '9k4Cw8PHtQqQKHHUD1HpE3TZJ2U.png', 'QbIjffpQ0CrcHxGfguD5wm6xCg.jpg', 'L6BcyMblnSWEi8LachXtKGL6KM.png', 'Nbbn3vumv0WzUVfWJ6U04Zqqk9I.jpg', 'bNqwvCZSZj9AiGOzwTfQfIzmQ.png', 'JJzAwmhljv0Eo7shZkuHbMGTgWM.jpg', 'S7MHU3jINgxXAvP7Mdx9DyHw4Tw.png', 'rethinking-microservices-thumbnail.jpg', 'RI9MvN1akAUNrsxP6wQhN2887sc.jpg', 'ulT5FdrsUM9oDBxqzTMMnxxazU.jpg', 'Forklift-table1-v2.png', 'ck6wxAXWIwHsQgbGCo4FOjbH5Kw.png', 'WZ5W3xXx5cwzZP1S5MN3riIig.jpg', 'YX1crHSLGumiRLg3MLgmQlzf0.png', 'request-many-discovery-small.png', 'EDWPJPVTXMSE469VstYm9awn53A.png', 'CHRFrCkPTvufdA4DyZWFQ4xi9k.png', 'ufeDDqY1gW5ZirPWTZ8NeQiKs.jpg', 'v8CspHQR1KCnZMRt4Fan1Wo3NE.jpg', '8ncPYWBHhQ8vzwTuQ6mkxYwEOs.png', 'kafka-vs-nats-compared-3.png', 'cloud-account-overview.png', 'B6K3oC6qcCJOt0MjLdlg5CSYWw.png', 'FEAOmYQ9v2qbaxr7KvIemwuyUXI.png', 'zdxjtzZ5XTmRkCNQlAjwLGgcU.jpg', 'a3kqTzakhsMX5DIx7bJ16V1Bk0.png', 'QRpjalQrcUFyXa1Guh8nCfa9az0.png', 'OiNsv3ZQ487SkQyqcVbVtJeGVrc.png', 'blogNorthSouthArchDiag.png', 'kv-bucket-viewer-full.png', '6IIQEKRNyY5xSSUBcatqum9N9k.jpg', 'KVvTBOWfyJuMD52LgJkC5HqM1Mc.jpg', 'i99kyVmrc5SKppv69vUiw7cTfX0.png', 'Forklift-table2-v2.png', 'di0HNS24QQK8aRioCkrvZ8a7kY.png', 'ZRUEuXPUD6RkpHFQpimnOaO5po.png', 'synadia-susecon-24.png', 'job-queue-go-user-details.png', 'nGUw1xSVMOcktk71kpmQ9XYIM.png', 'orbit-min.png', 'FJZAaXwksUmMaI0jANZQOhjSMA.jpg', 'BJjX4Id2Tzm0ro1wGMu2TQKsoR8.png', '1tGokW4Ct7eRkTIpKSU3hQTJ7iM.png', 'AXtH0vfi4IQ2jmg6PRlfg4msG0Q.png', 'Header-GoWorkQueue.png', '370347207.png']
    
    # Call the delete_files function with the provided folder path
    delete_files(folder_path, files_to_delete)

# This ensures the main method is only called when the script is executed directly
if __name__ == "__main__":
    main()
