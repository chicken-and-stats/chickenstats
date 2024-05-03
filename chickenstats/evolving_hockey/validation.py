import pandera as pa
from pandera.typing import Index, Series
from typing import Optional


class PBPSchema(pa.DataFrameModel):
    index: Index[int] = pa.Field(coerce=True)
    season: Series[int] = pa.Field(coerce=True)
    session: Series[str] = pa.Field(coerce=True)
    game_id: Series[int] = pa.Field(coerce=True)
    game_date: Series[str] = pa.Field(coerce=True)
    event_index: Series[int] = pa.Field(coerce=True)
    game_period: Series[int] = pa.Field(coerce=True)
    game_seconds: Series[int] = pa.Field(coerce=True)
    period_seconds: Series[int] = pa.Field(coerce=True)
    clock_time: Series[str] = pa.Field(coerce=True)
    strength_state: Series[str] = pa.Field(coerce=True, nullable=True)
    score_state: Series[str] = pa.Field(coerce=True, nullable=True)
    event_type: Series[str] = pa.Field(coerce=True)
    event_description: Series[str] = pa.Field(coerce=True, nullable=True)
    event_detail: Series[str] = pa.Field(coerce=True, nullable=True)
    event_zone: Series[str] = pa.Field(coerce=True, nullable=True)
    event_team: Series[str] = pa.Field(coerce=True, nullable=True)
    opp_team: Series[str] = pa.Field(coerce=True, nullable=True)
    is_home: Series[float] = pa.Field(coerce=True, nullable=True)
    home_zone: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    home_team: Optional[Series[str]] = pa.Field(coerce=True)
    away_team: Optional[Series[str]] = pa.Field(coerce=True)
    home_goalie: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    away_goalie: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    home_skaters: Optional[Series[int]] = pa.Field(coerce=True)
    away_skaters: Optional[Series[int]] = pa.Field(coerce=True)
    home_score: Optional[Series[int]] = pa.Field(coerce=True)
    away_score: Optional[Series[int]] = pa.Field(coerce=True)
    home_zonestart: Optional[Series[float]] = pa.Field(coerce=True, nullable=True)
    face_index: Optional[Series[int]] = pa.Field(coerce=True)
    pen_index: Optional[Series[int]] = pa.Field(coerce=True)
    shift_index: Optional[Series[int]] = pa.Field(coerce=True)
    game_score_state: Optional[Series[str]] = pa.Field(coerce=True)
    game_strength_state: Optional[Series[str]] = pa.Field(coerce=True)
    coords_x: Series[float] = pa.Field(coerce=True, nullable=True)
    coords_y: Series[float] = pa.Field(coerce=True, nullable=True)
    event_player_1: Series[str] = pa.Field(coerce=True, nullable=True)
    event_player_1_id: Series[str] = pa.Field(coerce=True, nullable=True)
    event_player_1_pos: Series[str] = pa.Field(coerce=True, nullable=True)
    event_player_2: Series[str] = pa.Field(coerce=True, nullable=True)
    event_player_2_id: Series[str] = pa.Field(coerce=True, nullable=True)
    event_player_2_pos: Series[str] = pa.Field(coerce=True, nullable=True)
    event_player_3: Series[str] = pa.Field(coerce=True, nullable=True)
    event_player_3_id: Series[str] = pa.Field(coerce=True, nullable=True)
    event_player_3_pos: Series[str] = pa.Field(coerce=True, nullable=True)
    event_length: Series[int] = pa.Field(coerce=True)
    high_danger: Series[int] = pa.Field(coerce=True)
    danger: Series[int] = pa.Field(coerce=True)
    pbp_distance: Series[float] = pa.Field(coerce=True, nullable=True)
    event_distance: Series[float] = pa.Field(coerce=True, nullable=True)
    event_angle: Series[float] = pa.Field(coerce=True, nullable=True)
    opp_strength_state: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_score_state: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_f: Series[str] = pa.Field(coerce=True, nullable=True)
    event_on_f_id: Series[str] = pa.Field(coerce=True, nullable=True)
    event_on_d: Series[str] = pa.Field(coerce=True, nullable=True)
    event_on_d_id: Series[str] = pa.Field(coerce=True, nullable=True)
    event_on_g: Series[str] = pa.Field(coerce=True, nullable=True)
    event_on_g_id: Series[str] = pa.Field(coerce=True, nullable=True)
    event_on_1: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_1_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_1_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_2: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_2_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_2_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_3: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_3_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_3_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_4: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_4_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_4_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_5: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_5_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_5_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_6: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_6_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_6_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_7: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_7_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    event_on_7_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_f: Series[str] = pa.Field(coerce=True, nullable=True)
    opp_on_f_id: Series[str] = pa.Field(coerce=True, nullable=True)
    opp_on_d: Series[str] = pa.Field(coerce=True, nullable=True)
    opp_on_d_id: Series[str] = pa.Field(coerce=True, nullable=True)
    opp_on_g: Series[str] = pa.Field(coerce=True, nullable=True)
    opp_on_g_id: Series[str] = pa.Field(coerce=True, nullable=True)
    opp_on_1: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_1_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_1_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_2: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_2_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_2_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_3: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_3_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_3_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_4: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_4_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_4_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_5: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_5_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_5_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_6: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_6_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_6_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_7: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_7_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_on_7_pos: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    change: Series[int] = pa.Field(coerce=True)
    zone_start: Series[str] = pa.Field(coerce=True, nullable=True)
    num_on: Series[float] = pa.Field(coerce=True, nullable=True)
    num_off: Series[float] = pa.Field(coerce=True, nullable=True)
    players_on: Series[str] = pa.Field(coerce=True, nullable=True)
    players_on_id: Series[str] = pa.Field(coerce=True, nullable=True)
    players_on_pos: Series[str] = pa.Field(coerce=True, nullable=True)
    players_off: Series[str] = pa.Field(coerce=True, nullable=True)
    players_off_id: Series[str] = pa.Field(coerce=True, nullable=True)
    players_off_pos: Series[str] = pa.Field(coerce=True, nullable=True)
    shot: Series[int] = pa.Field(coerce=True)
    hd_shot: Series[int] = pa.Field(coerce=True)
    shot_adj: Series[float] = pa.Field(coerce=True)
    goal: Series[int] = pa.Field(coerce=True)
    hd_goal: Series[int] = pa.Field(coerce=True)
    goal_adj: Series[float] = pa.Field(coerce=True)
    pred_goal: Series[float] = pa.Field(coerce=True, nullable=True)
    pred_goal_adj: Series[float] = pa.Field(coerce=True, nullable=True)
    fenwick: Series[int] = pa.Field(coerce=True)
    hd_fenwick: Series[int] = pa.Field(coerce=True)
    fenwick_adj: Series[float] = pa.Field(coerce=True)
    corsi: Series[int] = pa.Field(coerce=True)
    corsi_adj: Series[float] = pa.Field(coerce=True)
    miss: Series[int] = pa.Field(coerce=True)
    hd_miss: Series[int] = pa.Field(coerce=True)
    block: Series[int] = pa.Field(coerce=True)
    fac: Series[int] = pa.Field(coerce=True)
    hit: Series[int] = pa.Field(coerce=True)
    give: Series[int] = pa.Field(coerce=True)
    take: Series[int] = pa.Field(coerce=True)
    pen0: Series[int] = pa.Field(coerce=True)
    pen2: Series[int] = pa.Field(coerce=True)
    pen4: Series[int] = pa.Field(coerce=True)
    pen5: Series[int] = pa.Field(coerce=True)
    pen10: Series[int] = pa.Field(coerce=True)
    stop: Series[int] = pa.Field(coerce=True)
    ozf: Series[int] = pa.Field(coerce=True)
    nzf: Series[int] = pa.Field(coerce=True)
    dzf: Series[int] = pa.Field(coerce=True)
    ozs: Series[int] = pa.Field(coerce=True)
    nzs: Series[int] = pa.Field(coerce=True)
    dzs: Series[int] = pa.Field(coerce=True)
    otf: Series[int] = pa.Field(coerce=True)


class StatSchema(pa.DataFrameModel):
    index: Index[int] = pa.Field(coerce=True)
    season: Series[int] = pa.Field(coerce=True)
    session: Series[str] = pa.Field(coerce=True)
    game_id: Optional[Series[int]] = pa.Field(coerce=True)
    game_date: Optional[Series[str]] = pa.Field(coerce=True)
    player: Series[str] = pa.Field(coerce=True, nullable=True)
    player_id: Series[str] = pa.Field(coerce=True, nullable=True)
    position: Series[str] = pa.Field(coerce=True, nullable=True)
    team: Series[str] = pa.Field(coerce=True, nullable=True)
    opp_team: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    strength_state: Series[str] = pa.Field(coerce=True, nullable=True)
    score_state: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    game_period: Optional[Series[int]] = pa.Field(coerce=True)
    forwards: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    forwards_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    defense: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    defense_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    own_goalie: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    own_goalie_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_forwards: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_forwards_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_defense: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_defense_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_goalie: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    opp_goalie_id: Optional[Series[str]] = pa.Field(coerce=True, nullable=True)
    toi: Series[float] = pa.Field(coerce=True)
    g: Series[int] = pa.Field(coerce=True)
    ihdg: Series[int] = pa.Field(coerce=True)
    a1: Series[int] = pa.Field(coerce=True)
    a2: Series[int] = pa.Field(coerce=True)
    isf: Series[int] = pa.Field(coerce=True)
    ihdsf: Series[int] = pa.Field(coerce=True)
    iff: Series[int] = pa.Field(coerce=True)
    ihdf: Series[int] = pa.Field(coerce=True)
    icf: Series[int] = pa.Field(coerce=True)
    ixg: Series[float] = pa.Field(coerce=True)
    imsf: Series[int] = pa.Field(coerce=True)
    ihdm: Series[int] = pa.Field(coerce=True)
    isb: Series[int] = pa.Field(coerce=True)
    ibs: Series[int] = pa.Field(coerce=True)
    igive: Series[int] = pa.Field(coerce=True)
    itake: Series[int] = pa.Field(coerce=True)
    ihf: Series[int] = pa.Field(coerce=True)
    iht: Series[int] = pa.Field(coerce=True)
    ifow: Series[int] = pa.Field(coerce=True)
    ifol: Series[int] = pa.Field(coerce=True)
    iozfw: Series[int] = pa.Field(coerce=True)
    iozfl: Series[int] = pa.Field(coerce=True)
    inzfw: Series[int] = pa.Field(coerce=True)
    inzfl: Series[int] = pa.Field(coerce=True)
    idzfw: Series[int] = pa.Field(coerce=True)
    idzfl: Series[int] = pa.Field(coerce=True)
    a1_xg: Series[float] = pa.Field(coerce=True)
    a2_xg: Series[float] = pa.Field(coerce=True)
    ipent0: Series[int] = pa.Field(coerce=True)
    ipent2: Series[int] = pa.Field(coerce=True)
    ipent4: Series[int] = pa.Field(coerce=True)
    ipent5: Series[int] = pa.Field(coerce=True)
    ipent10: Series[int] = pa.Field(coerce=True)
    ipend0: Series[int] = pa.Field(coerce=True)
    ipend2: Series[int] = pa.Field(coerce=True)
    ipend4: Series[int] = pa.Field(coerce=True)
    ipend5: Series[int] = pa.Field(coerce=True)
    ipend10: Series[int] = pa.Field(coerce=True)
    ozs: Series[int] = pa.Field(coerce=True)
    nzs: Series[int] = pa.Field(coerce=True)
    dzs: Series[int] = pa.Field(coerce=True)
    otf: Series[int] = pa.Field(coerce=True)
    gf: Series[int] = pa.Field(coerce=True)
    gf_adj: Series[float] = pa.Field(coerce=True)
    hdgf: Series[int] = pa.Field(coerce=True)
    ga: Series[int] = pa.Field(coerce=True)
    ga_adj: Series[float] = pa.Field(coerce=True)
    hdga: Series[int] = pa.Field(coerce=True)
    xgf: Series[float] = pa.Field(coerce=True)
    xgf_adj: Series[float] = pa.Field(coerce=True)
    xga: Series[float] = pa.Field(coerce=True)
    xga_adj: Series[float] = pa.Field(coerce=True)
    sf: Series[int] = pa.Field(coerce=True)
    sf_adj: Series[float] = pa.Field(coerce=True)
    hdsf: Series[int] = pa.Field(coerce=True)
    sa: Series[int] = pa.Field(coerce=True)
    sa_adj: Series[float] = pa.Field(coerce=True)
    hdsa: Series[int] = pa.Field(coerce=True)
    ff: Series[int] = pa.Field(coerce=True)
    ff_adj: Series[float] = pa.Field(coerce=True)
    hdff: Series[int] = pa.Field(coerce=True)
    fa: Series[int] = pa.Field(coerce=True)
    fa_adj: Series[float] = pa.Field(coerce=True)
    hdfa: Series[int] = pa.Field(coerce=True)
    cf: Series[int] = pa.Field(coerce=True)
    cf_adj: Series[float] = pa.Field(coerce=True)
    ca: Series[int] = pa.Field(coerce=True)
    ca_adj: Series[float] = pa.Field(coerce=True)
    bsf: Series[int] = pa.Field(coerce=True)
    bsa: Series[int] = pa.Field(coerce=True)
    msf: Series[int] = pa.Field(coerce=True)
    hdmsf: Series[int] = pa.Field(coerce=True)
    msa: Series[int] = pa.Field(coerce=True)
    hdmsa: Series[int] = pa.Field(coerce=True)
    hf: Series[int] = pa.Field(coerce=True)
    ht: Series[int] = pa.Field(coerce=True)
    ozf: Series[int] = pa.Field(coerce=True)
    nzf: Series[int] = pa.Field(coerce=True)
    dzf: Series[int] = pa.Field(coerce=True)
    fow: Series[int] = pa.Field(coerce=True)
    fol: Series[int] = pa.Field(coerce=True)
    ozfw: Series[int] = pa.Field(coerce=True)
    ozfl: Series[int] = pa.Field(coerce=True)
    nzfw: Series[int] = pa.Field(coerce=True)
    nzfl: Series[int] = pa.Field(coerce=True)
    dzfw: Series[int] = pa.Field(coerce=True)
    dzfl: Series[int] = pa.Field(coerce=True)
    pent0: Series[int] = pa.Field(coerce=True)
    pent2: Series[int] = pa.Field(coerce=True)
    pent4: Series[int] = pa.Field(coerce=True)
    pent5: Series[int] = pa.Field(coerce=True)
    pent10: Series[int] = pa.Field(coerce=True)
    pend0: Series[int] = pa.Field(coerce=True)
    pend2: Series[int] = pa.Field(coerce=True)
    pend4: Series[int] = pa.Field(coerce=True)
    pend5: Series[int] = pa.Field(coerce=True)
    pend10: Series[int] = pa.Field(coerce=True)
