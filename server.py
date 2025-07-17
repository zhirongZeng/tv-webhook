# server.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("收到 TradingView 訊號：", data)
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(port=5000)
