from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    for i in range(3,99,3):
        return(i)
        if i==69:
            return('nice')
    return 'Hello world'