import { myPlayers } from "@/utils/myPlayers";
import axios from "axios";
import { ref } from "vue";
import { projectedRecord } from "./modelFetch";

export const savedTeams = ref([{email: "", username: "", teamName: "", date: "", record: "", players: []}]);

export const saveTeam = async (teamName: string) => {
    const name = localStorage.getItem('username');
    const email = localStorage.getItem('email');
    const currentDate = new Date();
    const month = String(currentDate.getMonth() + 1).padStart(2, '0'); // Months are zero-based, so we add 1 and pad with leading zeros if necessary.
    const day = String(currentDate.getDate()).padStart(2, '0'); // Pad the day with leading zeros if necessary.
    const year = String(currentDate.getFullYear());
    const formattedDate = `${month}/${day}/${year}`;
    const post = await axios.post('http://localhost:5001/saveTeam', 
        { 
            email: email, 
            username: name, 
            teamName: teamName,
            date: formattedDate,
            record: projectedRecord.value, 
            team: myPlayers.value 
        });
}

export const setSavedTeams = async () => {
    const userEmail = localStorage.getItem('email');
    const post = await axios.post('http://localhost:5001/getSavedTeams', {userEmail: userEmail});
    savedTeams.value = post.data;
}

export const deleteTeam = async (teamName: string) => {
    const userEmail = localStorage.getItem('email');
    const post = await axios.post('http://localhost:5001/deleteSavedTeam', 
        {userEmail: userEmail, teamName: teamName});
    setSavedTeams();
}