from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('container', 'v1', credentials=credentials)

# The parent (project and location) where the operations will be listed.
# Specified in the format 'projects/*/locations/*'.
# Location "-" matches all zones and all regions.
parent = 'projects/My First Project/locations/us-east1'  # TODO: Update placeholder value.

request = service.projects().locations().operations().list(parent=parent)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
