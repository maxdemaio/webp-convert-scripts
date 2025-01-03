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
    files_to_delete = ['Header-GoWorkQueue.png', '1MkTm8uVCuvwnoJKPJpBE3Nv5Z0.jpg', 'jPPBfsdozsFxQxWtAYe8jdYkZ4.png', 'FEAOmYQ9v2qbaxr7KvIemwuyUXI.png', 'saas-awards-thumbnail.png', 'job-queue-go-users.png', 'J69Jfm1sSw7fIAhEevhp1kc06o.png', 'header-love-about-nats.png', 'kv-bucket-viewer-full.png', 'OiNsv3ZQ487SkQyqcVbVtJeGVrc.png', 'request-many-chunks-small.png', 'a3kqTzakhsMX5DIx7bJ16V1Bk0.png', 'kv-bucket-viewer.png', 'cloud-limits-header.png', 'job-queue-go-architecture.png', 'cloud-connection-graph.png', 'EDWPJPVTXMSE469VstYm9awn53A.png', 'QbIjffpQ0CrcHxGfguD5wm6xCg.jpg', 'Zv4GggkgicRCuXYly7wkSAIoo.jpg', 'ufeDDqY1gW5ZirPWTZ8NeQiKs.jpg', 'WZ5W3xXx5cwzZP1S5MN3riIig.jpg', 'KVvTBOWfyJuMD52LgJkC5HqM1Mc.jpg', 'nGUw1xSVMOcktk71kpmQ9XYIM.png', 'CHRFrCkPTvufdA4DyZWFQ4xi9k.png', 'YX1crHSLGumiRLg3MLgmQlzf0.png', '1tGokW4Ct7eRkTIpKSU3hQTJ7iM.png', 'nats-and-kafka-compared-header.png', 'autonomous-cars.jpg', 'kafka-vs-nats-compared-2.png', '370347207.png', 'teWta2i0zFXBJhFoPzX0ZpoJaM.png', 'LPw5qDSI4VzSuLYDIJS0HBxT91E.png', 'Nbbn3vumv0WzUVfWJ6U04Zqqk9I.jpg', 'rethinking-microservices-thumbnail.jpg', 'Forklift-table1-v2.png', 'uk2pkbR1r5GKdqZtXeXthkSBus.jpg', 'nvSe1KiRJ0jwVVKPuM3CMI6LwRo.png', 'i9q9Ov492ktNm8JSTwqybze0.png', 'KNkqAlyd6L79D5RP0IUpCqLsQU.png', 'kafka-vs-nats-compared-3.png', '9VwI70aX6FwNidHlbDudZA9MAm8.jpg', 'di0HNS24QQK8aRioCkrvZ8a7kY.png', 'dataframed-edge-computing.png', 'request-many-discovery-small.png', 'JJzAwmhljv0Eo7shZkuHbMGTgWM.jpg', 'job-queue-go-default-account.png', 'RI9MvN1akAUNrsxP6wQhN2887sc.jpg', '9k4Cw8PHtQqQKHHUD1HpE3TZJ2U.png', 'blogNorthSouthArchDiag.png', 'L4cnQaIbnyucN4Km4ueeNNL4Dg.jpg', 'ZRUEuXPUD6RkpHFQpimnOaO5po.png', '7dGbw11p9ewjrAWqZPnIMZoqPI.jpg', 'cloud-account-overview.png', 'kbuPl0csYYNdYUpHfs4JriRGeQ.png', 'applications.png', 'B6K3oC6qcCJOt0MjLdlg5CSYWw.png', 'FKV09TJ8AnLqrhDArKDBJFMHfE.png', 'XNG32jZ74kVQK0vUfP0Si9wv32Y.jpg', '8ncPYWBHhQ8vzwTuQ6mkxYwEOs.png', 'BJjX4Id2Tzm0ro1wGMu2TQKsoR8.png', '9r7p7CxfjirKVmVYJIoxYpOZw7E.png', 'FJZAaXwksUmMaI0jANZQOhjSMA.jpg', 'zdxjtzZ5XTmRkCNQlAjwLGgcU.jpg', 'ulT5FdrsUM9oDBxqzTMMnxxazU.jpg', 'http-nats.jpg', 'AXtH0vfi4IQ2jmg6PRlfg4msG0Q.png', 'wMCrZBTFsmHy4saKkB078Cs2I5w.jpg', 'orbit-min.png', 'QRpjalQrcUFyXa1Guh8nCfa9az0.png', 'bNqwvCZSZj9AiGOzwTfQfIzmQ.png', 'cobHDygvkHzZeGgkqLmkGqKEzbs.jpg', 'applications-history.png', 'Header-EastWestNorthSouth.png', 'nats-and-pathway-arch.png', 'S7MHU3jINgxXAvP7Mdx9DyHw4Tw.png', 'cloud-user-management.png', 'ck6wxAXWIwHsQgbGCo4FOjbH5Kw.png', '6IIQEKRNyY5xSSUBcatqum9N9k.jpg', 'gbqdnVEeRzQa6khOcbeBFSFDNA8.jpg', 'Forklift-table2-v2.png', 'FRsvZey28q3OsI9wHwrKm3QddY.png', 'shed-light.png', '8GXu8H0IKSNibRM1iLhI3SeEJ0.png', 'kafka-vs-nats-compared-1.png', 'i99kyVmrc5SKppv69vUiw7cTfX0.png', 'L6BcyMblnSWEi8LachXtKGL6KM.png', 'Forklift-header-v2.png', '1RunhJs2IqPDYDxmDifVtMfjTcI.jpg', 'v8CspHQR1KCnZMRt4Fan1Wo3NE.jpg', 'synadia-susecon-24.png', 'GvnQCPKEqBYFPnhITsNXLxehF0.jpg', 'job-queue-go-user-details.png']
    
    # Call the delete_files function with the provided folder path
    delete_files(folder_path, files_to_delete)

# This ensures the main method is only called when the script is executed directly
if __name__ == "__main__":
    main()
