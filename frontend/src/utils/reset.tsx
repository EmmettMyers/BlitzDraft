import { projectedRecord, totalScore } from "@/services/modelFetch";
import { emptyMyPlayers, playersFilled } from "./myPlayers";
import { myRank, roomTeamRankings, scoresReady } from "@/services/roomHandler";
import { pickNumber } from "@/services/statistics";

export const resetMetrics = (): void => {
    emptyMyPlayers();
    playersFilled.value = false;
    projectedRecord.value = "";
    totalScore.value = 0;
    myRank.value = 0;
    scoresReady.value = false;
    roomTeamRankings.value = [];
    pickNumber.value = 0;
}