from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    
    # List of Integers
    numbers = [10, 30, 44, 17,35,58,60,88]
 
    #Sorting list of Integers
    numbers.sort(reverse=True)
    return "Third largest number :"+ str(numbers[1])


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)