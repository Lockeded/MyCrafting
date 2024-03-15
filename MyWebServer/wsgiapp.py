def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type','text/html')]
    start_response(status, headers)
    return [b"<h1>Hello, web!</h1>"]