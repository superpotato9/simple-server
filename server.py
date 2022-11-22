from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import random
print("simple server")
print('version 1.0')
def random_out(x):
    return random.randint(1,10)
files = {
'/':['index.html', 'text/html', 'f'], #f == text file, c == code eg function i == img 
'/random':[random_out, 'text/html', 'c'],
'/image.jpeg':['image.jpeg', 'image/jpeg', 'i'],
'/style.css':['style.css', 'text/css', 'f']
}# format url name: filename

hostName = "localhost"  
serverPort = 1900

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            file_list = files[self.path]
            if file_list[2] == 'f':
                with open(file_list[0],  'r') as file:
                    data = file.read()
                    self.send_response(200)
                    self.send_header("Content-type", file_list[1])
                    self.end_headers()
                    self.wfile.write(bytes(data, "utf-8"))
            

            if file_list[2] == 'i':
                with open(file_list[0],  'rb') as file:
                    data = file.read()
                    self.send_response(200)
                    self.send_header("Content-type", file_list[1])
                    self.end_headers()
                    self.wfile.write(data)
            elif file_list[2] == 'c':
                self.send_response(200)
                self.send_header("Content-type", file_list[1])
                self.end_headers()
                self.wfile.write(bytes(str(file_list[0](self.path)), "utf-8"))
                
                
        except KeyError:
            print('404 accessing ', self.path)
            self.send_response(404)
            self.send_header("Content-type", 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<h1> error 404 </h1> <p> the server couldn't find what you were looking for</p>", "utf-8"))
            

            
            
