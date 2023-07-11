import secrets
from flask import Flask, request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS
from players import *
from model import *

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route("/getPlayers", methods=['POST'])
def getPlayersRoute():
    team = request.json['team']
    return jsonify(getPlayersByTeam(team))

@app.route("/gradeTeam", methods=['POST'])
def gradeTeamRoute():
    stats = request.json['stats']
    return jsonify(gradeTeam(stats, 100))

@socketio.on("connect")
def connected():
    print("client has connected")

@socketio.on('data')
def handle_message(data):
    print("data: ", str(data))
    players.append(data['team'])
    emit("data", { 'team': players }, broadcast = True)

@socketio.on("disconnect")
def disconnected():
    print("user disconnected")

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5001)