from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Анализатор оптовых продаж FMCG</h1><p>Веб-сервер успешно запущен!</p>'

if __name__ == '__main__':
    app.run(debug=True)
