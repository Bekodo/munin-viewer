from flask import Flask, render_template
import functions

app = Flask(__name__,static_url_path='/munin/viewer/static')

@app.route('/munin/viewer/')
@app.route('/munin/viewer/<service>')
def service(service="cpu2"):
    services = functions.getConf()
    template_data = {'services':services}
    chars = functions.getChars(service)
    template_data['service']=service
    template_data['chars']=chars
    return render_template('table.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005,debug=False)
