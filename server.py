import http.server
import socketserver
import json
import os
import urllib.parse

PORT = 3000
ROOT = os.path.dirname(os.path.abspath(__file__))
CUSTOM_WORDS_FILE = os.path.join(ROOT, "custom-words.json")

if not os.path.exists(CUSTOM_WORDS_FILE):
    with open(CUSTOM_WORDS_FILE, "w", encoding="utf-8") as f:
        f.write("[]")

def read_custom_words():
    try:
        with open(CUSTOM_WORDS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def write_custom_words(words):
    with open(CUSTOM_WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, indent=2)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == "/api/custom-words":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(read_custom_words()).encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == "/api/add-word":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode("utf-8"))
                nari = data.get("nari", "").strip().lower()
                english = data.get("english", "").strip().lower()
                category = data.get("category", "Custom").strip()
                if not category:
                    category = "Custom"
                
                if not nari or not english:
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "nari and english are required"}).encode("utf-8"))
                    return

                words = read_custom_words()
                words = [w for w in words if w.get("english", "").lower() != english]
                words.append({"english": english, "nari": nari, "category": category, "custom": True})
                write_custom_words(words)
                
                print(f"[add-word] {nari} = {english} ({category})")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True, "word": {"nari": nari, "english": english, "category": category}}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == "/api/remove-word":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode("utf-8"))
                english = data.get("english", "").strip()
                
                words = read_custom_words()
                words = [w for w in words if w.get("english", "").lower() != english.lower()]
                write_custom_words(words)
                
                print(f"[remove-word] {english}")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": True}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Nari running at http://localhost:{PORT}")
    httpd.serve_forever()
