#Install flask , install neede depdencies for huggin face  + create an enviroment(). 
from flask import Flask, render_template, request
from transformers import pipeline

summarizer = pipeline("summarization")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    if request.method == 'POST':
        text = request.form['UserText']
        summary = summarizer(text, max_length=157, min_length=30, do_sample=False)
        summary = summary[0]['summary_text']
        print(summary)
        
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)

