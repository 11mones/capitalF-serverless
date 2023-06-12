from http.server import BaseHTTPRequestHandler
from urllib import parse
import urllib.request
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        list_of_def = []
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_list = parse.parse_qsl(url_components.query)
        my_dict = dict(query_list)

        if 'country' in my_dict:
            country = my_dict.get('country')
            country_url = f"https://restcountries.com/v3.1/name/{country}"

            response = urllib.request.urlopen(country_url)
            data = json.loads(response.read())

            for element in data:
                d = element['capital'][0]
                message = "The capital of {} is {}".format(country, d)
                list_of_def.append(message)

        if 'capital' in my_dict:
            capital = my_dict.get('capital')
            capital_url = f"https://restcountries.com/v3.1/capital/{capital}"

            response = urllib.request.urlopen(capital_url)
            data = json.loads(response.read())

            for element in data:
                country = element['name']['common']
                message = "{} is the capital of {}".format(capital, country)
                list_of_def.append(message)

        message = '\n'.join(list_of_def)
        self.wfile.write(message.encode())
        return
