from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def render_static(name=None):
	return render_template('index.html',name=name)
if __name__ == '__main__':
	app.run(host = '0.0.0.0',port=5005, debug=True)
                                      