import axios from "axios";
import { ref } from "vue";
import socket from "./socket";

export const room = ref("");
export const roomError = ref(false);
export const roomPlayers = ref([{name: "", email: ""}]);

socket.connect();

export const createRoom = async () => {
    socket.emit('createRoom', ["Emmett Myers", "emmettleemyers@gmail.com"]);
}

export const joinRoom = async (roomCode: string) => {
    socket.emit('joinRoom', [roomCode, "Emmett Myers", "emmettleemyers@gmail.com"]);
}

export const leaveRoom = async () => {
    socket.emit('leaveRoom', "emmettleemyers@gmail.com");
    room.value = "";
    roomPlayers.value = [];
}

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
    roomPlayers.value = data.roomPlayers;
    roomError.value = false;
});