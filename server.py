from flask import Flask, request, render_template

from chat import generate_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_result():
    query = request.form.get('query', '')
    
    if query:
        res = generate_text(text=query)
        
        return res, 200
    
    return 'Some error occured! Please try again.', 400

@app.route('/clear')
def clear_result():
    return 'Plug your new prompt here. Previous result has been cleared!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)