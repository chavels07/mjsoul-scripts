import dhs_pb2 as _dhs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Text, Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionAnGangAddGang(_message.Message):
    __slots__ = ["doras", "operation", "seat", "tiles", "tingpais", "type", "zhenting"]
    DORAS_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILES_FIELD_NUMBER: ClassVar[int]
    TINGPAIS_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    operation: OptionalOperationList
    seat: int
    tiles: str
    tingpais: _containers.RepeatedCompositeFieldContainer[TingPaiInfo]
    type: int
    zhenting: bool
    def __init__(self, seat: Optional[int] = ..., type: Optional[int] = ..., tiles: Optional[str] = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ..., doras: Optional[Iterable[str]] = ..., zhenting: bool = ..., tingpais: Optional[Iterable[Union[TingPaiInfo, Mapping]]] = ...) -> None: ...

class ActionBaBei(_message.Message):
    __slots__ = ["doras", "moqie", "operation", "seat", "tingpais", "zhenting"]
    DORAS_FIELD_NUMBER: ClassVar[int]
    MOQIE_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TINGPAIS_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    moqie: bool
    operation: OptionalOperationList
    seat: int
    tingpais: _containers.RepeatedCompositeFieldContainer[TingPaiInfo]
    zhenting: bool
    def __init__(self, seat: Optional[int] = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ..., doras: Optional[Iterable[str]] = ..., zhenting: bool = ..., tingpais: Optional[Iterable[Union[TingPaiInfo, Mapping]]] = ..., moqie: bool = ...) -> None: ...

class ActionChiPengGang(_message.Message):
    __slots__ = ["froms", "liqi", "operation", "seat", "tiles", "tingpais", "type", "zhenting"]
    FROMS_FIELD_NUMBER: ClassVar[int]
    LIQI_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILES_FIELD_NUMBER: ClassVar[int]
    TINGPAIS_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    froms: _containers.RepeatedScalarFieldContainer[int]
    liqi: LiQiSuccess
    operation: OptionalOperationList
    seat: int
    tiles: _containers.RepeatedScalarFieldContainer[str]
    tingpais: _containers.RepeatedCompositeFieldContainer[TingPaiDiscardInfo]
    type: int
    zhenting: bool
    def __init__(self, seat: Optional[int] = ..., type: Optional[int] = ..., tiles: Optional[Iterable[str]] = ..., froms: Optional[Iterable[int]] = ..., liqi: Optional[Union[LiQiSuccess, Mapping]] = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ..., zhenting: bool = ..., tingpais: Optional[Iterable[Union[TingPaiDiscardInfo, Mapping]]] = ...) -> None: ...

class ActionDealTile(_message.Message):
    __slots__ = ["doras", "left_tile_count", "liqi", "operation", "seat", "tile", "tingpais", "zhenting"]
    DORAS_FIELD_NUMBER: ClassVar[int]
    LEFT_TILE_COUNT_FIELD_NUMBER: ClassVar[int]
    LIQI_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILE_FIELD_NUMBER: ClassVar[int]
    TINGPAIS_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    left_tile_count: int
    liqi: LiQiSuccess
    operation: OptionalOperationList
    seat: int
    tile: str
    tingpais: _containers.RepeatedCompositeFieldContainer[TingPaiDiscardInfo]
    zhenting: bool
    def __init__(self, seat: Optional[int] = ..., tile: Optional[str] = ..., left_tile_count: Optional[int] = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ..., liqi: Optional[Union[LiQiSuccess, Mapping]] = ..., doras: Optional[Iterable[str]] = ..., zhenting: bool = ..., tingpais: Optional[Iterable[Union[TingPaiDiscardInfo, Mapping]]] = ...) -> None: ...

class ActionDiscardTile(_message.Message):
    __slots__ = ["doras", "is_liqi", "is_wliqi", "moqie", "operation", "seat", "tile", "tingpais", "zhenting"]
    DORAS_FIELD_NUMBER: ClassVar[int]
    IS_LIQI_FIELD_NUMBER: ClassVar[int]
    IS_WLIQI_FIELD_NUMBER: ClassVar[int]
    MOQIE_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILE_FIELD_NUMBER: ClassVar[int]
    TINGPAIS_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    is_liqi: bool
    is_wliqi: bool
    moqie: bool
    operation: OptionalOperationList
    seat: int
    tile: str
    tingpais: _containers.RepeatedCompositeFieldContainer[TingPaiInfo]
    zhenting: bool
    def __init__(self, seat: Optional[int] = ..., tile: Optional[str] = ..., is_liqi: bool = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ..., moqie: bool = ..., zhenting: bool = ..., tingpais: Optional[Iterable[Union[TingPaiInfo, Mapping]]] = ..., doras: Optional[Iterable[str]] = ..., is_wliqi: bool = ...) -> None: ...

class ActionHule(_message.Message):
    __slots__ = ["delta_scores", "doras", "gameend", "hules", "old_scores", "scores", "wait_timeout"]
    DELTA_SCORES_FIELD_NUMBER: ClassVar[int]
    DORAS_FIELD_NUMBER: ClassVar[int]
    GAMEEND_FIELD_NUMBER: ClassVar[int]
    HULES_FIELD_NUMBER: ClassVar[int]
    OLD_SCORES_FIELD_NUMBER: ClassVar[int]
    SCORES_FIELD_NUMBER: ClassVar[int]
    WAIT_TIMEOUT_FIELD_NUMBER: ClassVar[int]
    delta_scores: _containers.RepeatedScalarFieldContainer[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    gameend: GameEnd
    hules: _containers.RepeatedCompositeFieldContainer[HuleInfo]
    old_scores: _containers.RepeatedScalarFieldContainer[int]
    scores: _containers.RepeatedScalarFieldContainer[int]
    wait_timeout: int
    def __init__(self, hules: Optional[Iterable[Union[HuleInfo, Mapping]]] = ..., old_scores: Optional[Iterable[int]] = ..., delta_scores: Optional[Iterable[int]] = ..., wait_timeout: Optional[int] = ..., scores: Optional[Iterable[int]] = ..., gameend: Optional[Union[GameEnd, Mapping]] = ..., doras: Optional[Iterable[str]] = ...) -> None: ...

class ActionLiuJu(_message.Message):
    __slots__ = ["allplayertiles", "gameend", "liqi", "seat", "tiles", "type"]
    ALLPLAYERTILES_FIELD_NUMBER: ClassVar[int]
    GAMEEND_FIELD_NUMBER: ClassVar[int]
    LIQI_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILES_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    allplayertiles: _containers.RepeatedScalarFieldContainer[str]
    gameend: GameEnd
    liqi: LiQiSuccess
    seat: int
    tiles: _containers.RepeatedScalarFieldContainer[str]
    type: int
    def __init__(self, type: Optional[int] = ..., gameend: Optional[Union[GameEnd, Mapping]] = ..., seat: Optional[int] = ..., tiles: Optional[Iterable[str]] = ..., liqi: Optional[Union[LiQiSuccess, Mapping]] = ..., allplayertiles: Optional[Iterable[str]] = ...) -> None: ...

class ActionMJStart(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionNewRound(_message.Message):
    __slots__ = ["al", "ben", "chang", "dora", "doras", "ju", "left_tile_count", "liqibang", "md5", "operation", "scores", "tiles", "tingpais0", "tingpais1"]
    AL_FIELD_NUMBER: ClassVar[int]
    BEN_FIELD_NUMBER: ClassVar[int]
    CHANG_FIELD_NUMBER: ClassVar[int]
    DORAS_FIELD_NUMBER: ClassVar[int]
    DORA_FIELD_NUMBER: ClassVar[int]
    JU_FIELD_NUMBER: ClassVar[int]
    LEFT_TILE_COUNT_FIELD_NUMBER: ClassVar[int]
    LIQIBANG_FIELD_NUMBER: ClassVar[int]
    MD5_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    SCORES_FIELD_NUMBER: ClassVar[int]
    TILES_FIELD_NUMBER: ClassVar[int]
    TINGPAIS0_FIELD_NUMBER: ClassVar[int]
    TINGPAIS1_FIELD_NUMBER: ClassVar[int]
    al: bool
    ben: int
    chang: int
    dora: str
    doras: _containers.RepeatedScalarFieldContainer[str]
    ju: int
    left_tile_count: int
    liqibang: int
    md5: str
    operation: OptionalOperationList
    scores: _containers.RepeatedScalarFieldContainer[int]
    tiles: _containers.RepeatedScalarFieldContainer[str]
    tingpais0: _containers.RepeatedCompositeFieldContainer[TingPaiDiscardInfo]
    tingpais1: _containers.RepeatedCompositeFieldContainer[TingPaiInfo]
    def __init__(self, chang: Optional[int] = ..., ju: Optional[int] = ..., ben: Optional[int] = ..., tiles: Optional[Iterable[str]] = ..., dora: Optional[str] = ..., scores: Optional[Iterable[int]] = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ..., liqibang: Optional[int] = ..., tingpais0: Optional[Iterable[Union[TingPaiDiscardInfo, Mapping]]] = ..., tingpais1: Optional[Iterable[Union[TingPaiInfo, Mapping]]] = ..., al: bool = ..., md5: Optional[str] = ..., left_tile_count: Optional[int] = ..., doras: Optional[Iterable[str]] = ...) -> None: ...

class ActionNoTile(_message.Message):
    __slots__ = ["gameend", "liujumanguan", "players", "scores"]
    GAMEEND_FIELD_NUMBER: ClassVar[int]
    LIUJUMANGUAN_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    SCORES_FIELD_NUMBER: ClassVar[int]
    gameend: bool
    liujumanguan: bool
    players: _containers.RepeatedCompositeFieldContainer[NoTilePlayerInfo]
    scores: _containers.RepeatedCompositeFieldContainer[NoTileScoreInfo]
    def __init__(self, liujumanguan: bool = ..., players: Optional[Iterable[Union[NoTilePlayerInfo, Mapping]]] = ..., scores: Optional[Iterable[Union[NoTileScoreInfo, Mapping]]] = ..., gameend: bool = ...) -> None: ...

class ActionPrototype(_message.Message):
    __slots__ = ["data", "name", "step"]
    DATA_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    STEP_FIELD_NUMBER: ClassVar[int]
    data: bytes
    name: str
    step: int
    def __init__(self, step: Optional[int] = ..., name: Optional[str] = ..., data: Optional[bytes] = ...) -> None: ...

class FanInfo(_message.Message):
    __slots__ = ["id", "name", "val"]
    ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    VAL_FIELD_NUMBER: ClassVar[int]
    id: int
    name: str
    val: int
    def __init__(self, name: Optional[str] = ..., val: Optional[int] = ..., id: Optional[int] = ...) -> None: ...

class GameDetailRecords(_message.Message):
    __slots__ = ["records"]
    RECORDS_FIELD_NUMBER: ClassVar[int]
    records: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, records: Optional[Iterable[bytes]] = ...) -> None: ...

class GameEnd(_message.Message):
    __slots__ = ["scores"]
    SCORES_FIELD_NUMBER: ClassVar[int]
    scores: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, scores: Optional[Iterable[int]] = ...) -> None: ...

class GameRestore(_message.Message):
    __slots__ = ["actions", "game_state", "last_pause_time_ms", "passed_waiting_time", "snapshot", "start_time"]
    ACTIONS_FIELD_NUMBER: ClassVar[int]
    GAME_STATE_FIELD_NUMBER: ClassVar[int]
    LAST_PAUSE_TIME_MS_FIELD_NUMBER: ClassVar[int]
    PASSED_WAITING_TIME_FIELD_NUMBER: ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[ActionPrototype]
    game_state: int
    last_pause_time_ms: int
    passed_waiting_time: int
    snapshot: GameSnapshot
    start_time: int
    def __init__(self, snapshot: Optional[Union[GameSnapshot, Mapping]] = ..., actions: Optional[Iterable[Union[ActionPrototype, Mapping]]] = ..., passed_waiting_time: Optional[int] = ..., game_state: Optional[int] = ..., start_time: Optional[int] = ..., last_pause_time_ms: Optional[int] = ...) -> None: ...

class GameSnapshot(_message.Message):
    __slots__ = ["ben", "chang", "doras", "hands", "index_player", "ju", "left_tile_count", "liqibang", "players", "zhenting"]
    class PlayerSnapshot(_message.Message):
        __slots__ = ["liqiposition", "mings", "qipais", "score", "tilenum"]
        class Fulu(_message.Message):
            __slots__ = ["tile", "type"]
            FROM_FIELD_NUMBER: ClassVar[int]
            TILE_FIELD_NUMBER: ClassVar[int]
            TYPE_FIELD_NUMBER: ClassVar[int]
            tile: _containers.RepeatedScalarFieldContainer[str]
            type: int
            def __init__(self, type: Optional[int] = ..., tile: Optional[Iterable[str]] = ..., **kwargs) -> None: ...
        LIQIPOSITION_FIELD_NUMBER: ClassVar[int]
        MINGS_FIELD_NUMBER: ClassVar[int]
        QIPAIS_FIELD_NUMBER: ClassVar[int]
        SCORE_FIELD_NUMBER: ClassVar[int]
        TILENUM_FIELD_NUMBER: ClassVar[int]
        liqiposition: int
        mings: _containers.RepeatedCompositeFieldContainer[GameSnapshot.PlayerSnapshot.Fulu]
        qipais: _containers.RepeatedScalarFieldContainer[str]
        score: int
        tilenum: int
        def __init__(self, score: Optional[int] = ..., liqiposition: Optional[int] = ..., tilenum: Optional[int] = ..., qipais: Optional[Iterable[str]] = ..., mings: Optional[Iterable[Union[GameSnapshot.PlayerSnapshot.Fulu, Mapping]]] = ...) -> None: ...
    BEN_FIELD_NUMBER: ClassVar[int]
    CHANG_FIELD_NUMBER: ClassVar[int]
    DORAS_FIELD_NUMBER: ClassVar[int]
    HANDS_FIELD_NUMBER: ClassVar[int]
    INDEX_PLAYER_FIELD_NUMBER: ClassVar[int]
    JU_FIELD_NUMBER: ClassVar[int]
    LEFT_TILE_COUNT_FIELD_NUMBER: ClassVar[int]
    LIQIBANG_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    ben: int
    chang: int
    doras: _containers.RepeatedScalarFieldContainer[str]
    hands: _containers.RepeatedScalarFieldContainer[str]
    index_player: int
    ju: int
    left_tile_count: int
    liqibang: int
    players: _containers.RepeatedCompositeFieldContainer[GameSnapshot.PlayerSnapshot]
    zhenting: bool
    def __init__(self, chang: Optional[int] = ..., ju: Optional[int] = ..., ben: Optional[int] = ..., index_player: Optional[int] = ..., left_tile_count: Optional[int] = ..., hands: Optional[Iterable[str]] = ..., doras: Optional[Iterable[str]] = ..., liqibang: Optional[int] = ..., players: Optional[Iterable[Union[GameSnapshot.PlayerSnapshot, Mapping]]] = ..., zhenting: bool = ...) -> None: ...

class HuleInfo(_message.Message):
    __slots__ = ["count", "doras", "fans", "fu", "hand", "hu_tile", "li_doras", "liqi", "ming", "point_rong", "point_sum", "point_zimo_qin", "point_zimo_xian", "qinjia", "seat", "title", "title_id", "yiman", "zimo"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    DORAS_FIELD_NUMBER: ClassVar[int]
    FANS_FIELD_NUMBER: ClassVar[int]
    FU_FIELD_NUMBER: ClassVar[int]
    HAND_FIELD_NUMBER: ClassVar[int]
    HU_TILE_FIELD_NUMBER: ClassVar[int]
    LIQI_FIELD_NUMBER: ClassVar[int]
    LI_DORAS_FIELD_NUMBER: ClassVar[int]
    MING_FIELD_NUMBER: ClassVar[int]
    POINT_RONG_FIELD_NUMBER: ClassVar[int]
    POINT_SUM_FIELD_NUMBER: ClassVar[int]
    POINT_ZIMO_QIN_FIELD_NUMBER: ClassVar[int]
    POINT_ZIMO_XIAN_FIELD_NUMBER: ClassVar[int]
    QINJIA_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    TITLE_ID_FIELD_NUMBER: ClassVar[int]
    YIMAN_FIELD_NUMBER: ClassVar[int]
    ZIMO_FIELD_NUMBER: ClassVar[int]
    count: int
    doras: _containers.RepeatedScalarFieldContainer[str]
    fans: _containers.RepeatedCompositeFieldContainer[FanInfo]
    fu: int
    hand: _containers.RepeatedScalarFieldContainer[str]
    hu_tile: str
    li_doras: _containers.RepeatedScalarFieldContainer[str]
    liqi: bool
    ming: _containers.RepeatedScalarFieldContainer[str]
    point_rong: int
    point_sum: int
    point_zimo_qin: int
    point_zimo_xian: int
    qinjia: bool
    seat: int
    title: str
    title_id: int
    yiman: bool
    zimo: bool
    def __init__(self, hand: Optional[Iterable[str]] = ..., ming: Optional[Iterable[str]] = ..., hu_tile: Optional[str] = ..., seat: Optional[int] = ..., zimo: bool = ..., qinjia: bool = ..., liqi: bool = ..., doras: Optional[Iterable[str]] = ..., li_doras: Optional[Iterable[str]] = ..., yiman: bool = ..., count: Optional[int] = ..., fans: Optional[Iterable[Union[FanInfo, Mapping]]] = ..., fu: Optional[int] = ..., title: Optional[str] = ..., point_rong: Optional[int] = ..., point_zimo_qin: Optional[int] = ..., point_zimo_xian: Optional[int] = ..., title_id: Optional[int] = ..., point_sum: Optional[int] = ...) -> None: ...

class LiQiSuccess(_message.Message):
    __slots__ = ["liqibang", "score", "seat"]
    LIQIBANG_FIELD_NUMBER: ClassVar[int]
    SCORE_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    liqibang: int
    score: int
    seat: int
    def __init__(self, seat: Optional[int] = ..., score: Optional[int] = ..., liqibang: Optional[int] = ...) -> None: ...

class NoTilePlayerInfo(_message.Message):
    __slots__ = ["hand", "tingpai", "tings"]
    HAND_FIELD_NUMBER: ClassVar[int]
    TINGPAI_FIELD_NUMBER: ClassVar[int]
    TINGS_FIELD_NUMBER: ClassVar[int]
    hand: _containers.RepeatedScalarFieldContainer[str]
    tingpai: bool
    tings: _containers.RepeatedCompositeFieldContainer[TingPaiInfo]
    def __init__(self, tingpai: bool = ..., hand: Optional[Iterable[str]] = ..., tings: Optional[Iterable[Union[TingPaiInfo, Mapping]]] = ...) -> None: ...

class NoTileScoreInfo(_message.Message):
    __slots__ = ["delta_scores", "doras", "hand", "ming", "old_scores", "score", "seat"]
    DELTA_SCORES_FIELD_NUMBER: ClassVar[int]
    DORAS_FIELD_NUMBER: ClassVar[int]
    HAND_FIELD_NUMBER: ClassVar[int]
    MING_FIELD_NUMBER: ClassVar[int]
    OLD_SCORES_FIELD_NUMBER: ClassVar[int]
    SCORE_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    delta_scores: _containers.RepeatedScalarFieldContainer[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    hand: _containers.RepeatedScalarFieldContainer[str]
    ming: _containers.RepeatedScalarFieldContainer[str]
    old_scores: _containers.RepeatedScalarFieldContainer[int]
    score: int
    seat: int
    def __init__(self, seat: Optional[int] = ..., old_scores: Optional[Iterable[int]] = ..., delta_scores: Optional[Iterable[int]] = ..., hand: Optional[Iterable[str]] = ..., ming: Optional[Iterable[str]] = ..., doras: Optional[Iterable[str]] = ..., score: Optional[int] = ...) -> None: ...

class NotifyAccountLevelChange(_message.Message):
    __slots__ = ["final", "origin", "type"]
    FINAL_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    final: _dhs_pb2.AccountLevel
    origin: _dhs_pb2.AccountLevel
    type: int
    def __init__(self, origin: Optional[Union[_dhs_pb2.AccountLevel, Mapping]] = ..., final: Optional[Union[_dhs_pb2.AccountLevel, Mapping]] = ..., type: Optional[int] = ...) -> None: ...

class NotifyAccountLogout(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NotifyAccountUpdate(_message.Message):
    __slots__ = ["update"]
    UPDATE_FIELD_NUMBER: ClassVar[int]
    update: _dhs_pb2.AccountUpdate
    def __init__(self, update: Optional[Union[_dhs_pb2.AccountUpdate, Mapping]] = ...) -> None: ...

class NotifyActivityChange(_message.Message):
    __slots__ = ["end_activities", "new_activities"]
    END_ACTIVITIES_FIELD_NUMBER: ClassVar[int]
    NEW_ACTIVITIES_FIELD_NUMBER: ClassVar[int]
    end_activities: _containers.RepeatedScalarFieldContainer[int]
    new_activities: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.Activity]
    def __init__(self, new_activities: Optional[Iterable[Union[_dhs_pb2.Activity, Mapping]]] = ..., end_activities: Optional[Iterable[int]] = ...) -> None: ...

class NotifyActivityPoint(_message.Message):
    __slots__ = ["activity_points"]
    class ActivityPoint(_message.Message):
        __slots__ = ["activity_id", "point"]
        ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
        POINT_FIELD_NUMBER: ClassVar[int]
        activity_id: int
        point: int
        def __init__(self, activity_id: Optional[int] = ..., point: Optional[int] = ...) -> None: ...
    ACTIVITY_POINTS_FIELD_NUMBER: ClassVar[int]
    activity_points: _containers.RepeatedCompositeFieldContainer[NotifyActivityPoint.ActivityPoint]
    def __init__(self, activity_points: Optional[Iterable[Union[NotifyActivityPoint.ActivityPoint, Mapping]]] = ...) -> None: ...

class NotifyActivityReward(_message.Message):
    __slots__ = ["activity_reward"]
    class ActivityReward(_message.Message):
        __slots__ = ["activity_id", "rewards"]
        ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
        REWARDS_FIELD_NUMBER: ClassVar[int]
        activity_id: int
        rewards: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.RewardSlot]
        def __init__(self, activity_id: Optional[int] = ..., rewards: Optional[Iterable[Union[_dhs_pb2.RewardSlot, Mapping]]] = ...) -> None: ...
    ACTIVITY_REWARD_FIELD_NUMBER: ClassVar[int]
    activity_reward: _containers.RepeatedCompositeFieldContainer[NotifyActivityReward.ActivityReward]
    def __init__(self, activity_reward: Optional[Iterable[Union[NotifyActivityReward.ActivityReward, Mapping]]] = ...) -> None: ...

class NotifyActivityTaskUpdate(_message.Message):
    __slots__ = ["progresses"]
    PROGRESSES_FIELD_NUMBER: ClassVar[int]
    progresses: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.TaskProgress]
    def __init__(self, progresses: Optional[Iterable[Union[_dhs_pb2.TaskProgress, Mapping]]] = ...) -> None: ...

class NotifyAnnouncementUpdate(_message.Message):
    __slots__ = ["announcements", "sort"]
    ANNOUNCEMENTS_FIELD_NUMBER: ClassVar[int]
    SORT_FIELD_NUMBER: ClassVar[int]
    announcements: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.Announcement]
    sort: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, announcements: Optional[Iterable[Union[_dhs_pb2.Announcement, Mapping]]] = ..., sort: Optional[Iterable[int]] = ...) -> None: ...

class NotifyAnotherLogin(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NotifyClientMessage(_message.Message):
    __slots__ = ["content", "sender", "type"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    SENDER_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    content: str
    sender: _dhs_pb2.PlayerBaseView
    type: int
    def __init__(self, sender: Optional[Union[_dhs_pb2.PlayerBaseView, Mapping]] = ..., type: Optional[int] = ..., content: Optional[str] = ...) -> None: ...

class NotifyDailyTaskUpdate(_message.Message):
    __slots__ = ["max_daily_task_count", "progresses", "refresh_count"]
    MAX_DAILY_TASK_COUNT_FIELD_NUMBER: ClassVar[int]
    PROGRESSES_FIELD_NUMBER: ClassVar[int]
    REFRESH_COUNT_FIELD_NUMBER: ClassVar[int]
    max_daily_task_count: int
    progresses: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.TaskProgress]
    refresh_count: int
    def __init__(self, progresses: Optional[Iterable[Union[_dhs_pb2.TaskProgress, Mapping]]] = ..., max_daily_task_count: Optional[int] = ..., refresh_count: Optional[int] = ...) -> None: ...

class NotifyDeleteMail(_message.Message):
    __slots__ = ["mail_id_list"]
    MAIL_ID_LIST_FIELD_NUMBER: ClassVar[int]
    mail_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, mail_id_list: Optional[Iterable[int]] = ...) -> None: ...

class NotifyFriendChange(_message.Message):
    __slots__ = ["account_id", "friend", "type"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    FRIEND_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    account_id: int
    friend: _dhs_pb2.Friend
    type: int
    def __init__(self, account_id: Optional[int] = ..., type: Optional[int] = ..., friend: Optional[Union[_dhs_pb2.Friend, Mapping]] = ...) -> None: ...

class NotifyFriendStateChange(_message.Message):
    __slots__ = ["active_state", "target_id"]
    ACTIVE_STATE_FIELD_NUMBER: ClassVar[int]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    active_state: _dhs_pb2.AccountActiveState
    target_id: int
    def __init__(self, target_id: Optional[int] = ..., active_state: Optional[Union[_dhs_pb2.AccountActiveState, Mapping]] = ...) -> None: ...

class NotifyFriendViewChange(_message.Message):
    __slots__ = ["base", "target_id"]
    BASE_FIELD_NUMBER: ClassVar[int]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    base: _dhs_pb2.PlayerBaseView
    target_id: int
    def __init__(self, target_id: Optional[int] = ..., base: Optional[Union[_dhs_pb2.PlayerBaseView, Mapping]] = ...) -> None: ...

class NotifyGameBroadcast(_message.Message):
    __slots__ = ["content", "seat"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    content: str
    seat: int
    def __init__(self, seat: Optional[int] = ..., content: Optional[str] = ...) -> None: ...

class NotifyGameEndResult(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: ClassVar[int]
    result: _dhs_pb2.GameEndResult
    def __init__(self, result: Optional[Union[_dhs_pb2.GameEndResult, Mapping]] = ...) -> None: ...

class NotifyGameFinishReward(_message.Message):
    __slots__ = ["character_gift", "level_change", "main_character", "match_chest", "mode_id"]
    class CharacterGift(_message.Message):
        __slots__ = ["add", "final", "is_graded", "origin"]
        ADD_FIELD_NUMBER: ClassVar[int]
        FINAL_FIELD_NUMBER: ClassVar[int]
        IS_GRADED_FIELD_NUMBER: ClassVar[int]
        ORIGIN_FIELD_NUMBER: ClassVar[int]
        add: int
        final: int
        is_graded: bool
        origin: int
        def __init__(self, origin: Optional[int] = ..., final: Optional[int] = ..., add: Optional[int] = ..., is_graded: bool = ...) -> None: ...
    class LevelChange(_message.Message):
        __slots__ = ["final", "origin", "type"]
        FINAL_FIELD_NUMBER: ClassVar[int]
        ORIGIN_FIELD_NUMBER: ClassVar[int]
        TYPE_FIELD_NUMBER: ClassVar[int]
        final: _dhs_pb2.AccountLevel
        origin: _dhs_pb2.AccountLevel
        type: int
        def __init__(self, origin: Optional[Union[_dhs_pb2.AccountLevel, Mapping]] = ..., final: Optional[Union[_dhs_pb2.AccountLevel, Mapping]] = ..., type: Optional[int] = ...) -> None: ...
    class MainCharacter(_message.Message):
        __slots__ = ["add", "exp", "level"]
        ADD_FIELD_NUMBER: ClassVar[int]
        EXP_FIELD_NUMBER: ClassVar[int]
        LEVEL_FIELD_NUMBER: ClassVar[int]
        add: int
        exp: int
        level: int
        def __init__(self, level: Optional[int] = ..., exp: Optional[int] = ..., add: Optional[int] = ...) -> None: ...
    class MatchChest(_message.Message):
        __slots__ = ["chest_id", "final", "is_graded", "origin", "rewards"]
        CHEST_ID_FIELD_NUMBER: ClassVar[int]
        FINAL_FIELD_NUMBER: ClassVar[int]
        IS_GRADED_FIELD_NUMBER: ClassVar[int]
        ORIGIN_FIELD_NUMBER: ClassVar[int]
        REWARDS_FIELD_NUMBER: ClassVar[int]
        chest_id: int
        final: int
        is_graded: bool
        origin: int
        rewards: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.RewardSlot]
        def __init__(self, chest_id: Optional[int] = ..., origin: Optional[int] = ..., final: Optional[int] = ..., is_graded: bool = ..., rewards: Optional[Iterable[Union[_dhs_pb2.RewardSlot, Mapping]]] = ...) -> None: ...
    CHARACTER_GIFT_FIELD_NUMBER: ClassVar[int]
    LEVEL_CHANGE_FIELD_NUMBER: ClassVar[int]
    MAIN_CHARACTER_FIELD_NUMBER: ClassVar[int]
    MATCH_CHEST_FIELD_NUMBER: ClassVar[int]
    MODE_ID_FIELD_NUMBER: ClassVar[int]
    character_gift: NotifyGameFinishReward.CharacterGift
    level_change: NotifyGameFinishReward.LevelChange
    main_character: NotifyGameFinishReward.MainCharacter
    match_chest: NotifyGameFinishReward.MatchChest
    mode_id: int
    def __init__(self, mode_id: Optional[int] = ..., level_change: Optional[Union[NotifyGameFinishReward.LevelChange, Mapping]] = ..., match_chest: Optional[Union[NotifyGameFinishReward.MatchChest, Mapping]] = ..., main_character: Optional[Union[NotifyGameFinishReward.MainCharacter, Mapping]] = ..., character_gift: Optional[Union[NotifyGameFinishReward.CharacterGift, Mapping]] = ...) -> None: ...

class NotifyGamePause(_message.Message):
    __slots__ = ["paused"]
    PAUSED_FIELD_NUMBER: ClassVar[int]
    paused: bool
    def __init__(self, paused: bool = ...) -> None: ...

class NotifyGameTerminate(_message.Message):
    __slots__ = ["reason"]
    REASON_FIELD_NUMBER: ClassVar[int]
    reason: str
    def __init__(self, reason: Optional[str] = ...) -> None: ...

class NotifyGiftSendRefresh(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NotifyLeaderboardPoint(_message.Message):
    __slots__ = ["leaderboard_points"]
    class LeaderboardPoint(_message.Message):
        __slots__ = ["leaderboard_id", "point"]
        LEADERBOARD_ID_FIELD_NUMBER: ClassVar[int]
        POINT_FIELD_NUMBER: ClassVar[int]
        leaderboard_id: int
        point: int
        def __init__(self, leaderboard_id: Optional[int] = ..., point: Optional[int] = ...) -> None: ...
    LEADERBOARD_POINTS_FIELD_NUMBER: ClassVar[int]
    leaderboard_points: _containers.RepeatedCompositeFieldContainer[NotifyLeaderboardPoint.LeaderboardPoint]
    def __init__(self, leaderboard_points: Optional[Iterable[Union[NotifyLeaderboardPoint.LeaderboardPoint, Mapping]]] = ...) -> None: ...

class NotifyMatchGameStart(_message.Message):
    __slots__ = ["connect_token", "game_url", "game_uuid", "location", "match_mode_id"]
    CONNECT_TOKEN_FIELD_NUMBER: ClassVar[int]
    GAME_URL_FIELD_NUMBER: ClassVar[int]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    LOCATION_FIELD_NUMBER: ClassVar[int]
    MATCH_MODE_ID_FIELD_NUMBER: ClassVar[int]
    connect_token: str
    game_url: str
    game_uuid: str
    location: str
    match_mode_id: int
    def __init__(self, game_url: Optional[str] = ..., connect_token: Optional[str] = ..., game_uuid: Optional[str] = ..., match_mode_id: Optional[int] = ..., location: Optional[str] = ...) -> None: ...

class NotifyMatchTimeout(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NotifyNewComment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NotifyNewFriendApply(_message.Message):
    __slots__ = ["account_id", "apply_time", "removed_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    APPLY_TIME_FIELD_NUMBER: ClassVar[int]
    REMOVED_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    apply_time: int
    removed_id: int
    def __init__(self, account_id: Optional[int] = ..., apply_time: Optional[int] = ..., removed_id: Optional[int] = ...) -> None: ...

class NotifyNewGame(_message.Message):
    __slots__ = ["game_uuid", "player_list"]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    PLAYER_LIST_FIELD_NUMBER: ClassVar[int]
    game_uuid: str
    player_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, game_uuid: Optional[str] = ..., player_list: Optional[Iterable[str]] = ...) -> None: ...

class NotifyNewMail(_message.Message):
    __slots__ = ["mail"]
    MAIL_FIELD_NUMBER: ClassVar[int]
    mail: _dhs_pb2.Mail
    def __init__(self, mail: Optional[Union[_dhs_pb2.Mail, Mapping]] = ...) -> None: ...

class NotifyPayResult(_message.Message):
    __slots__ = ["goods_id", "order_id", "pay_result"]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    PAY_RESULT_FIELD_NUMBER: ClassVar[int]
    goods_id: int
    order_id: str
    pay_result: int
    def __init__(self, pay_result: Optional[int] = ..., order_id: Optional[str] = ..., goods_id: Optional[int] = ...) -> None: ...

class NotifyPlayerConnectionState(_message.Message):
    __slots__ = ["seat", "state"]
    SEAT_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    seat: int
    state: _dhs_pb2.GamePlayerState
    def __init__(self, seat: Optional[int] = ..., state: Optional[Union[_dhs_pb2.GamePlayerState, str]] = ...) -> None: ...

class NotifyPlayerLoadGameReady(_message.Message):
    __slots__ = ["ready_id_list"]
    READY_ID_LIST_FIELD_NUMBER: ClassVar[int]
    ready_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ready_id_list: Optional[Iterable[int]] = ...) -> None: ...

class NotifyReviveCoinUpdate(_message.Message):
    __slots__ = ["has_gained"]
    HAS_GAINED_FIELD_NUMBER: ClassVar[int]
    has_gained: bool
    def __init__(self, has_gained: bool = ...) -> None: ...

class NotifyRollingNotice(_message.Message):
    __slots__ = ["notice"]
    NOTICE_FIELD_NUMBER: ClassVar[int]
    notice: _dhs_pb2.RollingNotice
    def __init__(self, notice: Optional[Union[_dhs_pb2.RollingNotice, Mapping]] = ...) -> None: ...

class NotifyRoomGameStart(_message.Message):
    __slots__ = ["connect_token", "game_url", "game_uuid", "location"]
    CONNECT_TOKEN_FIELD_NUMBER: ClassVar[int]
    GAME_URL_FIELD_NUMBER: ClassVar[int]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    LOCATION_FIELD_NUMBER: ClassVar[int]
    connect_token: str
    game_url: str
    game_uuid: str
    location: str
    def __init__(self, game_url: Optional[str] = ..., connect_token: Optional[str] = ..., game_uuid: Optional[str] = ..., location: Optional[str] = ...) -> None: ...

class NotifyRoomKickOut(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NotifyRoomPlayerReady(_message.Message):
    __slots__ = ["account_id", "ready"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    READY_FIELD_NUMBER: ClassVar[int]
    account_id: int
    ready: bool
    def __init__(self, account_id: Optional[int] = ..., ready: bool = ...) -> None: ...

class NotifyRoomPlayerUpdate(_message.Message):
    __slots__ = ["owner_id", "remove_list", "robot_count", "update_list"]
    OWNER_ID_FIELD_NUMBER: ClassVar[int]
    REMOVE_LIST_FIELD_NUMBER: ClassVar[int]
    ROBOT_COUNT_FIELD_NUMBER: ClassVar[int]
    UPDATE_LIST_FIELD_NUMBER: ClassVar[int]
    owner_id: int
    remove_list: _containers.RepeatedScalarFieldContainer[int]
    robot_count: int
    update_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.PlayerBaseView]
    def __init__(self, update_list: Optional[Iterable[Union[_dhs_pb2.PlayerBaseView, Mapping]]] = ..., remove_list: Optional[Iterable[int]] = ..., owner_id: Optional[int] = ..., robot_count: Optional[int] = ...) -> None: ...

class NotifyServerSetting(_message.Message):
    __slots__ = ["settings"]
    SETTINGS_FIELD_NUMBER: ClassVar[int]
    settings: _dhs_pb2.ServerSettings
    def __init__(self, settings: Optional[Union[_dhs_pb2.ServerSettings, Mapping]] = ...) -> None: ...

class NotifyShopUpdate(_message.Message):
    __slots__ = ["shop_info"]
    SHOP_INFO_FIELD_NUMBER: ClassVar[int]
    shop_info: _dhs_pb2.ShopInfo
    def __init__(self, shop_info: Optional[Union[_dhs_pb2.ShopInfo, Mapping]] = ...) -> None: ...

class NotifyVipLevelChange(_message.Message):
    __slots__ = ["buddy_bonus", "friend_max_count", "gift_limit", "record_collect_limit", "zhp_cost_refresh_limit", "zhp_free_refresh_limit"]
    BUDDY_BONUS_FIELD_NUMBER: ClassVar[int]
    FRIEND_MAX_COUNT_FIELD_NUMBER: ClassVar[int]
    GIFT_LIMIT_FIELD_NUMBER: ClassVar[int]
    RECORD_COLLECT_LIMIT_FIELD_NUMBER: ClassVar[int]
    ZHP_COST_REFRESH_LIMIT_FIELD_NUMBER: ClassVar[int]
    ZHP_FREE_REFRESH_LIMIT_FIELD_NUMBER: ClassVar[int]
    buddy_bonus: float
    friend_max_count: int
    gift_limit: int
    record_collect_limit: int
    zhp_cost_refresh_limit: int
    zhp_free_refresh_limit: int
    def __init__(self, gift_limit: Optional[int] = ..., friend_max_count: Optional[int] = ..., zhp_free_refresh_limit: Optional[int] = ..., zhp_cost_refresh_limit: Optional[int] = ..., buddy_bonus: Optional[float] = ..., record_collect_limit: Optional[int] = ...) -> None: ...

class OptionalOperation(_message.Message):
    __slots__ = ["combination", "type"]
    COMBINATION_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    combination: _containers.RepeatedScalarFieldContainer[str]
    type: int
    def __init__(self, type: Optional[int] = ..., combination: Optional[Iterable[str]] = ...) -> None: ...

class OptionalOperationList(_message.Message):
    __slots__ = ["operation_list", "seat", "time_add", "time_fixed"]
    OPERATION_LIST_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TIME_ADD_FIELD_NUMBER: ClassVar[int]
    TIME_FIXED_FIELD_NUMBER: ClassVar[int]
    operation_list: _containers.RepeatedCompositeFieldContainer[OptionalOperation]
    seat: int
    time_add: int
    time_fixed: int
    def __init__(self, seat: Optional[int] = ..., operation_list: Optional[Iterable[Union[OptionalOperation, Mapping]]] = ..., time_add: Optional[int] = ..., time_fixed: Optional[int] = ...) -> None: ...

class RecordAnGangAddGang(_message.Message):
    __slots__ = ["doras", "operations", "seat", "tiles", "type"]
    DORAS_FIELD_NUMBER: ClassVar[int]
    OPERATIONS_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILES_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    operations: _containers.RepeatedCompositeFieldContainer[OptionalOperationList]
    seat: int
    tiles: str
    type: int
    def __init__(self, seat: Optional[int] = ..., type: Optional[int] = ..., tiles: Optional[str] = ..., doras: Optional[Iterable[str]] = ..., operations: Optional[Iterable[Union[OptionalOperationList, Mapping]]] = ...) -> None: ...

class RecordBaBei(_message.Message):
    __slots__ = ["doras", "moqie", "operations", "seat"]
    DORAS_FIELD_NUMBER: ClassVar[int]
    MOQIE_FIELD_NUMBER: ClassVar[int]
    OPERATIONS_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    moqie: bool
    operations: _containers.RepeatedCompositeFieldContainer[OptionalOperationList]
    seat: int
    def __init__(self, seat: Optional[int] = ..., doras: Optional[Iterable[str]] = ..., operations: Optional[Iterable[Union[OptionalOperationList, Mapping]]] = ..., moqie: bool = ...) -> None: ...

class RecordChiPengGang(_message.Message):
    __slots__ = ["froms", "liqi", "operation", "seat", "tiles", "type", "zhenting"]
    FROMS_FIELD_NUMBER: ClassVar[int]
    LIQI_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILES_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    froms: _containers.RepeatedScalarFieldContainer[int]
    liqi: LiQiSuccess
    operation: OptionalOperationList
    seat: int
    tiles: _containers.RepeatedScalarFieldContainer[str]
    type: int
    zhenting: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, seat: Optional[int] = ..., type: Optional[int] = ..., tiles: Optional[Iterable[str]] = ..., froms: Optional[Iterable[int]] = ..., liqi: Optional[Union[LiQiSuccess, Mapping]] = ..., zhenting: Optional[Iterable[bool]] = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ...) -> None: ...

class RecordDealTile(_message.Message):
    __slots__ = ["doras", "left_tile_count", "liqi", "operation", "seat", "tile", "zhenting"]
    DORAS_FIELD_NUMBER: ClassVar[int]
    LEFT_TILE_COUNT_FIELD_NUMBER: ClassVar[int]
    LIQI_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILE_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    left_tile_count: int
    liqi: LiQiSuccess
    operation: OptionalOperationList
    seat: int
    tile: str
    zhenting: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, seat: Optional[int] = ..., tile: Optional[str] = ..., left_tile_count: Optional[int] = ..., liqi: Optional[Union[LiQiSuccess, Mapping]] = ..., doras: Optional[Iterable[str]] = ..., zhenting: Optional[Iterable[bool]] = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ...) -> None: ...

class RecordDiscardTile(_message.Message):
    __slots__ = ["doras", "is_liqi", "is_wliqi", "moqie", "operations", "seat", "tile", "tingpais", "zhenting"]
    DORAS_FIELD_NUMBER: ClassVar[int]
    IS_LIQI_FIELD_NUMBER: ClassVar[int]
    IS_WLIQI_FIELD_NUMBER: ClassVar[int]
    MOQIE_FIELD_NUMBER: ClassVar[int]
    OPERATIONS_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILE_FIELD_NUMBER: ClassVar[int]
    TINGPAIS_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    is_liqi: bool
    is_wliqi: bool
    moqie: bool
    operations: _containers.RepeatedCompositeFieldContainer[OptionalOperationList]
    seat: int
    tile: str
    tingpais: _containers.RepeatedCompositeFieldContainer[TingPaiInfo]
    zhenting: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, seat: Optional[int] = ..., tile: Optional[str] = ..., is_liqi: bool = ..., moqie: bool = ..., zhenting: Optional[Iterable[bool]] = ..., tingpais: Optional[Iterable[Union[TingPaiInfo, Mapping]]] = ..., doras: Optional[Iterable[str]] = ..., is_wliqi: bool = ..., operations: Optional[Iterable[Union[OptionalOperationList, Mapping]]] = ...) -> None: ...

class RecordHule(_message.Message):
    __slots__ = ["delta_scores", "doras", "gameend", "hules", "old_scores", "scores", "wait_timeout"]
    DELTA_SCORES_FIELD_NUMBER: ClassVar[int]
    DORAS_FIELD_NUMBER: ClassVar[int]
    GAMEEND_FIELD_NUMBER: ClassVar[int]
    HULES_FIELD_NUMBER: ClassVar[int]
    OLD_SCORES_FIELD_NUMBER: ClassVar[int]
    SCORES_FIELD_NUMBER: ClassVar[int]
    WAIT_TIMEOUT_FIELD_NUMBER: ClassVar[int]
    delta_scores: _containers.RepeatedScalarFieldContainer[int]
    doras: _containers.RepeatedScalarFieldContainer[str]
    gameend: GameEnd
    hules: _containers.RepeatedCompositeFieldContainer[HuleInfo]
    old_scores: _containers.RepeatedScalarFieldContainer[int]
    scores: _containers.RepeatedScalarFieldContainer[int]
    wait_timeout: int
    def __init__(self, hules: Optional[Iterable[Union[HuleInfo, Mapping]]] = ..., old_scores: Optional[Iterable[int]] = ..., delta_scores: Optional[Iterable[int]] = ..., wait_timeout: Optional[int] = ..., scores: Optional[Iterable[int]] = ..., gameend: Optional[Union[GameEnd, Mapping]] = ..., doras: Optional[Iterable[str]] = ...) -> None: ...

class RecordLiuJu(_message.Message):
    __slots__ = ["allplayertiles", "gameend", "liqi", "seat", "tiles", "type"]
    ALLPLAYERTILES_FIELD_NUMBER: ClassVar[int]
    GAMEEND_FIELD_NUMBER: ClassVar[int]
    LIQI_FIELD_NUMBER: ClassVar[int]
    SEAT_FIELD_NUMBER: ClassVar[int]
    TILES_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    allplayertiles: _containers.RepeatedScalarFieldContainer[str]
    gameend: GameEnd
    liqi: LiQiSuccess
    seat: int
    tiles: _containers.RepeatedScalarFieldContainer[str]
    type: int
    def __init__(self, type: Optional[int] = ..., gameend: Optional[Union[GameEnd, Mapping]] = ..., seat: Optional[int] = ..., tiles: Optional[Iterable[str]] = ..., liqi: Optional[Union[LiQiSuccess, Mapping]] = ..., allplayertiles: Optional[Iterable[str]] = ...) -> None: ...

class RecordNewRound(_message.Message):
    __slots__ = ["ben", "chang", "dora", "doras", "ju", "left_tile_count", "liqibang", "md5", "operation", "paishan", "scores", "tiles0", "tiles1", "tiles2", "tiles3", "tingpai"]
    class TingPai(_message.Message):
        __slots__ = ["seat", "tingpais1"]
        SEAT_FIELD_NUMBER: ClassVar[int]
        TINGPAIS1_FIELD_NUMBER: ClassVar[int]
        seat: int
        tingpais1: _containers.RepeatedCompositeFieldContainer[TingPaiInfo]
        def __init__(self, seat: Optional[int] = ..., tingpais1: Optional[Iterable[Union[TingPaiInfo, Mapping]]] = ...) -> None: ...
    BEN_FIELD_NUMBER: ClassVar[int]
    CHANG_FIELD_NUMBER: ClassVar[int]
    DORAS_FIELD_NUMBER: ClassVar[int]
    DORA_FIELD_NUMBER: ClassVar[int]
    JU_FIELD_NUMBER: ClassVar[int]
    LEFT_TILE_COUNT_FIELD_NUMBER: ClassVar[int]
    LIQIBANG_FIELD_NUMBER: ClassVar[int]
    MD5_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    PAISHAN_FIELD_NUMBER: ClassVar[int]
    SCORES_FIELD_NUMBER: ClassVar[int]
    TILES0_FIELD_NUMBER: ClassVar[int]
    TILES1_FIELD_NUMBER: ClassVar[int]
    TILES2_FIELD_NUMBER: ClassVar[int]
    TILES3_FIELD_NUMBER: ClassVar[int]
    TINGPAI_FIELD_NUMBER: ClassVar[int]
    ben: int
    chang: int
    dora: str
    doras: _containers.RepeatedScalarFieldContainer[str]
    ju: int
    left_tile_count: int
    liqibang: int
    md5: str
    operation: OptionalOperationList
    paishan: str
    scores: _containers.RepeatedScalarFieldContainer[int]
    tiles0: _containers.RepeatedScalarFieldContainer[str]
    tiles1: _containers.RepeatedScalarFieldContainer[str]
    tiles2: _containers.RepeatedScalarFieldContainer[str]
    tiles3: _containers.RepeatedScalarFieldContainer[str]
    tingpai: _containers.RepeatedCompositeFieldContainer[RecordNewRound.TingPai]
    def __init__(self, chang: Optional[int] = ..., ju: Optional[int] = ..., ben: Optional[int] = ..., dora: Optional[str] = ..., scores: Optional[Iterable[int]] = ..., liqibang: Optional[int] = ..., tiles0: Optional[Iterable[str]] = ..., tiles1: Optional[Iterable[str]] = ..., tiles2: Optional[Iterable[str]] = ..., tiles3: Optional[Iterable[str]] = ..., tingpai: Optional[Iterable[Union[RecordNewRound.TingPai, Mapping]]] = ..., operation: Optional[Union[OptionalOperationList, Mapping]] = ..., md5: Optional[str] = ..., paishan: Optional[str] = ..., left_tile_count: Optional[int] = ..., doras: Optional[Iterable[str]] = ...) -> None: ...

class RecordNoTile(_message.Message):
    __slots__ = ["gameend", "liujumanguan", "players", "scores"]
    GAMEEND_FIELD_NUMBER: ClassVar[int]
    LIUJUMANGUAN_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    SCORES_FIELD_NUMBER: ClassVar[int]
    gameend: bool
    liujumanguan: bool
    players: _containers.RepeatedCompositeFieldContainer[NoTilePlayerInfo]
    scores: _containers.RepeatedCompositeFieldContainer[NoTileScoreInfo]
    def __init__(self, liujumanguan: bool = ..., players: Optional[Iterable[Union[NoTilePlayerInfo, Mapping]]] = ..., scores: Optional[Iterable[Union[NoTileScoreInfo, Mapping]]] = ..., gameend: bool = ...) -> None: ...

class ReqAccountInfo(_message.Message):
    __slots__ = ["account_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    def __init__(self, account_id: Optional[int] = ...) -> None: ...

class ReqAccountList(_message.Message):
    __slots__ = ["account_id_list"]
    ACCOUNT_ID_LIST_FIELD_NUMBER: ClassVar[int]
    account_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, account_id_list: Optional[Iterable[int]] = ...) -> None: ...

class ReqAccountStatisticInfo(_message.Message):
    __slots__ = ["account_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    def __init__(self, account_id: Optional[int] = ...) -> None: ...

class ReqAddCollectedGameRecord(_message.Message):
    __slots__ = ["end_time", "remarks", "start_time", "uuid"]
    END_TIME_FIELD_NUMBER: ClassVar[int]
    REMARKS_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    end_time: int
    remarks: str
    start_time: int
    uuid: str
    def __init__(self, uuid: Optional[str] = ..., remarks: Optional[str] = ..., start_time: Optional[int] = ..., end_time: Optional[int] = ...) -> None: ...

class ReqApplyFriend(_message.Message):
    __slots__ = ["target_id"]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    target_id: int
    def __init__(self, target_id: Optional[int] = ...) -> None: ...

class ReqAuthGame(_message.Message):
    __slots__ = ["account_id", "game_uuid", "token"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    TOKEN_FIELD_NUMBER: ClassVar[int]
    account_id: int
    game_uuid: str
    token: str
    def __init__(self, account_id: Optional[int] = ..., token: Optional[str] = ..., game_uuid: Optional[str] = ...) -> None: ...

class ReqBindAccount(_message.Message):
    __slots__ = ["account", "password"]
    ACCOUNT_FIELD_NUMBER: ClassVar[int]
    PASSWORD_FIELD_NUMBER: ClassVar[int]
    account: str
    password: str
    def __init__(self, account: Optional[str] = ..., password: Optional[str] = ...) -> None: ...

class ReqBindEmail(_message.Message):
    __slots__ = ["code", "email", "password"]
    CODE_FIELD_NUMBER: ClassVar[int]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    PASSWORD_FIELD_NUMBER: ClassVar[int]
    code: str
    email: str
    password: str
    def __init__(self, email: Optional[str] = ..., code: Optional[str] = ..., password: Optional[str] = ...) -> None: ...

class ReqBindPhoneNumber(_message.Message):
    __slots__ = ["code", "password", "phone"]
    CODE_FIELD_NUMBER: ClassVar[int]
    PASSWORD_FIELD_NUMBER: ClassVar[int]
    PHONE_FIELD_NUMBER: ClassVar[int]
    code: str
    password: str
    phone: str
    def __init__(self, code: Optional[str] = ..., phone: Optional[str] = ..., password: Optional[str] = ...) -> None: ...

class ReqBroadcastInGame(_message.Message):
    __slots__ = ["content", "except_self"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    EXCEPT_SELF_FIELD_NUMBER: ClassVar[int]
    content: str
    except_self: bool
    def __init__(self, content: Optional[str] = ..., except_self: bool = ...) -> None: ...

class ReqBuyFromChestShop(_message.Message):
    __slots__ = ["count", "goods_id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    count: int
    goods_id: int
    def __init__(self, goods_id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...

class ReqBuyFromShop(_message.Message):
    __slots__ = ["bill_short_cut", "count", "deal_price", "goods_id"]
    BILL_SHORT_CUT_FIELD_NUMBER: ClassVar[int]
    COUNT_FIELD_NUMBER: ClassVar[int]
    DEAL_PRICE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    bill_short_cut: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.BillShortcut]
    count: int
    deal_price: int
    goods_id: int
    def __init__(self, goods_id: Optional[int] = ..., count: Optional[int] = ..., bill_short_cut: Optional[Iterable[Union[_dhs_pb2.BillShortcut, Mapping]]] = ..., deal_price: Optional[int] = ...) -> None: ...

class ReqBuyFromZHP(_message.Message):
    __slots__ = ["count", "goods_id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    count: int
    goods_id: int
    def __init__(self, goods_id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...

class ReqBuyShiLian(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: ClassVar[int]
    type: int
    def __init__(self, type: Optional[int] = ...) -> None: ...

class ReqCancelGooglePlayOrder(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    order_id: str
    def __init__(self, order_id: Optional[str] = ...) -> None: ...

class ReqCancelMatchQueue(_message.Message):
    __slots__ = ["match_mode"]
    MATCH_MODE_FIELD_NUMBER: ClassVar[int]
    match_mode: int
    def __init__(self, match_mode: Optional[int] = ...) -> None: ...

class ReqChangeAvatar(_message.Message):
    __slots__ = ["avatar_id"]
    AVATAR_ID_FIELD_NUMBER: ClassVar[int]
    avatar_id: int
    def __init__(self, avatar_id: Optional[int] = ...) -> None: ...

class ReqChangeCharacterSkin(_message.Message):
    __slots__ = ["character_id", "skin"]
    CHARACTER_ID_FIELD_NUMBER: ClassVar[int]
    SKIN_FIELD_NUMBER: ClassVar[int]
    character_id: int
    skin: int
    def __init__(self, character_id: Optional[int] = ..., skin: Optional[int] = ...) -> None: ...

class ReqChangeCharacterView(_message.Message):
    __slots__ = ["character_id", "item_id", "slot"]
    CHARACTER_ID_FIELD_NUMBER: ClassVar[int]
    ITEM_ID_FIELD_NUMBER: ClassVar[int]
    SLOT_FIELD_NUMBER: ClassVar[int]
    character_id: int
    item_id: int
    slot: int
    def __init__(self, character_id: Optional[int] = ..., slot: Optional[int] = ..., item_id: Optional[int] = ...) -> None: ...

class ReqChangeCollectedGameRecordRemarks(_message.Message):
    __slots__ = ["remarks", "uuid"]
    REMARKS_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    remarks: str
    uuid: str
    def __init__(self, uuid: Optional[str] = ..., remarks: Optional[str] = ...) -> None: ...

class ReqChangeCommonView(_message.Message):
    __slots__ = ["slot", "value"]
    SLOT_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    slot: int
    value: int
    def __init__(self, slot: Optional[int] = ..., value: Optional[int] = ...) -> None: ...

class ReqChangeMainCharacter(_message.Message):
    __slots__ = ["character_id"]
    CHARACTER_ID_FIELD_NUMBER: ClassVar[int]
    character_id: int
    def __init__(self, character_id: Optional[int] = ...) -> None: ...

class ReqChiPengGang(_message.Message):
    __slots__ = ["cancel_operation", "index", "timeuse", "type"]
    CANCEL_OPERATION_FIELD_NUMBER: ClassVar[int]
    INDEX_FIELD_NUMBER: ClassVar[int]
    TIMEUSE_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    cancel_operation: bool
    index: int
    timeuse: int
    type: int
    def __init__(self, type: Optional[int] = ..., index: Optional[int] = ..., cancel_operation: bool = ..., timeuse: Optional[int] = ...) -> None: ...

class ReqClientMessage(_message.Message):
    __slots__ = ["message", "timestamp"]
    MESSAGE_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    message: str
    timestamp: int
    def __init__(self, timestamp: Optional[int] = ..., message: Optional[str] = ...) -> None: ...

class ReqCompleteActivityTask(_message.Message):
    __slots__ = ["task_id"]
    TASK_ID_FIELD_NUMBER: ClassVar[int]
    task_id: int
    def __init__(self, task_id: Optional[int] = ...) -> None: ...

class ReqComposeShard(_message.Message):
    __slots__ = ["item_id"]
    ITEM_ID_FIELD_NUMBER: ClassVar[int]
    item_id: int
    def __init__(self, item_id: Optional[int] = ...) -> None: ...

class ReqCreateAlipayAppOrder(_message.Message):
    __slots__ = ["account_id", "client_type", "goods_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    client_type: int
    goods_id: int
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ...) -> None: ...

class ReqCreateAlipayOrder(_message.Message):
    __slots__ = ["account_id", "alipay_trade_type", "client_type", "goods_id", "return_url"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    ALIPAY_TRADE_TYPE_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    account_id: int
    alipay_trade_type: str
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., alipay_trade_type: Optional[str] = ..., return_url: Optional[str] = ...) -> None: ...

class ReqCreateAlipayScanOrder(_message.Message):
    __slots__ = ["account_id", "client_type", "goods_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    client_type: int
    goods_id: int
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ...) -> None: ...

class ReqCreateBillingOrder(_message.Message):
    __slots__ = ["account_id", "client_type", "goods_id", "payment_platform"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    PAYMENT_PLATFORM_FIELD_NUMBER: ClassVar[int]
    account_id: int
    client_type: int
    goods_id: int
    payment_platform: int
    def __init__(self, goods_id: Optional[int] = ..., payment_platform: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ...) -> None: ...

class ReqCreateENAlipayOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateENJCBOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateENMasterCardOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateENPaypalOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateENVisaOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateEmailVerifyCode(_message.Message):
    __slots__ = ["email", "usage"]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    USAGE_FIELD_NUMBER: ClassVar[int]
    email: str
    usage: int
    def __init__(self, email: Optional[str] = ..., usage: Optional[int] = ...) -> None: ...

class ReqCreateJPAuOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateJPCreditCardOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateJPDocomoOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateJPPaypalOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateJPSoftbankOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateJPWebMoneyOrder(_message.Message):
    __slots__ = ["access_token", "account_id", "client_type", "goods_id", "return_url"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    RETURN_URL_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    client_type: int
    goods_id: int
    return_url: str
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., return_url: Optional[str] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqCreateNickname(_message.Message):
    __slots__ = ["advertise_str", "nickname"]
    ADVERTISE_STR_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    advertise_str: str
    nickname: str
    def __init__(self, nickname: Optional[str] = ..., advertise_str: Optional[str] = ...) -> None: ...

class ReqCreatePhoneVerifyCode(_message.Message):
    __slots__ = ["phone", "usage"]
    PHONE_FIELD_NUMBER: ClassVar[int]
    USAGE_FIELD_NUMBER: ClassVar[int]
    phone: str
    usage: int
    def __init__(self, phone: Optional[str] = ..., usage: Optional[int] = ...) -> None: ...

class ReqCreateRoom(_message.Message):
    __slots__ = ["mode", "player_count", "public_live"]
    MODE_FIELD_NUMBER: ClassVar[int]
    PLAYER_COUNT_FIELD_NUMBER: ClassVar[int]
    PUBLIC_LIVE_FIELD_NUMBER: ClassVar[int]
    mode: _dhs_pb2.GameMode
    player_count: int
    public_live: bool
    def __init__(self, player_count: Optional[int] = ..., mode: Optional[Union[_dhs_pb2.GameMode, Mapping]] = ..., public_live: bool = ...) -> None: ...

class ReqCreateWechatAppOrder(_message.Message):
    __slots__ = ["account_id", "account_ip", "client_type", "goods_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_IP_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    account_ip: str
    client_type: int
    goods_id: int
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., account_ip: Optional[str] = ...) -> None: ...

class ReqCreateWechatNativeOrder(_message.Message):
    __slots__ = ["account_id", "account_ip", "client_type", "goods_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_IP_FIELD_NUMBER: ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: ClassVar[int]
    GOODS_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    account_ip: str
    client_type: int
    goods_id: int
    def __init__(self, goods_id: Optional[int] = ..., client_type: Optional[int] = ..., account_id: Optional[int] = ..., account_ip: Optional[str] = ...) -> None: ...

class ReqCurrentMatchInfo(_message.Message):
    __slots__ = ["mode_list"]
    MODE_LIST_FIELD_NUMBER: ClassVar[int]
    mode_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, mode_list: Optional[Iterable[int]] = ...) -> None: ...

class ReqDeleteComment(_message.Message):
    __slots__ = ["delete_list", "target_id"]
    DELETE_LIST_FIELD_NUMBER: ClassVar[int]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    delete_list: _containers.RepeatedScalarFieldContainer[int]
    target_id: int
    def __init__(self, target_id: Optional[int] = ..., delete_list: Optional[Iterable[int]] = ...) -> None: ...

class ReqDeleteMail(_message.Message):
    __slots__ = ["mail_id"]
    MAIL_ID_FIELD_NUMBER: ClassVar[int]
    mail_id: int
    def __init__(self, mail_id: Optional[int] = ...) -> None: ...

class ReqDoActivitySignIn(_message.Message):
    __slots__ = ["activity_id"]
    ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
    activity_id: int
    def __init__(self, activity_id: Optional[int] = ...) -> None: ...

class ReqEmailLogin(_message.Message):
    __slots__ = ["client_version", "currency_platforms", "device", "email", "gen_access_token", "password", "random_key", "reconnect"]
    CLIENT_VERSION_FIELD_NUMBER: ClassVar[int]
    CURRENCY_PLATFORMS_FIELD_NUMBER: ClassVar[int]
    DEVICE_FIELD_NUMBER: ClassVar[int]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    GEN_ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    PASSWORD_FIELD_NUMBER: ClassVar[int]
    RANDOM_KEY_FIELD_NUMBER: ClassVar[int]
    RECONNECT_FIELD_NUMBER: ClassVar[int]
    client_version: str
    currency_platforms: _containers.RepeatedScalarFieldContainer[int]
    device: _dhs_pb2.ClientDeviceInfo
    email: str
    gen_access_token: bool
    password: str
    random_key: str
    reconnect: bool
    def __init__(self, email: Optional[str] = ..., password: Optional[str] = ..., reconnect: bool = ..., device: Optional[Union[_dhs_pb2.ClientDeviceInfo, Mapping]] = ..., random_key: Optional[str] = ..., client_version: Optional[str] = ..., gen_access_token: bool = ..., currency_platforms: Optional[Iterable[int]] = ...) -> None: ...

class ReqEnterCustomizedContest(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqExchangeActivityItem(_message.Message):
    __slots__ = ["exchange_id"]
    EXCHANGE_ID_FIELD_NUMBER: ClassVar[int]
    exchange_id: int
    def __init__(self, exchange_id: Optional[int] = ...) -> None: ...

class ReqExchangeCurrency(_message.Message):
    __slots__ = ["count", "id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    count: int
    id: int
    def __init__(self, id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...

class ReqFetchActivityFlipInfo(_message.Message):
    __slots__ = ["activity_id"]
    ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
    activity_id: int
    def __init__(self, activity_id: Optional[int] = ...) -> None: ...

class ReqFetchCommentContent(_message.Message):
    __slots__ = ["comment_id_list", "target_id"]
    COMMENT_ID_LIST_FIELD_NUMBER: ClassVar[int]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    comment_id_list: _containers.RepeatedScalarFieldContainer[int]
    target_id: int
    def __init__(self, target_id: Optional[int] = ..., comment_id_list: Optional[Iterable[int]] = ...) -> None: ...

class ReqFetchCommentList(_message.Message):
    __slots__ = ["target_id"]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    target_id: int
    def __init__(self, target_id: Optional[int] = ...) -> None: ...

class ReqFetchCustomizedContestByContestId(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: ClassVar[int]
    contest_id: int
    def __init__(self, contest_id: Optional[int] = ...) -> None: ...

class ReqFetchCustomizedContestExtendInfo(_message.Message):
    __slots__ = ["uid_list"]
    UID_LIST_FIELD_NUMBER: ClassVar[int]
    uid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, uid_list: Optional[Iterable[int]] = ...) -> None: ...

class ReqFetchCustomizedContestGameLiveList(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqFetchCustomizedContestGameRecords(_message.Message):
    __slots__ = ["last_index", "unique_id"]
    LAST_INDEX_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    last_index: int
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., last_index: Optional[int] = ...) -> None: ...

class ReqFetchCustomizedContestList(_message.Message):
    __slots__ = ["count", "start"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    START_FIELD_NUMBER: ClassVar[int]
    count: int
    start: int
    def __init__(self, start: Optional[int] = ..., count: Optional[int] = ...) -> None: ...

class ReqFetchCustomizedContestOnlineInfo(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqFetchRankPointLeaderboard(_message.Message):
    __slots__ = ["leaderboard_id"]
    LEADERBOARD_ID_FIELD_NUMBER: ClassVar[int]
    leaderboard_id: int
    def __init__(self, leaderboard_id: Optional[int] = ...) -> None: ...

class ReqGMCommand(_message.Message):
    __slots__ = ["command"]
    COMMAND_FIELD_NUMBER: ClassVar[int]
    command: str
    def __init__(self, command: Optional[str] = ...) -> None: ...

class ReqGMCommandInGaming(_message.Message):
    __slots__ = ["json_data"]
    JSON_DATA_FIELD_NUMBER: ClassVar[int]
    json_data: str
    def __init__(self, json_data: Optional[str] = ...) -> None: ...

class ReqGainAccumulatedPointActivityReward(_message.Message):
    __slots__ = ["activity_id", "reward_id"]
    ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
    REWARD_ID_FIELD_NUMBER: ClassVar[int]
    activity_id: int
    reward_id: int
    def __init__(self, activity_id: Optional[int] = ..., reward_id: Optional[int] = ...) -> None: ...

class ReqGainRankPointReward(_message.Message):
    __slots__ = ["activity_id", "leaderboard_id"]
    ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
    LEADERBOARD_ID_FIELD_NUMBER: ClassVar[int]
    activity_id: int
    leaderboard_id: int
    def __init__(self, leaderboard_id: Optional[int] = ..., activity_id: Optional[int] = ...) -> None: ...

class ReqGainVipReward(_message.Message):
    __slots__ = ["vip_level"]
    VIP_LEVEL_FIELD_NUMBER: ClassVar[int]
    vip_level: int
    def __init__(self, vip_level: Optional[int] = ...) -> None: ...

class ReqGameLiveInfo(_message.Message):
    __slots__ = ["game_uuid"]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    game_uuid: str
    def __init__(self, game_uuid: Optional[str] = ...) -> None: ...

class ReqGameLiveLeftSegment(_message.Message):
    __slots__ = ["game_uuid", "last_segment_id"]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    LAST_SEGMENT_ID_FIELD_NUMBER: ClassVar[int]
    game_uuid: str
    last_segment_id: int
    def __init__(self, game_uuid: Optional[str] = ..., last_segment_id: Optional[int] = ...) -> None: ...

class ReqGameLiveList(_message.Message):
    __slots__ = ["filter_id"]
    FILTER_ID_FIELD_NUMBER: ClassVar[int]
    filter_id: int
    def __init__(self, filter_id: Optional[int] = ...) -> None: ...

class ReqGameRecord(_message.Message):
    __slots__ = ["game_uuid"]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    game_uuid: str
    def __init__(self, game_uuid: Optional[str] = ...) -> None: ...

class ReqGameRecordList(_message.Message):
    __slots__ = ["count", "start", "type"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    START_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    count: int
    start: int
    type: int
    def __init__(self, start: Optional[int] = ..., count: Optional[int] = ..., type: Optional[int] = ...) -> None: ...

class ReqGameRecordsDetail(_message.Message):
    __slots__ = ["uuid_list"]
    UUID_LIST_FIELD_NUMBER: ClassVar[int]
    uuid_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid_list: Optional[Iterable[str]] = ...) -> None: ...

class ReqHandleFriendApply(_message.Message):
    __slots__ = ["method", "target_id"]
    METHOD_FIELD_NUMBER: ClassVar[int]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    method: int
    target_id: int
    def __init__(self, target_id: Optional[int] = ..., method: Optional[int] = ...) -> None: ...

class ReqHeatBeat(_message.Message):
    __slots__ = ["no_operation_counter"]
    NO_OPERATION_COUNTER_FIELD_NUMBER: ClassVar[int]
    no_operation_counter: int
    def __init__(self, no_operation_counter: Optional[int] = ...) -> None: ...

class ReqJoinCustomizedContestChatRoom(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqJoinMatchQueue(_message.Message):
    __slots__ = ["match_mode"]
    MATCH_MODE_FIELD_NUMBER: ClassVar[int]
    match_mode: int
    def __init__(self, match_mode: Optional[int] = ...) -> None: ...

class ReqJoinRoom(_message.Message):
    __slots__ = ["room_id"]
    ROOM_ID_FIELD_NUMBER: ClassVar[int]
    room_id: int
    def __init__(self, room_id: Optional[int] = ...) -> None: ...

class ReqLeaveComment(_message.Message):
    __slots__ = ["content", "target_id"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    content: str
    target_id: int
    def __init__(self, target_id: Optional[int] = ..., content: Optional[str] = ...) -> None: ...

class ReqLevelLeaderboard(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: ClassVar[int]
    type: int
    def __init__(self, type: Optional[int] = ...) -> None: ...

class ReqLogin(_message.Message):
    __slots__ = ["account", "client_version", "currency_platforms", "device", "gen_access_token", "password", "random_key", "reconnect", "type"]
    ACCOUNT_FIELD_NUMBER: ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: ClassVar[int]
    CURRENCY_PLATFORMS_FIELD_NUMBER: ClassVar[int]
    DEVICE_FIELD_NUMBER: ClassVar[int]
    GEN_ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    PASSWORD_FIELD_NUMBER: ClassVar[int]
    RANDOM_KEY_FIELD_NUMBER: ClassVar[int]
    RECONNECT_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    account: str
    client_version: str
    currency_platforms: _containers.RepeatedScalarFieldContainer[int]
    device: _dhs_pb2.ClientDeviceInfo
    gen_access_token: bool
    password: str
    random_key: str
    reconnect: bool
    type: int
    def __init__(self, account: Optional[str] = ..., password: Optional[str] = ..., reconnect: bool = ..., device: Optional[Union[_dhs_pb2.ClientDeviceInfo, Mapping]] = ..., random_key: Optional[str] = ..., client_version: Optional[str] = ..., gen_access_token: bool = ..., currency_platforms: Optional[Iterable[int]] = ..., type: Optional[int] = ...) -> None: ...

class ReqLoginBeat(_message.Message):
    __slots__ = ["contract"]
    CONTRACT_FIELD_NUMBER: ClassVar[int]
    contract: str
    def __init__(self, contract: Optional[str] = ...) -> None: ...

class ReqLogout(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReqModifyBirthday(_message.Message):
    __slots__ = ["birthday"]
    BIRTHDAY_FIELD_NUMBER: ClassVar[int]
    birthday: int
    def __init__(self, birthday: Optional[int] = ...) -> None: ...

class ReqModifyNickname(_message.Message):
    __slots__ = ["nickname", "use_item_id"]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    USE_ITEM_ID_FIELD_NUMBER: ClassVar[int]
    nickname: str
    use_item_id: int
    def __init__(self, nickname: Optional[str] = ..., use_item_id: Optional[int] = ...) -> None: ...

class ReqModifyPassword(_message.Message):
    __slots__ = ["new_password", "old_password", "secure_token"]
    NEW_PASSWORD_FIELD_NUMBER: ClassVar[int]
    OLD_PASSWORD_FIELD_NUMBER: ClassVar[int]
    SECURE_TOKEN_FIELD_NUMBER: ClassVar[int]
    new_password: str
    old_password: str
    secure_token: str
    def __init__(self, new_password: Optional[str] = ..., old_password: Optional[str] = ..., secure_token: Optional[str] = ...) -> None: ...

class ReqModifyRoom(_message.Message):
    __slots__ = ["robot_count"]
    ROBOT_COUNT_FIELD_NUMBER: ClassVar[int]
    robot_count: int
    def __init__(self, robot_count: Optional[int] = ...) -> None: ...

class ReqModifySignature(_message.Message):
    __slots__ = ["signature"]
    SIGNATURE_FIELD_NUMBER: ClassVar[int]
    signature: str
    def __init__(self, signature: Optional[str] = ...) -> None: ...

class ReqMultiAccountId(_message.Message):
    __slots__ = ["account_id_list"]
    ACCOUNT_ID_LIST_FIELD_NUMBER: ClassVar[int]
    account_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, account_id_list: Optional[Iterable[int]] = ...) -> None: ...

class ReqOauth2Auth(_message.Message):
    __slots__ = ["code", "type", "uid"]
    CODE_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    UID_FIELD_NUMBER: ClassVar[int]
    code: str
    type: int
    uid: str
    def __init__(self, type: Optional[int] = ..., code: Optional[str] = ..., uid: Optional[str] = ...) -> None: ...

class ReqOauth2Check(_message.Message):
    __slots__ = ["access_token", "type"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    access_token: str
    type: int
    def __init__(self, type: Optional[int] = ..., access_token: Optional[str] = ...) -> None: ...

class ReqOauth2Login(_message.Message):
    __slots__ = ["access_token", "client_version", "currency_platforms", "device", "random_key", "reconnect", "type"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: ClassVar[int]
    CURRENCY_PLATFORMS_FIELD_NUMBER: ClassVar[int]
    DEVICE_FIELD_NUMBER: ClassVar[int]
    RANDOM_KEY_FIELD_NUMBER: ClassVar[int]
    RECONNECT_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    access_token: str
    client_version: str
    currency_platforms: _containers.RepeatedScalarFieldContainer[int]
    device: _dhs_pb2.ClientDeviceInfo
    random_key: str
    reconnect: bool
    type: int
    def __init__(self, type: Optional[int] = ..., access_token: Optional[str] = ..., reconnect: bool = ..., device: Optional[Union[_dhs_pb2.ClientDeviceInfo, Mapping]] = ..., random_key: Optional[str] = ..., client_version: Optional[str] = ..., currency_platforms: Optional[Iterable[int]] = ...) -> None: ...

class ReqOauth2Signup(_message.Message):
    __slots__ = ["access_token", "advertise_str", "email", "type"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ADVERTISE_STR_FIELD_NUMBER: ClassVar[int]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    access_token: str
    advertise_str: str
    email: str
    type: int
    def __init__(self, type: Optional[int] = ..., access_token: Optional[str] = ..., email: Optional[str] = ..., advertise_str: Optional[str] = ...) -> None: ...

class ReqOpenChest(_message.Message):
    __slots__ = ["chest_id", "count", "use_ticket"]
    CHEST_ID_FIELD_NUMBER: ClassVar[int]
    COUNT_FIELD_NUMBER: ClassVar[int]
    USE_TICKET_FIELD_NUMBER: ClassVar[int]
    chest_id: int
    count: int
    use_ticket: bool
    def __init__(self, chest_id: Optional[int] = ..., count: Optional[int] = ..., use_ticket: bool = ...) -> None: ...

class ReqOpenManualItem(_message.Message):
    __slots__ = ["count", "item_id", "select_id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    ITEM_ID_FIELD_NUMBER: ClassVar[int]
    SELECT_ID_FIELD_NUMBER: ClassVar[int]
    count: int
    item_id: int
    select_id: int
    def __init__(self, item_id: Optional[int] = ..., count: Optional[int] = ..., select_id: Optional[int] = ...) -> None: ...

class ReqOpenRandomRewardItem(_message.Message):
    __slots__ = ["item_id"]
    ITEM_ID_FIELD_NUMBER: ClassVar[int]
    item_id: int
    def __init__(self, item_id: Optional[int] = ...) -> None: ...

class ReqPayMonthTicket(_message.Message):
    __slots__ = ["ticket_id"]
    TICKET_ID_FIELD_NUMBER: ClassVar[int]
    ticket_id: int
    def __init__(self, ticket_id: Optional[int] = ...) -> None: ...

class ReqPlatformBillingProducts(_message.Message):
    __slots__ = ["shelves_id"]
    SHELVES_ID_FIELD_NUMBER: ClassVar[int]
    shelves_id: int
    def __init__(self, shelves_id: Optional[int] = ...) -> None: ...

class ReqReadAnnouncement(_message.Message):
    __slots__ = ["announcement_id"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: ClassVar[int]
    announcement_id: int
    def __init__(self, announcement_id: Optional[int] = ...) -> None: ...

class ReqReadMail(_message.Message):
    __slots__ = ["mail_id"]
    MAIL_ID_FIELD_NUMBER: ClassVar[int]
    mail_id: int
    def __init__(self, mail_id: Optional[int] = ...) -> None: ...

class ReqRecieveActivityFlipTask(_message.Message):
    __slots__ = ["task_id"]
    TASK_ID_FIELD_NUMBER: ClassVar[int]
    task_id: int
    def __init__(self, task_id: Optional[int] = ...) -> None: ...

class ReqRefreshDailyTask(_message.Message):
    __slots__ = ["task_id"]
    TASK_ID_FIELD_NUMBER: ClassVar[int]
    task_id: int
    def __init__(self, task_id: Optional[int] = ...) -> None: ...

class ReqRemoveCollectedGameRecord(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: ClassVar[int]
    uuid: str
    def __init__(self, uuid: Optional[str] = ...) -> None: ...

class ReqRemoveFriend(_message.Message):
    __slots__ = ["target_id"]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    target_id: int
    def __init__(self, target_id: Optional[int] = ...) -> None: ...

class ReqRollingNotice(_message.Message):
    __slots__ = ["notice"]
    NOTICE_FIELD_NUMBER: ClassVar[int]
    notice: _dhs_pb2.RollingNotice
    def __init__(self, notice: Optional[Union[_dhs_pb2.RollingNotice, Mapping]] = ...) -> None: ...

class ReqRoomKick(_message.Message):
    __slots__ = ["account_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    def __init__(self, account_id: Optional[int] = ...) -> None: ...

class ReqRoomReady(_message.Message):
    __slots__ = ["ready"]
    READY_FIELD_NUMBER: ClassVar[int]
    ready: bool
    def __init__(self, ready: bool = ...) -> None: ...

class ReqRoomStart(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReqSayChatMessage(_message.Message):
    __slots__ = ["content"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    content: str
    def __init__(self, content: Optional[str] = ...) -> None: ...

class ReqSearchAccountById(_message.Message):
    __slots__ = ["account_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    def __init__(self, account_id: Optional[int] = ...) -> None: ...

class ReqSearchAccountByPattern(_message.Message):
    __slots__ = ["pattern", "search_next"]
    PATTERN_FIELD_NUMBER: ClassVar[int]
    SEARCH_NEXT_FIELD_NUMBER: ClassVar[int]
    pattern: str
    search_next: bool
    def __init__(self, search_next: bool = ..., pattern: Optional[str] = ...) -> None: ...

class ReqSelfOperation(_message.Message):
    __slots__ = ["cancel_operation", "index", "moqie", "tile", "timeuse", "type"]
    CANCEL_OPERATION_FIELD_NUMBER: ClassVar[int]
    INDEX_FIELD_NUMBER: ClassVar[int]
    MOQIE_FIELD_NUMBER: ClassVar[int]
    TILE_FIELD_NUMBER: ClassVar[int]
    TIMEUSE_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    cancel_operation: bool
    index: int
    moqie: bool
    tile: str
    timeuse: int
    type: int
    def __init__(self, type: Optional[int] = ..., index: Optional[int] = ..., tile: Optional[str] = ..., cancel_operation: bool = ..., moqie: bool = ..., timeuse: Optional[int] = ...) -> None: ...

class ReqSellItem(_message.Message):
    __slots__ = ["sells"]
    class Item(_message.Message):
        __slots__ = ["count", "item_id"]
        COUNT_FIELD_NUMBER: ClassVar[int]
        ITEM_ID_FIELD_NUMBER: ClassVar[int]
        count: int
        item_id: int
        def __init__(self, item_id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...
    SELLS_FIELD_NUMBER: ClassVar[int]
    sells: _containers.RepeatedCompositeFieldContainer[ReqSellItem.Item]
    def __init__(self, sells: Optional[Iterable[Union[ReqSellItem.Item, Mapping]]] = ...) -> None: ...

class ReqSendClientMessage(_message.Message):
    __slots__ = ["content", "target_id", "type"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    TARGET_ID_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    content: str
    target_id: int
    type: int
    def __init__(self, target_id: Optional[int] = ..., type: Optional[int] = ..., content: Optional[str] = ...) -> None: ...

class ReqSendGiftToCharacter(_message.Message):
    __slots__ = ["character_id", "gifts"]
    class Gift(_message.Message):
        __slots__ = ["count", "item_id"]
        COUNT_FIELD_NUMBER: ClassVar[int]
        ITEM_ID_FIELD_NUMBER: ClassVar[int]
        count: int
        item_id: int
        def __init__(self, item_id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...
    CHARACTER_ID_FIELD_NUMBER: ClassVar[int]
    GIFTS_FIELD_NUMBER: ClassVar[int]
    character_id: int
    gifts: _containers.RepeatedCompositeFieldContainer[ReqSendGiftToCharacter.Gift]
    def __init__(self, character_id: Optional[int] = ..., gifts: Optional[Iterable[Union[ReqSendGiftToCharacter.Gift, Mapping]]] = ...) -> None: ...

class ReqShopPurchase(_message.Message):
    __slots__ = ["id", "type"]
    ID_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    id: int
    type: str
    def __init__(self, type: Optional[str] = ..., id: Optional[int] = ...) -> None: ...

class ReqSignupAccount(_message.Message):
    __slots__ = ["account", "code", "password", "type"]
    ACCOUNT_FIELD_NUMBER: ClassVar[int]
    CODE_FIELD_NUMBER: ClassVar[int]
    PASSWORD_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    account: str
    code: str
    password: str
    type: int
    def __init__(self, account: Optional[str] = ..., password: Optional[str] = ..., code: Optional[str] = ..., type: Optional[int] = ...) -> None: ...

class ReqSolveGooglePlayOrder(_message.Message):
    __slots__ = ["inapp_data_signature", "inapp_purchase_data"]
    INAPP_DATA_SIGNATURE_FIELD_NUMBER: ClassVar[int]
    INAPP_PURCHASE_DATA_FIELD_NUMBER: ClassVar[int]
    inapp_data_signature: str
    inapp_purchase_data: str
    def __init__(self, inapp_purchase_data: Optional[str] = ..., inapp_data_signature: Optional[str] = ...) -> None: ...

class ReqStartCustomizedContest(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqSyncGame(_message.Message):
    __slots__ = ["round_id", "step"]
    ROUND_ID_FIELD_NUMBER: ClassVar[int]
    STEP_FIELD_NUMBER: ClassVar[int]
    round_id: str
    step: int
    def __init__(self, round_id: Optional[str] = ..., step: Optional[int] = ...) -> None: ...

class ReqTakeAttachment(_message.Message):
    __slots__ = ["mail_id"]
    MAIL_ID_FIELD_NUMBER: ClassVar[int]
    mail_id: int
    def __init__(self, mail_id: Optional[int] = ...) -> None: ...

class ReqTargetCustomizedContest(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqUpdateAccountSettings(_message.Message):
    __slots__ = ["setting"]
    SETTING_FIELD_NUMBER: ClassVar[int]
    setting: _dhs_pb2.AccountSetting
    def __init__(self, setting: Optional[Union[_dhs_pb2.AccountSetting, Mapping]] = ...) -> None: ...

class ReqUpdateClientValue(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    key: int
    value: int
    def __init__(self, key: Optional[int] = ..., value: Optional[int] = ...) -> None: ...

class ReqUpdateCommentSetting(_message.Message):
    __slots__ = ["comment_allow"]
    COMMENT_ALLOW_FIELD_NUMBER: ClassVar[int]
    comment_allow: int
    def __init__(self, comment_allow: Optional[int] = ...) -> None: ...

class ReqUpdateIDCardInfo(_message.Message):
    __slots__ = ["card_no", "fullname"]
    CARD_NO_FIELD_NUMBER: ClassVar[int]
    FULLNAME_FIELD_NUMBER: ClassVar[int]
    card_no: str
    fullname: str
    def __init__(self, fullname: Optional[str] = ..., card_no: Optional[str] = ...) -> None: ...

class ReqUpdateReadComment(_message.Message):
    __slots__ = ["read_id"]
    READ_ID_FIELD_NUMBER: ClassVar[int]
    read_id: int
    def __init__(self, read_id: Optional[int] = ...) -> None: ...

class ReqUpgradeCharacter(_message.Message):
    __slots__ = ["character_id"]
    CHARACTER_ID_FIELD_NUMBER: ClassVar[int]
    character_id: int
    def __init__(self, character_id: Optional[int] = ...) -> None: ...

class ReqUseBagItem(_message.Message):
    __slots__ = ["item_id"]
    ITEM_ID_FIELD_NUMBER: ClassVar[int]
    item_id: int
    def __init__(self, item_id: Optional[int] = ...) -> None: ...

class ReqUseGiftCode(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: ClassVar[int]
    code: str
    def __init__(self, code: Optional[str] = ...) -> None: ...

class ReqUseTitle(_message.Message):
    __slots__ = ["title"]
    TITLE_FIELD_NUMBER: ClassVar[int]
    title: int
    def __init__(self, title: Optional[int] = ...) -> None: ...

class ReqVerifyCodeForSecure(_message.Message):
    __slots__ = ["code", "operation"]
    CODE_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    code: str
    operation: int
    def __init__(self, code: Optional[str] = ..., operation: Optional[int] = ...) -> None: ...

class ResAccountActivityData(_message.Message):
    __slots__ = ["accumulated_point_list", "error", "exchange_records", "flip_task_progress_list", "rank_data_list", "sign_in_data", "task_progress_list"]
    class ActivitySignInData(_message.Message):
        __slots__ = ["activity_id", "sign_in_count"]
        ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
        SIGN_IN_COUNT_FIELD_NUMBER: ClassVar[int]
        activity_id: int
        sign_in_count: int
        def __init__(self, activity_id: Optional[int] = ..., sign_in_count: Optional[int] = ...) -> None: ...
    ACCUMULATED_POINT_LIST_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    EXCHANGE_RECORDS_FIELD_NUMBER: ClassVar[int]
    FLIP_TASK_PROGRESS_LIST_FIELD_NUMBER: ClassVar[int]
    RANK_DATA_LIST_FIELD_NUMBER: ClassVar[int]
    SIGN_IN_DATA_FIELD_NUMBER: ClassVar[int]
    TASK_PROGRESS_LIST_FIELD_NUMBER: ClassVar[int]
    accumulated_point_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.ActivityAccumulatedPointData]
    error: _dhs_pb2.Error
    exchange_records: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.ExchangeRecord]
    flip_task_progress_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.TaskProgress]
    rank_data_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.ActivityRankPointData]
    sign_in_data: _containers.RepeatedCompositeFieldContainer[ResAccountActivityData.ActivitySignInData]
    task_progress_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.TaskProgress]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., exchange_records: Optional[Iterable[Union[_dhs_pb2.ExchangeRecord, Mapping]]] = ..., task_progress_list: Optional[Iterable[Union[_dhs_pb2.TaskProgress, Mapping]]] = ..., accumulated_point_list: Optional[Iterable[Union[_dhs_pb2.ActivityAccumulatedPointData, Mapping]]] = ..., rank_data_list: Optional[Iterable[Union[_dhs_pb2.ActivityRankPointData, Mapping]]] = ..., flip_task_progress_list: Optional[Iterable[Union[_dhs_pb2.TaskProgress, Mapping]]] = ..., sign_in_data: Optional[Iterable[Union[ResAccountActivityData.ActivitySignInData, Mapping]]] = ...) -> None: ...

class ResAccountCharacterInfo(_message.Message):
    __slots__ = ["unlock_list"]
    UNLOCK_LIST_FIELD_NUMBER: ClassVar[int]
    unlock_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, unlock_list: Optional[Iterable[int]] = ...) -> None: ...

class ResAccountInfo(_message.Message):
    __slots__ = ["account", "error", "room"]
    ACCOUNT_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ROOM_FIELD_NUMBER: ClassVar[int]
    account: _dhs_pb2.Account
    error: _dhs_pb2.Error
    room: _dhs_pb2.Room
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., account: Optional[Union[_dhs_pb2.Account, Mapping]] = ..., room: Optional[Union[_dhs_pb2.Room, Mapping]] = ...) -> None: ...

class ResAccountSettings(_message.Message):
    __slots__ = ["error", "settings"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SETTINGS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    settings: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.AccountSetting]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., settings: Optional[Iterable[Union[_dhs_pb2.AccountSetting, Mapping]]] = ...) -> None: ...

class ResAccountStates(_message.Message):
    __slots__ = ["error", "states"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    STATES_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    states: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.AccountActiveState]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., states: Optional[Iterable[Union[_dhs_pb2.AccountActiveState, Mapping]]] = ...) -> None: ...

class ResAccountStatisticInfo(_message.Message):
    __slots__ = ["detail_data", "error", "statistic_data"]
    DETAIL_DATA_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    STATISTIC_DATA_FIELD_NUMBER: ClassVar[int]
    detail_data: _dhs_pb2.AccountDetailStatisticV2
    error: _dhs_pb2.Error
    statistic_data: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.AccountStatisticData]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., statistic_data: Optional[Iterable[Union[_dhs_pb2.AccountStatisticData, Mapping]]] = ..., detail_data: Optional[Union[_dhs_pb2.AccountDetailStatisticV2, Mapping]] = ...) -> None: ...

class ResAchievement(_message.Message):
    __slots__ = ["error", "progresses"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PROGRESSES_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    progresses: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.AchievementProgress]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., progresses: Optional[Iterable[Union[_dhs_pb2.AchievementProgress, Mapping]]] = ...) -> None: ...

class ResActivityList(_message.Message):
    __slots__ = ["activities", "error"]
    ACTIVITIES_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    activities: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.Activity]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., activities: Optional[Iterable[Union[_dhs_pb2.Activity, Mapping]]] = ...) -> None: ...

class ResAddCollectedGameRecord(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ...) -> None: ...

class ResAnnouncement(_message.Message):
    __slots__ = ["announcements", "error", "read_list", "sort"]
    ANNOUNCEMENTS_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    READ_LIST_FIELD_NUMBER: ClassVar[int]
    SORT_FIELD_NUMBER: ClassVar[int]
    announcements: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.Announcement]
    error: _dhs_pb2.Error
    read_list: _containers.RepeatedScalarFieldContainer[int]
    sort: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., announcements: Optional[Iterable[Union[_dhs_pb2.Announcement, Mapping]]] = ..., sort: Optional[Iterable[int]] = ..., read_list: Optional[Iterable[int]] = ...) -> None: ...

class ResAuthGame(_message.Message):
    __slots__ = ["error", "game_config", "is_game_start", "players", "ready_id_list", "seat_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    GAME_CONFIG_FIELD_NUMBER: ClassVar[int]
    IS_GAME_START_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    READY_ID_LIST_FIELD_NUMBER: ClassVar[int]
    SEAT_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    game_config: _dhs_pb2.GameConfig
    is_game_start: bool
    players: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.PlayerGameView]
    ready_id_list: _containers.RepeatedScalarFieldContainer[int]
    seat_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., players: Optional[Iterable[Union[_dhs_pb2.PlayerGameView, Mapping]]] = ..., seat_list: Optional[Iterable[int]] = ..., is_game_start: bool = ..., game_config: Optional[Union[_dhs_pb2.GameConfig, Mapping]] = ..., ready_id_list: Optional[Iterable[int]] = ...) -> None: ...

class ResBagInfo(_message.Message):
    __slots__ = ["bag", "error"]
    BAG_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    bag: _dhs_pb2.Bag
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., bag: Optional[Union[_dhs_pb2.Bag, Mapping]] = ...) -> None: ...

class ResBuyFromChestShop(_message.Message):
    __slots__ = ["chest_id", "consume_count", "error"]
    CHEST_ID_FIELD_NUMBER: ClassVar[int]
    CONSUME_COUNT_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    chest_id: int
    consume_count: int
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., chest_id: Optional[int] = ..., consume_count: Optional[int] = ...) -> None: ...

class ResBuyFromShop(_message.Message):
    __slots__ = ["error", "rewards"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    REWARDS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    rewards: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.RewardSlot]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., rewards: Optional[Iterable[Union[_dhs_pb2.RewardSlot, Mapping]]] = ...) -> None: ...

class ResChangeCollectedGameRecordRemarks(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ...) -> None: ...

class ResCharacterInfo(_message.Message):
    __slots__ = ["characters", "error", "main_character_id", "send_gift_count", "send_gift_limit", "skins"]
    CHARACTERS_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    MAIN_CHARACTER_ID_FIELD_NUMBER: ClassVar[int]
    SEND_GIFT_COUNT_FIELD_NUMBER: ClassVar[int]
    SEND_GIFT_LIMIT_FIELD_NUMBER: ClassVar[int]
    SKINS_FIELD_NUMBER: ClassVar[int]
    characters: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.Character]
    error: _dhs_pb2.Error
    main_character_id: int
    send_gift_count: int
    send_gift_limit: int
    skins: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., characters: Optional[Iterable[Union[_dhs_pb2.Character, Mapping]]] = ..., skins: Optional[Iterable[int]] = ..., main_character_id: Optional[int] = ..., send_gift_count: Optional[int] = ..., send_gift_limit: Optional[int] = ...) -> None: ...

class ResClientValue(_message.Message):
    __slots__ = ["datas", "recharged_count"]
    class Value(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: int
        def __init__(self, key: Optional[int] = ..., value: Optional[int] = ...) -> None: ...
    DATAS_FIELD_NUMBER: ClassVar[int]
    RECHARGED_COUNT_FIELD_NUMBER: ClassVar[int]
    datas: _containers.RepeatedCompositeFieldContainer[ResClientValue.Value]
    recharged_count: int
    def __init__(self, datas: Optional[Iterable[Union[ResClientValue.Value, Mapping]]] = ..., recharged_count: Optional[int] = ...) -> None: ...

class ResCollectedGameRecordList(_message.Message):
    __slots__ = ["error", "record_collect_limit", "record_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    RECORD_COLLECT_LIMIT_FIELD_NUMBER: ClassVar[int]
    RECORD_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    record_collect_limit: int
    record_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.RecordCollectedData]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., record_list: Optional[Iterable[Union[_dhs_pb2.RecordCollectedData, Mapping]]] = ..., record_collect_limit: Optional[int] = ...) -> None: ...

class ResCommentSetting(_message.Message):
    __slots__ = ["comment_allow", "error"]
    COMMENT_ALLOW_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    comment_allow: int
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., comment_allow: Optional[int] = ...) -> None: ...

class ResCommonView(_message.Message):
    __slots__ = ["error", "slots"]
    class Slot(_message.Message):
        __slots__ = ["slot", "value"]
        SLOT_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        slot: int
        value: int
        def __init__(self, slot: Optional[int] = ..., value: Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: ClassVar[int]
    SLOTS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    slots: _containers.RepeatedCompositeFieldContainer[ResCommonView.Slot]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., slots: Optional[Iterable[Union[ResCommonView.Slot, Mapping]]] = ...) -> None: ...

class ResConnectionInfo(_message.Message):
    __slots__ = ["client_endpoint", "error"]
    CLIENT_ENDPOINT_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    client_endpoint: _dhs_pb2.NetworkEndpoint
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., client_endpoint: Optional[Union[_dhs_pb2.NetworkEndpoint, Mapping]] = ...) -> None: ...

class ResCreateAlipayAppOrder(_message.Message):
    __slots__ = ["alipay_url", "error"]
    ALIPAY_URL_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    alipay_url: str
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., alipay_url: Optional[str] = ...) -> None: ...

class ResCreateAlipayOrder(_message.Message):
    __slots__ = ["alipay_url", "error"]
    ALIPAY_URL_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    alipay_url: str
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., alipay_url: Optional[str] = ...) -> None: ...

class ResCreateAlipayScanOrder(_message.Message):
    __slots__ = ["error", "order_id", "qr_code", "qrcode_buffer"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    QRCODE_BUFFER_FIELD_NUMBER: ClassVar[int]
    QR_CODE_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    qr_code: str
    qrcode_buffer: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., qrcode_buffer: Optional[str] = ..., order_id: Optional[str] = ..., qr_code: Optional[str] = ...) -> None: ...

class ResCreateBillingOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateENAlipayOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateENJCBOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateENMasterCardOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateENPaypalOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateENVisaOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateJPAuOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateJPCreditCardOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateJPDocomoOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateJPPaypalOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateJPSoftbankOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateJPWebMoneyOrder(_message.Message):
    __slots__ = ["error", "order_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCreateRoom(_message.Message):
    __slots__ = ["error", "room"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ROOM_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    room: _dhs_pb2.Room
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., room: Optional[Union[_dhs_pb2.Room, Mapping]] = ...) -> None: ...

class ResCreateWechatAppOrder(_message.Message):
    __slots__ = ["call_wechat_app_param", "error"]
    class CallWechatAppParam(_message.Message):
        __slots__ = ["appid", "noncestr", "package", "partnerid", "prepayid", "sign", "timestamp"]
        APPID_FIELD_NUMBER: ClassVar[int]
        NONCESTR_FIELD_NUMBER: ClassVar[int]
        PACKAGE_FIELD_NUMBER: ClassVar[int]
        PARTNERID_FIELD_NUMBER: ClassVar[int]
        PREPAYID_FIELD_NUMBER: ClassVar[int]
        SIGN_FIELD_NUMBER: ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: ClassVar[int]
        appid: str
        noncestr: str
        package: str
        partnerid: str
        prepayid: str
        sign: str
        timestamp: str
        def __init__(self, appid: Optional[str] = ..., partnerid: Optional[str] = ..., prepayid: Optional[str] = ..., package: Optional[str] = ..., noncestr: Optional[str] = ..., timestamp: Optional[str] = ..., sign: Optional[str] = ...) -> None: ...
    CALL_WECHAT_APP_PARAM_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    call_wechat_app_param: ResCreateWechatAppOrder.CallWechatAppParam
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., call_wechat_app_param: Optional[Union[ResCreateWechatAppOrder.CallWechatAppParam, Mapping]] = ...) -> None: ...

class ResCreateWechatNativeOrder(_message.Message):
    __slots__ = ["error", "order_id", "qrcode_buffer"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ORDER_ID_FIELD_NUMBER: ClassVar[int]
    QRCODE_BUFFER_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    order_id: str
    qrcode_buffer: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., qrcode_buffer: Optional[str] = ..., order_id: Optional[str] = ...) -> None: ...

class ResCurrentMatchInfo(_message.Message):
    __slots__ = ["error", "matches"]
    class CurrentMatchInfo(_message.Message):
        __slots__ = ["mode_id", "playing_count"]
        MODE_ID_FIELD_NUMBER: ClassVar[int]
        PLAYING_COUNT_FIELD_NUMBER: ClassVar[int]
        mode_id: int
        playing_count: int
        def __init__(self, mode_id: Optional[int] = ..., playing_count: Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: ClassVar[int]
    MATCHES_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    matches: _containers.RepeatedCompositeFieldContainer[ResCurrentMatchInfo.CurrentMatchInfo]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., matches: Optional[Iterable[Union[ResCurrentMatchInfo.CurrentMatchInfo, Mapping]]] = ...) -> None: ...

class ResDailySignInInfo(_message.Message):
    __slots__ = ["error", "sign_in_days"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SIGN_IN_DAYS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    sign_in_days: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., sign_in_days: Optional[int] = ...) -> None: ...

class ResDailyTask(_message.Message):
    __slots__ = ["error", "has_refresh_count", "max_daily_task_count", "progresses", "refresh_count"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    HAS_REFRESH_COUNT_FIELD_NUMBER: ClassVar[int]
    MAX_DAILY_TASK_COUNT_FIELD_NUMBER: ClassVar[int]
    PROGRESSES_FIELD_NUMBER: ClassVar[int]
    REFRESH_COUNT_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    has_refresh_count: bool
    max_daily_task_count: int
    progresses: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.TaskProgress]
    refresh_count: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., progresses: Optional[Iterable[Union[_dhs_pb2.TaskProgress, Mapping]]] = ..., has_refresh_count: bool = ..., max_daily_task_count: Optional[int] = ..., refresh_count: Optional[int] = ...) -> None: ...

class ResDoActivitySignIn(_message.Message):
    __slots__ = ["error", "rewards", "sign_in_count"]
    class RewardData(_message.Message):
        __slots__ = ["count", "resource_id"]
        COUNT_FIELD_NUMBER: ClassVar[int]
        RESOURCE_ID_FIELD_NUMBER: ClassVar[int]
        count: int
        resource_id: int
        def __init__(self, resource_id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: ClassVar[int]
    REWARDS_FIELD_NUMBER: ClassVar[int]
    SIGN_IN_COUNT_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    rewards: _containers.RepeatedCompositeFieldContainer[ResDoActivitySignIn.RewardData]
    sign_in_count: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., rewards: Optional[Iterable[Union[ResDoActivitySignIn.RewardData, Mapping]]] = ..., sign_in_count: Optional[int] = ...) -> None: ...

class ResEnterCustomizedContest(_message.Message):
    __slots__ = ["detail_info", "error", "is_followed", "player_report"]
    DETAIL_INFO_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    IS_FOLLOWED_FIELD_NUMBER: ClassVar[int]
    PLAYER_REPORT_FIELD_NUMBER: ClassVar[int]
    detail_info: _dhs_pb2.CustomizedContestDetail
    error: _dhs_pb2.Error
    is_followed: bool
    player_report: _dhs_pb2.CustomizedContestPlayerReport
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., detail_info: Optional[Union[_dhs_pb2.CustomizedContestDetail, Mapping]] = ..., player_report: Optional[Union[_dhs_pb2.CustomizedContestPlayerReport, Mapping]] = ..., is_followed: bool = ...) -> None: ...

class ResEnterGame(_message.Message):
    __slots__ = ["error", "game_restore", "is_end", "step"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    GAME_RESTORE_FIELD_NUMBER: ClassVar[int]
    IS_END_FIELD_NUMBER: ClassVar[int]
    STEP_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    game_restore: GameRestore
    is_end: bool
    step: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., is_end: bool = ..., step: Optional[int] = ..., game_restore: Optional[Union[GameRestore, Mapping]] = ...) -> None: ...

class ResExchangeActivityItem(_message.Message):
    __slots__ = ["error", "execute_reward"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    EXECUTE_REWARD_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    execute_reward: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.ExecuteReward]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., execute_reward: Optional[Iterable[Union[_dhs_pb2.ExecuteReward, Mapping]]] = ...) -> None: ...

class ResFetchActivityFlipInfo(_message.Message):
    __slots__ = ["count", "rewards"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    REWARDS_FIELD_NUMBER: ClassVar[int]
    count: int
    rewards: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, rewards: Optional[Iterable[int]] = ..., count: Optional[int] = ...) -> None: ...

class ResFetchCommentContent(_message.Message):
    __slots__ = ["comments", "error"]
    COMMENTS_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.CommentItem]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., comments: Optional[Iterable[Union[_dhs_pb2.CommentItem, Mapping]]] = ...) -> None: ...

class ResFetchCommentList(_message.Message):
    __slots__ = ["comment_allow", "comment_id_list", "error", "last_read_id"]
    COMMENT_ALLOW_FIELD_NUMBER: ClassVar[int]
    COMMENT_ID_LIST_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    LAST_READ_ID_FIELD_NUMBER: ClassVar[int]
    comment_allow: int
    comment_id_list: _containers.RepeatedScalarFieldContainer[int]
    error: _dhs_pb2.Error
    last_read_id: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., comment_allow: Optional[int] = ..., comment_id_list: Optional[Iterable[int]] = ..., last_read_id: Optional[int] = ...) -> None: ...

class ResFetchCustomizedContestByContestId(_message.Message):
    __slots__ = ["contest_info", "error"]
    CONTEST_INFO_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    contest_info: _dhs_pb2.CustomizedContestAbstract
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., contest_info: Optional[Union[_dhs_pb2.CustomizedContestAbstract, Mapping]] = ...) -> None: ...

class ResFetchCustomizedContestExtendInfo(_message.Message):
    __slots__ = ["error", "extend_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    EXTEND_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    extend_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.CustomizedContestExtend]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., extend_list: Optional[Iterable[Union[_dhs_pb2.CustomizedContestExtend, Mapping]]] = ...) -> None: ...

class ResFetchCustomizedContestGameLiveList(_message.Message):
    __slots__ = ["error", "live_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    LIVE_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    live_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.GameLiveHead]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., live_list: Optional[Iterable[Union[_dhs_pb2.GameLiveHead, Mapping]]] = ...) -> None: ...

class ResFetchCustomizedContestGameRecords(_message.Message):
    __slots__ = ["error", "next_index", "record_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    NEXT_INDEX_FIELD_NUMBER: ClassVar[int]
    RECORD_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    next_index: int
    record_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.RecordGame]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., next_index: Optional[int] = ..., record_list: Optional[Iterable[Union[_dhs_pb2.RecordGame, Mapping]]] = ...) -> None: ...

class ResFetchCustomizedContestList(_message.Message):
    __slots__ = ["contests", "error", "follow_contests"]
    CONTESTS_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    FOLLOW_CONTESTS_FIELD_NUMBER: ClassVar[int]
    contests: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.CustomizedContestBase]
    error: _dhs_pb2.Error
    follow_contests: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.CustomizedContestBase]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., contests: Optional[Iterable[Union[_dhs_pb2.CustomizedContestBase, Mapping]]] = ..., follow_contests: Optional[Iterable[Union[_dhs_pb2.CustomizedContestBase, Mapping]]] = ...) -> None: ...

class ResFetchCustomizedContestOnlineInfo(_message.Message):
    __slots__ = ["error", "online_player"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ONLINE_PLAYER_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    online_player: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., online_player: Optional[int] = ...) -> None: ...

class ResFetchRankPointLeaderboard(_message.Message):
    __slots__ = ["error", "items", "last_refresh_time"]
    class Item(_message.Message):
        __slots__ = ["account_id", "point", "rank", "view"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        POINT_FIELD_NUMBER: ClassVar[int]
        RANK_FIELD_NUMBER: ClassVar[int]
        VIEW_FIELD_NUMBER: ClassVar[int]
        account_id: int
        point: int
        rank: int
        view: _dhs_pb2.PlayerBaseView
        def __init__(self, account_id: Optional[int] = ..., rank: Optional[int] = ..., view: Optional[Union[_dhs_pb2.PlayerBaseView, Mapping]] = ..., point: Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: ClassVar[int]
    ITEMS_FIELD_NUMBER: ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    items: _containers.RepeatedCompositeFieldContainer[ResFetchRankPointLeaderboard.Item]
    last_refresh_time: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., items: Optional[Iterable[Union[ResFetchRankPointLeaderboard.Item, Mapping]]] = ..., last_refresh_time: Optional[int] = ...) -> None: ...

class ResFriendApplyList(_message.Message):
    __slots__ = ["applies", "error"]
    class FriendApply(_message.Message):
        __slots__ = ["account_id", "apply_time"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        APPLY_TIME_FIELD_NUMBER: ClassVar[int]
        account_id: int
        apply_time: int
        def __init__(self, account_id: Optional[int] = ..., apply_time: Optional[int] = ...) -> None: ...
    APPLIES_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    applies: _containers.RepeatedCompositeFieldContainer[ResFriendApplyList.FriendApply]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., applies: Optional[Iterable[Union[ResFriendApplyList.FriendApply, Mapping]]] = ...) -> None: ...

class ResFriendList(_message.Message):
    __slots__ = ["error", "friend_max_count", "friends"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    FRIENDS_FIELD_NUMBER: ClassVar[int]
    FRIEND_MAX_COUNT_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    friend_max_count: int
    friends: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.Friend]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., friends: Optional[Iterable[Union[_dhs_pb2.Friend, Mapping]]] = ..., friend_max_count: Optional[int] = ...) -> None: ...

class ResGameLiveInfo(_message.Message):
    __slots__ = ["error", "left_start_seconds", "live_head", "now_millisecond", "segments"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    LEFT_START_SECONDS_FIELD_NUMBER: ClassVar[int]
    LIVE_HEAD_FIELD_NUMBER: ClassVar[int]
    NOW_MILLISECOND_FIELD_NUMBER: ClassVar[int]
    SEGMENTS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    left_start_seconds: int
    live_head: _dhs_pb2.GameLiveHead
    now_millisecond: int
    segments: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.GameLiveSegmentUri]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., left_start_seconds: Optional[int] = ..., live_head: Optional[Union[_dhs_pb2.GameLiveHead, Mapping]] = ..., segments: Optional[Iterable[Union[_dhs_pb2.GameLiveSegmentUri, Mapping]]] = ..., now_millisecond: Optional[int] = ...) -> None: ...

class ResGameLiveLeftSegment(_message.Message):
    __slots__ = ["error", "live_state", "now_millisecond", "segment_end_millisecond", "segments"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    LIVE_STATE_FIELD_NUMBER: ClassVar[int]
    NOW_MILLISECOND_FIELD_NUMBER: ClassVar[int]
    SEGMENTS_FIELD_NUMBER: ClassVar[int]
    SEGMENT_END_MILLISECOND_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    live_state: int
    now_millisecond: int
    segment_end_millisecond: int
    segments: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.GameLiveSegmentUri]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., live_state: Optional[int] = ..., segments: Optional[Iterable[Union[_dhs_pb2.GameLiveSegmentUri, Mapping]]] = ..., now_millisecond: Optional[int] = ..., segment_end_millisecond: Optional[int] = ...) -> None: ...

class ResGameLiveList(_message.Message):
    __slots__ = ["error", "live_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    LIVE_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    live_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.GameLiveHead]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., live_list: Optional[Iterable[Union[_dhs_pb2.GameLiveHead, Mapping]]] = ...) -> None: ...

class ResGamePlayerState(_message.Message):
    __slots__ = ["error", "state_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    STATE_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    state_list: _containers.RepeatedScalarFieldContainer[_dhs_pb2.GamePlayerState]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., state_list: Optional[Iterable[Union[_dhs_pb2.GamePlayerState, str]]] = ...) -> None: ...

class ResGameRecord(_message.Message):
    __slots__ = ["data", "data_url", "error", "head"]
    DATA_FIELD_NUMBER: ClassVar[int]
    DATA_URL_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    HEAD_FIELD_NUMBER: ClassVar[int]
    data: bytes
    data_url: str
    error: _dhs_pb2.Error
    head: _dhs_pb2.RecordGame
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., head: Optional[Union[_dhs_pb2.RecordGame, Mapping]] = ..., data: Optional[bytes] = ..., data_url: Optional[str] = ...) -> None: ...

class ResGameRecordList(_message.Message):
    __slots__ = ["error", "record_list", "total_count"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    RECORD_LIST_FIELD_NUMBER: ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    record_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.RecordGame]
    total_count: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., total_count: Optional[int] = ..., record_list: Optional[Iterable[Union[_dhs_pb2.RecordGame, Mapping]]] = ...) -> None: ...

class ResGameRecordsDetail(_message.Message):
    __slots__ = ["error", "record_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    RECORD_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    record_list: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.RecordGame]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., record_list: Optional[Iterable[Union[_dhs_pb2.RecordGame, Mapping]]] = ...) -> None: ...

class ResIDCardInfo(_message.Message):
    __slots__ = ["country", "error", "is_authed"]
    COUNTRY_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    IS_AUTHED_FIELD_NUMBER: ClassVar[int]
    country: str
    error: _dhs_pb2.Error
    is_authed: bool
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., is_authed: bool = ..., country: Optional[str] = ...) -> None: ...

class ResJoinCustomizedContestChatRoom(_message.Message):
    __slots__ = ["chat_history", "error"]
    CHAT_HISTORY_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    chat_history: _containers.RepeatedScalarFieldContainer[bytes]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., chat_history: Optional[Iterable[bytes]] = ...) -> None: ...

class ResJoinRoom(_message.Message):
    __slots__ = ["error", "room"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ROOM_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    room: _dhs_pb2.Room
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., room: Optional[Union[_dhs_pb2.Room, Mapping]] = ...) -> None: ...

class ResLevelLeaderboard(_message.Message):
    __slots__ = ["error", "items", "self_rank"]
    class Item(_message.Message):
        __slots__ = ["account_id", "level"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        LEVEL_FIELD_NUMBER: ClassVar[int]
        account_id: int
        level: _dhs_pb2.AccountLevel
        def __init__(self, account_id: Optional[int] = ..., level: Optional[Union[_dhs_pb2.AccountLevel, Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: ClassVar[int]
    ITEMS_FIELD_NUMBER: ClassVar[int]
    SELF_RANK_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    items: _containers.RepeatedCompositeFieldContainer[ResLevelLeaderboard.Item]
    self_rank: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., items: Optional[Iterable[Union[ResLevelLeaderboard.Item, Mapping]]] = ..., self_rank: Optional[int] = ...) -> None: ...

class ResLogin(_message.Message):
    __slots__ = ["access_token", "account", "account_id", "error", "game_info", "has_unread_announcement"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    GAME_INFO_FIELD_NUMBER: ClassVar[int]
    HAS_UNREAD_ANNOUNCEMENT_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account: _dhs_pb2.Account
    account_id: int
    error: _dhs_pb2.Error
    game_info: _dhs_pb2.GameConnectInfo
    has_unread_announcement: bool
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., account_id: Optional[int] = ..., account: Optional[Union[_dhs_pb2.Account, Mapping]] = ..., game_info: Optional[Union[_dhs_pb2.GameConnectInfo, Mapping]] = ..., has_unread_announcement: bool = ..., access_token: Optional[str] = ...) -> None: ...

class ResLogout(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ...) -> None: ...

class ResMailInfo(_message.Message):
    __slots__ = ["error", "mails"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    MAILS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    mails: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.Mail]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., mails: Optional[Iterable[Union[_dhs_pb2.Mail, Mapping]]] = ...) -> None: ...

class ResMisc(_message.Message):
    __slots__ = ["error", "faiths", "recharged_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    FAITHS_FIELD_NUMBER: ClassVar[int]
    RECHARGED_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    faiths: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.FaithData]
    recharged_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., recharged_list: Optional[Iterable[int]] = ..., faiths: Optional[Iterable[Union[_dhs_pb2.FaithData, Mapping]]] = ...) -> None: ...

class ResModNicknameTime(_message.Message):
    __slots__ = ["last_mod_time"]
    LAST_MOD_TIME_FIELD_NUMBER: ClassVar[int]
    last_mod_time: int
    def __init__(self, last_mod_time: Optional[int] = ...) -> None: ...

class ResMonthTicketInfo(_message.Message):
    __slots__ = ["month_ticket_info"]
    MONTH_TICKET_INFO_FIELD_NUMBER: ClassVar[int]
    month_ticket_info: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.MonthTicketInfo]
    def __init__(self, month_ticket_info: Optional[Iterable[Union[_dhs_pb2.MonthTicketInfo, Mapping]]] = ...) -> None: ...

class ResMultiAccountBrief(_message.Message):
    __slots__ = ["error", "players"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    players: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.PlayerBaseView]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., players: Optional[Iterable[Union[_dhs_pb2.PlayerBaseView, Mapping]]] = ...) -> None: ...

class ResOauth2Auth(_message.Message):
    __slots__ = ["access_token", "error"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    access_token: str
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., access_token: Optional[str] = ...) -> None: ...

class ResOauth2Check(_message.Message):
    __slots__ = ["error", "has_account"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    HAS_ACCOUNT_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    has_account: bool
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., has_account: bool = ...) -> None: ...

class ResOauth2Signup(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ...) -> None: ...

class ResOpenChest(_message.Message):
    __slots__ = ["error", "results", "total_open_count"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    RESULTS_FIELD_NUMBER: ClassVar[int]
    TOTAL_OPEN_COUNT_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    results: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.OpenResult]
    total_open_count: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., results: Optional[Iterable[Union[_dhs_pb2.OpenResult, Mapping]]] = ..., total_open_count: Optional[int] = ...) -> None: ...

class ResOpenRandomRewardItem(_message.Message):
    __slots__ = ["error", "results"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    RESULTS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    results: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.OpenResult]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., results: Optional[Iterable[Union[_dhs_pb2.OpenResult, Mapping]]] = ...) -> None: ...

class ResPayMonthTicket(_message.Message):
    __slots__ = ["error", "resource_count", "resource_id"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    RESOURCE_COUNT_FIELD_NUMBER: ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    resource_count: int
    resource_id: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., resource_id: Optional[int] = ..., resource_count: Optional[int] = ...) -> None: ...

class ResPlatformBillingProducts(_message.Message):
    __slots__ = ["error", "products"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PRODUCTS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    products: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.BillingProduct]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., products: Optional[Iterable[Union[_dhs_pb2.BillingProduct, Mapping]]] = ...) -> None: ...

class ResRecieveActivityFlipTask(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    count: int
    def __init__(self, count: Optional[int] = ...) -> None: ...

class ResRefreshDailyTask(_message.Message):
    __slots__ = ["error", "progress", "refresh_count"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PROGRESS_FIELD_NUMBER: ClassVar[int]
    REFRESH_COUNT_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    progress: _dhs_pb2.TaskProgress
    refresh_count: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., progress: Optional[Union[_dhs_pb2.TaskProgress, Mapping]] = ..., refresh_count: Optional[int] = ...) -> None: ...

class ResRefreshZHPShop(_message.Message):
    __slots__ = ["error", "zhp"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ZHP_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    zhp: _dhs_pb2.ZHPShop
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., zhp: Optional[Union[_dhs_pb2.ZHPShop, Mapping]] = ...) -> None: ...

class ResRemoveCollectedGameRecord(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ...) -> None: ...

class ResReviveCoinInfo(_message.Message):
    __slots__ = ["error", "has_gained"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    HAS_GAINED_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    has_gained: bool
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., has_gained: bool = ...) -> None: ...

class ResSearchAccountById(_message.Message):
    __slots__ = ["error", "player"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PLAYER_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    player: _dhs_pb2.PlayerBaseView
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., player: Optional[Union[_dhs_pb2.PlayerBaseView, Mapping]] = ...) -> None: ...

class ResSearchAccountByPattern(_message.Message):
    __slots__ = ["decode_id", "error", "is_finished", "match_accounts"]
    DECODE_ID_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    IS_FINISHED_FIELD_NUMBER: ClassVar[int]
    MATCH_ACCOUNTS_FIELD_NUMBER: ClassVar[int]
    decode_id: int
    error: _dhs_pb2.Error
    is_finished: bool
    match_accounts: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., is_finished: bool = ..., match_accounts: Optional[Iterable[int]] = ..., decode_id: Optional[int] = ...) -> None: ...

class ResSelfRoom(_message.Message):
    __slots__ = ["error", "room"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    ROOM_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    room: _dhs_pb2.Room
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., room: Optional[Union[_dhs_pb2.Room, Mapping]] = ...) -> None: ...

class ResSendGiftToCharacter(_message.Message):
    __slots__ = ["error", "exp", "level"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    EXP_FIELD_NUMBER: ClassVar[int]
    LEVEL_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    exp: int
    level: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., level: Optional[int] = ..., exp: Optional[int] = ...) -> None: ...

class ResServerSettings(_message.Message):
    __slots__ = ["settings"]
    SETTINGS_FIELD_NUMBER: ClassVar[int]
    settings: _dhs_pb2.ServerSettings
    def __init__(self, settings: Optional[Union[_dhs_pb2.ServerSettings, Mapping]] = ...) -> None: ...

class ResServerTime(_message.Message):
    __slots__ = ["server_time"]
    SERVER_TIME_FIELD_NUMBER: ClassVar[int]
    server_time: int
    def __init__(self, server_time: Optional[int] = ...) -> None: ...

class ResShopInfo(_message.Message):
    __slots__ = ["error", "shop_info"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SHOP_INFO_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    shop_info: _dhs_pb2.ShopInfo
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., shop_info: Optional[Union[_dhs_pb2.ShopInfo, Mapping]] = ...) -> None: ...

class ResShopPurchase(_message.Message):
    __slots__ = ["error", "update"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    UPDATE_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    update: _dhs_pb2.AccountUpdate
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., update: Optional[Union[_dhs_pb2.AccountUpdate, Mapping]] = ...) -> None: ...

class ResSignupAccount(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ...) -> None: ...

class ResSyncGame(_message.Message):
    __slots__ = ["error", "game_restore", "is_end", "step"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    GAME_RESTORE_FIELD_NUMBER: ClassVar[int]
    IS_END_FIELD_NUMBER: ClassVar[int]
    STEP_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    game_restore: GameRestore
    is_end: bool
    step: int
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., is_end: bool = ..., step: Optional[int] = ..., game_restore: Optional[Union[GameRestore, Mapping]] = ...) -> None: ...

class ResTitleList(_message.Message):
    __slots__ = ["error", "title_list"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    TITLE_LIST_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    title_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., title_list: Optional[Iterable[int]] = ...) -> None: ...

class ResUpgradeCharacter(_message.Message):
    __slots__ = ["character", "error"]
    CHARACTER_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    character: _dhs_pb2.Character
    error: _dhs_pb2.Error
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., character: Optional[Union[_dhs_pb2.Character, Mapping]] = ...) -> None: ...

class ResUseGiftCode(_message.Message):
    __slots__ = ["error", "rewards"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    REWARDS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    rewards: _containers.RepeatedCompositeFieldContainer[_dhs_pb2.RewardSlot]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., rewards: Optional[Iterable[Union[_dhs_pb2.RewardSlot, Mapping]]] = ...) -> None: ...

class ResVerfiyCodeForSecure(_message.Message):
    __slots__ = ["error", "secure_token"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SECURE_TOKEN_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    secure_token: str
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., secure_token: Optional[str] = ...) -> None: ...

class ResVipReward(_message.Message):
    __slots__ = ["error", "gained_vip_levels"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    GAINED_VIP_LEVELS_FIELD_NUMBER: ClassVar[int]
    error: _dhs_pb2.Error
    gained_vip_levels: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[_dhs_pb2.Error, Mapping]] = ..., gained_vip_levels: Optional[Iterable[int]] = ...) -> None: ...

class TingPaiDiscardInfo(_message.Message):
    __slots__ = ["infos", "tile", "zhenting"]
    INFOS_FIELD_NUMBER: ClassVar[int]
    TILE_FIELD_NUMBER: ClassVar[int]
    ZHENTING_FIELD_NUMBER: ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[TingPaiInfo]
    tile: str
    zhenting: bool
    def __init__(self, tile: Optional[str] = ..., zhenting: bool = ..., infos: Optional[Iterable[Union[TingPaiInfo, Mapping]]] = ...) -> None: ...

class TingPaiInfo(_message.Message):
    __slots__ = ["biao_dora_count", "count", "fu", "haveyi", "tile", "yiman"]
    BIAO_DORA_COUNT_FIELD_NUMBER: ClassVar[int]
    COUNT_FIELD_NUMBER: ClassVar[int]
    FU_FIELD_NUMBER: ClassVar[int]
    HAVEYI_FIELD_NUMBER: ClassVar[int]
    TILE_FIELD_NUMBER: ClassVar[int]
    YIMAN_FIELD_NUMBER: ClassVar[int]
    biao_dora_count: int
    count: int
    fu: int
    haveyi: bool
    tile: str
    yiman: bool
    def __init__(self, tile: Optional[str] = ..., haveyi: bool = ..., yiman: bool = ..., count: Optional[int] = ..., fu: Optional[int] = ..., biao_dora_count: Optional[int] = ...) -> None: ...
