from flask import Flask, render_template
import functions

app = Flask(__name__,static_url_path='/munin/viewer/static')

@app.route('/munin/viewer/')
@app.route('/munin/viewer/<service>')
def service(service="cpu"):
    chars = functions.getChars(service)
    return render_template('table.html', chars=chars, service=service)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)
