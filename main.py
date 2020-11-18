from flask import Flask, render_template
import functions
import sys

app = Flask(__name__,static_url_path='/munin/viewer/static')

@app.route('/munin/viewer/')
@app.route('/munin/viewer/<service>')
def service(service="cpu2"):
    services = functions.getConf('services')
    chars = functions.getChars(services,service)
    template_data = {'services':services}
    template_data['service']=service
    template_data['chars']=chars
    if service == 'extra':
        return render_template('table_extra.html', **template_data)
    else:
        return render_template('table.html', **template_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005,debug=False)
