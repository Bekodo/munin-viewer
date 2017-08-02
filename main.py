from flask import Flask, render_template
import functions

app = Flask(__name__)

@app.route('/cpu')
def cpu():
    chars = functions.getChars()
    return render_template('table.html', chars=chars)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)
