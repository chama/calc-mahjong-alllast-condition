from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', titile='calc')




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)