import { ref } from 'vue';

export const myPlayers = ref([
    { pos: 'QB', name: '', team: '' },
    { pos: 'RB', name: '', team: '' },
    { pos: 'WR1', name: '', team: '' },
    { pos: 'WR2', name: '', team: '' },
    { pos: 'WR3', name: '', team: '' },
    { pos: 'TE', name: '', team: '' },
    { pos: 'OL', name: '', team: '' },
    { pos: 'DEF', name: '', team: '' },
]);

export function setPlayer(pos: string, name: string, team: string) {
    const player = myPlayers.value.find((p) => p.pos === pos);
    if (player) {
        player.name = name;
        player.team = team;
    }
}