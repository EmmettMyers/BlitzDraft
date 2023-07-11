import { Player } from "@/types/types";
import axios from "axios";

export let teamPlayerData: Player[];

export const fetchTeamPlayerData = async (finalTeam: string) => {
    const fetch = await axios.post('http://localhost:5001/getPlayers', {team: finalTeam});
    const data = fetch.data;
    const qb: Player = {pos: "QB", name: data.qb[0], stats: data.qb.slice(2, 6), image: data.qb[6]};
    const rb: Player = {pos: "RB", name: data.rb[0], stats: data.rb.slice(1, 5), image: data.rb[5]};
    const wr1: Player = {pos: "WR1", name: data.wr1[0], stats: data.wr1.slice(1, 4), image: data.wr1[4]};
    const wr2: Player = {pos: "WR2", name: data.wr2[0], stats: data.wr2.slice(1, 4), image: data.wr2[4]};
    const wr3: Player = {pos: "WR3", name: data.wr3[0], stats: data.wr3.slice(1, 4), image: data.wr3[4]};
    const te: Player = {pos: "TE", name: data.te[0], stats: data.te.slice(1, 4), image: data.te[4]};
    const ol: Player = {pos: "OL", name: finalTeam, stats: data.ol.slice(1)};
    const def: Player = {pos: "DEF", name: finalTeam, stats: data.def.slice(1, 5)};
    teamPlayerData = [qb, rb, wr1, wr2, wr3, te, ol, def];
}

