from webapp import create_app

app = create_app()

if __name__ ==  '__main__':
    #app.run(host='192.168.1.2', port=5000, debug=True, threaded=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True)

