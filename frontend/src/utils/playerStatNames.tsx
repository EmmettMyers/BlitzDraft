type Stats = {
    [key: string]: {
        stats: string[];
    };
};
  
export const statNames: Stats = {
    QB: {
        stats: ["Comp%", "Pass Yds", "Pass TD", "Int"],
    },
    RB: {
        stats: ["Rush Yds", "Rush TD", "Yds/rush", "Fumbles"],
    },
    WR1: {
        stats: ["Ctch%", "Rec Yds", "Rec TD"],
    },
    WR2: {
        stats: ["Ctch%", "Rec Yds", "Rec TD"],
    },
    WR3: {
        stats: ["Ctch%", "Rec Yds", "Rec TD"],
    },
    TE: {
        stats: ["Ctch%", "Rec Yds", "Rec TD"],
    },
    OL: {
        stats: ["QB Sacks", "Sacks/g", "Yds/rush"],
    },
    DEF: {
        stats: ["Sacks", "Points", "Yds/play", "Turnover%"],
    },
};
