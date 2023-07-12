import axios from "axios";
import { ref } from "vue";

export const projectedRecord = ref("");

export const getTeamModelRecord = async (stats: number[]) => {
    const post = await axios.post('http://localhost:5001/gradeTeam', {stats: stats});
    const wins = post.data;
    const losses = 17 - wins;
    projectedRecord.value = wins + "-" + losses;
}