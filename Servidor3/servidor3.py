from flask import Flask
servidor = Flask(__name__)
@servidor.route('/')

def hola():
    return "Hola desde el servidor 3"
    
if __name__ == '__main__':
    servidor.run(host='0.0.0.0')