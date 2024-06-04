'''
1. Install flask in your terminal - > (pip install Flask), 
then install neede depdencies for huggin face + create an enviroment. Follow the instructions here - > https://huggingface.co/docs/transformers/en/installation
# 2. import the needed libraries 
'''
from flask import Flask, render_template, request
from transformers import pipeline

#3. Download the pipeline 
summarizer = pipeline("summarization")

#4. Initialize the application 
app = Flask(__name__)


#4. This is the decorator that bind the function index to the user view
'''
+ In other words it speciies the URL adress as '/', and HTTP methods that would be allowed to use while accesing URL
+ we use GET to retrive data from the server , POST - to sumbit data to the server through the HTML form 
+

'''
@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    
    #5. if user submit the button 
    if request.method == 'POST':
        
        #6. then retrieves and store the value, in our case the user text from the form 
        text = request.form['UserText']
        
        #7. summarize the user text with the help of Huggin Face model,  save the summarized text 
        summary = summarizer(text, max_length=157, min_length=30, do_sample=False)
        
        #8.  model will output a result in a dictionary form, and we need to index the key 'summary_text' in order to get just a string with summary 
        summary = summary[0]['summary_text']
        print(summary)

    #9. finally flask renders the html template, and we pass our genereted summary to the HTML file, so it can display it to the user. 
    return render_template('index.html', summary=summary)

#10 Lastly we run the app 
if __name__ == '__main__':
    app.run(debug=True)

