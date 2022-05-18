from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():     #index関数の定義
    return render_template("index.html")   #index.htmlファイルを読み込む

if __name__ == '__main__':
    app.run(debug=True)   #デバッグモードOn
