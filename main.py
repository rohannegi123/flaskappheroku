from flask import Flask

app= Flask(__name__)
@app.route('/', methods = ['Get', 'Post'])
def wow():
    return "<h1>Abhijeet future tiktoker</h1>"

if __name__ == "__main__":
    app.run()
