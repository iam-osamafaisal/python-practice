import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name, 'gztar', source)
    print(f" Backup created successfully: {backup_file_name}.tar.gz")

source = r"D:\python-workshop-practice"  # jaha se backup lena hai
destination = r"D:\python-workshop-practice\backups"  # jaha backup store karna hai

backup_files(source, destination)
