from http.server import BaseHTTPRequestHandler
import requests 
from urllib import parse
 

    
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    list_of_dif=[]
    message="testing"
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)
    

   




    self.wfile.write(message.encode())
    return