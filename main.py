from flask import Flask, render_template
import functions

app = Flask(__name__)

@app.route('/viewer/')
@app.route('/viewer/<service>')
def service(service="cpu"):
    chars = functions.getChars(service)
    return render_template('table.html', chars=chars, service=service)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
