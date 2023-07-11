import { Player } from "@/types/types";
import axios from "axios";
import { ref } from "vue";

export const projectedRecord = ref("");

export const postSelectedPlayer = async (player: Player, team: string) => {
    const post = await axios.post('http://localhost:5001/selectPlayer', {player: player, team: team});
    const data = post.data;
}

export const getTeamModelRecord = async (stats: number[]) => {
    const post = await axios.post('http://localhost:5001/gradeTeam', {stats: stats});
    const wins = post.data;
    const losses = 17 - wins;
    projectedRecord.value = wins + "-" + losses;
}