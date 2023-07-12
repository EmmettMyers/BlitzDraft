import axios from "axios";
import { ref } from "vue";
import socket from "./socket";

export const scoresReady = ref(false);
export const startMPGame = ref(false);
export const room = ref("");
export const roomError = ref(false);
export const roomPlayers = ref([{name: "", email: ""}]);

socket.connect();

export const sendScore = async (score: number) => {
    socket.emit('sendScore', [room.value, "emmettleemyers@gmail.com", score]);
}

export const startGame = async () => {
    socket.emit('startGame', room.value);
}

export const createRoom = async () => {
    socket.emit('createRoom', ["Emmett Myers", "emmettleemyers@gmail.com"]);
}

export const joinRoom = async (roomCode: string) => {
    socket.emit('joinRoom', [roomCode, "Emmett Myers", "emmettleemyers@gmail.com"]);
}

export const leaveRoom = async () => {
    socket.emit('leaveRoom', [room.value, "emmettleemyers@gmail.com"]);
    room.value = "";
    roomPlayers.value = [];
}

socket.on('startGame', (data: any) => {
    const roomId = data;
    if (room.value == roomId){
        startMPGame.value = true;
    }
});

socket.on('createRoom', (data: any) => {
    room.value = data.roomId;
    const allPlayers: any = [];
    for (const player of data.roomPlayers){
        allPlayers.push({name: player[0], email: player[1]});
    }
    roomPlayers.value = allPlayers;
});

socket.on('invalidRoom', () => {
    roomError.value = true;
});

socket.on('joinedRoom', (data: any) => {
    room.value = data.roomId;
    const allPlayers: any = [];
    for (const player of data.roomPlayers){
        allPlayers.push({name: player.name, email: player.email});
    }
    roomPlayers.value = allPlayers;
    roomError.value = false;
});

socket.on('leftRoom', (data: any) => {
    const allPlayers: any = [];
    for (const player of data){
        allPlayers.push({name: player.name, email: player.email});
    }
    roomPlayers.value = allPlayers;
});

socket.on('allScoresSent', () => {
    alert("all scored")
    scoresReady.value = true;
});