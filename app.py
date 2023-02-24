from minimapi import Minimapi

api = Minimapi('model.json', 'pysondb', 'db/')

api.serve_static('static')

if __name__ == '__main__':
	api.app.run(debug=True, host='0.0.0.0', port=80)