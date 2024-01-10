from flask import Flask, render_template, request
from text_summarization import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summmary, original_Text, len_of_Org_text, len_of_sum_text = summarizer(rawtext)

    return render_template('summary.html', summmary=summmary, original_Text=original_Text, len_of_Org_text=len_of_Org_text, len_of_sum_text=len_of_sum_text) 

if __name__ == "__main__":
    app.run(debug=True)