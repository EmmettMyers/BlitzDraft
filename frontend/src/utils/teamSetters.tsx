import { teamColors } from "@/styles/team_colors";
import { teamNames } from "./teamNames";

export const setColor = (type: string, team: string): string => {
    if (team == ''){
        return "#414141"
    }
    const fullTeam: string[] = team.split(' ');
    let mascot = "";
    if (team == "San Francisco 49ers"){
        mascot = "fortyniners";
    } else {
        mascot = fullTeam[fullTeam.length - 1].toLowerCase();
    }
    if (type == "primary"){
        return teamColors[mascot].primaryColor;
    } else if (type == "secondary"){
        return teamColors[mascot].secondaryColor;
    } else {
        return teamColors[mascot].uniqueColor;
    }
}

export const setImage = (team: string): string => {
    const abbreviation = teamNames[team];
    return `https://static.www.nfl.com/t_person_squared_mobile_2x/f_auto/league/api/clubs/logos/${abbreviation}`
}