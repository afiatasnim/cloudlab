from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a = []
    
    for e in range(1, 101):
        if e % 2 == 0:
            a.append(e)
    
    return str(a)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
