import os

API_HOST = 'https://reqres.in/'
REGISTRATION_ENDPOINT = 'api/register'
contentType = {'Content-Type': 'application/json'}

project_dir = os.path.dirname(os.path.realpath(__file__))
reports_dir = project_dir + '\\reports\\'
feature_files_dir = project_dir + '\\tests\\features\\'
keywords_dir = project_dir + '\\tests\\step_defs\\'
