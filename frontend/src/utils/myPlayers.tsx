import { getTeamModelRecord } from '@/services/modelFetch';
import { ref } from 'vue';

export const myPlayers = ref([
    { pos: 'QB', name: '', team: '', stats: [0] },
    { pos: 'RB', name: '', team: '', stats: [0] },
    { pos: 'WR1', name: '', team: '', stats: [0] },
    { pos: 'WR2', name: '', team: '', stats: [0] },
    { pos: 'WR3', name: '', team: '', stats: [0] },
    { pos: 'TE', name: '', team: '', stats: [0] },
    { pos: 'OL', name: '', team: '', stats: [0] },
    { pos: 'DEF', name: '', team: '', stats: [0] },
]);

export const myPlayersFull = ref([
    { pos: 'QB', name: 'Tom Brady', team: 'Tampa Bay Buccaneers' },
    { pos: 'RB', name: 'Derrick Henry', team: 'Tennessee Titans' },
    { pos: 'WR1', name: 'DeAndre Hopkins', team: 'Arizona Cardinals' },
    { pos: 'WR2', name: 'Stefon Diggs', team: 'Buffalo Bills' },
    { pos: 'WR3', name: 'Tyreek Hill', team: 'Kansas City Chiefs' },
    { pos: 'TE', name: 'Travis Kelce', team: 'Kansas City Chiefs' },
    { pos: 'OL', name: 'Detroit Lions', team: 'Detroit Lions' },
    { pos: 'DEF', name: 'Chicago Bears', team: 'Chicago Bears' },
]);
  
export const playersFilled = ref(false);

export function emptyMyPlayers() {
    myPlayers.value.forEach((player) => {
        player.name = '';
        player.team = '';
        player.stats = [0];
    });
}

export function setPlayer(pos: string, name: string, team: string, stats: number[]) {
    const player = myPlayers.value.find((p) => p.pos === pos);
    if (player) {
        player.name = name;
        player.team = team;
        player.stats = stats;
    }
    checkIfTeamFilled();
}

const checkIfTeamFilled = () => {
    const filled = myPlayers.value.every(player => player.name !== '' && player.team !== '');
    if (filled){
        playersFilled.value = filled;
        const allStats: number[] = myPlayers.value.reduce((acc: number[], player: any) => {
            return acc.concat(player.stats);
        }, []);
        getTeamModelRecord(allStats);
    }
}