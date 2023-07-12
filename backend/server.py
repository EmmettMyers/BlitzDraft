import random
import secrets
import string
from flask import Flask, request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS
from players import *
from model import *
from rooms import *

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
def connectedSocket():
    print("client has connected")

@socketio.on('createRoom')
def createRoomSocket(data):
    room_id = ''.join(random.choices(string.ascii_uppercase, k=6))
    user_name = str(data[0])
    user_email = str(data[1])
    playingUsers.append([room_id, user_name, user_email, {}, {}, {}, {}, {}, {}, {}, {}])
    roomPlayers = []
    for player in playingUsers:
        if player[0] == room_id:
            roomPlayers.append([player[1], player[2]])
    print("user created room: ", user_email)
    print(playingUsers)
    emit("createRoom", { 'roomId': room_id, 'roomPlayers': roomPlayers }, broadcast = True)

@socketio.on('joinRoom')
def joinRoomSocket(data):
    room_id = str(data[0])
    roomReal = False
    for user in playingUsers:
        if user[0] == room_id:
            roomReal = True
            break
    if roomReal:
        user_name = str(data[1])
        user_email = str(data[2])
        playingUsers.append([room_id, user_name, user_email, {}, {}, {}, {}, {}, {}, {}, {}])
        roomPlayers = []
        for player in playingUsers:
            if player[0] == room_id:
                roomPlayers.append({'name': player[1], 'email': player[2]})
        print("user joined room: ", user_email)
        print(playingUsers)
        emit("joinedRoom", { 'roomId': room_id, 'roomPlayers': roomPlayers }, broadcast = True)
    else:
        emit("invalidRoom", broadcast = True)

@socketio.on('leaveRoom')
def leaveRoomSocket(data):
    user_email = str(data)
    for user in playingUsers:
        if user[2] == user_email:
            playingUsers.remove(user)
            print("user left room: ", user_email)
    print(playingUsers)

@socketio.on("disconnect")
def disconnectedSocket():
    print("user disconnected")

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5001)