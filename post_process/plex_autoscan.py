#!/usr/bin/python
import os
import json
import requests

def main():
	print("Plex Autoscan Post Script")
	url = "http://localhost:3689/apikey"

	files = json.loads(os.environ.get('MH_FILES'))
	if not (files):
        print("Error - Did not find environment variables.")
        return

	for filename in files:
		dirname = os.path.dirname(filename)
		payload = {'eventType': 'Manual'
				   'filepath': dirname}
		try:
			requests.post(url, json=payload)
		except Exception as e:
			print("Error - Request failed")
			print(e)

if __name__ == "__main__":
    main()
