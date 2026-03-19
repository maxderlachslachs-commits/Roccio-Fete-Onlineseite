import http.server
import socketserver

PORT = 4040

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server läuft:")
    print(f"http://localhost:{PORT}")
    httpd.serve_forever()
