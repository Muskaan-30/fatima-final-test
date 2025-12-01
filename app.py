from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
  # REPLACE 'YourLastName' below with your actual last name
  return 'Welcome to Fatima Final Test API Server' 
  
@app.route('/host')
def host_name():
  return hostname

@app.route('/ip')
def host_ip():
  return ip_address

if __name__ == '__main__':
    # Running on 0.0.0.0 is required for container access
    app.run(host='0.0.0.0', port=5000)