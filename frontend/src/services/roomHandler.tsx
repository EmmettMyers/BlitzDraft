import axios from "axios";
import { ref } from "vue";
import socket from "./socket";
import { myPlayers } from "@/utils/myPlayers";

export const scoresReady = ref(false);
export const startMPGame = ref(false);
export const room = ref("");
export const roomError = ref(false);
export const roomPlayers = ref([{name: "", email: ""}]);
export const myRank = ref(0);
export const roomTeamRankings = ref([]);

socket.connect();

export const sendScore = async (score: number) => {
    socket.emit('sendScore', [room.value, localStorage.getItem('email'), score, myPlayers]);
}

export const startGame = async () => {
    socket.emit('startGame', room.value);
}

export const createRoom = async () => {
    socket.emit('createRoom', [localStorage.getItem('username'), localStorage.getItem('email')]);
}

export const joinRoom = async (roomCode: string) => {
    socket.emit('joinRoom', [roomCode, localStorage.getItem('username'), localStorage.getItem('email')]);
}

export const leaveRoom = async () => {
    socket.emit('leaveRoom', [room.value, localStorage.getItem('email')]);
    room.value = "";
    roomPlayers.value = [];
}

socket.on('startGame', (data: any) => {
    roomTeamRankings.value = [];
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

socket.on('allScoresSent', (data: any) => {
    scoresReady.value = true;
    roomTeamRankings.value = data;
    myRank.value = data.findIndex((person: any[]) => person[1] === localStorage.getItem('username'));
});