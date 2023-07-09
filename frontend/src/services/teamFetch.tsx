import axios from "axios";

export let teamPlayerData = [{pos: "", name: "", stats: ""}];

export const fetchTeamPlayerData = async (finalTeam: string) => {
    const fetch = await axios.post('http://localhost:5001/getPlayers', {team: finalTeam});
    const data = fetch.data;
    const qb = {pos: "QB", name: data.qb[0], stats: data.qb.slice(3, 6), image: data.qb[6]};
    const rb = {pos: "RB", name: data.rb[0], stats: data.rb.slice(1, 4), image: data.rb[5]};
    const wr1 = {pos: "WR1", name: data.wr1[0], stats: data.wr1.slice(1, 4), image: data.wr1[4]};
    const wr2 = {pos: "WR2", name: data.wr2[0], stats: data.wr2.slice(1, 4), image: data.wr2[4]};
    const wr3 = {pos: "WR3", name: data.wr3[0], stats: data.wr3.slice(1, 4), image: data.wr3[4]};
    const te = {pos: "TE", name: data.te[0], stats: data.te.slice(1, 4), image: data.te[4]};
    const ol = {pos: "OL", name: finalTeam, stats: data.ol.slice(1)};
    const def = {pos: "DEF", name: finalTeam, stats: [data.def[1], data.def[3], data.def[4]]};
    teamPlayerData = [qb, rb, wr1, wr2, wr3, te, ol, def];
}

