from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

drive.CreateFile({'id': '1IJJeFUl1DPl50FvQsOlXQi6cpsXxNQwn'}).GetContentFile('zipline.sh')
