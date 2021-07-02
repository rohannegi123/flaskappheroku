from flask import Flask

app= Flask(__name__)
@app.route('/', methods = ['Get', 'Post'])
def wow():
    return "<h1>this is flask</h1>"

if __name__ == "__main__":
    app.run()
