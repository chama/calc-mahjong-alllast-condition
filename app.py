from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='calc', message='オーラスの条件計算をします。')

@app.route('/', methods=['POST'])
def form():
    m_point = request.form.get('my_point')
    e_point = request.form.get('en_point')
    kyoutaku = request.form.get('kyoutaku')
    honba = request.form.get('honba')
    tumibou = request.form.get('tumibou')
    return render_template('index.html', title='calc', message=[m_point, e_point, kyoutaku, honba, tumibou])



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)