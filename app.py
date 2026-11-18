from flask import Flask, request
from my_analyzer import analyze_csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    html = '''
    <h1>Анализатор оптовых продаж FMCG</h1>
    <form method="post" enctype="multipart/form-data">
        <p>Загрузите выгрузку продаж (CSV):</p>
        <input type="file" name="file" accept=".csv" required>
        <button type="submit">Анализировать</button>
    </form>
    '''
    
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file:
            content = uploaded_file.read().decode('cp1251').splitlines()
            result = analyze_csv(content)
            
            html += f"<hr><h2>Итого выручка: {result['total_revenue']:.2f} руб.</h2>"
            html += f"<p>Средняя выручка на клиента: {result['average_revenue']:.2f} руб.</p><ul>"
            
            for client, total in result['clients'].items():
                badge = ' <b>[VIP]</b>' if total > 30000 else ''
                html += f"<li>{client}: {total:.2f} руб.{badge}</li>"
            html += "</ul>"
            
    return html

# ЗДЕСЬ НАПИШИ СВОЙ МАРШРУТ @app.route('/about') САМ!
@app.route('/about')
def about():
    return '<h1>О сервисе</h1><p>Анализатор оптовых продаж FMCG.</p>'
    
if __name__ == '__main__':
    app.run(debug=True)
 