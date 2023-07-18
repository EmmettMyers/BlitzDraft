import axios from "axios";
import { ref } from "vue";

export const pickNumber = ref(0);

export const avgRecord = ref("N/A");
export const highRecord = ref("N/A");
export const lowRecord = ref("N/A");
export const avgRank = ref("N/A");
export const mostDraftedPlayers = ref("");
export const mostRolledTeams = ref("");
export const leastRolledTeams = ref("");
export const positionADP = ref([]);
export const allRecords = ref([]);
export const allRanks = ref([]);

export const getStats = async () => {
    const email = localStorage.getItem('email');
    const post = await axios.post('http://localhost:5001/getStats', { email: email });
    const stats = post.data;
    if (stats.avgRec != 0)
        avgRecord.value = stats.avgRec;
    if (stats.highRec != 0)
        highRecord.value = stats.highRec;
    if (stats.lowRec != 17)
        lowRecord.value = stats.lowRec;
    if (stats.avgRank != 0)
        avgRank.value = "#" + stats.avgRank;
    mostDraftedPlayers.value = stats.highPlayers;
    mostRolledTeams.value = stats.highTeams;
    leastRolledTeams.value = stats.lowTeams;
    positionADP.value = stats.posADP;
    allRecords.value = stats.allRecords;
    allRanks.value = stats.allRanks;
}

export const postDraftPick = async (player: any, team: string) => {
    if (player.pos == "OL"){
        player.name = player.name.trim().split(' ').pop().concat(" OL");
    } else if (player.pos == "DEF"){
        player.name = player.name.trim().split(' ').pop().concat(" DEF");
    }
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