from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Text, Union

AUTH: GamePlayerState
DESCRIPTOR: _descriptor.FileDescriptor
NULL: GamePlayerState
READY: GamePlayerState
SYNCING: GamePlayerState

class Account(_message.Message):
    __slots__ = ["account_id", "anti_addiction", "avatar_id", "birthday", "diamond", "email", "email_verify", "gold", "level", "level3", "login_time", "logout_time", "nickname", "phone", "phone_verify", "platform_diamond", "room_id", "signature", "title", "vip"]
    class PlatformDiamond(_message.Message):
        __slots__ = ["count", "id"]
        COUNT_FIELD_NUMBER: ClassVar[int]
        ID_FIELD_NUMBER: ClassVar[int]
        count: int
        id: int
        def __init__(self, id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    ANTI_ADDICTION_FIELD_NUMBER: ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: ClassVar[int]
    DIAMOND_FIELD_NUMBER: ClassVar[int]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    EMAIL_VERIFY_FIELD_NUMBER: ClassVar[int]
    GOLD_FIELD_NUMBER: ClassVar[int]
    LEVEL3_FIELD_NUMBER: ClassVar[int]
    LEVEL_FIELD_NUMBER: ClassVar[int]
    LOGIN_TIME_FIELD_NUMBER: ClassVar[int]
    LOGOUT_TIME_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    PHONE_FIELD_NUMBER: ClassVar[int]
    PHONE_VERIFY_FIELD_NUMBER: ClassVar[int]
    PLATFORM_DIAMOND_FIELD_NUMBER: ClassVar[int]
    ROOM_ID_FIELD_NUMBER: ClassVar[int]
    SIGNATURE_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    VIP_FIELD_NUMBER: ClassVar[int]
    account_id: int
    anti_addiction: AntiAddiction
    avatar_id: int
    birthday: int
    diamond: int
    email: str
    email_verify: int
    gold: int
    level: AccountLevel
    level3: AccountLevel
    login_time: int
    logout_time: int
    nickname: str
    phone: str
    phone_verify: int
    platform_diamond: _containers.RepeatedCompositeFieldContainer[Account.PlatformDiamond]
    room_id: int
    signature: str
    title: int
    vip: int
    def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ..., login_time: Optional[int] = ..., logout_time: Optional[int] = ..., room_id: Optional[int] = ..., anti_addiction: Optional[Union[AntiAddiction, Mapping]] = ..., title: Optional[int] = ..., signature: Optional[str] = ..., email: Optional[str] = ..., email_verify: Optional[int] = ..., gold: Optional[int] = ..., diamond: Optional[int] = ..., avatar_id: Optional[int] = ..., vip: Optional[int] = ..., birthday: Optional[int] = ..., phone: Optional[str] = ..., phone_verify: Optional[int] = ..., platform_diamond: Optional[Iterable[Union[Account.PlatformDiamond, Mapping]]] = ..., level: Optional[Union[AccountLevel, Mapping]] = ..., level3: Optional[Union[AccountLevel, Mapping]] = ...) -> None: ...

class AccountActiveState(_message.Message):
    __slots__ = ["account_id", "is_online", "login_time", "logout_time", "playing"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: ClassVar[int]
    LOGIN_TIME_FIELD_NUMBER: ClassVar[int]
    LOGOUT_TIME_FIELD_NUMBER: ClassVar[int]
    PLAYING_FIELD_NUMBER: ClassVar[int]
    account_id: int
    is_online: bool
    login_time: int
    logout_time: int
    playing: AccountPlayingGame
    def __init__(self, account_id: Optional[int] = ..., login_time: Optional[int] = ..., logout_time: Optional[int] = ..., is_online: bool = ..., playing: Optional[Union[AccountPlayingGame, Mapping]] = ...) -> None: ...

class AccountCacheView(_message.Message):
    __slots__ = ["account_id", "avatar_id", "cache_version", "is_online", "level", "level3", "login_time", "logout_time", "nickname", "playing_game", "room_id", "title", "vip"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: ClassVar[int]
    CACHE_VERSION_FIELD_NUMBER: ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: ClassVar[int]
    LEVEL3_FIELD_NUMBER: ClassVar[int]
    LEVEL_FIELD_NUMBER: ClassVar[int]
    LOGIN_TIME_FIELD_NUMBER: ClassVar[int]
    LOGOUT_TIME_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    PLAYING_GAME_FIELD_NUMBER: ClassVar[int]
    ROOM_ID_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    VIP_FIELD_NUMBER: ClassVar[int]
    account_id: int
    avatar_id: int
    cache_version: int
    is_online: bool
    level: AccountLevel
    level3: AccountLevel
    login_time: int
    logout_time: int
    nickname: str
    playing_game: AccountPlayingGame
    room_id: int
    title: int
    vip: int
    def __init__(self, cache_version: Optional[int] = ..., account_id: Optional[int] = ..., nickname: Optional[str] = ..., login_time: Optional[int] = ..., logout_time: Optional[int] = ..., is_online: bool = ..., room_id: Optional[int] = ..., title: Optional[int] = ..., avatar_id: Optional[int] = ..., vip: Optional[int] = ..., level: Optional[Union[AccountLevel, Mapping]] = ..., playing_game: Optional[Union[AccountPlayingGame, Mapping]] = ..., level3: Optional[Union[AccountLevel, Mapping]] = ...) -> None: ...

class AccountDetailStatistic(_message.Message):
    __slots__ = ["fan", "fan_achieved", "game_mode", "liujumanguan"]
    FAN_ACHIEVED_FIELD_NUMBER: ClassVar[int]
    FAN_FIELD_NUMBER: ClassVar[int]
    GAME_MODE_FIELD_NUMBER: ClassVar[int]
    LIUJUMANGUAN_FIELD_NUMBER: ClassVar[int]
    fan: _containers.RepeatedCompositeFieldContainer[AccountStatisticByFan]
    fan_achieved: _containers.RepeatedCompositeFieldContainer[AccountFanAchieved]
    game_mode: _containers.RepeatedCompositeFieldContainer[AccountStatisticByGameMode]
    liujumanguan: int
    def __init__(self, game_mode: Optional[Iterable[Union[AccountStatisticByGameMode, Mapping]]] = ..., fan: Optional[Iterable[Union[AccountStatisticByFan, Mapping]]] = ..., liujumanguan: Optional[int] = ..., fan_achieved: Optional[Iterable[Union[AccountFanAchieved, Mapping]]] = ...) -> None: ...

class AccountDetailStatisticByCategory(_message.Message):
    __slots__ = ["category", "detail_statistic"]
    CATEGORY_FIELD_NUMBER: ClassVar[int]
    DETAIL_STATISTIC_FIELD_NUMBER: ClassVar[int]
    category: int
    detail_statistic: AccountDetailStatistic
    def __init__(self, category: Optional[int] = ..., detail_statistic: Optional[Union[AccountDetailStatistic, Mapping]] = ...) -> None: ...

class AccountDetailStatisticV2(_message.Message):
    __slots__ = ["customized_contest_statistic", "friend_room_statistic", "leisure_match_statistic", "rank_statistic"]
    class CustomizedContestStatistic(_message.Message):
        __slots__ = ["month_refresh_time", "month_statistic", "total_statistic"]
        MONTH_REFRESH_TIME_FIELD_NUMBER: ClassVar[int]
        MONTH_STATISTIC_FIELD_NUMBER: ClassVar[int]
        TOTAL_STATISTIC_FIELD_NUMBER: ClassVar[int]
        month_refresh_time: int
        month_statistic: AccountDetailStatistic
        total_statistic: AccountDetailStatistic
        def __init__(self, total_statistic: Optional[Union[AccountDetailStatistic, Mapping]] = ..., month_statistic: Optional[Union[AccountDetailStatistic, Mapping]] = ..., month_refresh_time: Optional[int] = ...) -> None: ...
    class RankStatistic(_message.Message):
        __slots__ = ["month_refresh_time", "month_statistic", "total_statistic"]
        class RankData(_message.Message):
            __slots__ = ["all_level_statistic", "level_data_list"]
            class RankLevelData(_message.Message):
                __slots__ = ["rank_level", "statistic"]
                RANK_LEVEL_FIELD_NUMBER: ClassVar[int]
                STATISTIC_FIELD_NUMBER: ClassVar[int]
                rank_level: int
                statistic: AccountDetailStatistic
                def __init__(self, rank_level: Optional[int] = ..., statistic: Optional[Union[AccountDetailStatistic, Mapping]] = ...) -> None: ...
            ALL_LEVEL_STATISTIC_FIELD_NUMBER: ClassVar[int]
            LEVEL_DATA_LIST_FIELD_NUMBER: ClassVar[int]
            all_level_statistic: AccountDetailStatistic
            level_data_list: _containers.RepeatedCompositeFieldContainer[AccountDetailStatisticV2.RankStatistic.RankData.RankLevelData]
            def __init__(self, all_level_statistic: Optional[Union[AccountDetailStatistic, Mapping]] = ..., level_data_list: Optional[Iterable[Union[AccountDetailStatisticV2.RankStatistic.RankData.RankLevelData, Mapping]]] = ...) -> None: ...
        MONTH_REFRESH_TIME_FIELD_NUMBER: ClassVar[int]
        MONTH_STATISTIC_FIELD_NUMBER: ClassVar[int]
        TOTAL_STATISTIC_FIELD_NUMBER: ClassVar[int]
        month_refresh_time: int
        month_statistic: AccountDetailStatisticV2.RankStatistic.RankData
        total_statistic: AccountDetailStatisticV2.RankStatistic.RankData
        def __init__(self, total_statistic: Optional[Union[AccountDetailStatisticV2.RankStatistic.RankData, Mapping]] = ..., month_statistic: Optional[Union[AccountDetailStatisticV2.RankStatistic.RankData, Mapping]] = ..., month_refresh_time: Optional[int] = ...) -> None: ...
    CUSTOMIZED_CONTEST_STATISTIC_FIELD_NUMBER: ClassVar[int]
    FRIEND_ROOM_STATISTIC_FIELD_NUMBER: ClassVar[int]
    LEISURE_MATCH_STATISTIC_FIELD_NUMBER: ClassVar[int]
    RANK_STATISTIC_FIELD_NUMBER: ClassVar[int]
    customized_contest_statistic: AccountDetailStatisticV2.CustomizedContestStatistic
    friend_room_statistic: AccountDetailStatistic
    leisure_match_statistic: AccountDetailStatistic
    rank_statistic: AccountDetailStatisticV2.RankStatistic
    def __init__(self, friend_room_statistic: Optional[Union[AccountDetailStatistic, Mapping]] = ..., rank_statistic: Optional[Union[AccountDetailStatisticV2.RankStatistic, Mapping]] = ..., customized_contest_statistic: Optional[Union[AccountDetailStatisticV2.CustomizedContestStatistic, Mapping]] = ..., leisure_match_statistic: Optional[Union[AccountDetailStatistic, Mapping]] = ...) -> None: ...

class AccountFanAchieved(_message.Message):
    __slots__ = ["fan", "liujumanguan", "mahjong_category"]
    FAN_FIELD_NUMBER: ClassVar[int]
    LIUJUMANGUAN_FIELD_NUMBER: ClassVar[int]
    MAHJONG_CATEGORY_FIELD_NUMBER: ClassVar[int]
    fan: _containers.RepeatedCompositeFieldContainer[AccountStatisticByFan]
    liujumanguan: int
    mahjong_category: int
    def __init__(self, mahjong_category: Optional[int] = ..., fan: Optional[Iterable[Union[AccountStatisticByFan, Mapping]]] = ..., liujumanguan: Optional[int] = ...) -> None: ...

class AccountLevel(_message.Message):
    __slots__ = ["id", "score"]
    ID_FIELD_NUMBER: ClassVar[int]
    SCORE_FIELD_NUMBER: ClassVar[int]
    id: int
    score: int
    def __init__(self, id: Optional[int] = ..., score: Optional[int] = ...) -> None: ...

class AccountMahjongStatistic(_message.Message):
    __slots__ = ["final_position_counts", "highest_hu", "recent_10_game_result", "recent_10_hu_summary", "recent_20_hu_summary", "recent_hu", "recent_round"]
    class GameResult(_message.Message):
        __slots__ = ["final_point", "rank"]
        FINAL_POINT_FIELD_NUMBER: ClassVar[int]
        RANK_FIELD_NUMBER: ClassVar[int]
        final_point: int
        rank: int
        def __init__(self, rank: Optional[int] = ..., final_point: Optional[int] = ...) -> None: ...
    class HighestHuRecord(_message.Message):
        __slots__ = ["doranum", "fanshu", "hands", "hupai", "ming", "title", "title_id"]
        DORANUM_FIELD_NUMBER: ClassVar[int]
        FANSHU_FIELD_NUMBER: ClassVar[int]
        HANDS_FIELD_NUMBER: ClassVar[int]
        HUPAI_FIELD_NUMBER: ClassVar[int]
        MING_FIELD_NUMBER: ClassVar[int]
        TITLE_FIELD_NUMBER: ClassVar[int]
        TITLE_ID_FIELD_NUMBER: ClassVar[int]
        doranum: int
        fanshu: int
        hands: _containers.RepeatedScalarFieldContainer[str]
        hupai: str
        ming: _containers.RepeatedScalarFieldContainer[str]
        title: str
        title_id: int
        def __init__(self, fanshu: Optional[int] = ..., doranum: Optional[int] = ..., title: Optional[str] = ..., hands: Optional[Iterable[str]] = ..., ming: Optional[Iterable[str]] = ..., hupai: Optional[str] = ..., title_id: Optional[int] = ...) -> None: ...
    class HuSummary(_message.Message):
        __slots__ = ["dora_round_count", "total_count", "total_fan"]
        DORA_ROUND_COUNT_FIELD_NUMBER: ClassVar[int]
        TOTAL_COUNT_FIELD_NUMBER: ClassVar[int]
        TOTAL_FAN_FIELD_NUMBER: ClassVar[int]
        dora_round_count: int
        total_count: int
        total_fan: int
        def __init__(self, total_count: Optional[int] = ..., dora_round_count: Optional[int] = ..., total_fan: Optional[int] = ...) -> None: ...
    class LiQi10Summary(_message.Message):
        __slots__ = ["total_fanshu", "total_xuanshang"]
        TOTAL_FANSHU_FIELD_NUMBER: ClassVar[int]
        TOTAL_XUANSHANG_FIELD_NUMBER: ClassVar[int]
        total_fanshu: int
        total_xuanshang: int
        def __init__(self, total_xuanshang: Optional[int] = ..., total_fanshu: Optional[int] = ...) -> None: ...
    class Liqi20Summary(_message.Message):
        __slots__ = ["average_hu_point", "total_count", "total_lidora_count"]
        AVERAGE_HU_POINT_FIELD_NUMBER: ClassVar[int]
        TOTAL_COUNT_FIELD_NUMBER: ClassVar[int]
        TOTAL_LIDORA_COUNT_FIELD_NUMBER: ClassVar[int]
        average_hu_point: int
        total_count: int
        total_lidora_count: int
        def __init__(self, total_count: Optional[int] = ..., total_lidora_count: Optional[int] = ..., average_hu_point: Optional[int] = ...) -> None: ...
    class RoundSummary(_message.Message):
        __slots__ = ["fangchong_count", "rong_count", "total_count", "zimo_count"]
        FANGCHONG_COUNT_FIELD_NUMBER: ClassVar[int]
        RONG_COUNT_FIELD_NUMBER: ClassVar[int]
        TOTAL_COUNT_FIELD_NUMBER: ClassVar[int]
        ZIMO_COUNT_FIELD_NUMBER: ClassVar[int]
        fangchong_count: int
        rong_count: int
        total_count: int
        zimo_count: int
        def __init__(self, total_count: Optional[int] = ..., rong_count: Optional[int] = ..., zimo_count: Optional[int] = ..., fangchong_count: Optional[int] = ...) -> None: ...
    FINAL_POSITION_COUNTS_FIELD_NUMBER: ClassVar[int]
    HIGHEST_HU_FIELD_NUMBER: ClassVar[int]
    RECENT_10_GAME_RESULT_FIELD_NUMBER: ClassVar[int]
    RECENT_10_HU_SUMMARY_FIELD_NUMBER: ClassVar[int]
    RECENT_20_HU_SUMMARY_FIELD_NUMBER: ClassVar[int]
    RECENT_HU_FIELD_NUMBER: ClassVar[int]
    RECENT_ROUND_FIELD_NUMBER: ClassVar[int]
    final_position_counts: _containers.RepeatedScalarFieldContainer[int]
    highest_hu: AccountMahjongStatistic.HighestHuRecord
    recent_10_game_result: _containers.RepeatedCompositeFieldContainer[AccountMahjongStatistic.GameResult]
    recent_10_hu_summary: AccountMahjongStatistic.LiQi10Summary
    recent_20_hu_summary: AccountMahjongStatistic.Liqi20Summary
    recent_hu: AccountMahjongStatistic.HuSummary
    recent_round: AccountMahjongStatistic.RoundSummary
    def __init__(self, final_position_counts: Optional[Iterable[int]] = ..., recent_round: Optional[Union[AccountMahjongStatistic.RoundSummary, Mapping]] = ..., recent_hu: Optional[Union[AccountMahjongStatistic.HuSummary, Mapping]] = ..., highest_hu: Optional[Union[AccountMahjongStatistic.HighestHuRecord, Mapping]] = ..., recent_20_hu_summary: Optional[Union[AccountMahjongStatistic.Liqi20Summary, Mapping]] = ..., recent_10_hu_summary: Optional[Union[AccountMahjongStatistic.LiQi10Summary, Mapping]] = ..., recent_10_game_result: Optional[Iterable[Union[AccountMahjongStatistic.GameResult, Mapping]]] = ...) -> None: ...

class AccountOwnerData(_message.Message):
    __slots__ = ["unlock_characters"]
    UNLOCK_CHARACTERS_FIELD_NUMBER: ClassVar[int]
    unlock_characters: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, unlock_characters: Optional[Iterable[int]] = ...) -> None: ...

class AccountPlayingGame(_message.Message):
    __slots__ = ["category", "game_uuid", "meta"]
    CATEGORY_FIELD_NUMBER: ClassVar[int]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    META_FIELD_NUMBER: ClassVar[int]
    category: int
    game_uuid: str
    meta: GameMetaData
    def __init__(self, game_uuid: Optional[str] = ..., category: Optional[int] = ..., meta: Optional[Union[GameMetaData, Mapping]] = ...) -> None: ...

class AccountSetting(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    key: int
    value: int
    def __init__(self, key: Optional[int] = ..., value: Optional[int] = ...) -> None: ...

class AccountShiLian(_message.Message):
    __slots__ = ["state", "step"]
    STATE_FIELD_NUMBER: ClassVar[int]
    STEP_FIELD_NUMBER: ClassVar[int]
    state: int
    step: int
    def __init__(self, step: Optional[int] = ..., state: Optional[int] = ...) -> None: ...

class AccountStatisticByFan(_message.Message):
    __slots__ = ["fan_id", "sum"]
    FAN_ID_FIELD_NUMBER: ClassVar[int]
    SUM_FIELD_NUMBER: ClassVar[int]
    fan_id: int
    sum: int
    def __init__(self, fan_id: Optional[int] = ..., sum: Optional[int] = ...) -> None: ...

class AccountStatisticByGameMode(_message.Message):
    __slots__ = ["dadian_sum", "fly_count", "game_count_sum", "game_final_position", "gold_earn_sum", "highest_lianzhuang", "liqi_count_sum", "ming_count_sum", "mode", "rank_score", "round_count_sum", "round_end", "score_earn_sum", "xun_count_sum"]
    class RankScore(_message.Message):
        __slots__ = ["count", "rank", "score_sum"]
        COUNT_FIELD_NUMBER: ClassVar[int]
        RANK_FIELD_NUMBER: ClassVar[int]
        SCORE_SUM_FIELD_NUMBER: ClassVar[int]
        count: int
        rank: int
        score_sum: int
        def __init__(self, rank: Optional[int] = ..., score_sum: Optional[int] = ..., count: Optional[int] = ...) -> None: ...
    class RoundEndData(_message.Message):
        __slots__ = ["sum", "type"]
        SUM_FIELD_NUMBER: ClassVar[int]
        TYPE_FIELD_NUMBER: ClassVar[int]
        sum: int
        type: int
        def __init__(self, type: Optional[int] = ..., sum: Optional[int] = ...) -> None: ...
    DADIAN_SUM_FIELD_NUMBER: ClassVar[int]
    FLY_COUNT_FIELD_NUMBER: ClassVar[int]
    GAME_COUNT_SUM_FIELD_NUMBER: ClassVar[int]
    GAME_FINAL_POSITION_FIELD_NUMBER: ClassVar[int]
    GOLD_EARN_SUM_FIELD_NUMBER: ClassVar[int]
    HIGHEST_LIANZHUANG_FIELD_NUMBER: ClassVar[int]
    LIQI_COUNT_SUM_FIELD_NUMBER: ClassVar[int]
    MING_COUNT_SUM_FIELD_NUMBER: ClassVar[int]
    MODE_FIELD_NUMBER: ClassVar[int]
    RANK_SCORE_FIELD_NUMBER: ClassVar[int]
    ROUND_COUNT_SUM_FIELD_NUMBER: ClassVar[int]
    ROUND_END_FIELD_NUMBER: ClassVar[int]
    SCORE_EARN_SUM_FIELD_NUMBER: ClassVar[int]
    XUN_COUNT_SUM_FIELD_NUMBER: ClassVar[int]
    dadian_sum: float
    fly_count: int
    game_count_sum: int
    game_final_position: _containers.RepeatedScalarFieldContainer[int]
    gold_earn_sum: float
    highest_lianzhuang: int
    liqi_count_sum: int
    ming_count_sum: int
    mode: int
    rank_score: _containers.RepeatedCompositeFieldContainer[AccountStatisticByGameMode.RankScore]
    round_count_sum: int
    round_end: _containers.RepeatedCompositeFieldContainer[AccountStatisticByGameMode.RoundEndData]
    score_earn_sum: int
    xun_count_sum: int
    def __init__(self, mode: Optional[int] = ..., game_count_sum: Optional[int] = ..., game_final_position: Optional[Iterable[int]] = ..., fly_count: Optional[int] = ..., gold_earn_sum: Optional[float] = ..., round_count_sum: Optional[int] = ..., dadian_sum: Optional[float] = ..., round_end: Optional[Iterable[Union[AccountStatisticByGameMode.RoundEndData, Mapping]]] = ..., ming_count_sum: Optional[int] = ..., liqi_count_sum: Optional[int] = ..., xun_count_sum: Optional[int] = ..., highest_lianzhuang: Optional[int] = ..., score_earn_sum: Optional[int] = ..., rank_score: Optional[Iterable[Union[AccountStatisticByGameMode.RankScore, Mapping]]] = ...) -> None: ...

class AccountStatisticData(_message.Message):
    __slots__ = ["game_category", "mahjong_category", "statistic"]
    GAME_CATEGORY_FIELD_NUMBER: ClassVar[int]
    MAHJONG_CATEGORY_FIELD_NUMBER: ClassVar[int]
    STATISTIC_FIELD_NUMBER: ClassVar[int]
    game_category: int
    mahjong_category: int
    statistic: AccountMahjongStatistic
    def __init__(self, mahjong_category: Optional[int] = ..., game_category: Optional[int] = ..., statistic: Optional[Union[AccountMahjongStatistic, Mapping]] = ...) -> None: ...

class AccountUpdate(_message.Message):
    __slots__ = ["achievement", "activity_task", "bag", "character", "daily_task", "new_recharged_list", "numerical", "shilian", "title"]
    class AchievementUpdate(_message.Message):
        __slots__ = ["progresses"]
        PROGRESSES_FIELD_NUMBER: ClassVar[int]
        progresses: _containers.RepeatedCompositeFieldContainer[AchievementProgress]
        def __init__(self, progresses: Optional[Iterable[Union[AchievementProgress, Mapping]]] = ...) -> None: ...
    class ActivityTaskUpdate(_message.Message):
        __slots__ = ["progresses"]
        PROGRESSES_FIELD_NUMBER: ClassVar[int]
        progresses: _containers.RepeatedCompositeFieldContainer[TaskProgress]
        def __init__(self, progresses: Optional[Iterable[Union[TaskProgress, Mapping]]] = ...) -> None: ...
    class CharacterUpdate(_message.Message):
        __slots__ = ["characters", "skins"]
        CHARACTERS_FIELD_NUMBER: ClassVar[int]
        SKINS_FIELD_NUMBER: ClassVar[int]
        characters: _containers.RepeatedCompositeFieldContainer[Character]
        skins: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, characters: Optional[Iterable[Union[Character, Mapping]]] = ..., skins: Optional[Iterable[int]] = ...) -> None: ...
    class DailyTaskUpdate(_message.Message):
        __slots__ = ["progresses"]
        PROGRESSES_FIELD_NUMBER: ClassVar[int]
        progresses: _containers.RepeatedCompositeFieldContainer[TaskProgress]
        def __init__(self, progresses: Optional[Iterable[Union[TaskProgress, Mapping]]] = ...) -> None: ...
    class NumericalUpdate(_message.Message):
        __slots__ = ["final", "id"]
        FINAL_FIELD_NUMBER: ClassVar[int]
        ID_FIELD_NUMBER: ClassVar[int]
        final: int
        id: int
        def __init__(self, id: Optional[int] = ..., final: Optional[int] = ...) -> None: ...
    class TitleUpdate(_message.Message):
        __slots__ = ["new_titles"]
        NEW_TITLES_FIELD_NUMBER: ClassVar[int]
        new_titles: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, new_titles: Optional[Iterable[int]] = ...) -> None: ...
    ACHIEVEMENT_FIELD_NUMBER: ClassVar[int]
    ACTIVITY_TASK_FIELD_NUMBER: ClassVar[int]
    BAG_FIELD_NUMBER: ClassVar[int]
    CHARACTER_FIELD_NUMBER: ClassVar[int]
    DAILY_TASK_FIELD_NUMBER: ClassVar[int]
    NEW_RECHARGED_LIST_FIELD_NUMBER: ClassVar[int]
    NUMERICAL_FIELD_NUMBER: ClassVar[int]
    SHILIAN_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    achievement: AccountUpdate.AchievementUpdate
    activity_task: AccountUpdate.ActivityTaskUpdate
    bag: BagUpdate
    character: AccountUpdate.CharacterUpdate
    daily_task: AccountUpdate.DailyTaskUpdate
    new_recharged_list: _containers.RepeatedScalarFieldContainer[int]
    numerical: _containers.RepeatedCompositeFieldContainer[AccountUpdate.NumericalUpdate]
    shilian: AccountShiLian
    title: AccountUpdate.TitleUpdate
    def __init__(self, numerical: Optional[Iterable[Union[AccountUpdate.NumericalUpdate, Mapping]]] = ..., character: Optional[Union[AccountUpdate.CharacterUpdate, Mapping]] = ..., bag: Optional[Union[BagUpdate, Mapping]] = ..., achievement: Optional[Union[AccountUpdate.AchievementUpdate, Mapping]] = ..., shilian: Optional[Union[AccountShiLian, Mapping]] = ..., daily_task: Optional[Union[AccountUpdate.DailyTaskUpdate, Mapping]] = ..., title: Optional[Union[AccountUpdate.TitleUpdate, Mapping]] = ..., new_recharged_list: Optional[Iterable[int]] = ..., activity_task: Optional[Union[AccountUpdate.ActivityTaskUpdate, Mapping]] = ...) -> None: ...

class AchievementProgress(_message.Message):
    __slots__ = ["achieved", "counter", "date", "id"]
    ACHIEVED_FIELD_NUMBER: ClassVar[int]
    COUNTER_FIELD_NUMBER: ClassVar[int]
    DATE_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    achieved: bool
    counter: int
    date: int
    id: int
    def __init__(self, id: Optional[int] = ..., counter: Optional[int] = ..., achieved: bool = ..., date: Optional[int] = ...) -> None: ...

class Activity(_message.Message):
    __slots__ = ["activity_id", "end_time", "start_time", "type"]
    ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
    END_TIME_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    activity_id: int
    end_time: int
    start_time: int
    type: str
    def __init__(self, activity_id: Optional[int] = ..., start_time: Optional[int] = ..., end_time: Optional[int] = ..., type: Optional[str] = ...) -> None: ...

class ActivityAccumulatedPointData(_message.Message):
    __slots__ = ["activity_id", "gained_reward_list", "point"]
    ACTIVITY_ID_FIELD_NUMBER: ClassVar[int]
    GAINED_REWARD_LIST_FIELD_NUMBER: ClassVar[int]
    POINT_FIELD_NUMBER: ClassVar[int]
    activity_id: int
    gained_reward_list: _containers.RepeatedScalarFieldContainer[int]
    point: int
    def __init__(self, activity_id: Optional[int] = ..., point: Optional[int] = ..., gained_reward_list: Optional[Iterable[int]] = ...) -> None: ...

class ActivityRankPointData(_message.Message):
    __slots__ = ["gainable_time", "gained_reward", "leaderboard_id", "point"]
    GAINABLE_TIME_FIELD_NUMBER: ClassVar[int]
    GAINED_REWARD_FIELD_NUMBER: ClassVar[int]
    LEADERBOARD_ID_FIELD_NUMBER: ClassVar[int]
    POINT_FIELD_NUMBER: ClassVar[int]
    gainable_time: int
    gained_reward: bool
    leaderboard_id: int
    point: int
    def __init__(self, leaderboard_id: Optional[int] = ..., point: Optional[int] = ..., gained_reward: bool = ..., gainable_time: Optional[int] = ...) -> None: ...

class Announcement(_message.Message):
    __slots__ = ["content", "id", "title"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    content: str
    id: int
    title: str
    def __init__(self, id: Optional[int] = ..., title: Optional[str] = ..., content: Optional[str] = ...) -> None: ...

class AntiAddiction(_message.Message):
    __slots__ = ["online_duration"]
    ONLINE_DURATION_FIELD_NUMBER: ClassVar[int]
    online_duration: int
    def __init__(self, online_duration: Optional[int] = ...) -> None: ...

class Bag(_message.Message):
    __slots__ = ["daily_gain_record", "items"]
    DAILY_GAIN_RECORD_FIELD_NUMBER: ClassVar[int]
    ITEMS_FIELD_NUMBER: ClassVar[int]
    daily_gain_record: _containers.RepeatedCompositeFieldContainer[ItemGainRecords]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, items: Optional[Iterable[Union[Item, Mapping]]] = ..., daily_gain_record: Optional[Iterable[Union[ItemGainRecords, Mapping]]] = ...) -> None: ...

class BagUpdate(_message.Message):
    __slots__ = ["update_daily_gain_record", "update_items"]
    UPDATE_DAILY_GAIN_RECORD_FIELD_NUMBER: ClassVar[int]
    UPDATE_ITEMS_FIELD_NUMBER: ClassVar[int]
    update_daily_gain_record: _containers.RepeatedCompositeFieldContainer[ItemGainRecords]
    update_items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, update_items: Optional[Iterable[Union[Item, Mapping]]] = ..., update_daily_gain_record: Optional[Iterable[Union[ItemGainRecords, Mapping]]] = ...) -> None: ...

class BillShortcut(_message.Message):
    __slots__ = ["count", "deal_price", "id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    DEAL_PRICE_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    count: int
    deal_price: int
    id: int
    def __init__(self, id: Optional[int] = ..., count: Optional[int] = ..., deal_price: Optional[int] = ...) -> None: ...

class BillingGoods(_message.Message):
    __slots__ = ["desc", "icon", "id", "name", "resource_count", "resource_id"]
    DESC_FIELD_NUMBER: ClassVar[int]
    ICON_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    RESOURCE_COUNT_FIELD_NUMBER: ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: ClassVar[int]
    desc: str
    icon: str
    id: str
    name: str
    resource_count: int
    resource_id: int
    def __init__(self, id: Optional[str] = ..., name: Optional[str] = ..., desc: Optional[str] = ..., icon: Optional[str] = ..., resource_id: Optional[int] = ..., resource_count: Optional[int] = ...) -> None: ...

class BillingProduct(_message.Message):
    __slots__ = ["currency_code", "currency_price", "goods", "sort_weight"]
    CURRENCY_CODE_FIELD_NUMBER: ClassVar[int]
    CURRENCY_PRICE_FIELD_NUMBER: ClassVar[int]
    GOODS_FIELD_NUMBER: ClassVar[int]
    SORT_WEIGHT_FIELD_NUMBER: ClassVar[int]
    currency_code: str
    currency_price: int
    goods: BillingGoods
    sort_weight: int
    def __init__(self, goods: Optional[Union[BillingGoods, Mapping]] = ..., currency_code: Optional[str] = ..., currency_price: Optional[int] = ..., sort_weight: Optional[int] = ...) -> None: ...

class BuyRecord(_message.Message):
    __slots__ = ["count", "id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    count: int
    id: int
    def __init__(self, id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...

class ChangeNicknameRecord(_message.Message):
    __slots__ = ["time", "to"]
    FROM_FIELD_NUMBER: ClassVar[int]
    TIME_FIELD_NUMBER: ClassVar[int]
    TO_FIELD_NUMBER: ClassVar[int]
    time: int
    to: str
    def __init__(self, to: Optional[str] = ..., time: Optional[int] = ..., **kwargs) -> None: ...

class Character(_message.Message):
    __slots__ = ["charid", "exp", "extra_emoji", "is_upgraded", "level", "skin", "views"]
    class ViewSlotSet(_message.Message):
        __slots__ = ["item_id", "slot"]
        ITEM_ID_FIELD_NUMBER: ClassVar[int]
        SLOT_FIELD_NUMBER: ClassVar[int]
        item_id: int
        slot: int
        def __init__(self, slot: Optional[int] = ..., item_id: Optional[int] = ...) -> None: ...
    CHARID_FIELD_NUMBER: ClassVar[int]
    EXP_FIELD_NUMBER: ClassVar[int]
    EXTRA_EMOJI_FIELD_NUMBER: ClassVar[int]
    IS_UPGRADED_FIELD_NUMBER: ClassVar[int]
    LEVEL_FIELD_NUMBER: ClassVar[int]
    SKIN_FIELD_NUMBER: ClassVar[int]
    VIEWS_FIELD_NUMBER: ClassVar[int]
    charid: int
    exp: int
    extra_emoji: _containers.RepeatedScalarFieldContainer[int]
    is_upgraded: bool
    level: int
    skin: int
    views: _containers.RepeatedCompositeFieldContainer[Character.ViewSlotSet]
    def __init__(self, charid: Optional[int] = ..., level: Optional[int] = ..., exp: Optional[int] = ..., views: Optional[Iterable[Union[Character.ViewSlotSet, Mapping]]] = ..., skin: Optional[int] = ..., is_upgraded: bool = ..., extra_emoji: Optional[Iterable[int]] = ...) -> None: ...

class ChestData(_message.Message):
    __slots__ = ["chest_id", "consume_count", "face_black_count", "total_open_count"]
    CHEST_ID_FIELD_NUMBER: ClassVar[int]
    CONSUME_COUNT_FIELD_NUMBER: ClassVar[int]
    FACE_BLACK_COUNT_FIELD_NUMBER: ClassVar[int]
    TOTAL_OPEN_COUNT_FIELD_NUMBER: ClassVar[int]
    chest_id: int
    consume_count: int
    face_black_count: int
    total_open_count: int
    def __init__(self, chest_id: Optional[int] = ..., total_open_count: Optional[int] = ..., consume_count: Optional[int] = ..., face_black_count: Optional[int] = ...) -> None: ...

class ChestDataV2(_message.Message):
    __slots__ = ["chest_id", "face_black_count", "total_open_count"]
    CHEST_ID_FIELD_NUMBER: ClassVar[int]
    FACE_BLACK_COUNT_FIELD_NUMBER: ClassVar[int]
    TOTAL_OPEN_COUNT_FIELD_NUMBER: ClassVar[int]
    chest_id: int
    face_black_count: int
    total_open_count: int
    def __init__(self, chest_id: Optional[int] = ..., total_open_count: Optional[int] = ..., face_black_count: Optional[int] = ...) -> None: ...

class ClientDeviceInfo(_message.Message):
    __slots__ = ["browser", "device_type", "os", "os_version"]
    BROWSER_FIELD_NUMBER: ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: ClassVar[int]
    OS_FIELD_NUMBER: ClassVar[int]
    OS_VERSION_FIELD_NUMBER: ClassVar[int]
    browser: str
    device_type: str
    os: str
    os_version: str
    def __init__(self, device_type: Optional[str] = ..., os: Optional[str] = ..., os_version: Optional[str] = ..., browser: Optional[str] = ...) -> None: ...

class CommentItem(_message.Message):
    __slots__ = ["comment_id", "commenter", "content", "timestamp"]
    COMMENTER_FIELD_NUMBER: ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: ClassVar[int]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    comment_id: int
    commenter: PlayerBaseView
    content: str
    timestamp: int
    def __init__(self, comment_id: Optional[int] = ..., timestamp: Optional[int] = ..., commenter: Optional[Union[PlayerBaseView, Mapping]] = ..., content: Optional[str] = ...) -> None: ...

class ContestDetailRule(_message.Message):
    __slots__ = ["ai_level", "bianjietishi", "can_jifei", "changbang_value", "disable_multi_yukaman", "fandian", "have_biao_dora", "have_gang_biao_dora", "have_gang_li_dora", "have_helelianzhuang", "have_helezhongju", "have_jiuzhongjiupai", "have_li_dora", "have_liujumanguan", "have_nanruxiru", "have_qieshangmanguan", "have_sanjiahele", "have_sifenglianda", "have_sigangsanle", "have_sijializhi", "have_tingpailianzhuang", "have_tingpaizhongju", "have_toutiao", "have_yifa", "have_zimosun", "init_point", "jingsuanyuandian", "liqibang_value", "ming_dora_immediately_open", "noting_fafu_1", "noting_fafu_2", "noting_fafu_3", "shunweima_2", "shunweima_3", "shunweima_4", "tianbian_value"]
    AI_LEVEL_FIELD_NUMBER: ClassVar[int]
    BIANJIETISHI_FIELD_NUMBER: ClassVar[int]
    CAN_JIFEI_FIELD_NUMBER: ClassVar[int]
    CHANGBANG_VALUE_FIELD_NUMBER: ClassVar[int]
    DISABLE_MULTI_YUKAMAN_FIELD_NUMBER: ClassVar[int]
    FANDIAN_FIELD_NUMBER: ClassVar[int]
    HAVE_BIAO_DORA_FIELD_NUMBER: ClassVar[int]
    HAVE_GANG_BIAO_DORA_FIELD_NUMBER: ClassVar[int]
    HAVE_GANG_LI_DORA_FIELD_NUMBER: ClassVar[int]
    HAVE_HELELIANZHUANG_FIELD_NUMBER: ClassVar[int]
    HAVE_HELEZHONGJU_FIELD_NUMBER: ClassVar[int]
    HAVE_JIUZHONGJIUPAI_FIELD_NUMBER: ClassVar[int]
    HAVE_LIUJUMANGUAN_FIELD_NUMBER: ClassVar[int]
    HAVE_LI_DORA_FIELD_NUMBER: ClassVar[int]
    HAVE_NANRUXIRU_FIELD_NUMBER: ClassVar[int]
    HAVE_QIESHANGMANGUAN_FIELD_NUMBER: ClassVar[int]
    HAVE_SANJIAHELE_FIELD_NUMBER: ClassVar[int]
    HAVE_SIFENGLIANDA_FIELD_NUMBER: ClassVar[int]
    HAVE_SIGANGSANLE_FIELD_NUMBER: ClassVar[int]
    HAVE_SIJIALIZHI_FIELD_NUMBER: ClassVar[int]
    HAVE_TINGPAILIANZHUANG_FIELD_NUMBER: ClassVar[int]
    HAVE_TINGPAIZHONGJU_FIELD_NUMBER: ClassVar[int]
    HAVE_TOUTIAO_FIELD_NUMBER: ClassVar[int]
    HAVE_YIFA_FIELD_NUMBER: ClassVar[int]
    HAVE_ZIMOSUN_FIELD_NUMBER: ClassVar[int]
    INIT_POINT_FIELD_NUMBER: ClassVar[int]
    JINGSUANYUANDIAN_FIELD_NUMBER: ClassVar[int]
    LIQIBANG_VALUE_FIELD_NUMBER: ClassVar[int]
    MING_DORA_IMMEDIATELY_OPEN_FIELD_NUMBER: ClassVar[int]
    NOTING_FAFU_1_FIELD_NUMBER: ClassVar[int]
    NOTING_FAFU_2_FIELD_NUMBER: ClassVar[int]
    NOTING_FAFU_3_FIELD_NUMBER: ClassVar[int]
    SHUNWEIMA_2_FIELD_NUMBER: ClassVar[int]
    SHUNWEIMA_3_FIELD_NUMBER: ClassVar[int]
    SHUNWEIMA_4_FIELD_NUMBER: ClassVar[int]
    TIANBIAN_VALUE_FIELD_NUMBER: ClassVar[int]
    ai_level: int
    bianjietishi: bool
    can_jifei: bool
    changbang_value: int
    disable_multi_yukaman: bool
    fandian: int
    have_biao_dora: bool
    have_gang_biao_dora: bool
    have_gang_li_dora: bool
    have_helelianzhuang: bool
    have_helezhongju: bool
    have_jiuzhongjiupai: bool
    have_li_dora: bool
    have_liujumanguan: bool
    have_nanruxiru: bool
    have_qieshangmanguan: bool
    have_sanjiahele: bool
    have_sifenglianda: bool
    have_sigangsanle: bool
    have_sijializhi: bool
    have_tingpailianzhuang: bool
    have_tingpaizhongju: bool
    have_toutiao: bool
    have_yifa: bool
    have_zimosun: bool
    init_point: int
    jingsuanyuandian: int
    liqibang_value: int
    ming_dora_immediately_open: bool
    noting_fafu_1: int
    noting_fafu_2: int
    noting_fafu_3: int
    shunweima_2: int
    shunweima_3: int
    shunweima_4: int
    tianbian_value: int
    def __init__(self, init_point: Optional[int] = ..., fandian: Optional[int] = ..., can_jifei: bool = ..., tianbian_value: Optional[int] = ..., liqibang_value: Optional[int] = ..., changbang_value: Optional[int] = ..., noting_fafu_1: Optional[int] = ..., noting_fafu_2: Optional[int] = ..., noting_fafu_3: Optional[int] = ..., have_liujumanguan: bool = ..., have_qieshangmanguan: bool = ..., have_biao_dora: bool = ..., have_gang_biao_dora: bool = ..., ming_dora_immediately_open: bool = ..., have_li_dora: bool = ..., have_gang_li_dora: bool = ..., have_sifenglianda: bool = ..., have_sigangsanle: bool = ..., have_sijializhi: bool = ..., have_jiuzhongjiupai: bool = ..., have_sanjiahele: bool = ..., have_toutiao: bool = ..., have_helelianzhuang: bool = ..., have_helezhongju: bool = ..., have_tingpailianzhuang: bool = ..., have_tingpaizhongju: bool = ..., have_yifa: bool = ..., have_nanruxiru: bool = ..., jingsuanyuandian: Optional[int] = ..., shunweima_2: Optional[int] = ..., shunweima_3: Optional[int] = ..., shunweima_4: Optional[int] = ..., bianjietishi: bool = ..., ai_level: Optional[int] = ..., have_zimosun: bool = ..., disable_multi_yukaman: bool = ...) -> None: ...

class ContestDetailRuleV2(_message.Message):
    __slots__ = ["extra_rule", "game_rule"]
    class ExtraRule(_message.Message):
        __slots__ = ["max_game_count", "required_level"]
        MAX_GAME_COUNT_FIELD_NUMBER: ClassVar[int]
        REQUIRED_LEVEL_FIELD_NUMBER: ClassVar[int]
        max_game_count: int
        required_level: int
        def __init__(self, required_level: Optional[int] = ..., max_game_count: Optional[int] = ...) -> None: ...
    EXTRA_RULE_FIELD_NUMBER: ClassVar[int]
    GAME_RULE_FIELD_NUMBER: ClassVar[int]
    extra_rule: ContestDetailRuleV2.ExtraRule
    game_rule: ContestDetailRule
    def __init__(self, game_rule: Optional[Union[ContestDetailRule, Mapping]] = ..., extra_rule: Optional[Union[ContestDetailRuleV2.ExtraRule, Mapping]] = ...) -> None: ...

class ContestGameInfo(_message.Message):
    __slots__ = ["end_time", "game_uuid", "players", "start_time"]
    class Player(_message.Message):
        __slots__ = ["account_id", "nickname"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        NICKNAME_FIELD_NUMBER: ClassVar[int]
        account_id: int
        nickname: str
        def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ...) -> None: ...
    END_TIME_FIELD_NUMBER: ClassVar[int]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    end_time: int
    game_uuid: str
    players: _containers.RepeatedCompositeFieldContainer[ContestGameInfo.Player]
    start_time: int
    def __init__(self, game_uuid: Optional[str] = ..., players: Optional[Iterable[Union[ContestGameInfo.Player, Mapping]]] = ..., start_time: Optional[int] = ..., end_time: Optional[int] = ...) -> None: ...

class ContestMatchingPlayer(_message.Message):
    __slots__ = ["account_id", "controller", "nickname"]
    class Controller(_message.Message):
        __slots__ = ["account_id", "nickname"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        NICKNAME_FIELD_NUMBER: ClassVar[int]
        account_id: int
        nickname: str
        def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    CONTROLLER_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    account_id: int
    controller: ContestMatchingPlayer.Controller
    nickname: str
    def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ..., controller: Optional[Union[ContestMatchingPlayer.Controller, Mapping]] = ...) -> None: ...

class ContestPlayerInfo(_message.Message):
    __slots__ = ["account_id", "nickname"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    account_id: int
    nickname: str
    def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ...) -> None: ...

class CustomizedContest(_message.Message):
    __slots__ = ["contest_id", "contest_name", "create_time", "creator_id", "deadline", "finish_time", "open", "rank_rule", "start_time", "state", "unique_id"]
    CONTEST_ID_FIELD_NUMBER: ClassVar[int]
    CONTEST_NAME_FIELD_NUMBER: ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: ClassVar[int]
    DEADLINE_FIELD_NUMBER: ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: ClassVar[int]
    OPEN_FIELD_NUMBER: ClassVar[int]
    RANK_RULE_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    contest_id: int
    contest_name: str
    create_time: int
    creator_id: int
    deadline: int
    finish_time: int
    open: bool
    rank_rule: int
    start_time: int
    state: int
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., creator_id: Optional[int] = ..., contest_id: Optional[int] = ..., contest_name: Optional[str] = ..., state: Optional[int] = ..., create_time: Optional[int] = ..., start_time: Optional[int] = ..., finish_time: Optional[int] = ..., open: bool = ..., rank_rule: Optional[int] = ..., deadline: Optional[int] = ...) -> None: ...

class CustomizedContestAbstract(_message.Message):
    __slots__ = ["contest_id", "contest_name", "create_time", "creator_id", "finish_time", "open", "public_notice", "start_time", "state", "unique_id"]
    CONTEST_ID_FIELD_NUMBER: ClassVar[int]
    CONTEST_NAME_FIELD_NUMBER: ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: ClassVar[int]
    OPEN_FIELD_NUMBER: ClassVar[int]
    PUBLIC_NOTICE_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    contest_id: int
    contest_name: str
    create_time: int
    creator_id: int
    finish_time: int
    open: bool
    public_notice: str
    start_time: int
    state: int
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., contest_id: Optional[int] = ..., contest_name: Optional[str] = ..., state: Optional[int] = ..., creator_id: Optional[int] = ..., create_time: Optional[int] = ..., start_time: Optional[int] = ..., finish_time: Optional[int] = ..., open: bool = ..., public_notice: Optional[str] = ...) -> None: ...

class CustomizedContestBase(_message.Message):
    __slots__ = ["contest_id", "contest_name", "create_time", "creator_id", "finish_time", "open", "start_time", "state", "unique_id"]
    CONTEST_ID_FIELD_NUMBER: ClassVar[int]
    CONTEST_NAME_FIELD_NUMBER: ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: ClassVar[int]
    OPEN_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    contest_id: int
    contest_name: str
    create_time: int
    creator_id: int
    finish_time: int
    open: bool
    start_time: int
    state: int
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., contest_id: Optional[int] = ..., contest_name: Optional[str] = ..., state: Optional[int] = ..., creator_id: Optional[int] = ..., create_time: Optional[int] = ..., start_time: Optional[int] = ..., finish_time: Optional[int] = ..., open: bool = ...) -> None: ...

class CustomizedContestDetail(_message.Message):
    __slots__ = ["contest_id", "contest_name", "create_time", "creator_id", "finish_time", "game_mode", "open", "private_notice", "rank_rule", "start_time", "state", "unique_id"]
    CONTEST_ID_FIELD_NUMBER: ClassVar[int]
    CONTEST_NAME_FIELD_NUMBER: ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: ClassVar[int]
    GAME_MODE_FIELD_NUMBER: ClassVar[int]
    OPEN_FIELD_NUMBER: ClassVar[int]
    PRIVATE_NOTICE_FIELD_NUMBER: ClassVar[int]
    RANK_RULE_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    contest_id: int
    contest_name: str
    create_time: int
    creator_id: int
    finish_time: int
    game_mode: GameMode
    open: bool
    private_notice: str
    rank_rule: int
    start_time: int
    state: int
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., contest_id: Optional[int] = ..., contest_name: Optional[str] = ..., state: Optional[int] = ..., creator_id: Optional[int] = ..., create_time: Optional[int] = ..., start_time: Optional[int] = ..., finish_time: Optional[int] = ..., open: bool = ..., rank_rule: Optional[int] = ..., game_mode: Optional[Union[GameMode, Mapping]] = ..., private_notice: Optional[str] = ...) -> None: ...

class CustomizedContestExtend(_message.Message):
    __slots__ = ["public_notice", "unique_id"]
    PUBLIC_NOTICE_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    public_notice: str
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., public_notice: Optional[str] = ...) -> None: ...

class CustomizedContestGameEnd(_message.Message):
    __slots__ = ["players"]
    class Item(_message.Message):
        __slots__ = ["account_id", "nickname", "total_point"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        NICKNAME_FIELD_NUMBER: ClassVar[int]
        TOTAL_POINT_FIELD_NUMBER: ClassVar[int]
        account_id: int
        nickname: str
        total_point: int
        def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ..., total_point: Optional[int] = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[CustomizedContestGameEnd.Item]
    def __init__(self, players: Optional[Iterable[Union[CustomizedContestGameEnd.Item, Mapping]]] = ...) -> None: ...

class CustomizedContestGameStart(_message.Message):
    __slots__ = ["players"]
    class Item(_message.Message):
        __slots__ = ["account_id", "nickname"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        NICKNAME_FIELD_NUMBER: ClassVar[int]
        account_id: int
        nickname: str
        def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[CustomizedContestGameStart.Item]
    def __init__(self, players: Optional[Iterable[Union[CustomizedContestGameStart.Item, Mapping]]] = ...) -> None: ...

class CustomizedContestPlayerReport(_message.Message):
    __slots__ = ["point", "rank", "rank_rule", "recent_game_ranks", "total_game_count"]
    POINT_FIELD_NUMBER: ClassVar[int]
    RANK_FIELD_NUMBER: ClassVar[int]
    RANK_RULE_FIELD_NUMBER: ClassVar[int]
    RECENT_GAME_RANKS_FIELD_NUMBER: ClassVar[int]
    TOTAL_GAME_COUNT_FIELD_NUMBER: ClassVar[int]
    point: int
    rank: int
    rank_rule: int
    recent_game_ranks: _containers.RepeatedScalarFieldContainer[int]
    total_game_count: int
    def __init__(self, rank_rule: Optional[int] = ..., rank: Optional[int] = ..., point: Optional[int] = ..., recent_game_ranks: Optional[Iterable[int]] = ..., total_game_count: Optional[int] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ["code", "json_param", "str_params", "u32_params"]
    CODE_FIELD_NUMBER: ClassVar[int]
    JSON_PARAM_FIELD_NUMBER: ClassVar[int]
    STR_PARAMS_FIELD_NUMBER: ClassVar[int]
    U32_PARAMS_FIELD_NUMBER: ClassVar[int]
    code: int
    json_param: str
    str_params: _containers.RepeatedScalarFieldContainer[str]
    u32_params: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, code: Optional[int] = ..., u32_params: Optional[Iterable[int]] = ..., str_params: Optional[Iterable[str]] = ..., json_param: Optional[str] = ...) -> None: ...

class ExchangeRecord(_message.Message):
    __slots__ = ["count", "exchange_id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    EXCHANGE_ID_FIELD_NUMBER: ClassVar[int]
    count: int
    exchange_id: int
    def __init__(self, exchange_id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...

class ExecuteReward(_message.Message):
    __slots__ = ["replace", "replace_count", "reward"]
    REPLACE_COUNT_FIELD_NUMBER: ClassVar[int]
    REPLACE_FIELD_NUMBER: ClassVar[int]
    REWARD_FIELD_NUMBER: ClassVar[int]
    replace: RewardSlot
    replace_count: int
    reward: RewardSlot
    def __init__(self, reward: Optional[Union[RewardSlot, Mapping]] = ..., replace: Optional[Union[RewardSlot, Mapping]] = ..., replace_count: Optional[int] = ...) -> None: ...

class FaithData(_message.Message):
    __slots__ = ["consume_count", "faith_id", "total_open_count"]
    CONSUME_COUNT_FIELD_NUMBER: ClassVar[int]
    FAITH_ID_FIELD_NUMBER: ClassVar[int]
    TOTAL_OPEN_COUNT_FIELD_NUMBER: ClassVar[int]
    consume_count: int
    faith_id: int
    total_open_count: int
    def __init__(self, faith_id: Optional[int] = ..., total_open_count: Optional[int] = ..., consume_count: Optional[int] = ...) -> None: ...

class Friend(_message.Message):
    __slots__ = ["base", "state"]
    BASE_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    base: PlayerBaseView
    state: AccountActiveState
    def __init__(self, base: Optional[Union[PlayerBaseView, Mapping]] = ..., state: Optional[Union[AccountActiveState, Mapping]] = ...) -> None: ...

class GameConfig(_message.Message):
    __slots__ = ["category", "meta", "mode"]
    CATEGORY_FIELD_NUMBER: ClassVar[int]
    META_FIELD_NUMBER: ClassVar[int]
    MODE_FIELD_NUMBER: ClassVar[int]
    category: int
    meta: GameMetaData
    mode: GameMode
    def __init__(self, category: Optional[int] = ..., mode: Optional[Union[GameMode, Mapping]] = ..., meta: Optional[Union[GameMetaData, Mapping]] = ...) -> None: ...

class GameConnectInfo(_message.Message):
    __slots__ = ["connect_token", "game_uuid", "location"]
    CONNECT_TOKEN_FIELD_NUMBER: ClassVar[int]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    LOCATION_FIELD_NUMBER: ClassVar[int]
    connect_token: str
    game_uuid: str
    location: str
    def __init__(self, connect_token: Optional[str] = ..., game_uuid: Optional[str] = ..., location: Optional[str] = ...) -> None: ...

class GameDetailRule(_message.Message):
    __slots__ = ["ai_level", "bianjietishi", "can_jifei", "changbang_value", "disable_multi_yukaman", "dora_count", "fandian", "fanfu", "guyi_mode", "have_biao_dora", "have_gang_biao_dora", "have_gang_li_dora", "have_helelianzhuang", "have_helezhongju", "have_jiuzhongjiupai", "have_li_dora", "have_liujumanguan", "have_nanruxiru", "have_qieshangmanguan", "have_sanjiahele", "have_sifenglianda", "have_sigangsanle", "have_sijializhi", "have_tingpailianzhuang", "have_tingpaizhongju", "have_toutiao", "have_yifa", "have_zimosun", "init_point", "jingsuanyuandian", "liqibang_value", "ming_dora_immediately_open", "noting_fafu_1", "noting_fafu_2", "noting_fafu_3", "shiduan", "shunweima_2", "shunweima_3", "shunweima_4", "tianbian_value", "time_add", "time_fixed"]
    AI_LEVEL_FIELD_NUMBER: ClassVar[int]
    BIANJIETISHI_FIELD_NUMBER: ClassVar[int]
    CAN_JIFEI_FIELD_NUMBER: ClassVar[int]
    CHANGBANG_VALUE_FIELD_NUMBER: ClassVar[int]
    DISABLE_MULTI_YUKAMAN_FIELD_NUMBER: ClassVar[int]
    DORA_COUNT_FIELD_NUMBER: ClassVar[int]
    FANDIAN_FIELD_NUMBER: ClassVar[int]
    FANFU_FIELD_NUMBER: ClassVar[int]
    GUYI_MODE_FIELD_NUMBER: ClassVar[int]
    HAVE_BIAO_DORA_FIELD_NUMBER: ClassVar[int]
    HAVE_GANG_BIAO_DORA_FIELD_NUMBER: ClassVar[int]
    HAVE_GANG_LI_DORA_FIELD_NUMBER: ClassVar[int]
    HAVE_HELELIANZHUANG_FIELD_NUMBER: ClassVar[int]
    HAVE_HELEZHONGJU_FIELD_NUMBER: ClassVar[int]
    HAVE_JIUZHONGJIUPAI_FIELD_NUMBER: ClassVar[int]
    HAVE_LIUJUMANGUAN_FIELD_NUMBER: ClassVar[int]
    HAVE_LI_DORA_FIELD_NUMBER: ClassVar[int]
    HAVE_NANRUXIRU_FIELD_NUMBER: ClassVar[int]
    HAVE_QIESHANGMANGUAN_FIELD_NUMBER: ClassVar[int]
    HAVE_SANJIAHELE_FIELD_NUMBER: ClassVar[int]
    HAVE_SIFENGLIANDA_FIELD_NUMBER: ClassVar[int]
    HAVE_SIGANGSANLE_FIELD_NUMBER: ClassVar[int]
    HAVE_SIJIALIZHI_FIELD_NUMBER: ClassVar[int]
    HAVE_TINGPAILIANZHUANG_FIELD_NUMBER: ClassVar[int]
    HAVE_TINGPAIZHONGJU_FIELD_NUMBER: ClassVar[int]
    HAVE_TOUTIAO_FIELD_NUMBER: ClassVar[int]
    HAVE_YIFA_FIELD_NUMBER: ClassVar[int]
    HAVE_ZIMOSUN_FIELD_NUMBER: ClassVar[int]
    INIT_POINT_FIELD_NUMBER: ClassVar[int]
    JINGSUANYUANDIAN_FIELD_NUMBER: ClassVar[int]
    LIQIBANG_VALUE_FIELD_NUMBER: ClassVar[int]
    MING_DORA_IMMEDIATELY_OPEN_FIELD_NUMBER: ClassVar[int]
    NOTING_FAFU_1_FIELD_NUMBER: ClassVar[int]
    NOTING_FAFU_2_FIELD_NUMBER: ClassVar[int]
    NOTING_FAFU_3_FIELD_NUMBER: ClassVar[int]
    SHIDUAN_FIELD_NUMBER: ClassVar[int]
    SHUNWEIMA_2_FIELD_NUMBER: ClassVar[int]
    SHUNWEIMA_3_FIELD_NUMBER: ClassVar[int]
    SHUNWEIMA_4_FIELD_NUMBER: ClassVar[int]
    TIANBIAN_VALUE_FIELD_NUMBER: ClassVar[int]
    TIME_ADD_FIELD_NUMBER: ClassVar[int]
    TIME_FIXED_FIELD_NUMBER: ClassVar[int]
    ai_level: int
    bianjietishi: bool
    can_jifei: bool
    changbang_value: int
    disable_multi_yukaman: bool
    dora_count: int
    fandian: int
    fanfu: int
    guyi_mode: int
    have_biao_dora: bool
    have_gang_biao_dora: bool
    have_gang_li_dora: bool
    have_helelianzhuang: bool
    have_helezhongju: bool
    have_jiuzhongjiupai: bool
    have_li_dora: bool
    have_liujumanguan: bool
    have_nanruxiru: bool
    have_qieshangmanguan: bool
    have_sanjiahele: bool
    have_sifenglianda: bool
    have_sigangsanle: bool
    have_sijializhi: bool
    have_tingpailianzhuang: bool
    have_tingpaizhongju: bool
    have_toutiao: bool
    have_yifa: bool
    have_zimosun: bool
    init_point: int
    jingsuanyuandian: int
    liqibang_value: int
    ming_dora_immediately_open: bool
    noting_fafu_1: int
    noting_fafu_2: int
    noting_fafu_3: int
    shiduan: int
    shunweima_2: int
    shunweima_3: int
    shunweima_4: int
    tianbian_value: int
    time_add: int
    time_fixed: int
    def __init__(self, time_fixed: Optional[int] = ..., time_add: Optional[int] = ..., dora_count: Optional[int] = ..., shiduan: Optional[int] = ..., init_point: Optional[int] = ..., fandian: Optional[int] = ..., can_jifei: bool = ..., tianbian_value: Optional[int] = ..., liqibang_value: Optional[int] = ..., changbang_value: Optional[int] = ..., noting_fafu_1: Optional[int] = ..., noting_fafu_2: Optional[int] = ..., noting_fafu_3: Optional[int] = ..., have_liujumanguan: bool = ..., have_qieshangmanguan: bool = ..., have_biao_dora: bool = ..., have_gang_biao_dora: bool = ..., ming_dora_immediately_open: bool = ..., have_li_dora: bool = ..., have_gang_li_dora: bool = ..., have_sifenglianda: bool = ..., have_sigangsanle: bool = ..., have_sijializhi: bool = ..., have_jiuzhongjiupai: bool = ..., have_sanjiahele: bool = ..., have_toutiao: bool = ..., have_helelianzhuang: bool = ..., have_helezhongju: bool = ..., have_tingpailianzhuang: bool = ..., have_tingpaizhongju: bool = ..., have_yifa: bool = ..., have_nanruxiru: bool = ..., jingsuanyuandian: Optional[int] = ..., shunweima_2: Optional[int] = ..., shunweima_3: Optional[int] = ..., shunweima_4: Optional[int] = ..., bianjietishi: bool = ..., ai_level: Optional[int] = ..., have_zimosun: bool = ..., disable_multi_yukaman: bool = ..., fanfu: Optional[int] = ..., guyi_mode: Optional[int] = ...) -> None: ...

class GameEndAction(_message.Message):
    __slots__ = ["state"]
    STATE_FIELD_NUMBER: ClassVar[int]
    state: int
    def __init__(self, state: Optional[int] = ...) -> None: ...

class GameEndResult(_message.Message):
    __slots__ = ["players"]
    class PlayerItem(_message.Message):
        __slots__ = ["gold", "grading_score", "part_point_1", "part_point_2", "seat", "total_point"]
        GOLD_FIELD_NUMBER: ClassVar[int]
        GRADING_SCORE_FIELD_NUMBER: ClassVar[int]
        PART_POINT_1_FIELD_NUMBER: ClassVar[int]
        PART_POINT_2_FIELD_NUMBER: ClassVar[int]
        SEAT_FIELD_NUMBER: ClassVar[int]
        TOTAL_POINT_FIELD_NUMBER: ClassVar[int]
        gold: int
        grading_score: int
        part_point_1: int
        part_point_2: int
        seat: int
        total_point: int
        def __init__(self, seat: Optional[int] = ..., total_point: Optional[int] = ..., part_point_1: Optional[int] = ..., part_point_2: Optional[int] = ..., grading_score: Optional[int] = ..., gold: Optional[int] = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[GameEndResult.PlayerItem]
    def __init__(self, players: Optional[Iterable[Union[GameEndResult.PlayerItem, Mapping]]] = ...) -> None: ...

class GameFinalSnapshot(_message.Message):
    __slots__ = ["account_views", "calculate_param", "category", "create_time", "final_players", "finish_time", "meta", "mode", "rounds", "seats", "start_time", "state", "uuid"]
    class CalculateParam(_message.Message):
        __slots__ = ["init_point", "jingsuanyuandian", "rank_points"]
        INIT_POINT_FIELD_NUMBER: ClassVar[int]
        JINGSUANYUANDIAN_FIELD_NUMBER: ClassVar[int]
        RANK_POINTS_FIELD_NUMBER: ClassVar[int]
        init_point: int
        jingsuanyuandian: int
        rank_points: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, init_point: Optional[int] = ..., jingsuanyuandian: Optional[int] = ..., rank_points: Optional[Iterable[int]] = ...) -> None: ...
    class FinalPlayer(_message.Message):
        __slots__ = ["gold", "grading_score", "part_point_1", "part_point_2", "seat", "total_point"]
        GOLD_FIELD_NUMBER: ClassVar[int]
        GRADING_SCORE_FIELD_NUMBER: ClassVar[int]
        PART_POINT_1_FIELD_NUMBER: ClassVar[int]
        PART_POINT_2_FIELD_NUMBER: ClassVar[int]
        SEAT_FIELD_NUMBER: ClassVar[int]
        TOTAL_POINT_FIELD_NUMBER: ClassVar[int]
        gold: int
        grading_score: int
        part_point_1: int
        part_point_2: int
        seat: int
        total_point: int
        def __init__(self, seat: Optional[int] = ..., total_point: Optional[int] = ..., part_point_1: Optional[int] = ..., part_point_2: Optional[int] = ..., grading_score: Optional[int] = ..., gold: Optional[int] = ...) -> None: ...
    class GameSeat(_message.Message):
        __slots__ = ["account_id", "client_address", "is_connected", "notify_endpoint", "type"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        CLIENT_ADDRESS_FIELD_NUMBER: ClassVar[int]
        IS_CONNECTED_FIELD_NUMBER: ClassVar[int]
        NOTIFY_ENDPOINT_FIELD_NUMBER: ClassVar[int]
        TYPE_FIELD_NUMBER: ClassVar[int]
        account_id: int
        client_address: str
        is_connected: bool
        notify_endpoint: NetworkEndpoint
        type: int
        def __init__(self, type: Optional[int] = ..., account_id: Optional[int] = ..., notify_endpoint: Optional[Union[NetworkEndpoint, Mapping]] = ..., client_address: Optional[str] = ..., is_connected: bool = ...) -> None: ...
    ACCOUNT_VIEWS_FIELD_NUMBER: ClassVar[int]
    CALCULATE_PARAM_FIELD_NUMBER: ClassVar[int]
    CATEGORY_FIELD_NUMBER: ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    FINAL_PLAYERS_FIELD_NUMBER: ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: ClassVar[int]
    META_FIELD_NUMBER: ClassVar[int]
    MODE_FIELD_NUMBER: ClassVar[int]
    ROUNDS_FIELD_NUMBER: ClassVar[int]
    SEATS_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    account_views: _containers.RepeatedCompositeFieldContainer[PlayerGameView]
    calculate_param: GameFinalSnapshot.CalculateParam
    category: int
    create_time: int
    final_players: _containers.RepeatedCompositeFieldContainer[GameFinalSnapshot.FinalPlayer]
    finish_time: int
    meta: GameMetaData
    mode: GameMode
    rounds: _containers.RepeatedCompositeFieldContainer[GameRoundSnapshot]
    seats: _containers.RepeatedCompositeFieldContainer[GameFinalSnapshot.GameSeat]
    start_time: int
    state: int
    uuid: str
    def __init__(self, uuid: Optional[str] = ..., state: Optional[int] = ..., category: Optional[int] = ..., mode: Optional[Union[GameMode, Mapping]] = ..., meta: Optional[Union[GameMetaData, Mapping]] = ..., calculate_param: Optional[Union[GameFinalSnapshot.CalculateParam, Mapping]] = ..., create_time: Optional[int] = ..., start_time: Optional[int] = ..., finish_time: Optional[int] = ..., seats: Optional[Iterable[Union[GameFinalSnapshot.GameSeat, Mapping]]] = ..., rounds: Optional[Iterable[Union[GameRoundSnapshot, Mapping]]] = ..., account_views: Optional[Iterable[Union[PlayerGameView, Mapping]]] = ..., final_players: Optional[Iterable[Union[GameFinalSnapshot.FinalPlayer, Mapping]]] = ...) -> None: ...

class GameLiveHead(_message.Message):
    __slots__ = ["game_config", "players", "seat_list", "start_time", "uuid"]
    GAME_CONFIG_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    SEAT_LIST_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    game_config: GameConfig
    players: _containers.RepeatedCompositeFieldContainer[PlayerGameView]
    seat_list: _containers.RepeatedScalarFieldContainer[int]
    start_time: int
    uuid: str
    def __init__(self, uuid: Optional[str] = ..., start_time: Optional[int] = ..., game_config: Optional[Union[GameConfig, Mapping]] = ..., players: Optional[Iterable[Union[PlayerGameView, Mapping]]] = ..., seat_list: Optional[Iterable[int]] = ...) -> None: ...

class GameLiveSegment(_message.Message):
    __slots__ = ["actions"]
    ACTIONS_FIELD_NUMBER: ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[GameLiveUnit]
    def __init__(self, actions: Optional[Iterable[Union[GameLiveUnit, Mapping]]] = ...) -> None: ...

class GameLiveSegmentUri(_message.Message):
    __slots__ = ["segment_id", "segment_uri"]
    SEGMENT_ID_FIELD_NUMBER: ClassVar[int]
    SEGMENT_URI_FIELD_NUMBER: ClassVar[int]
    segment_id: int
    segment_uri: str
    def __init__(self, segment_id: Optional[int] = ..., segment_uri: Optional[str] = ...) -> None: ...

class GameLiveUnit(_message.Message):
    __slots__ = ["action_category", "action_data", "timestamp"]
    ACTION_CATEGORY_FIELD_NUMBER: ClassVar[int]
    ACTION_DATA_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    action_category: int
    action_data: bytes
    timestamp: int
    def __init__(self, timestamp: Optional[int] = ..., action_category: Optional[int] = ..., action_data: Optional[bytes] = ...) -> None: ...

class GameMetaData(_message.Message):
    __slots__ = ["contest_uid", "mode_id", "room_id"]
    CONTEST_UID_FIELD_NUMBER: ClassVar[int]
    MODE_ID_FIELD_NUMBER: ClassVar[int]
    ROOM_ID_FIELD_NUMBER: ClassVar[int]
    contest_uid: int
    mode_id: int
    room_id: int
    def __init__(self, room_id: Optional[int] = ..., mode_id: Optional[int] = ..., contest_uid: Optional[int] = ...) -> None: ...

class GameMode(_message.Message):
    __slots__ = ["ai", "detail_rule", "extendinfo", "mode", "testing_environment"]
    AI_FIELD_NUMBER: ClassVar[int]
    DETAIL_RULE_FIELD_NUMBER: ClassVar[int]
    EXTENDINFO_FIELD_NUMBER: ClassVar[int]
    MODE_FIELD_NUMBER: ClassVar[int]
    TESTING_ENVIRONMENT_FIELD_NUMBER: ClassVar[int]
    ai: bool
    detail_rule: GameDetailRule
    extendinfo: str
    mode: int
    testing_environment: GameTestingEnvironmentSet
    def __init__(self, mode: Optional[int] = ..., ai: bool = ..., extendinfo: Optional[str] = ..., detail_rule: Optional[Union[GameDetailRule, Mapping]] = ..., testing_environment: Optional[Union[GameTestingEnvironmentSet, Mapping]] = ...) -> None: ...

class GameNewRoundState(_message.Message):
    __slots__ = ["seat_states"]
    SEAT_STATES_FIELD_NUMBER: ClassVar[int]
    seat_states: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, seat_states: Optional[Iterable[int]] = ...) -> None: ...

class GameNoopAction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GameRoundHuData(_message.Message):
    __slots__ = ["babei_count", "biao_dora_count", "fan_sum", "fans", "fu_sum", "hupai", "li_dora_count", "red_dora_count", "score", "title_id", "xuan_shang_count", "xun", "yakuman_count"]
    class Fan(_message.Message):
        __slots__ = ["count", "fan", "id"]
        COUNT_FIELD_NUMBER: ClassVar[int]
        FAN_FIELD_NUMBER: ClassVar[int]
        ID_FIELD_NUMBER: ClassVar[int]
        count: int
        fan: int
        id: int
        def __init__(self, id: Optional[int] = ..., count: Optional[int] = ..., fan: Optional[int] = ...) -> None: ...
    class HuPai(_message.Message):
        __slots__ = ["liqi", "seat", "tile"]
        LIQI_FIELD_NUMBER: ClassVar[int]
        SEAT_FIELD_NUMBER: ClassVar[int]
        TILE_FIELD_NUMBER: ClassVar[int]
        liqi: int
        seat: int
        tile: str
        def __init__(self, tile: Optional[str] = ..., seat: Optional[int] = ..., liqi: Optional[int] = ...) -> None: ...
    BABEI_COUNT_FIELD_NUMBER: ClassVar[int]
    BIAO_DORA_COUNT_FIELD_NUMBER: ClassVar[int]
    FANS_FIELD_NUMBER: ClassVar[int]
    FAN_SUM_FIELD_NUMBER: ClassVar[int]
    FU_SUM_FIELD_NUMBER: ClassVar[int]
    HUPAI_FIELD_NUMBER: ClassVar[int]
    LI_DORA_COUNT_FIELD_NUMBER: ClassVar[int]
    RED_DORA_COUNT_FIELD_NUMBER: ClassVar[int]
    SCORE_FIELD_NUMBER: ClassVar[int]
    TITLE_ID_FIELD_NUMBER: ClassVar[int]
    XUAN_SHANG_COUNT_FIELD_NUMBER: ClassVar[int]
    XUN_FIELD_NUMBER: ClassVar[int]
    YAKUMAN_COUNT_FIELD_NUMBER: ClassVar[int]
    babei_count: int
    biao_dora_count: int
    fan_sum: int
    fans: _containers.RepeatedCompositeFieldContainer[GameRoundHuData.Fan]
    fu_sum: int
    hupai: GameRoundHuData.HuPai
    li_dora_count: int
    red_dora_count: int
    score: int
    title_id: int
    xuan_shang_count: int
    xun: int
    yakuman_count: int
    def __init__(self, hupai: Optional[Union[GameRoundHuData.HuPai, Mapping]] = ..., fans: Optional[Iterable[Union[GameRoundHuData.Fan, Mapping]]] = ..., score: Optional[int] = ..., xun: Optional[int] = ..., title_id: Optional[int] = ..., fan_sum: Optional[int] = ..., fu_sum: Optional[int] = ..., yakuman_count: Optional[int] = ..., biao_dora_count: Optional[int] = ..., red_dora_count: Optional[int] = ..., li_dora_count: Optional[int] = ..., babei_count: Optional[int] = ..., xuan_shang_count: Optional[int] = ...) -> None: ...

class GameRoundPlayer(_message.Message):
    __slots__ = ["rank", "result", "score"]
    RANK_FIELD_NUMBER: ClassVar[int]
    RESULT_FIELD_NUMBER: ClassVar[int]
    SCORE_FIELD_NUMBER: ClassVar[int]
    rank: int
    result: GameRoundPlayerResult
    score: int
    def __init__(self, score: Optional[int] = ..., rank: Optional[int] = ..., result: Optional[Union[GameRoundPlayerResult, Mapping]] = ...) -> None: ...

class GameRoundPlayerResult(_message.Message):
    __slots__ = ["hands", "hu", "is_fulu", "is_liujumanguan", "lian_zhuang", "liqi_type", "ming", "type"]
    HANDS_FIELD_NUMBER: ClassVar[int]
    HU_FIELD_NUMBER: ClassVar[int]
    IS_FULU_FIELD_NUMBER: ClassVar[int]
    IS_LIUJUMANGUAN_FIELD_NUMBER: ClassVar[int]
    LIAN_ZHUANG_FIELD_NUMBER: ClassVar[int]
    LIQI_TYPE_FIELD_NUMBER: ClassVar[int]
    MING_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    hands: _containers.RepeatedScalarFieldContainer[str]
    hu: GameRoundHuData
    is_fulu: bool
    is_liujumanguan: bool
    lian_zhuang: int
    liqi_type: int
    ming: _containers.RepeatedScalarFieldContainer[str]
    type: int
    def __init__(self, type: Optional[int] = ..., hands: Optional[Iterable[str]] = ..., ming: Optional[Iterable[str]] = ..., liqi_type: Optional[int] = ..., is_fulu: bool = ..., is_liujumanguan: bool = ..., lian_zhuang: Optional[int] = ..., hu: Optional[Union[GameRoundHuData, Mapping]] = ...) -> None: ...

class GameRoundSnapshot(_message.Message):
    __slots__ = ["ben", "ju", "players"]
    BEN_FIELD_NUMBER: ClassVar[int]
    JU_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    ben: int
    ju: int
    players: _containers.RepeatedCompositeFieldContainer[GameRoundPlayer]
    def __init__(self, ju: Optional[int] = ..., ben: Optional[int] = ..., players: Optional[Iterable[Union[GameRoundPlayer, Mapping]]] = ...) -> None: ...

class GameRuleSetting(_message.Message):
    __slots__ = ["detail_rule_v2", "dora_count", "round_type", "shiduan", "thinking_type", "use_detail_rule"]
    DETAIL_RULE_V2_FIELD_NUMBER: ClassVar[int]
    DORA_COUNT_FIELD_NUMBER: ClassVar[int]
    ROUND_TYPE_FIELD_NUMBER: ClassVar[int]
    SHIDUAN_FIELD_NUMBER: ClassVar[int]
    THINKING_TYPE_FIELD_NUMBER: ClassVar[int]
    USE_DETAIL_RULE_FIELD_NUMBER: ClassVar[int]
    detail_rule_v2: ContestDetailRuleV2
    dora_count: int
    round_type: int
    shiduan: bool
    thinking_type: int
    use_detail_rule: bool
    def __init__(self, round_type: Optional[int] = ..., shiduan: bool = ..., dora_count: Optional[int] = ..., thinking_type: Optional[int] = ..., use_detail_rule: bool = ..., detail_rule_v2: Optional[Union[ContestDetailRuleV2, Mapping]] = ...) -> None: ...

class GameTestingEnvironmentSet(_message.Message):
    __slots__ = ["left_count", "paixing"]
    LEFT_COUNT_FIELD_NUMBER: ClassVar[int]
    PAIXING_FIELD_NUMBER: ClassVar[int]
    left_count: int
    paixing: int
    def __init__(self, paixing: Optional[int] = ..., left_count: Optional[int] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ["item_id", "stack"]
    ITEM_ID_FIELD_NUMBER: ClassVar[int]
    STACK_FIELD_NUMBER: ClassVar[int]
    item_id: int
    stack: int
    def __init__(self, item_id: Optional[int] = ..., stack: Optional[int] = ...) -> None: ...

class ItemGainRecord(_message.Message):
    __slots__ = ["count", "item_id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    ITEM_ID_FIELD_NUMBER: ClassVar[int]
    count: int
    item_id: int
    def __init__(self, item_id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...

class ItemGainRecords(_message.Message):
    __slots__ = ["limit_source_id", "record_time", "records"]
    LIMIT_SOURCE_ID_FIELD_NUMBER: ClassVar[int]
    RECORDS_FIELD_NUMBER: ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: ClassVar[int]
    limit_source_id: int
    record_time: int
    records: _containers.RepeatedCompositeFieldContainer[ItemGainRecord]
    def __init__(self, record_time: Optional[int] = ..., limit_source_id: Optional[int] = ..., records: Optional[Iterable[Union[ItemGainRecord, Mapping]]] = ...) -> None: ...

class Mail(_message.Message):
    __slots__ = ["attachments", "content", "create_time", "expire_time", "mail_id", "reference_id", "state", "take_attachment", "title"]
    ATTACHMENTS_FIELD_NUMBER: ClassVar[int]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: ClassVar[int]
    MAIL_ID_FIELD_NUMBER: ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    TAKE_ATTACHMENT_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    attachments: _containers.RepeatedCompositeFieldContainer[RewardSlot]
    content: str
    create_time: int
    expire_time: int
    mail_id: int
    reference_id: int
    state: int
    take_attachment: bool
    title: str
    def __init__(self, mail_id: Optional[int] = ..., state: Optional[int] = ..., take_attachment: bool = ..., title: Optional[str] = ..., content: Optional[str] = ..., attachments: Optional[Iterable[Union[RewardSlot, Mapping]]] = ..., create_time: Optional[int] = ..., expire_time: Optional[int] = ..., reference_id: Optional[int] = ...) -> None: ...

class MonthTicketInfo(_message.Message):
    __slots__ = ["end_time", "id", "last_pay_time"]
    END_TIME_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LAST_PAY_TIME_FIELD_NUMBER: ClassVar[int]
    end_time: int
    id: int
    last_pay_time: int
    def __init__(self, id: Optional[int] = ..., end_time: Optional[int] = ..., last_pay_time: Optional[int] = ...) -> None: ...

class NetworkEndpoint(_message.Message):
    __slots__ = ["address", "family", "port"]
    ADDRESS_FIELD_NUMBER: ClassVar[int]
    FAMILY_FIELD_NUMBER: ClassVar[int]
    PORT_FIELD_NUMBER: ClassVar[int]
    address: str
    family: str
    port: int
    def __init__(self, family: Optional[str] = ..., address: Optional[str] = ..., port: Optional[int] = ...) -> None: ...

class NotifyContestGameEnd(_message.Message):
    __slots__ = ["game_uuid", "unique_id"]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    game_uuid: str
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., game_uuid: Optional[str] = ...) -> None: ...

class NotifyContestGameStart(_message.Message):
    __slots__ = ["game_info", "unique_id"]
    GAME_INFO_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    game_info: ContestGameInfo
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., game_info: Optional[Union[ContestGameInfo, Mapping]] = ...) -> None: ...

class NotifyContestManagerKick(_message.Message):
    __slots__ = ["reason"]
    REASON_FIELD_NUMBER: ClassVar[int]
    reason: int
    def __init__(self, reason: Optional[int] = ...) -> None: ...

class NotifyContestMatchingPlayer(_message.Message):
    __slots__ = ["account_id", "nickname", "type", "unique_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    nickname: str
    type: int
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., type: Optional[int] = ..., account_id: Optional[int] = ..., nickname: Optional[str] = ...) -> None: ...

class NotifyContestMatchingPlayerLock(_message.Message):
    __slots__ = ["account_id", "manager_id", "type", "unique_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    MANAGER_ID_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    manager_id: int
    type: int
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., type: Optional[int] = ..., account_id: Optional[int] = ..., manager_id: Optional[int] = ...) -> None: ...

class NotifyContestNoticeUpdate(_message.Message):
    __slots__ = ["content", "notice_type", "unique_id"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    content: str
    notice_type: int
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ..., notice_type: Optional[int] = ..., content: Optional[str] = ...) -> None: ...

class OpenResult(_message.Message):
    __slots__ = ["replace", "reward"]
    REPLACE_FIELD_NUMBER: ClassVar[int]
    REWARD_FIELD_NUMBER: ClassVar[int]
    replace: RewardSlot
    reward: RewardSlot
    def __init__(self, reward: Optional[Union[RewardSlot, Mapping]] = ..., replace: Optional[Union[RewardSlot, Mapping]] = ...) -> None: ...

class PaymentSetting(_message.Message):
    __slots__ = ["alipay", "open_payment", "payment_info", "payment_info_show_type", "wechat"]
    class AlipayData(_message.Message):
        __slots__ = ["disable_create", "payment_source_platform"]
        DISABLE_CREATE_FIELD_NUMBER: ClassVar[int]
        PAYMENT_SOURCE_PLATFORM_FIELD_NUMBER: ClassVar[int]
        disable_create: bool
        payment_source_platform: int
        def __init__(self, disable_create: bool = ..., payment_source_platform: Optional[int] = ...) -> None: ...
    class WechatData(_message.Message):
        __slots__ = ["disable_create", "enable_credit", "payment_source_platform"]
        DISABLE_CREATE_FIELD_NUMBER: ClassVar[int]
        ENABLE_CREDIT_FIELD_NUMBER: ClassVar[int]
        PAYMENT_SOURCE_PLATFORM_FIELD_NUMBER: ClassVar[int]
        disable_create: bool
        enable_credit: bool
        payment_source_platform: int
        def __init__(self, disable_create: bool = ..., payment_source_platform: Optional[int] = ..., enable_credit: bool = ...) -> None: ...
    ALIPAY_FIELD_NUMBER: ClassVar[int]
    OPEN_PAYMENT_FIELD_NUMBER: ClassVar[int]
    PAYMENT_INFO_FIELD_NUMBER: ClassVar[int]
    PAYMENT_INFO_SHOW_TYPE_FIELD_NUMBER: ClassVar[int]
    WECHAT_FIELD_NUMBER: ClassVar[int]
    alipay: PaymentSetting.AlipayData
    open_payment: int
    payment_info: str
    payment_info_show_type: int
    wechat: PaymentSetting.WechatData
    def __init__(self, open_payment: Optional[int] = ..., payment_info_show_type: Optional[int] = ..., payment_info: Optional[str] = ..., wechat: Optional[Union[PaymentSetting.WechatData, Mapping]] = ..., alipay: Optional[Union[PaymentSetting.AlipayData, Mapping]] = ...) -> None: ...

class PlayerBaseView(_message.Message):
    __slots__ = ["account_id", "avatar_id", "level", "level3", "nickname", "title"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: ClassVar[int]
    LEVEL3_FIELD_NUMBER: ClassVar[int]
    LEVEL_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    account_id: int
    avatar_id: int
    level: AccountLevel
    level3: AccountLevel
    nickname: str
    title: int
    def __init__(self, account_id: Optional[int] = ..., avatar_id: Optional[int] = ..., title: Optional[int] = ..., nickname: Optional[str] = ..., level: Optional[Union[AccountLevel, Mapping]] = ..., level3: Optional[Union[AccountLevel, Mapping]] = ...) -> None: ...

class PlayerGameView(_message.Message):
    __slots__ = ["account_id", "avatar_id", "character", "level", "level3", "nickname", "title"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: ClassVar[int]
    CHARACTER_FIELD_NUMBER: ClassVar[int]
    LEVEL3_FIELD_NUMBER: ClassVar[int]
    LEVEL_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    account_id: int
    avatar_id: int
    character: Character
    level: AccountLevel
    level3: AccountLevel
    nickname: str
    title: int
    def __init__(self, account_id: Optional[int] = ..., avatar_id: Optional[int] = ..., title: Optional[int] = ..., nickname: Optional[str] = ..., level: Optional[Union[AccountLevel, Mapping]] = ..., character: Optional[Union[Character, Mapping]] = ..., level3: Optional[Union[AccountLevel, Mapping]] = ...) -> None: ...

class RecordCollectedData(_message.Message):
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

class RecordGame(_message.Message):
    __slots__ = ["accounts", "config", "end_time", "result", "start_time", "uuid"]
    class AccountInfo(_message.Message):
        __slots__ = ["account_id", "avatar_id", "character", "level", "level3", "nickname", "seat", "title"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        AVATAR_ID_FIELD_NUMBER: ClassVar[int]
        CHARACTER_FIELD_NUMBER: ClassVar[int]
        LEVEL3_FIELD_NUMBER: ClassVar[int]
        LEVEL_FIELD_NUMBER: ClassVar[int]
        NICKNAME_FIELD_NUMBER: ClassVar[int]
        SEAT_FIELD_NUMBER: ClassVar[int]
        TITLE_FIELD_NUMBER: ClassVar[int]
        account_id: int
        avatar_id: int
        character: Character
        level: AccountLevel
        level3: AccountLevel
        nickname: str
        seat: int
        title: int
        def __init__(self, account_id: Optional[int] = ..., seat: Optional[int] = ..., nickname: Optional[str] = ..., avatar_id: Optional[int] = ..., character: Optional[Union[Character, Mapping]] = ..., title: Optional[int] = ..., level: Optional[Union[AccountLevel, Mapping]] = ..., level3: Optional[Union[AccountLevel, Mapping]] = ...) -> None: ...
    ACCOUNTS_FIELD_NUMBER: ClassVar[int]
    CONFIG_FIELD_NUMBER: ClassVar[int]
    END_TIME_FIELD_NUMBER: ClassVar[int]
    RESULT_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[RecordGame.AccountInfo]
    config: GameConfig
    end_time: int
    result: GameEndResult
    start_time: int
    uuid: str
    def __init__(self, uuid: Optional[str] = ..., start_time: Optional[int] = ..., end_time: Optional[int] = ..., config: Optional[Union[GameConfig, Mapping]] = ..., accounts: Optional[Iterable[Union[RecordGame.AccountInfo, Mapping]]] = ..., result: Optional[Union[GameEndResult, Mapping]] = ...) -> None: ...

class ReqCommon(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReqContestManageLogin(_message.Message):
    __slots__ = ["account", "gen_access_token", "password", "type"]
    ACCOUNT_FIELD_NUMBER: ClassVar[int]
    GEN_ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    PASSWORD_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    account: str
    gen_access_token: bool
    password: str
    type: int
    def __init__(self, account: Optional[str] = ..., password: Optional[str] = ..., gen_access_token: bool = ..., type: Optional[int] = ...) -> None: ...

class ReqContestManageOauth2Auth(_message.Message):
    __slots__ = ["code", "type", "uid"]
    CODE_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    UID_FIELD_NUMBER: ClassVar[int]
    code: str
    type: int
    uid: str
    def __init__(self, type: Optional[int] = ..., code: Optional[str] = ..., uid: Optional[str] = ...) -> None: ...

class ReqContestManageOauth2Login(_message.Message):
    __slots__ = ["access_token", "reconnect", "type"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    RECONNECT_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    access_token: str
    reconnect: bool
    type: int
    def __init__(self, type: Optional[int] = ..., access_token: Optional[str] = ..., reconnect: bool = ...) -> None: ...

class ReqCreateContestGame(_message.Message):
    __slots__ = ["ai_level", "chat_broadcast_for_end", "open_live", "random_position", "slots", "tag"]
    class Slot(_message.Message):
        __slots__ = ["account_id", "seat", "start_point"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        SEAT_FIELD_NUMBER: ClassVar[int]
        START_POINT_FIELD_NUMBER: ClassVar[int]
        account_id: int
        seat: int
        start_point: int
        def __init__(self, account_id: Optional[int] = ..., start_point: Optional[int] = ..., seat: Optional[int] = ...) -> None: ...
    AI_LEVEL_FIELD_NUMBER: ClassVar[int]
    CHAT_BROADCAST_FOR_END_FIELD_NUMBER: ClassVar[int]
    OPEN_LIVE_FIELD_NUMBER: ClassVar[int]
    RANDOM_POSITION_FIELD_NUMBER: ClassVar[int]
    SLOTS_FIELD_NUMBER: ClassVar[int]
    TAG_FIELD_NUMBER: ClassVar[int]
    ai_level: int
    chat_broadcast_for_end: bool
    open_live: bool
    random_position: bool
    slots: _containers.RepeatedCompositeFieldContainer[ReqCreateContestGame.Slot]
    tag: str
    def __init__(self, slots: Optional[Iterable[Union[ReqCreateContestGame.Slot, Mapping]]] = ..., tag: Optional[str] = ..., random_position: bool = ..., open_live: bool = ..., chat_broadcast_for_end: bool = ..., ai_level: Optional[int] = ...) -> None: ...

class ReqCreateCustomizedContest(_message.Message):
    __slots__ = ["contest_name", "finish_time", "game_rule_setting", "open", "rank_rule", "start_time"]
    CONTEST_NAME_FIELD_NUMBER: ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: ClassVar[int]
    GAME_RULE_SETTING_FIELD_NUMBER: ClassVar[int]
    OPEN_FIELD_NUMBER: ClassVar[int]
    RANK_RULE_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    contest_name: str
    finish_time: int
    game_rule_setting: GameRuleSetting
    open: bool
    rank_rule: int
    start_time: int
    def __init__(self, contest_name: Optional[str] = ..., start_time: Optional[int] = ..., finish_time: Optional[int] = ..., open: bool = ..., rank_rule: Optional[int] = ..., game_rule_setting: Optional[Union[GameRuleSetting, Mapping]] = ...) -> None: ...

class ReqDeleteCustomizedContest(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqFetchContestNotice(_message.Message):
    __slots__ = ["notice_types"]
    NOTICE_TYPES_FIELD_NUMBER: ClassVar[int]
    notice_types: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, notice_types: Optional[Iterable[int]] = ...) -> None: ...

class ReqFetchCustomizedContestGameRecordList(_message.Message):
    __slots__ = ["last_index"]
    LAST_INDEX_FIELD_NUMBER: ClassVar[int]
    last_index: int
    def __init__(self, last_index: Optional[int] = ...) -> None: ...

class ReqLockGamePlayer(_message.Message):
    __slots__ = ["account_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    def __init__(self, account_id: Optional[int] = ...) -> None: ...

class ReqManageContest(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqPauseContestGame(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: ClassVar[int]
    uuid: str
    def __init__(self, uuid: Optional[str] = ...) -> None: ...

class ReqProlongContest(_message.Message):
    __slots__ = ["unique_id"]
    UNIQUE_ID_FIELD_NUMBER: ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: Optional[int] = ...) -> None: ...

class ReqRemoveContestGameRecord(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: ClassVar[int]
    uuid: str
    def __init__(self, uuid: Optional[str] = ...) -> None: ...

class ReqResumeContestGame(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: ClassVar[int]
    uuid: str
    def __init__(self, uuid: Optional[str] = ...) -> None: ...

class ReqSearchAccountByEid(_message.Message):
    __slots__ = ["eids"]
    EIDS_FIELD_NUMBER: ClassVar[int]
    eids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, eids: Optional[Iterable[int]] = ...) -> None: ...

class ReqSearchAccountByNickname(_message.Message):
    __slots__ = ["query_nicknames"]
    QUERY_NICKNAMES_FIELD_NUMBER: ClassVar[int]
    query_nicknames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, query_nicknames: Optional[Iterable[str]] = ...) -> None: ...

class ReqTerminateContestGame(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: ClassVar[int]
    uuid: str
    def __init__(self, uuid: Optional[str] = ...) -> None: ...

class ReqUnlockGamePlayer(_message.Message):
    __slots__ = ["account_id"]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    account_id: int
    def __init__(self, account_id: Optional[int] = ...) -> None: ...

class ReqUpdateContestGameRule(_message.Message):
    __slots__ = ["contest_name", "finish_time", "game_rule_setting", "open", "rank_rule", "start_time"]
    CONTEST_NAME_FIELD_NUMBER: ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: ClassVar[int]
    GAME_RULE_SETTING_FIELD_NUMBER: ClassVar[int]
    OPEN_FIELD_NUMBER: ClassVar[int]
    RANK_RULE_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    contest_name: str
    finish_time: int
    game_rule_setting: GameRuleSetting
    open: bool
    rank_rule: int
    start_time: int
    def __init__(self, contest_name: Optional[str] = ..., start_time: Optional[int] = ..., finish_time: Optional[int] = ..., open: bool = ..., rank_rule: Optional[int] = ..., game_rule_setting: Optional[Union[GameRuleSetting, Mapping]] = ...) -> None: ...

class ReqUpdateCustomizedContestChatSetting(_message.Message):
    __slots__ = ["account_ids", "chat_limit_type", "nicknames", "setting_type"]
    ACCOUNT_IDS_FIELD_NUMBER: ClassVar[int]
    CHAT_LIMIT_TYPE_FIELD_NUMBER: ClassVar[int]
    NICKNAMES_FIELD_NUMBER: ClassVar[int]
    SETTING_TYPE_FIELD_NUMBER: ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    chat_limit_type: int
    nicknames: _containers.RepeatedScalarFieldContainer[str]
    setting_type: int
    def __init__(self, setting_type: Optional[int] = ..., nicknames: Optional[Iterable[str]] = ..., account_ids: Optional[Iterable[int]] = ..., chat_limit_type: Optional[int] = ...) -> None: ...

class ReqUpdateCustomizedContestManager(_message.Message):
    __slots__ = ["account_ids", "nicknames", "setting_type"]
    ACCOUNT_IDS_FIELD_NUMBER: ClassVar[int]
    NICKNAMES_FIELD_NUMBER: ClassVar[int]
    SETTING_TYPE_FIELD_NUMBER: ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    nicknames: _containers.RepeatedScalarFieldContainer[str]
    setting_type: int
    def __init__(self, setting_type: Optional[int] = ..., nicknames: Optional[Iterable[str]] = ..., account_ids: Optional[Iterable[int]] = ...) -> None: ...

class ReqUpdateCustomizedContestNotice(_message.Message):
    __slots__ = ["content", "notice_type"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: ClassVar[int]
    content: str
    notice_type: int
    def __init__(self, notice_type: Optional[int] = ..., content: Optional[str] = ...) -> None: ...

class ReqUpdateCustomizedContestPlayer(_message.Message):
    __slots__ = ["account_ids", "nicknames", "setting_type"]
    ACCOUNT_IDS_FIELD_NUMBER: ClassVar[int]
    NICKNAMES_FIELD_NUMBER: ClassVar[int]
    SETTING_TYPE_FIELD_NUMBER: ClassVar[int]
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    nicknames: _containers.RepeatedScalarFieldContainer[str]
    setting_type: int
    def __init__(self, setting_type: Optional[int] = ..., nicknames: Optional[Iterable[str]] = ..., account_ids: Optional[Iterable[int]] = ...) -> None: ...

class ReqUpdateGameTag(_message.Message):
    __slots__ = ["tag", "uuid"]
    TAG_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    tag: str
    uuid: str
    def __init__(self, uuid: Optional[str] = ..., tag: Optional[str] = ...) -> None: ...

class ResAccountUpdate(_message.Message):
    __slots__ = ["error", "update"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    UPDATE_FIELD_NUMBER: ClassVar[int]
    error: Error
    update: AccountUpdate
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., update: Optional[Union[AccountUpdate, Mapping]] = ...) -> None: ...

class ResCommon(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    error: Error
    def __init__(self, error: Optional[Union[Error, Mapping]] = ...) -> None: ...

class ResContestManageLogin(_message.Message):
    __slots__ = ["access_token", "account_id", "diamond", "error", "last_create_time", "nickname"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    DIAMOND_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    LAST_CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    diamond: int
    error: Error
    last_create_time: int
    nickname: str
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., account_id: Optional[int] = ..., nickname: Optional[str] = ..., access_token: Optional[str] = ..., diamond: Optional[int] = ..., last_create_time: Optional[int] = ...) -> None: ...

class ResContestManageOauth2Auth(_message.Message):
    __slots__ = ["access_token", "error"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    access_token: str
    error: Error
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., access_token: Optional[str] = ...) -> None: ...

class ResContestManageOauth2Login(_message.Message):
    __slots__ = ["access_token", "account_id", "diamond", "error", "last_create_time", "nickname"]
    ACCESS_TOKEN_FIELD_NUMBER: ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
    DIAMOND_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    LAST_CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    NICKNAME_FIELD_NUMBER: ClassVar[int]
    access_token: str
    account_id: int
    diamond: int
    error: Error
    last_create_time: int
    nickname: str
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., account_id: Optional[int] = ..., nickname: Optional[str] = ..., access_token: Optional[str] = ..., diamond: Optional[int] = ..., last_create_time: Optional[int] = ...) -> None: ...

class ResCreateContestGame(_message.Message):
    __slots__ = ["error", "game_uuid"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    GAME_UUID_FIELD_NUMBER: ClassVar[int]
    error: Error
    game_uuid: str
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., game_uuid: Optional[str] = ...) -> None: ...

class ResCreateCustomizedContest(_message.Message):
    __slots__ = ["contest", "diamond", "error"]
    CONTEST_FIELD_NUMBER: ClassVar[int]
    DIAMOND_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    contest: CustomizedContest
    diamond: int
    error: Error
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., contest: Optional[Union[CustomizedContest, Mapping]] = ..., diamond: Optional[int] = ...) -> None: ...

class ResCustomizedContestChatInfo(_message.Message):
    __slots__ = ["chat_limit_roster", "chat_limit_type", "error"]
    class Item(_message.Message):
        __slots__ = ["account_id", "nickname"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        NICKNAME_FIELD_NUMBER: ClassVar[int]
        account_id: int
        nickname: str
        def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ...) -> None: ...
    CHAT_LIMIT_ROSTER_FIELD_NUMBER: ClassVar[int]
    CHAT_LIMIT_TYPE_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    chat_limit_roster: _containers.RepeatedCompositeFieldContainer[ResCustomizedContestChatInfo.Item]
    chat_limit_type: int
    error: Error
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., chat_limit_type: Optional[int] = ..., chat_limit_roster: Optional[Iterable[Union[ResCustomizedContestChatInfo.Item, Mapping]]] = ...) -> None: ...

class ResFetchContestGameRule(_message.Message):
    __slots__ = ["error", "game_rule_setting"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    GAME_RULE_SETTING_FIELD_NUMBER: ClassVar[int]
    error: Error
    game_rule_setting: GameRuleSetting
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., game_rule_setting: Optional[Union[GameRuleSetting, Mapping]] = ...) -> None: ...

class ResFetchContestNotice(_message.Message):
    __slots__ = ["error", "notices"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    NOTICES_FIELD_NUMBER: ClassVar[int]
    error: Error
    notices: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., notices: Optional[Iterable[str]] = ...) -> None: ...

class ResFetchCustomizedContestGameRecordList(_message.Message):
    __slots__ = ["error", "next_index", "record_list"]
    class Item(_message.Message):
        __slots__ = ["record", "tag"]
        RECORD_FIELD_NUMBER: ClassVar[int]
        TAG_FIELD_NUMBER: ClassVar[int]
        record: RecordGame
        tag: str
        def __init__(self, record: Optional[Union[RecordGame, Mapping]] = ..., tag: Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: ClassVar[int]
    NEXT_INDEX_FIELD_NUMBER: ClassVar[int]
    RECORD_LIST_FIELD_NUMBER: ClassVar[int]
    error: Error
    next_index: int
    record_list: _containers.RepeatedCompositeFieldContainer[ResFetchCustomizedContestGameRecordList.Item]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., next_index: Optional[int] = ..., record_list: Optional[Iterable[Union[ResFetchCustomizedContestGameRecordList.Item, Mapping]]] = ...) -> None: ...

class ResFetchCustomizedContestManager(_message.Message):
    __slots__ = ["error", "players"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    error: Error
    players: _containers.RepeatedCompositeFieldContainer[ContestPlayerInfo]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., players: Optional[Iterable[Union[ContestPlayerInfo, Mapping]]] = ...) -> None: ...

class ResFetchCustomizedContestPlayer(_message.Message):
    __slots__ = ["error", "players"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    error: Error
    players: _containers.RepeatedCompositeFieldContainer[ContestPlayerInfo]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., players: Optional[Iterable[Union[ContestPlayerInfo, Mapping]]] = ...) -> None: ...

class ResFetchRelatedContestList(_message.Message):
    __slots__ = ["contests", "error"]
    CONTESTS_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    contests: _containers.RepeatedCompositeFieldContainer[CustomizedContest]
    error: Error
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., contests: Optional[Iterable[Union[CustomizedContest, Mapping]]] = ...) -> None: ...

class ResManageContest(_message.Message):
    __slots__ = ["contest", "error"]
    CONTEST_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    contest: CustomizedContest
    error: Error
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., contest: Optional[Union[CustomizedContest, Mapping]] = ...) -> None: ...

class ResProlongContest(_message.Message):
    __slots__ = ["deadline", "error"]
    DEADLINE_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    deadline: int
    error: Error
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., deadline: Optional[int] = ...) -> None: ...

class ResSearchAccountByEid(_message.Message):
    __slots__ = ["error", "search_result"]
    class Item(_message.Message):
        __slots__ = ["account_id", "nickname"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        NICKNAME_FIELD_NUMBER: ClassVar[int]
        account_id: int
        nickname: str
        def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: ClassVar[int]
    SEARCH_RESULT_FIELD_NUMBER: ClassVar[int]
    error: Error
    search_result: _containers.RepeatedCompositeFieldContainer[ResSearchAccountByEid.Item]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., search_result: Optional[Iterable[Union[ResSearchAccountByEid.Item, Mapping]]] = ...) -> None: ...

class ResSearchAccountByNickname(_message.Message):
    __slots__ = ["error", "search_result"]
    class Item(_message.Message):
        __slots__ = ["account_id", "nickname"]
        ACCOUNT_ID_FIELD_NUMBER: ClassVar[int]
        NICKNAME_FIELD_NUMBER: ClassVar[int]
        account_id: int
        nickname: str
        def __init__(self, account_id: Optional[int] = ..., nickname: Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: ClassVar[int]
    SEARCH_RESULT_FIELD_NUMBER: ClassVar[int]
    error: Error
    search_result: _containers.RepeatedCompositeFieldContainer[ResSearchAccountByNickname.Item]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., search_result: Optional[Iterable[Union[ResSearchAccountByNickname.Item, Mapping]]] = ...) -> None: ...

class ResStartManageGame(_message.Message):
    __slots__ = ["error", "games", "players"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    GAMES_FIELD_NUMBER: ClassVar[int]
    PLAYERS_FIELD_NUMBER: ClassVar[int]
    error: Error
    games: _containers.RepeatedCompositeFieldContainer[ContestGameInfo]
    players: _containers.RepeatedCompositeFieldContainer[ContestMatchingPlayer]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., players: Optional[Iterable[Union[ContestMatchingPlayer, Mapping]]] = ..., games: Optional[Iterable[Union[ContestGameInfo, Mapping]]] = ...) -> None: ...

class ResUpdateCustomizedContestChatSetting(_message.Message):
    __slots__ = ["error", "failed_index"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    FAILED_INDEX_FIELD_NUMBER: ClassVar[int]
    error: Error
    failed_index: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., failed_index: Optional[Iterable[int]] = ...) -> None: ...

class ResUpdateCustomizedContestPlayer(_message.Message):
    __slots__ = ["error", "failed_index"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    FAILED_INDEX_FIELD_NUMBER: ClassVar[int]
    error: Error
    failed_index: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: Optional[Union[Error, Mapping]] = ..., failed_index: Optional[Iterable[int]] = ...) -> None: ...

class RewardPlusResult(_message.Message):
    __slots__ = ["count", "exchange", "id"]
    class Exchange(_message.Message):
        __slots__ = ["count", "exchange", "id"]
        COUNT_FIELD_NUMBER: ClassVar[int]
        EXCHANGE_FIELD_NUMBER: ClassVar[int]
        ID_FIELD_NUMBER: ClassVar[int]
        count: int
        exchange: int
        id: int
        def __init__(self, id: Optional[int] = ..., count: Optional[int] = ..., exchange: Optional[int] = ...) -> None: ...
    COUNT_FIELD_NUMBER: ClassVar[int]
    EXCHANGE_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    count: int
    exchange: RewardPlusResult.Exchange
    id: int
    def __init__(self, id: Optional[int] = ..., count: Optional[int] = ..., exchange: Optional[Union[RewardPlusResult.Exchange, Mapping]] = ...) -> None: ...

class RewardSlot(_message.Message):
    __slots__ = ["count", "id"]
    COUNT_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    count: int
    id: int
    def __init__(self, id: Optional[int] = ..., count: Optional[int] = ...) -> None: ...

class RollingNotice(_message.Message):
    __slots__ = ["content", "end_time", "id", "repeat_interval", "start_time"]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    END_TIME_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    REPEAT_INTERVAL_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    content: str
    end_time: int
    id: int
    repeat_interval: int
    start_time: int
    def __init__(self, id: Optional[int] = ..., content: Optional[str] = ..., start_time: Optional[int] = ..., end_time: Optional[int] = ..., repeat_interval: Optional[int] = ...) -> None: ...

class Room(_message.Message):
    __slots__ = ["is_playing", "max_player_count", "mode", "owner_id", "persons", "public_live", "ready_list", "robot_count", "room_id", "tournament_id"]
    IS_PLAYING_FIELD_NUMBER: ClassVar[int]
    MAX_PLAYER_COUNT_FIELD_NUMBER: ClassVar[int]
    MODE_FIELD_NUMBER: ClassVar[int]
    OWNER_ID_FIELD_NUMBER: ClassVar[int]
    PERSONS_FIELD_NUMBER: ClassVar[int]
    PUBLIC_LIVE_FIELD_NUMBER: ClassVar[int]
    READY_LIST_FIELD_NUMBER: ClassVar[int]
    ROBOT_COUNT_FIELD_NUMBER: ClassVar[int]
    ROOM_ID_FIELD_NUMBER: ClassVar[int]
    TOURNAMENT_ID_FIELD_NUMBER: ClassVar[int]
    is_playing: bool
    max_player_count: int
    mode: GameMode
    owner_id: int
    persons: _containers.RepeatedCompositeFieldContainer[PlayerGameView]
    public_live: bool
    ready_list: _containers.RepeatedScalarFieldContainer[int]
    robot_count: int
    room_id: int
    tournament_id: int
    def __init__(self, room_id: Optional[int] = ..., owner_id: Optional[int] = ..., mode: Optional[Union[GameMode, Mapping]] = ..., max_player_count: Optional[int] = ..., persons: Optional[Iterable[Union[PlayerGameView, Mapping]]] = ..., ready_list: Optional[Iterable[int]] = ..., is_playing: bool = ..., public_live: bool = ..., robot_count: Optional[int] = ..., tournament_id: Optional[int] = ...) -> None: ...

class ServerSettings(_message.Message):
    __slots__ = ["payment_setting"]
    PAYMENT_SETTING_FIELD_NUMBER: ClassVar[int]
    payment_setting: PaymentSetting
    def __init__(self, payment_setting: Optional[Union[PaymentSetting, Mapping]] = ...) -> None: ...

class ShopInfo(_message.Message):
    __slots__ = ["buy_records", "last_refresh_time", "zhp"]
    BUY_RECORDS_FIELD_NUMBER: ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: ClassVar[int]
    ZHP_FIELD_NUMBER: ClassVar[int]
    buy_records: _containers.RepeatedCompositeFieldContainer[BuyRecord]
    last_refresh_time: int
    zhp: ZHPShop
    def __init__(self, zhp: Optional[Union[ZHPShop, Mapping]] = ..., buy_records: Optional[Iterable[Union[BuyRecord, Mapping]]] = ..., last_refresh_time: Optional[int] = ...) -> None: ...

class TaskProgress(_message.Message):
    __slots__ = ["achieved", "counter", "id", "rewarded"]
    ACHIEVED_FIELD_NUMBER: ClassVar[int]
    COUNTER_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    REWARDED_FIELD_NUMBER: ClassVar[int]
    achieved: bool
    counter: int
    id: int
    rewarded: bool
    def __init__(self, id: Optional[int] = ..., counter: Optional[int] = ..., achieved: bool = ..., rewarded: bool = ...) -> None: ...

class Wrapper(_message.Message):
    __slots__ = ["data", "name"]
    DATA_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    data: bytes
    name: str
    def __init__(self, name: Optional[str] = ..., data: Optional[bytes] = ...) -> None: ...

class ZHPShop(_message.Message):
    __slots__ = ["buy_records", "cost_refresh", "free_refresh", "goods"]
    class RefreshCount(_message.Message):
        __slots__ = ["count", "limit"]
        COUNT_FIELD_NUMBER: ClassVar[int]
        LIMIT_FIELD_NUMBER: ClassVar[int]
        count: int
        limit: int
        def __init__(self, count: Optional[int] = ..., limit: Optional[int] = ...) -> None: ...
    BUY_RECORDS_FIELD_NUMBER: ClassVar[int]
    COST_REFRESH_FIELD_NUMBER: ClassVar[int]
    FREE_REFRESH_FIELD_NUMBER: ClassVar[int]
    GOODS_FIELD_NUMBER: ClassVar[int]
    buy_records: _containers.RepeatedCompositeFieldContainer[BuyRecord]
    cost_refresh: ZHPShop.RefreshCount
    free_refresh: ZHPShop.RefreshCount
    goods: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, goods: Optional[Iterable[int]] = ..., buy_records: Optional[Iterable[Union[BuyRecord, Mapping]]] = ..., free_refresh: Optional[Union[ZHPShop.RefreshCount, Mapping]] = ..., cost_refresh: Optional[Union[ZHPShop.RefreshCount, Mapping]] = ...) -> None: ...

class GamePlayerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
