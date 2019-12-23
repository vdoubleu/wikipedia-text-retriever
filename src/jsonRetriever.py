import requests
import json

data = open("raw-text.txt", 'a')

for x in range(0, 100):
    response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'query',
                'format': 'json',
                'generator': 'random',
                'grnnamespace': 0,
                'prop': 'extracts',
                'exintro': True,
                'explaintext': True,
            }
    ).json()
    try: 
        page = next(iter(response['query']['pages'].values()))

        print(page['extract'])

        data.write(page['extract'])
        data.write(" ")
    except Exception:
        pass

data.close()

