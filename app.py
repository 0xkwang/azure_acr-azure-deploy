from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>🚀 과제 3 성공: ACR을 통한 자동 배포 파이프라인이 개통되었습니다!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)