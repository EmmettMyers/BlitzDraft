import { Player } from "@/types/types";
import axios from "axios";

export const postSelectedPlayer = async (player: Player, team: string) => {
    const post = await axios.post('http://localhost:5001/selectPlayer', {player: player, team: team});
    const data = post.data;
}