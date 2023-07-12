import axios from "axios";
import { ref } from "vue";
import { sendScore } from "./roomHandler";

export const projectedRecord = ref("");
export const totalScore = ref(0);

export const getTeamModelRecord = async (stats: number[]) => {
    const post = await axios.post('http://localhost:5001/gradeTeam', {stats: stats});
    const wins = post.data;
    const losses = 17 - wins;
    projectedRecord.value = wins + "-" + losses;
}

export const getTeamTotalScore = async (stats: number[]) => {
    const post = await axios.post('http://localhost:5001/gradeTeamMP', {stats: stats});
    const score = post.data;
    totalScore.value = score;
    sendScore(score);
}