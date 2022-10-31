from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def show_about():
    return render_template('about.html', )

@app.route('/education')
def show_edu():
    return render_template('edu.html')

@app.route('/language')
def show_language():
    return render_template('language.html')

@app.route('/other')
def show_other():
    return render_template('other.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
