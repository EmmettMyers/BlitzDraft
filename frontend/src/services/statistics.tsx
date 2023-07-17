import axios from "axios";
import { ref } from "vue";

export const pickNumber = ref(0);

export const avgRecord = ref("");
export const highRecord = ref("");
export const lowRecord = ref("");
export const avgRank = ref("");
export const mostDraftedPlayers = ref("");
export const mostRolledTeams = ref("");
export const leastRolledTeams = ref("");

export const postDraftPick = async (player: any, team: string) => {
    pickNumber.value += 1;
    const email = localStorage.getItem('email');
    const post = await axios.post('http://localhost:5001/statDraftPick', 
        { 
            email: email,
            name: player.name,
            position: player.pos,
            team: team,
            pickNumber: pickNumber.value
        });
}

export const postRank = async (rank: number) => {
    const email = localStorage.getItem('email');
    const post = await axios.post('http://localhost:5001/statRank', 
        { 
            email: email,
            rank: rank
        });
}

export const postRecord = async (wins: number) => {
    const email = localStorage.getItem('email');
    const post = await axios.post('http://localhost:5001/statRecord', 
        { 
            email: email,
            wins: wins
        });
}