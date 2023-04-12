import sys


vi = sys.version_info

if vi.minor in (7, 8, 9):
    from __future__ import annotations  # for Python 3.7-3.9  # NOQA

if vi.minor < 11:
    from typing import Any, Optional, Callable
    from typing_extensions import (
        NotRequired,  # NOQA
        TypedDict
    )  # for Python <3.11 with (Not)Required
else:
    from typing import TypedDict, Any, Optional, Callable, NotRequired  # NOQA

del sys
del vi


RADIUS_CIRCLE: int = ...


class COLOR_FORMAT:
    UNKNOWN: int = 0
    L8: int = 1
    A8: int = 2
    I1: int = 3
    I2: int = 4
    I4: int = 5
    I8: int = 6
    A8L8: int = 7
    ARGB2222: int = 8
    RGB565: int = 9
    RGB565_CHROMA_KEYED: int = 10
    ARGB1555: int = 11
    ARGB4444: int = 12
    RGB565A8: int = 13
    ARGB8565: int = 14
    RGB888: int = 15
    RGB888_CHROMA_KEYED: int = 16
    ARGB8888: int = 17
    XRGB8888: int = 18
    XRGB8888_CHROMA_KEYED: int = 19
    NATIVE: int = RGB565
    NATIVE_CHROMA_KEYED: int = RGB565_CHROMA_KEYED
    NATIVE_ALPHA: int = ARGB8565
    NATIVE_REVERSED: int = 0x1A
    NATIVE_ALPHA_REVERSED: int = 27
    RAW: int = 28
    RAW_ALPHA: int = 29
    
    
class INDEV_TYPE:
    """
    Possible input device types
    """
    NONE: int = 0
    POINTER: int = 1
    KEYPAD: int = 2
    BUTTON: int = 3
    ENCODER: int = 4


class INDEV_STATE:
    """
    States for input devices
    """
    RELEASED: int = 0
    PRESSED: int = 1
    
    
class COVER_RES:
    """
    Cover check results.
    """
    COVER: int = 0
    NOT_COVER: int = 1
    MASKED: int = 2
    

class GRAD_DIR:
    """
    The direction of the gradient.
    """
    NONE: int = 0
    VER: int = 1
    HOR: int = 2


class STYLE:
    """
    Enumeration of all built in style properties
    """
    PROP_INV: int = 0
    WIDTH: int = 1
    MIN_WIDTH: int = 2
    MAX_WIDTH: int = 3
    HEIGHT: int = 4
    MIN_HEIGHT: int = 5
    MAX_HEIGHT: int = 6
    X: int = 7
    Y: int = 8
    ALIGN: int = 9
    LAYOUT: int = 10
    RADIUS: int = 11
    PAD_TOP: int = 16
    PAD_BOTTOM: int = 17
    PAD_LEFT: int = 18
    PAD_RIGHT: int = 19
    PAD_ROW: int = 20
    PAD_COLUMN: int = 21
    BASE_DIR: int = 22
    CLIP_CORNER: int = 23
    MARGIN_TOP: int = 24
    MARGIN_BOTTOM: int = 25
    MARGIN_LEFT: int = 26
    MARGIN_RIGHT: int = 27
    BG_COLOR: int = 32
    BG_OPA: int = 33
    BG_GRAD_COLOR: int = 34
    BG_GRAD_DIR: int = 35
    BG_MAIN_STOP: int = 36
    BG_GRAD_STOP: int = 37
    BG_GRAD: int = 38
    BG_DITHER_MODE: int = 39
    BG_IMG_SRC: int = 40
    BG_IMG_OPA: int = 41
    BG_IMG_RECOLOR: int = 42
    BG_IMG_RECOLOR_OPA: int = 43
    BG_IMG_TILED: int = 44
    BORDER_COLOR: int = 48
    BORDER_OPA: int = 49
    BORDER_WIDTH: int = 50
    BORDER_SIDE: int = 51
    BORDER_POST: int = 52
    OUTLINE_WIDTH: int = 53
    OUTLINE_COLOR: int = 54
    OUTLINE_OPA: int = 55
    OUTLINE_PAD: int = 56
    SHADOW_WIDTH: int = 64
    SHADOW_OFS_X: int = 65
    SHADOW_OFS_Y: int = 66
    SHADOW_SPREAD: int = 67
    SHADOW_COLOR: int = 68
    SHADOW_OPA: int = 69
    IMG_OPA: int = 70
    IMG_RECOLOR: int = 71
    IMG_RECOLOR_OPA: int = 72
    LINE_WIDTH: int = 73
    LINE_DASH_WIDTH: int = 74
    LINE_DASH_GAP: int = 75
    LINE_ROUNDED: int = 76
    LINE_COLOR: int = 77
    LINE_OPA: int = 78
    ARC_WIDTH: int = 80
    ARC_ROUNDED: int = 81
    ARC_COLOR: int = 82
    ARC_OPA: int = 83
    ARC_IMG_SRC: int = 84
    TEXT_COLOR: int = 85
    TEXT_OPA: int = 86
    TEXT_FONT: int = 87
    TEXT_LETTER_SPACE: int = 88
    TEXT_LINE_SPACE: int = 89
    TEXT_DECOR: int = 90
    TEXT_ALIGN: int = 91
    OPA: int = 96
    COLOR_FILTER_DSC: int = 97
    COLOR_FILTER_OPA: int = 98
    ANIM: int = 99
    ANIM_TIME: int = 100
    ANIM_SPEED: int = 101
    TRANSITION: int = 102
    BLEND_MODE: int = 103
    TRANSFORM_WIDTH: int = 104
    TRANSFORM_HEIGHT: int = 105
    TRANSLATE_X: int = 106
    TRANSLATE_Y: int = 107
    TRANSFORM_ZOOM: int = 108
    TRANSFORM_ANGLE: int = 109
    TRANSFORM_PIVOT_X: int = 110
    TRANSFORM_PIVOT_Y: int = 111
    PROP_ANY: int = 0xFFFF
    

class EVENT:
    """
    Type of event being sent to the object.
    """
    ALL: int = 0
    PRESSED: int = 1
    PRESSING: int = 2
    PRESS_LOST: int = 3
    SHORT_CLICKED: int = 4
    LONG_PRESSED: int = 5
    LONG_PRESSED_REPEAT: int = 6
    CLICKED: int = 7
    RELEASED: int = 8
    SCROLL_BEGIN: int = 9
    SCROLL_THROW_BEGIN: int = 10
    SCROLL_END: int = 11
    SCROLL: int = 12
    GESTURE: int = 13
    KEY: int = 14
    FOCUSED: int = 15
    DEFOCUSED: int = 16
    LEAVE: int = 17
    HIT_TEST: int = 18
    COVER_CHECK: int = 19
    REFR_EXT_DRAW_SIZE: int = 20
    DRAW_MAIN_BEGIN: int = 21
    DRAW_MAIN: int = 22
    DRAW_MAIN_END: int = 23
    DRAW_POST_BEGIN: int = 24
    DRAW_POST: int = 25
    DRAW_POST_END: int = 26
    DRAW_PART_BEGIN: int = 27
    DRAW_PART_END: int = 28
    VALUE_CHANGED: int = 29
    INSERT: int = 30
    REFRESH: int = 31
    READY: int = 32
    CANCEL: int = 33
    DELETE: int = 34
    CHILD_CHANGED: int = 35
    CHILD_CREATED: int = 36
    CHILD_DELETED: int = 37
    SCREEN_UNLOAD_START: int = 38
    SCREEN_LOAD_START: int = 39
    SCREEN_LOADED: int = 40
    SCREEN_UNLOADED: int = 41
    SIZE_CHANGED: int = 42
    STYLE_CHANGED: int = 43
    LAYOUT_CHANGED: int = 44
    GET_SELF_SIZE: int = 45
    INVALIDATE_AREA: int = 46
    RENDER_START: int = 47
    RENDER_READY: int = 48
    RESOLUTION_CHANGED: int = 49
    PREPROCESS: int = 0x80

class DISP_ROTATION:
    _0: int = 0
    _90: int = 1
    _180: int = 2
    _270: int = 3


class DISP_RENDER_MODE:
    PARTIAL: int = 0
    DIRECT: int = 1
    FULL: int = 2


class SCR_LOAD_ANIM:
    NONE: int = 0
    OVER_LEFT: int = 1
    OVER_RIGHT: int = 2
    OVER_TOP: int = 3
    OVER_BOTTOM: int = 4
    MOVE_LEFT: int = 5
    MOVE_RIGHT: int = 6
    MOVE_TOP: int = 7
    MOVE_BOTTOM: int = 8
    FADE_IN: int = 9
    FADE_ON: int = FADE_IN
    FADE_OUT: int = 10
    OUT_LEFT: int = 11
    OUT_RIGHT: int = 12
    OUT_TOP: int = 13
    OUT_BOTTOM: int = 14


class KEY:
    UP: int = 17
    DOWN: int = 18
    RIGHT: int = 19
    LEFT: int = 20
    ESC: int = 27
    DEL: int = 127
    BACKSPACE: int = 8
    ENTER: int = 10
    NEXT: int = 9
    PREV: int = 11
    HOME: int = 2
    END: int = 3


class GROUP_REFOCUS_POLICY:
    NEXT: int = 0
    PREV: int = 1


class STATE:
    """
    Possible states of a widget. OR-ed values are possible
    """
    DEFAULT: int = 0x0000
    CHECKED: int = 0x0001
    FOCUSED: int = 0x0002
    FOCUS_KEY: int = 0x0004
    EDITED: int = 0x0008
    HOVERED: int = 0x0010
    PRESSED: int = 0x0020
    SCROLLED: int = 0x0040
    DISABLED: int = 0x0080
    USER_1: int = 0x1000
    USER_2: int = 0x2000
    USER_3: int = 0x4000
    USER_4: int = 0x8000
    ANY: int = 0xFFFF


class PART:
    """
    The possible parts of widgets. The parts can be considered as
    the internal building block of the widgets.
    E.g. slider = background + indicator + knob Not all parts are
    used by every widget
    """
    MAIN: int = 0x000000
    SCROLLBAR: int = 0x010000
    INDICATOR: int = 0x020000
    KNOB: int = 0x030000
    SELECTED: int = 0x040000
    ITEMS: int = 0x050000
    TICKS: int = 0x060000
    CURSOR: int = 0x070000
    CUSTOM_FIRST: int = 0x080000
    ANY: int = 0x0F0000


class LAYER_TYPE:
    NONE: int = 0
    SIMPLE: int = 1
    TRANSFORM: int = 2


class SCROLLBAR_MODE:
    """
    Scrollbar modes: shows when should the scrollbars be visible
    """
    OFF: int = 0
    ON: int = 1
    ACTIVE: int = 2
    AUTO: int = 3


class SCROLL_SNAP:
    """
    Scroll span align options. Tells where to align
    the snappable children when scroll stops.
    """
    NONE: int = 0
    START: int = 1
    END: int = 2
    CENTER: int = 3


class FLEX_ALIGN:
    START: int = 0
    END: int = 1
    CENTER: int = 2
    SPACE_EVENLY: int = 3
    SPACE_AROUND: int = 4
    SPACE_BETWEEN: int = 5


class FLEX_FLOW:
    ROW: int = 0x00
    COLUMN: int = 0
    ROW_WRAP: int = 2
    ROW_REVERSE: int = 3
    ROW_WRAP_REVERSE: int = 3
    COLUMN_WRAP: int = 2
    COLUMN_REVERSE: int = 3
    COLUMN_WRAP_REVERSE: int = 3


class GRID_ALIGN:
    START: int = 0
    CENTER: int = 1
    END: int = 2
    STRETCH: int = 3
    SPACE_EVENLY: int = 4
    SPACE_AROUND: int = 5
    SPACE_BETWEEN: int = 6


class ANIM:
    """
    Can be used to indicate if animations are enabled or disabled in a case
    """
    OFF: int = 0
    ON: int = 1


class ALIGN:
    """
    Alignments
    """
    DEFAULT: int = 0
    TOP_LEFT: int = 1
    TOP_MID: int = 2
    TOP_RIGHT: int = 3
    BOTTOM_LEFT: int = 4
    BOTTOM_MID: int = 5
    BOTTOM_RIGHT: int = 6
    LEFT_MID: int = 7
    RIGHT_MID: int = 8
    CENTER: int = 9
    OUT_TOP_LEFT: int = 10
    OUT_TOP_MID: int = 11
    OUT_TOP_RIGHT: int = 12
    OUT_BOTTOM_LEFT: int = 13
    OUT_BOTTOM_MID: int = 14
    OUT_BOTTOM_RIGHT: int = 15
    OUT_LEFT_TOP: int = 16
    OUT_LEFT_MID: int = 17
    OUT_LEFT_BOTTOM: int = 18
    OUT_RIGHT_TOP: int = 19
    OUT_RIGHT_MID: int = 20
    OUT_RIGHT_BOTTOM: int = 21


class DIR:
    NONE: int = 0x00
    LEFT: int = 0
    RIGHT: int = 1
    TOP: int = 2
    BOTTOM: int = 3
    HOR: int = RIGHT
    VER: int = BOTTOM
    ALL: int = VER


class BASE_DIR:
    LTR: int = 0x00
    RTL: int = 0x01
    AUTO: int = 0x02
    NEUTRAL: int = 0x20
    WEAK: int = 0x21


class OPA:
    """
    Opacity percentages.
    """
    TRANSP: int = 0
    _0: int = 0
    _10: int = 25
    _20: int = 51
    _30: int = 76
    _40: int = 102
    _50: int = 127
    _60: int = 153
    _70: int = 178
    _80: int = 204
    _90: int = 229
    _100: int = 255
    COVER: int = 255


class PALETTE:
    RED: int = 0
    PINK: int = 1
    PURPLE: int = 2
    DEEP_PURPLE: int = 3
    INDIGO: int = 4
    BLUE: int = 5
    LIGHT_BLUE: int = 6
    CYAN: int = 7
    TEAL: int = 8
    GREEN: int = 9
    LIGHT_GREEN: int = 10
    LIME: int = 11
    YELLOW: int = 12
    AMBER: int = 13
    ORANGE: int = 14
    DEEP_ORANGE: int = 15
    BROWN: int = 16
    BLUE_GREY: int = 17
    GREY: int = 18
    NONE: int = 0xff


class BLEND_MODE:
    """
    Possible options how to blend opaque drawings
    """
    NORMAL: int = 0
    ADDITIVE: int = 1
    SUBTRACTIVE: int = 2
    MULTIPLY: int = 3
    REPLACE: int = 4


class TEXT_DECOR:
    """
    Some options to apply decorations on texts. 'OR'ed values can be used.
    """
    NONE: int = 0x00
    UNDERLINE: int = 0x01
    STRIKETHROUGH: int = 0x02


class BORDER_SIDE:
    """
    Selects on which sides border should be drawn 'OR'ed values can be used.
    """
    NONE: int = 0x00
    BOTTOM: int = 0x01
    TOP: int = 0x02
    LEFT: int = 0x04
    RIGHT: int = 0x08
    FULL: int = 0x0F
    INTERNAL: int = 0x10


class DITHER:
    """
    The dithering algorithm for the gradient
    Depends on LV_DRAW_SW_GRADIENT_DITHER
    """
    NONE: int = 0
    ORDERED: int = 1
    ERR_DIFF: int = 2


class TEXT_FLAG:
    """
    Options for text rendering.
    """
    NONE: int = 0x00
    RECOLOR: int = 0x01
    EXPAND: int = 0x02
    FIT: int = 0x04


class TEXT_CMD_STATE:
    """
    State machine for text renderer.
    """
    WAIT: int = 0
    PAR: int = 1
    IN: int = 2


class TEXT_ALIGN:
    """
    Label align policy
    """
    AUTO: int = 0
    LEFT: int = 1
    CENTER: int = 2
    RIGHT: int = 3


class RES:
    """
    LVGL error codes.
    """
    INV: int = 0
    OK: int = 1


class ANIM_IMG_PART_MAIN:
    ANIM_IMG_PART_MAIN: int = 0


class PART_TEXTAREA_PLACEHOLDER:
    PART_TEXTAREA_PLACEHOLDER: int = PART.CUSTOM_FIRST


class _type__anim_t(TypedDict):
    var: NotRequired[None]
    exec_cb: NotRequired["anim_exec_xcb_t"]
    start_cb: NotRequired["anim_start_cb_t"]
    ready_cb: NotRequired["anim_ready_cb_t"]
    deleted_cb: NotRequired["anim_deleted_cb_t"]
    get_value_cb: NotRequired["anim_get_value_cb_t"]
    user_data: NotRequired[None]
    path_cb: NotRequired["anim_path_cb_t"]
    start_value: NotRequired[int]
    current_value: NotRequired[int]
    end_value: NotRequired[int]
    time: NotRequired[int]
    act_time: NotRequired[int]
    playback_delay: NotRequired[int]
    playback_time: NotRequired[int]
    repeat_delay: NotRequired[int]
    repeat_cnt: NotRequired[int]
    early_apply: NotRequired[bool]
    last_timer_run: NotRequired[int]
    playback_now: NotRequired[bool]
    run_round: NotRequired[bool]
    start_cb_called: NotRequired[bool]


class _anim_t(object):
    """
    Describes an animation
    """
    """Variable to animate"""
    var: None = ...
    """Function to execute to animate"""
    exec_cb: "anim_exec_xcb_t" = ...
    """Call it when the animation is starts (considering"""
    start_cb: "anim_start_cb_t" = ...
    """Call it when the animation is ready"""
    ready_cb: "anim_ready_cb_t" = ...
    """Call it when the animation is deleted"""
    deleted_cb: "anim_deleted_cb_t" = ...
    """Get the current value in relative mode"""
    get_value_cb: "anim_get_value_cb_t" = ...
    """Custom user data"""
    user_data: None = ...
    """Describe the path (curve) of animations"""
    path_cb: "anim_path_cb_t" = ...
    """Start value"""
    start_value: int = ...
    """Current value"""
    current_value: int = ...
    """End value"""
    end_value: int = ...
    """Animation time in ms"""
    time: int = ...
    """Current time in animation. Set to negative to make delay."""
    act_time: int = ...
    """Wait before play back"""
    playback_delay: int = ...
    """Duration of playback animation"""
    playback_time: int = ...
    """Wait before repeat"""
    repeat_delay: int = ...
    """Repeat count for the animation"""
    repeat_cnt: int = ...
    """1: Apply start value immediately even is there is"""
    early_apply: bool = ...
    last_timer_run: int = ...
    """Play back is in progress"""
    playback_now: bool = ...
    """Indicates the animation has run in this round"""
    run_round: bool = ...
    """Indicates that the"""
    start_cb_called: bool = ...

    def __init__(self, fields: Optional[_type__anim_t] = {}, /):
        ...


class _type__bar_anim_t(TypedDict):
    bar: NotRequired["obj_t"]
    anim_start: NotRequired[int]
    anim_end: NotRequired[int]
    anim_state: NotRequired[int]


class _bar_anim_t(object):
    bar: "obj_t" = ...
    anim_start: int = ...
    anim_end: int = ...
    anim_state: int = ...

    def __init__(self, fields: Optional[_type__bar_anim_t] = {}, /):
        ...


class _type__color_filter_dsc_t(TypedDict):
    filter_cb: NotRequired["color_filter_cb_t"]
    user_data: NotRequired[None]


class _color_filter_dsc_t(object):
    filter_cb: "color_filter_cb_t" = ...
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type__color_filter_dsc_t] = {}, /):
        ...


class _type__disp_t(TypedDict):
    hor_res: NotRequired["coord_t"]
    ver_res: NotRequired["coord_t"]
    physical_hor_res: NotRequired["coord_t"]
    physical_ver_res: NotRequired["coord_t"]
    offset_x: NotRequired["coord_t"]
    offset_y: NotRequired["coord_t"]
    dpi: NotRequired[int]
    draw_buf_1: NotRequired[None]
    draw_buf_2: NotRequired[None]
    draw_buf_act: NotRequired[None]
    draw_buf_size: NotRequired[int]
    flushing: NotRequired[int]
    flushing_last: NotRequired[int]
    last_area: NotRequired[bool]
    last_part: NotRequired[bool]
    render_mode: NotRequired["disp_render_mode_t"]
    antialiasing: NotRequired[bool]
    rendering_in_progress: NotRequired[bool]
    color_format: NotRequired["color_format_t"]
    inv_areas: NotRequired["area_t"]
    inv_area_joined: NotRequired[int]
    inv_p: NotRequired[int]
    inv_en_cnt: NotRequired[int]
    draw_ctx: NotRequired["draw_ctx_t"]
    draw_ctx_init: NotRequired[Callable[["disp_t", "draw_ctx_t"], None]]
    draw_ctx_size: NotRequired[int]
    screens: NotRequired["obj_t"]
    act_scr: NotRequired["obj_t"]
    prev_scr: NotRequired["obj_t"]
    scr_to_load: NotRequired["obj_t"]
    bottom_layer: NotRequired["obj_t"]
    top_layer: NotRequired["obj_t"]
    sys_layer: NotRequired["obj_t"]
    screen_cnt: NotRequired[int]
    draw_prev_over_act: NotRequired[bool]
    del_prev: NotRequired[bool]
    driver_data: NotRequired[None]
    user_data: NotRequired[None]
    event_list: NotRequired["event_list_t"]
    sw_rotate: NotRequired[bool]
    rotation: NotRequired[int]
    theme: NotRequired["theme_t"]
    refr_timer: NotRequired["timer_t"]
    last_activity_time: NotRequired[int]
    last_render_start_time: NotRequired[int]
    color_chroma_key: NotRequired["color_t"]


class _disp_t(object):
    """Horizontal resolution."""
    hor_res: "coord_t" = ...
    """Vertical resolution."""
    ver_res: "coord_t" = ...
    """
    Horizontal resolution of the full / physical display. 
    Set to -1 for fullscreen mode.
    """
    physical_hor_res: "coord_t" = ...
    """
    Vertical resolution of the full / physical display. 
    Set to -1 for fullscreen mode.
    """
    physical_ver_res: "coord_t" = ...
    """
    Horizontal offset from the full / physical display. 
    Set to 0 for fullscreen mode.
    """
    offset_x: "coord_t" = ...
    """
    Vertical offset from the full / physical display. 
    Set to 0 for fullscreen mode.
    """
    offset_y: "coord_t" = ...
    dpi: int = ...
    """DPI (dot per inch) of the display. Default value is"""
    draw_buf_1: None = ...
    """Second display buffer."""
    draw_buf_2: None = ...
    """Internal, used by the library"""
    draw_buf_act: None = ...
    """In pixel count"""
    draw_buf_size: int = ...
    flushing: int = ...
    flushing_last: int = ...
    last_area: bool = ...
    last_part: bool = ...
    render_mode: "disp_render_mode_t" = ...
    """1: anti-aliasing is enabled on this display."""
    antialiasing: bool = ...
    """1: The current screen rendering is in progress"""
    rendering_in_progress: bool = ...
    color_format: "color_format_t" = ...
    """Invalidated (marked to redraw) areas"""
    inv_areas: "area_t" = ...
    inv_area_joined: int = ...
    inv_p: int = ...
    inv_en_cnt: int = ...
    draw_ctx: "draw_ctx_t" = ...
    draw_ctx_init: Callable[["disp_t", "draw_ctx_t"], None]
    draw_ctx_size: int = ...
    """Screens of the display Array of screen objects."""
    screens: "obj_t" = ...
    """Currently active screen on this display"""
    act_scr: "obj_t" = ...
    """Previous screen. Used during screen animations"""
    prev_scr: "obj_t" = ...
    """The screen prepared to load in lv_scr_load_anim"""
    scr_to_load: "obj_t" = ...
    bottom_layer: "obj_t" = ...
    top_layer: "obj_t" = ...
    sys_layer: "obj_t" = ...
    screen_cnt: int = ...
    draw_prev_over_act: bool = ...
    """1: Draw previous screen over active screen"""
    del_prev: bool = ...
    """
    1: Automatically delete the previous screen when 
    the screen load animation is ready Custom user data
    """
    driver_data: None = ...
    """Custom user data"""
    user_data: None = ...
    event_list: "event_list_t" = ...
    """1: use software rotation (slower)"""
    sw_rotate: bool = ...
    """Element of @lv_disp_rotation_t The theme assigned to the screen"""
    rotation: int = ...
    theme: "theme_t" = ...
    """A timer which periodically checks the dirty areas and refreshes them"""
    refr_timer: "timer_t" = ...
    """Last time when there was activity on this display"""
    last_activity_time: int = ...
    last_render_start_time: int = ...
    """On CHROMA_KEYED images this color will be transparent."""
    color_chroma_key: "color_t" = ...

    def __init__(self, fields: Optional[_type__disp_t] = {}, /):
        ...


class _type__draw_ctx_t(TypedDict):
    buf: NotRequired[None]
    buf_area: NotRequired["area_t"]
    clip_area: NotRequired["area_t"]
    color_format: NotRequired["color_format_t"]
    init_buf: NotRequired[Callable[["draw_ctx_t"], None]]
    layer_instance_size: NotRequired[int]
    user_data: NotRequired[None]


class _draw_ctx_t(object):
    """Pointer to a buffer to draw into"""
    buf: None = ...
    """The position and size of"""
    buf_area: "area_t" = ...
    """
    The current clip area with absolute coordinates,
    always the same or smaller than
    """
    clip_area: "area_t" = ...
    color_format: "color_format_t" = ...
    init_buf: Callable[["draw_ctx_t"], None]
    """Size of a layer context in bytes."""
    layer_instance_size: int = ...
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type__draw_ctx_t] = {}, /):
        ...


class _type__draw_label_hint_t(TypedDict):
    line_start: NotRequired[int]
    y: NotRequired[int]
    coord_y: NotRequired[int]


class _draw_label_hint_t(object):
    """
    Store some info to speed up drawing of very large texts It takes a lot of
    time to get the first visible character because all the previous characters
    needs to be checked to calculate the positions. This structure stores an
    earlier (e.g. at -1000 px) coordinate and the index of that line.
    Therefore the calculations can start from here.
    """
    """Index of the line at"""
    line_start: int = ...
    """Give the"""
    y: int = ...
    """
    The 'y1' coordinate of the label when the hint was saved. 
    Used to invalidate the hint if the label has moved too much.
    """
    coord_y: int = ...

    def __init__(self, fields: Optional[_type__draw_label_hint_t] = {}, /):
        ...


class _type__draw_layer_ctx_t(TypedDict):
    area_full: NotRequired["area_t"]
    area_act: NotRequired["area_t"]
    max_row_with_alpha: NotRequired["coord_t"]
    max_row_with_no_alpha: NotRequired["coord_t"]
    buf: NotRequired[None]
    clip_area: NotRequired["area_t"]
    buf_area: NotRequired["area_t"]
    color_format: NotRequired["color_format_t"]
    original: NotRequired["draw_layer_ctx_t"]


class _draw_layer_ctx_t(object):
    area_full: "area_t" = ...
    area_act: "area_t" = ...
    max_row_with_alpha: "coord_t" = ...
    max_row_with_no_alpha: "coord_t" = ...
    """Pointer to a buffer to draw into"""
    buf: None = ...
    """
    The current clip area with absolute coordinates, 
    always the same or smaller than
    """
    clip_area: "area_t" = ...
    """The position and size of"""
    buf_area: "area_t" = ...
    color_format: "color_format_t" = ...
    original: "draw_layer_ctx_t" = ...

    def __init__(self, fields: Optional[_type__draw_layer_ctx_t] = {}, /):
        ...


class _type__draw_mask_common_dsc_t(TypedDict):
    cb: NotRequired["draw_mask_xcb_t"]
    type: NotRequired["draw_mask_type_t"]


class _draw_mask_common_dsc_t(object):
    cb: "draw_mask_xcb_t" = ...
    type: "draw_mask_type_t" = ...

    def __init__(self, fields: Optional[_type__draw_mask_common_dsc_t] = {}, /):
        ...


class _type__draw_mask_map_param_t(TypedDict):
    dsc: NotRequired["draw_mask_common_dsc_t"]
    coords: NotRequired["area_t"]
    map: NotRequired["opa_t"]
    cfg: NotRequired["draw_mask_map_param_t"]


class _draw_mask_map_param_t(object):
    dsc: "draw_mask_common_dsc_t" = ...
    coords: "area_t" = ...
    map: "opa_t" = ...
    cfg: "draw_mask_map_param_t" = ...

    def __init__(self, fields: Optional[_type__draw_mask_map_param_t] = {}, /):
        ...


class _type__draw_mask_radius_circle_dsc_t(TypedDict):
    buf: NotRequired[None]
    cir_opa: NotRequired["opa_t"]
    x_start_on_y: NotRequired[int]
    opa_start_on_y: NotRequired[int]
    life: NotRequired[int]
    used_cnt: NotRequired[int]
    radius: NotRequired["coord_t"]


class _draw_mask_radius_circle_dsc_t(object):
    """Pointer to a buffer to draw into"""
    buf: None = ...
    cir_opa: "opa_t" = ...
    x_start_on_y: int = ...
    opa_start_on_y: int = ...
    life: int = ...
    used_cnt: int = ...
    radius: "coord_t" = ...

    def __init__(
            self,
            fields: Optional[_type__draw_mask_radius_circle_dsc_t] = {},
            /
    ):
        ...


class _type__draw_mask_saved_t(TypedDict):
    param: NotRequired[None]
    custom_id: NotRequired[None]


class _draw_mask_saved_t(object):
    param: None = ...
    custom_id: None = ...

    def __init__(self, fields: Optional[_type__draw_mask_saved_t] = {}, /):
        ...


class _type__event_t(TypedDict):
    target: NotRequired[None]
    current_target: NotRequired[None]
    code: NotRequired["event_code_t"]
    user_data: NotRequired[None]
    param: NotRequired[None]
    prev: NotRequired["event_t"]
    deleted: NotRequired[bool]
    stop_processing: NotRequired[bool]
    stop_bubbling: NotRequired[bool]


class _event_t(object):
    target: None = ...
    current_target: None = ...
    code: "event_code_t" = ...
    """Custom user data"""
    user_data: None = ...
    param: None = ...
    prev: "event_t" = ...
    deleted: bool = ...
    stop_processing: bool = ...
    stop_bubbling: bool = ...

    def __init__(self, fields: Optional[_type__event_t] = {}, /):
        ...


class _type__font_t(TypedDict):
    get_glyph_dsc: NotRequired[
        Callable[["font_t", "font_glyph_dsc_t", int, int], bool]]
    line_height: NotRequired["coord_t"]
    base_line: NotRequired["coord_t"]
    subpx: NotRequired[int]
    underline_position: NotRequired[int]
    underline_thickness: NotRequired[int]
    dsc: NotRequired["draw_mask_common_dsc_t"]
    fallback: NotRequired["font_t"]
    user_data: NotRequired[None]


class _font_t(object):
    """
    Describe the properties of a font
    """

    """Get a glyph's descriptor from a font"""
    get_glyph_dsc: Callable[["font_t", "font_glyph_dsc_t", int, int], bool]
    """The real line height where any text fits"""
    line_height: "coord_t" = ...
    """Base line measured from the top of the line_height"""
    base_line: "coord_t" = ...
    """An element of"""
    subpx: int = ...
    """
    Distance between the top of the underline and 
    base line (< 0 means below the base line)
    """
    underline_position: int = ...
    """Thickness of the underline"""
    underline_thickness: int = ...
    dsc: "draw_mask_common_dsc_t" = ...
    """Fallback font for missing glyph. Resolved recursively"""
    fallback: "font_t" = ...
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type__font_t] = {}, /):
        ...


class _type__fs_drv_t(TypedDict):
    letter: NotRequired[int]
    cache_size: NotRequired[int]
    ready_cb: NotRequired[Callable[["fs_drv_t"], bool]]
    user_data: NotRequired[None]


class _fs_drv_t(object):
    letter: int = ...
    cache_size: int = ...
    ready_cb: Callable[["fs_drv_t"], bool]
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type__fs_drv_t] = {}, /):
        ...


class _type__gradient_cache_t(TypedDict):
    key: NotRequired[int]
    life: NotRequired[int]
    filled: NotRequired[bool]
    not_cached: NotRequired[bool]
    map: NotRequired["opa_t"]
    alloc_size: NotRequired["coord_t"]
    size: NotRequired["coord_t"]


class _gradient_cache_t(object):
    """
    To avoid recomputing gradient for each draw operation,
    it's possible to cache the computation in this structure instance.
    Whenever possible, this structure is reused instead of
    recomputing the gradient map
    """

    """
    A discriminating key that's built from the drawing operation. 
    If the key does not match, the cache item is not used
    """
    key: int = ...
    life: int = ...
    """Used to skip dithering in it if already done"""
    filled: bool = ...
    """The cache was too small so this item is not managed by the cache"""
    not_cached: bool = ...
    map: "opa_t" = ...
    """The map allocated size in colors"""
    alloc_size: "coord_t" = ...
    """The computed gradient color map size, in colors"""
    size: "coord_t" = ...

    def __init__(self, fields: Optional[_type__gradient_cache_t] = {}, /):
        ...


class _type__group_t(TypedDict):
    obj_ll: NotRequired["ll_t"]
    obj_focus: NotRequired["obj_t"]
    focus_cb: NotRequired["group_focus_cb_t"]
    edge_cb: NotRequired["group_edge_cb_t"]
    user_data: NotRequired[None]
    frozen: NotRequired[bool]
    editing: NotRequired[bool]
    refocus_policy: NotRequired[bool]
    wrap: NotRequired[bool]


class _group_t(object):
    """
    Groups can be used to logically hold objects so that they can be
    individually focused. They are NOT for laying out objects on
    a screen (try layouts for that).
    """

    """Linked list to store the objects in the group"""
    obj_ll: "ll_t" = ...
    """The object in focus"""
    obj_focus: "obj_t" = ...
    """A function to call when a new object is focused (optional)"""
    focus_cb: "group_focus_cb_t" = ...
    """
    A function to call when an edge is reached, no more focus targets are 
    available in this direction (to allow edge feedback like a 
    sound or a scroll bounce)
    """
    edge_cb: "group_edge_cb_t" = ...
    """Custom user data"""
    user_data: None = ...
    """1: can't focus to new object"""
    frozen: bool = ...
    """1: Edit mode, 0: Navigate mode"""
    editing: bool = ...
    """
    1: Focus prev if focused on deletion. 
    0: Focus next if focused on deletion.
    """
    refocus_policy: bool = ...
    """
    1: Focus next/prev can wrap at end of list. 
    0: Focus next/prev stops at end of list.
    """
    wrap: bool = ...

    def __init__(self, fields: Optional[_type__group_t] = {}, /):
        ...


class _type__img_cache_entry_t(TypedDict):
    dec_dsc: NotRequired["img_decoder_dsc_t"]
    user_data: NotRequired[None]


class _img_cache_entry_t(object):
    """
    When loading images from the network it can take a
    long time to download and decode the image.
    """
    """Image information"""
    dec_dsc: "img_decoder_dsc_t" = ...
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type__img_cache_entry_t] = {}, /):
        ...


class _type__img_decoder_dsc_t(TypedDict):
    decoder: NotRequired["img_decoder_t"]
    src: NotRequired[None]
    color: NotRequired["color_t"]
    frame_id: NotRequired[int]
    src_type: NotRequired["img_src_t"]
    header: NotRequired["img_header_t"]
    img_data: NotRequired[int]
    palette: NotRequired["color32_t"]
    palette_size: NotRequired[int]
    time_to_open: NotRequired[int]
    error_msg: NotRequired[str]
    user_data: NotRequired[None]


class _img_decoder_dsc_t(object):
    """
    Describe an image decoding session. Stores data about the decoding
    """
    """The decoder which was able to open the image source"""
    decoder: "img_decoder_t" = ...
    """The image source. A file path like "S:my_img.png" or pointer to an"""
    src: None = ...
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    """Frame of the image, using with animated images"""
    frame_id: int = ...
    """Type of the source: file or variable. Can be set in"""
    src_type: "img_src_t" = ...
    """Info about the opened image: color format, size, etc. MUST be set in"""
    header: "img_header_t" = ...
    """
    Pointer to a buffer where the image's data (pixels) are 
    stored in a decoded, plain format. MUST be set in
    """
    img_data: int = ...
    palette: "color32_t" = ...
    palette_size: int = ...
    """How much time did it take to open the image. [ms] If not set"""
    time_to_open: int = ...
    """
    A text to display instead of the image when 
    the image can't be opened. Can be set in
    """
    error_msg: str = ...
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type__img_decoder_dsc_t] = {}, /):
        ...


class _type__img_decoder_t(TypedDict):
    info_cb: NotRequired["img_decoder_info_f_t"]
    open_cb: NotRequired["img_decoder_open_f_t"]
    read_line_cb: NotRequired["img_decoder_read_line_f_t"]
    close_cb: NotRequired["img_decoder_close_f_t"]
    user_data: NotRequired[None]


class _img_decoder_t(object):
    info_cb: "img_decoder_info_f_t" = ...
    open_cb: "img_decoder_open_f_t" = ...
    read_line_cb: "img_decoder_read_line_f_t" = ...
    close_cb: "img_decoder_close_f_t" = ...
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type__img_decoder_t] = {}, /):
        ...


class _type__indev_t(TypedDict):
    type: NotRequired["draw_mask_type_t"]
    state: NotRequired["indev_state_t"]
    long_pr_sent: NotRequired[bool]
    reset_query: NotRequired[bool]
    disabled: NotRequired[bool]
    wait_until_release: NotRequired[bool]
    pr_timestamp: NotRequired[int]
    longpr_rep_timestamp: NotRequired[int]
    driver_data: NotRequired[None]
    disp: NotRequired["disp_t"]
    read_timer: NotRequired["timer_t"]
    scroll_limit: NotRequired[int]
    scroll_throw: NotRequired[int]
    gesture_min_velocity: NotRequired[int]
    gesture_limit: NotRequired[int]
    long_press_time: NotRequired[int]
    long_press_repeat_time: NotRequired[int]
    act_point: NotRequired["point_t"]
    last_point: NotRequired["point_t"]
    last_raw_point: NotRequired["point_t"]
    vect: NotRequired["point_t"]
    scroll_sum: NotRequired["point_t"]
    scroll_throw_vect: NotRequired["point_t"]
    scroll_throw_vect_ori: NotRequired["point_t"]
    act_obj: NotRequired["obj_t"]
    last_obj: NotRequired["obj_t"]
    scroll_obj: NotRequired["obj_t"]
    last_pressed: NotRequired["obj_t"]
    scroll_area: NotRequired["area_t"]
    gesture_sum: NotRequired["point_t"]
    scroll_dir: NotRequired["dir_t"]
    gesture_dir: NotRequired["dir_t"]
    gesture_sent: NotRequired[bool]
    pointer: NotRequired["indev_t"]
    last_state: NotRequired["indev_state_t"]
    last_key: NotRequired[int]
    keypad: NotRequired["indev_t"]
    cursor: NotRequired["obj_t"]
    group: NotRequired["group_t"]
    btn_points: NotRequired["point_t"]


class _indev_t(object):
    type: "draw_mask_type_t" = ...
    """Current state of the input device."""
    state: "indev_state_t" = ...
    long_pr_sent: bool = ...
    reset_query: bool = ...
    disabled: bool = ...
    wait_until_release: bool = ...
    """Pressed time stamp"""
    pr_timestamp: int = ...
    """Long press repeat time stamp"""
    longpr_rep_timestamp: int = ...
    """
    1: Automatically delete the previous screen when the screen 
    load animation is ready Custom user data
    """
    driver_data: None = ...
    """Timer to periodically read the input device"""
    disp: "disp_t" = ...
    """Number of pixels to slide before actually drag the object"""
    read_timer: "timer_t" = ...
    """Drag throw slow-down in [%]. Greater value means faster slow-down"""
    scroll_limit: int = ...
    """
    At least this difference should be between two points to evaluate as gesture
    """
    scroll_throw: int = ...
    """At least this difference should be to send a gesture"""
    gesture_min_velocity: int = ...
    """Long press time in milliseconds"""
    gesture_limit: int = ...
    """Repeated trigger period in long press [ms]"""
    long_press_time: int = ...
    long_press_repeat_time: int = ...
    """Current point of input device."""
    act_point: "point_t" = ...
    """Last point of input device."""
    last_point: "point_t" = ...
    """Last point read from read_cb."""
    last_raw_point: "point_t" = ...
    """Difference between"""
    vect: "point_t" = ...
    scroll_sum: "point_t" = ...
    scroll_throw_vect: "point_t" = ...
    scroll_throw_vect_ori: "point_t" = ...
    act_obj: "obj_t" = ...
    last_obj: "obj_t" = ...
    scroll_obj: "obj_t" = ...
    last_pressed: "obj_t" = ...
    scroll_area: "area_t" = ...
    gesture_sum: "point_t" = ...
    scroll_dir: "dir_t" = ...
    gesture_dir: "dir_t" = ...
    gesture_sent: bool = ...
    pointer: "indev_t" = ...
    last_state: "indev_state_t" = ...
    last_key: int = ...
    keypad: "indev_t" = ...
    """Cursor for LV_INPUT_TYPE_POINTER"""
    cursor: "obj_t" = ...
    """Keypad destination group"""
    group: "group_t" = ...
    """
    Array points assigned to the button ()screen will be 
    pressed here by the buttons
    """
    btn_points: "point_t" = ...

    def __init__(self, fields: Optional[_type__indev_t] = {}, /):
        ...


class _type__obj_class_t(TypedDict):
    base_class: NotRequired["obj_class_t"]
    user_data: NotRequired[None]
    width_def: NotRequired["coord_t"]
    height_def: NotRequired["coord_t"]
    editable: NotRequired[int]
    group_def: NotRequired[int]
    instance_size: NotRequired[int]
    theme_inheritable: NotRequired[bool]


class _obj_class_t(object):
    """
    Describe the common methods of every object. Similar to a C++ class.
    """
    base_class: "obj_class_t" = ...
    """Custom user data"""
    user_data: None = ...
    width_def: "coord_t" = ...
    height_def: "coord_t" = ...
    """Value from"""
    editable: int = ...
    """Value from"""
    group_def: int = ...
    instance_size: int = ...
    """Value from"""
    theme_inheritable: bool = ...

    def __init__(self, fields: Optional[_type__obj_class_t] = {}, /):
        ...


class _type__obj_spec_attr_t(TypedDict):
    children: NotRequired["obj_t"]
    child_cnt: NotRequired[int]
    group_p: NotRequired["group_t"]
    event_list: NotRequired["event_list_t"]
    scroll: NotRequired["point_t"]
    ext_click_pad: NotRequired["coord_t"]
    ext_draw_size: NotRequired["coord_t"]
    scrollbar_mode: NotRequired["scrollbar_mode_t"]
    scroll_snap_x: NotRequired["scroll_snap_t"]
    scroll_snap_y: NotRequired["scroll_snap_t"]
    scroll_dir: NotRequired["dir_t"]
    layer_type: NotRequired[int]


class _obj_spec_attr_t(object):
    """
    Special, rarely used attributes.
    They are allocated automatically if any elements is set.
    """

    """Store the pointer of the children in an array."""
    children: "obj_t" = ...
    """Number of children"""
    child_cnt: int = ...
    group_p: "group_t" = ...
    event_list: "event_list_t" = ...
    """The current X/Y scroll offset"""
    scroll: "point_t" = ...
    """Extra click padding in all direction"""
    ext_click_pad: "coord_t" = ...
    """EXTend the size in every direction for drawing."""
    ext_draw_size: "coord_t" = ...
    """How to display scrollbars"""
    scrollbar_mode: "scrollbar_mode_t" = ...
    """Where to align the snappable children horizontally"""
    scroll_snap_x: "scroll_snap_t" = ...
    """Where to align the snappable children vertically"""
    scroll_snap_y: "scroll_snap_t" = ...
    scroll_dir: "dir_t" = ...
    """Cache the layer type here. Element of @lv_intermediate_layer_type_t"""
    layer_type: int = ...

    def __init__(self, fields: Optional[_type__obj_spec_attr_t] = {}, /):
        ...


class _type__obj_style_t(TypedDict):
    style: NotRequired["style_t"]
    selector: NotRequired[int]
    is_local: NotRequired[bool]
    is_trans: NotRequired[bool]


class _obj_style_t(object):
    style: "style_t" = ...
    selector: int = ...
    is_local: bool = ...
    is_trans: bool = ...

    def __init__(self, fields: Optional[_type__obj_style_t] = {}, /):
        ...


class _type__obj_style_transition_dsc_t(TypedDict):
    time: NotRequired[int]
    delay: NotRequired[int]
    selector: NotRequired[int]
    prop: NotRequired["style_prop_t"]
    path_cb: NotRequired["anim_path_cb_t"]
    user_data: NotRequired[None]


class _obj_style_transition_dsc_t(object):
    """Animation time in ms"""
    time: int = ...
    delay: int = ...
    selector: int = ...
    prop: "style_prop_t" = ...
    """Describe the path (curve) of animations"""
    path_cb: "anim_path_cb_t" = ...
    """Custom user data"""
    user_data: None = ...

    def __init__(
            self,
            fields: Optional[_type__obj_style_transition_dsc_t] = {},
            /
    ):
        ...


class _type__obj_t(TypedDict):
    class_p: NotRequired["obj_class_t"]
    parent: NotRequired["obj_t"]
    spec_attr: NotRequired["obj_spec_attr_t"]
    styles: NotRequired["obj_style_t"]
    user_data: NotRequired[None]
    coords: NotRequired["area_t"]
    flags: NotRequired["draw_layer_flags_t"]
    state: NotRequired["indev_state_t"]
    layout_inv: NotRequired[bool]
    scr_layout_inv: NotRequired[bool]
    skip_trans: NotRequired[bool]
    style_cnt: NotRequired[int]
    h_layout: NotRequired[bool]
    w_layout: NotRequired[bool]


class _obj_t(object):
    class_p: "obj_class_t" = ...
    parent: "obj_t" = ...
    spec_attr: "obj_spec_attr_t" = ...
    styles: "obj_style_t" = ...
    """Custom user data"""
    user_data: None = ...
    coords: "area_t" = ...
    flags: "draw_layer_flags_t" = ...
    """Current state of the input device."""
    state: "indev_state_t" = ...
    layout_inv: bool = ...
    scr_layout_inv: bool = ...
    skip_trans: bool = ...
    style_cnt: int = ...
    h_layout: bool = ...
    w_layout: bool = ...

    def __init__(self, fields: Optional[_type__obj_t] = {}, /):
        ...


class _type__theme_t(TypedDict):
    apply_cb: NotRequired["theme_apply_cb_t"]
    parent: NotRequired["obj_t"]
    user_data: NotRequired[None]
    disp: NotRequired["disp_t"]
    color_primary: NotRequired["color_t"]
    color_secondary: NotRequired["color_t"]
    font_small: NotRequired["font_t"]
    font_normal: NotRequired["font_t"]
    font_large: NotRequired["font_t"]
    flags: NotRequired["draw_layer_flags_t"]


class _theme_t(object):
    apply_cb: "theme_apply_cb_t" = ...
    parent: "obj_t" = ...
    """Custom user data"""
    user_data: None = ...
    """Timer to periodically read the input device"""
    disp: "disp_t" = ...
    color_primary: "color_t" = ...
    color_secondary: "color_t" = ...
    font_small: "font_t" = ...
    font_normal: "font_t" = ...
    font_large: "font_t" = ...
    flags: "draw_layer_flags_t" = ...

    def __init__(self, fields: Optional[_type__theme_t] = {}, /):
        ...


class _type__timer_t(TypedDict):
    period: NotRequired[int]
    last_run: NotRequired[int]
    timer_cb: NotRequired["timer_cb_t"]
    user_data: NotRequired[None]
    repeat_count: NotRequired[int]
    paused: NotRequired[bool]


class _timer_t(object):
    """
    Descriptor of a lv_timer
    """

    """How often the timer should run"""
    period: int = ...
    """Last time the timer ran"""
    last_run: int = ...
    """Timer function"""
    timer_cb: "timer_cb_t" = ...
    """Custom user data"""
    user_data: None = ...
    """1: One time; -1 : infinity; n>0: residual times"""
    repeat_count: int = ...
    paused: bool = ...

    def __init__(self, fields: Optional[_type__timer_t] = {}, /):
        ...


class _type__stbtt_kerningentry(TypedDict):
    glyph1: NotRequired[int]
    glyph2: NotRequired[int]
    advance: NotRequired[int]


class _stbtt_kerningentry(object):
    glyph1: int = ...
    glyph2: int = ...
    advance: int = ...

    def __init__(self, fields: Optional[_type__stbtt_kerningentry] = {}, /):
        ...


class _type_animimg_t(TypedDict):
    img: NotRequired["img_t"]
    anim: NotRequired["anim_t"]
    dsc: NotRequired["draw_mask_common_dsc_t"]
    pic_count: NotRequired[int]


class animimg_t(object):
    img: "img_t" = ...
    anim: "anim_t" = ...
    dsc: "draw_mask_common_dsc_t" = ...
    pic_count: int = ...

    def __init__(self, fields: Optional[_type_animimg_t] = {}, /):
        ...

    def set_src(self, dsc: Callable[["[]"], None], num: int, /) -> None:
        """
        Set the image animation images source.

        :param dsc:
        :type dsc: Callable[["[]"], None]

        :param num:
        :type num: int

        :returns:
        :retval: None
        """
        ...

    def start(self) -> None:
        """
        Startup the image animation.

        :returns:
        :retval: None
        """
        ...

    def set_duration(self, duration: int, /) -> None:
        """
        Set the image animation duration time. unit:ms

        :param duration:
        :type duration: int

        :returns:
        :retval: None
        """
        ...

    def set_repeat_count(self, count: int, /) -> None:
        """
        Set the image animation repeatly play times.

        :param count:
        :type count: int

        :returns:
        :retval: None
        """
        ...

    def get_src(self) -> None:
        """
        Get the image animation images source.

        :returns: a pointer that will point to a series images
        :retval: None
        """
        ...

    def get_src_count(self) -> int:
        """
        Get the image animation images source.

        :returns: the number of source images
        :retval: int
        """
        ...

    def get_duration(self) -> int:
        """
        Get the image animation duration time. unit:ms

        :returns: the animation duration time
        :retval: int
        """
        ...

    def get_repeat_count(self) -> int:
        """
        Get the image animation repeat play times.

        :returns: the repeat count
        :retval: int
        """
        ...


class _type_arc_t(TypedDict):
    obj: NotRequired["obj_t"]
    rotation: NotRequired[int]
    indic_angle_start: NotRequired[int]
    indic_angle_end: NotRequired[int]
    bg_angle_start: NotRequired[int]
    bg_angle_end: NotRequired[int]
    value: NotRequired[int]
    min_value: NotRequired[int]
    max_value: NotRequired[int]
    dragging: NotRequired[bool]
    type: NotRequired["draw_mask_type_t"]
    min_close: NotRequired[bool]
    chg_rate: NotRequired[int]
    last_tick: NotRequired[int]
    last_angle: NotRequired[int]
    knob_offset: NotRequired[int]


class arc_t(object):
    obj: "obj_t" = ...
    """Element of @lv_disp_rotation_t The theme assigned to the screen"""
    rotation: int = ...
    indic_angle_start: int = ...
    indic_angle_end: int = ...
    bg_angle_start: int = ...
    bg_angle_end: int = ...
    value: int = ...
    min_value: int = ...
    max_value: int = ...
    dragging: bool = ...
    type: "draw_mask_type_t" = ...
    min_close: bool = ...
    chg_rate: int = ...
    last_tick: int = ...
    last_angle: int = ...
    knob_offset: int = ...

    class MODE:
        NORMAL: int = 0
        SYMMETRICAL: int = 1
        REVERSE: int = 2

    class DRAW_PART:
        BACKGROUND: int = 0
        FOREGROUND: int = 1
        KNOB: int = 2

    def __init__(self, fields: Optional[_type_arc_t] = {}, /):
        ...

    def set_start_angle(self, start: int, /) -> None:
        """
        Set the start angle of an arc. 0 deg: right, 90 bottom, etc.

        :param start:
        :type start: int

        :returns:
        :retval: None
        """
        ...

    def set_end_angle(self, end: int, /) -> None:
        """
        Set the end angle of an arc. 0 deg: right, 90 bottom, etc.

        :param end:
        :type end: int

        :returns:
        :retval: None
        """
        ...

    def set_angles(self, start: int, end: int, /) -> None:
        """
        Set the start and end angles

        :param start:
        :type start: int

        :param end:
        :type end: int

        :returns:
        :retval: None
        """
        ...

    def set_bg_start_angle(self, start: int, /) -> None:
        """
        Set the start angle of an arc background. 0 deg: right, 90 bottom, etc.

        :param start:
        :type start: int

        :returns:
        :retval: None
        """
        ...

    def set_bg_end_angle(self, end: int, /) -> None:
        """
        Set the start angle of an arc background. 0 deg: right, 90 bottom etc.

        :param end:
        :type end: int

        :returns:
        :retval: None
        """
        ...

    def set_bg_angles(self, start: int, end: int, /) -> None:
        """
        Set the start and end angles of the arc background

        :param start:
        :type start: int

        :param end:
        :type end: int

        :returns:
        :retval: None
        """
        ...

    def set_rotation(self, rotation: int, /) -> None:
        """
        Set the rotation for the whole arc

        :param rotation:
        :type rotation: int

        :returns:
        :retval: None
        """
        ...

    def set_mode(self, type: "arc_mode_t", /) -> None:
        """
        Set the type of arc.

        :param type:
        :type type: "arc_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_value(self, value: int, /) -> None:
        """
        Set a new value on the arc

        :param value:
        :type value: int

        :returns:
        :retval: None
        """
        ...

    def set_range(self, min: int, max: int, /) -> None:
        """
        Set minimum and the maximum values of an arc

        :param min:
        :type min: int

        :param max:
        :type max: int

        :returns:
        :retval: None
        """
        ...

    def set_change_rate(self, rate: int, /) -> None:
        """
        Set a change rate to limit the speed how fast the arc should reach the pressed point.

        :param rate:
        :type rate: int

        :returns:
        :retval: None
        """
        ...

    def set_knob_offset(self, offset: int, /) -> None:
        """
        Set an offset for the knob from the main arc object

        :param offset:
        :type offset: int

        :returns:
        :retval: None
        """
        ...

    def get_angle_start(self) -> int:
        """
        Get the start angle of an arc.

        :returns: the start angle [0..360]
        :retval: int
        """
        ...

    def get_angle_end(self) -> int:
        """
        Get the end angle of an arc.

        :returns: the end angle [0..360]
        :retval: int
        """
        ...

    def get_bg_angle_start(self) -> int:
        """
        Get the start angle of an arc background.

        :returns: the start angle [0..360]
        :retval: int
        """
        ...

    def get_bg_angle_end(self) -> int:
        """
        Get the end angle of an arc background.

        :returns: the end angle [0..360]
        :retval: int
        """
        ...

    def get_value(self) -> int:
        """
        Get the value of an arc

        :returns: the value of the arc
        :retval: int
        """
        ...

    def get_min_value(self) -> int:
        """
        Get the minimum value of an arc

        :returns: the minimum value of the arc
        :retval: int
        """
        ...

    def get_max_value(self) -> int:
        """
        Get the maximum value of an arc

        :returns: the maximum value of the arc
        :retval: int
        """
        ...

    def get_mode(self) -> "arc_mode_t":
        """
        Get whether the arc is type or not.

        :returns: arc's mode
        :retval: "arc_mode_t"
        """
        ...

    def get_rotation(self) -> int:
        """
        Get the rotation for the whole arc

        :returns: arc's current rotation
        :retval: int
        """
        ...

    def get_knob_offset(self) -> int:
        """
        Get the current knob offset

        :returns: arc's current knob offset
        :retval: int
        """
        ...

    def align_obj_to_angle(
            self,
            obj_to_align: "obj_t",
            r_offset: "coord_t",
            /
    ) -> None:
        """
        Align an object to the current position of the arc (knob)

        :param obj_to_align:
        :type obj_to_align: "obj_t"

        :param r_offset:
        :type r_offset: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def rotate_obj_to_angle(
            self,
            obj_to_rotate: "obj_t",
            r_offset: "coord_t",
            /
    ) -> None:
        """
        Rotate an object to the current position of the arc (knob)

        :param obj_to_rotate:
        :type obj_to_rotate: "obj_t"

        :param r_offset:
        :type r_offset: "coord_t"

        :returns:
        :retval: None
        """
        ...


class _type_area_t(TypedDict):
    x1: NotRequired["coord_t"]
    y1: NotRequired["coord_t"]
    x2: NotRequired["coord_t"]
    y2: NotRequired["coord_t"]


class area_t(object):
    """
    Represents an area of the screen.
    """

    x1: "coord_t" = ...
    y1: "coord_t" = ...
    x2: "coord_t" = ...
    y2: "coord_t" = ...

    def __init__(self, fields: Optional[_type_area_t] = {}, /):
        ...

    def set(
            self,
            x1: "coord_t",
            y1: "coord_t",
            x2: "coord_t",
            y2: "coord_t",
            /
    ) -> None:
        """
        Initialize an area

        :param x1:
        :type x1: "coord_t"

        :param y1:
        :type y1: "coord_t"

        :param x2:
        :type x2: "coord_t"

        :param y2:
        :type y2: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def copy(self, src: "area_t", /) -> None:
        """
        Copy an area

        :param src:
        :type src: "area_t"

        :returns:
        :retval: None
        """
        ...

    def get_width(self) -> "coord_t":
        """
        Get the width of an area

        :returns: the width of the area (if x1 == x2 -> width = 1)
        :retval: "coord_t"
        """
        ...

    def get_height(self) -> "coord_t":
        """
        Get the height of an area

        :returns: the height of the area (if y1 == y2 -> height = 1)
        :retval: "coord_t"
        """
        ...

    def set_width(self, w: "coord_t", /) -> None:
        """
        Set the width of an area

        :param w:
        :type w: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_height(self, h: "coord_t", /) -> None:
        """
        Set the height of an area

        :param h:
        :type h: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def get_size(self) -> int:
        """
        Return with area of an area (x * y)

        :returns: size of area
        :retval: int
        """
        ...

    def increase(self, w_extra: "coord_t", h_extra: "coord_t", /) -> None:
        """
        :param w_extra:
        :type w_extra: "coord_t"

        :param h_extra:
        :type h_extra: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def move(self, x_ofs: "coord_t", y_ofs: "coord_t", /) -> None:
        """
        :param x_ofs:
        :type x_ofs: "coord_t"

        :param y_ofs:
        :type y_ofs: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def align(
            self,
            to_align: "area_t",
            align: "align_t",
            ofs_x: "coord_t",
            ofs_y: "coord_t",
            /
    ) -> None:
        """
        Align an area to an other

        :param to_align:
        :type to_align: "area_t"

        :param align:
        :type align: "align_t"

        :param ofs_x:
        :type ofs_x: "coord_t"

        :param ofs_y:
        :type ofs_y: "coord_t"

        :returns:
        :retval: None
        """
        ...


class _type_bar_t(TypedDict):
    obj: NotRequired["obj_t"]
    cur_value: NotRequired[int]
    min_value: NotRequired[int]
    max_value: NotRequired[int]
    start_value: NotRequired[int]
    indic_area: NotRequired["area_t"]
    cur_value_anim: NotRequired["bar_anim_t"]
    start_value_anim: NotRequired["bar_anim_t"]
    mode: NotRequired["bar_mode_t"]


class bar_t(object):
    obj: "obj_t" = ...
    """Current value of the bar"""
    cur_value: int = ...
    min_value: int = ...
    max_value: int = ...
    """Start value"""
    start_value: int = ...
    """Save the indicator area. Might be used by derived types"""
    indic_area: "area_t" = ...
    cur_value_anim: "bar_anim_t" = ...
    start_value_anim: "bar_anim_t" = ...
    """Type of bar"""
    mode: "bar_mode_t" = ...

    class MODE:
        NORMAL: int = 0
        SYMMETRICAL: int = 1
        RANGE: int = 2

    class DRAW_PART_INDICATOR:
        BAR_DRAW_PART_INDICATOR: int = 0

    def __init__(self, fields: Optional[_type_bar_t] = {}, /):
        ...

    def set_value(self, value: int, anim: "anim_enable_t", /) -> None:
        """
        Set a new value on the bar

        :param value:
        :type value: int

        :param anim:
        :type anim: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def set_start_value(
            self,
            start_value: int,
            anim: "anim_enable_t",
            /
    ) -> None:
        """
        Set a new start value on the bar

        :param start_value:
        :type start_value: int

        :param anim:
        :type anim: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def set_range(self, min: int, max: int, /) -> None:
        """
        Set minimum and the maximum values of a bar

        :param min:
        :type min: int

        :param max:
        :type max: int

        :returns:
        :retval: None
        """
        ...

    def set_mode(self, mode: "bar_mode_t", /) -> None:
        """
        Set the type of bar.

        :param mode:
        :type mode: "bar_mode_t"

        :returns:
        :retval: None
        """
        ...

    def get_value(self) -> int:
        """
        Get the value of a bar

        :returns: the value of the bar
        :retval: int
        """
        ...

    def get_start_value(self) -> int:
        """
        Get the start value of a bar

        :returns: the start value of the bar
        :retval: int
        """
        ...

    def get_min_value(self) -> int:
        """
        Get the minimum value of a bar

        :returns: the minimum value of the bar
        :retval: int
        """
        ...

    def get_max_value(self) -> int:
        """
        Get the maximum value of a bar

        :returns: the maximum value of the bar
        :retval: int
        """
        ...

    def get_mode(self) -> "bar_mode_t":
        """
        Get the type of bar.

        :returns: bar type from lv_bar_mode_t
        :retval: "bar_mode_t"
        """
        ...


class _type_btn_t(TypedDict):
    obj: NotRequired["obj_t"]


class btn_t(object):
    obj: "obj_t" = ...

    def __init__(self, fields: Optional[_type_btn_t] = {}, /):
        ...


class _type_btnmatrix_t(TypedDict):
    obj: NotRequired["obj_t"]
    map_p: NotRequired[str]
    button_areas: NotRequired["area_t"]
    ctrl_bits: NotRequired["btnmatrix_ctrl_t"]
    btn_cnt: NotRequired[int]
    row_cnt: NotRequired[int]
    btn_id_sel: NotRequired[int]
    one_check: NotRequired[bool]


class btnmatrix_t(object):
    obj: "obj_t" = ...
    map_p: str = ...
    button_areas: "area_t" = ...
    ctrl_bits: "btnmatrix_ctrl_t" = ...
    btn_cnt: int = ...
    row_cnt: int = ...
    btn_id_sel: int = ...
    one_check: bool = ...

    class CTRL:
        """
        Type to store button control bits (disabled, hidden etc.)
        The first 3 bits are used to store the width
        """
        HIDDEN: int = 0x0008
        NO_REPEAT: int = 0x0010
        DISABLED: int = 0x0020
        CHECKABLE: int = 0x0040
        CHECKED: int = 0x0080
        CLICK_TRIG: int = 0x0100
        POPOVER: int = 0x0200
        RECOLOR: int = 0x1000
        CUSTOM_1: int = 0x4000
        CUSTOM_2: int = 0x8000

    class DRAW_PART_BTN:
        BTNMATRIX_DRAW_PART_BTN: int = 0

    def __init__(self, fields: Optional[_type_btnmatrix_t] = {}, /):
        ...

    def set_map(self, map: Callable[["[]"], str], /) -> None:
        """
        Set a new map. Buttons will be created/deleted according to the map.
        The button matrix keeps a reference to the map and so the string
        array must not be deallocated during the life of the matrix.

        :param map:
        :type map: Callable[["[]"], str]

        :returns:
        :retval: None
        """
        ...

    def set_ctrl_map(
            self,
            ctrl_map: Callable[["[]"], "btnmatrix_ctrl_t"],
            /
    ) -> None:
        """
        Set the button control map (hidden, disabled etc.) for a button matrix.
        The control map array will be copied and so may be deallocated
        after this function returns.

        :param ctrl_map:
        :type ctrl_map: Callable[["[]"], "btnmatrix_ctrl_t"]

        :returns:
        :retval: None
        """
        ...

    def set_selected_btn(self, btn_id: int, /) -> None:
        """
        Set the selected buttons

        :param btn_id:
        :type btn_id: int

        :returns:
        :retval: None
        """
        ...

    def set_btn_ctrl(self, btn_id: int, ctrl: "btnmatrix_ctrl_t", /) -> None:
        """
        Set the attributes of a button of the button matrix

        :param btn_id:
        :type btn_id: int

        :param ctrl:
        :type ctrl: "btnmatrix_ctrl_t"

        :returns:
        :retval: None
        """
        ...

    def clear_btn_ctrl(self, btn_id: int, ctrl: "btnmatrix_ctrl_t", /) -> None:
        """
        Clear the attributes of a button of the button matrix

        :param btn_id:
        :type btn_id: int

        :param ctrl:
        :type ctrl: "btnmatrix_ctrl_t"

        :returns:
        :retval: None
        """
        ...

    def set_btn_ctrl_all(self, ctrl: "btnmatrix_ctrl_t", /) -> None:
        """
        Set attributes of all buttons of a button matrix

        :param ctrl:
        :type ctrl: "btnmatrix_ctrl_t"

        :returns:
        :retval: None
        """
        ...

    def clear_btn_ctrl_all(self, ctrl: "btnmatrix_ctrl_t", /) -> None:
        """
        Clear the attributes of all buttons of a button matrix

        :param ctrl:
        :type ctrl: "btnmatrix_ctrl_t"

        :returns:
        :retval: None
        """
        ...

    def set_btn_width(self, btn_id: int, width: int, /) -> None:
        """
        Set a single button's relative width. This method will
        cause the matrix be regenerated and is a relatively expensive
        operation. It is recommended that initial width be specified using

        :param btn_id:
        :type btn_id: int

        :param width:
        :type width: int

        :returns:
        :retval: None
        """
        ...

    def set_one_checked(self, en: bool, /) -> None:
        """
        Make the button matrix like a selector widget
        (only one button may be checked at a time).

        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def get_map(self) -> str:
        """
        Get the current map of a button matrix

        :returns: the current map
        :retval: str
        """
        ...

    def get_selected_btn(self) -> int:
        """
        Get the index of the lastly "activated" button by the user
        (pressed, released, focused etc) Useful in the

        :returns:
        :retval: int
        """
        ...

    def get_btn_text(self, btn_id: int, /) -> str:
        """
        Get the button's text

        :param btn_id:
        :type btn_id: int

        :returns: text of btn_index` button
        :retval: str
        """
        ...

    def has_btn_ctrl(self, btn_id: int, ctrl: "btnmatrix_ctrl_t", /) -> bool:
        """
        Get the whether a control value is enabled or
        disabled for button of a button matrix

        :param btn_id:
        :type btn_id: int

        :param ctrl:
        :type ctrl: "btnmatrix_ctrl_t"

        :returns: true: the control attribute is enabled false: disabled
        :retval: bool
        """
        ...

    def get_one_checked(self) -> bool:
        """
        Tell whether "one check" mode is enabled or not.

        :returns: true: "one check" mode is enabled; false: disabled
        :retval: bool
        """
        ...

    def get_popovers(self) -> bool:
        """
        Tell whether "popovers" mode is enabled or not.

        :returns: true: "popovers" mode is enabled; false: disabled
        :retval: bool
        """
        ...


class _type_calendar_date_t(TypedDict):
    year: NotRequired[int]
    month: NotRequired[int]
    day: NotRequired[int]


class calendar_date_t(object):
    """
    Represents a date on the calendar object (platform-agnostic).
    """

    year: int = ...
    month: int = ...
    """1..12"""
    day: int = ...

    def __init__(self, fields: Optional[_type_calendar_date_t] = {}, /):
        ...

    def set_today_date(self, year: int, month: int, day: int, /) -> None:
        """
        Set the today's date

        :param year:
        :type year: int

        :param month:
        :type month: int

        :param day:
        :type day: int

        :returns:
        :retval: None
        """
        ...

    def set_showed_date(self, year: int, month: int, /) -> None:
        """
        Set the currently showed

        :param year:
        :type year: int

        :param month:
        :type month: int

        :returns:
        :retval: None
        """
        ...

    def set_highlighted_dates(
            self,
            highlighted: Callable[["[]"], "calendar_date_t"],
            date_num: int,
            /
    ) -> None:
        """
        Set the highlighted dates

        :param highlighted:
        :type highlighted: Callable[["[]"], "calendar_date_t"]

        :param date_num:
        :type date_num: int

        :returns:
        :retval: None
        """
        ...

    def set_day_names(self, day_names: str, /) -> None:
        """
        Set the name of the days

        :param day_names:
        :type day_names: str

        :returns:
        :retval: None
        """
        ...

    def get_btnmatrix(self) -> "obj_t":
        """
        Get the button matrix object of the calendar.
        It shows the dates and day names.

        :returns: pointer to a the button matrix
        :retval: "obj_t"
        """
        ...

    def get_today_date(self) -> "calendar_date_t":
        """
        Get the today's date

        :returns: return pointer to an
        :retval: "calendar_date_t"
        """
        ...

    def get_showed_date(self) -> "calendar_date_t":
        """
        Get the currently showed

        :returns: pointer to an
        :retval: "calendar_date_t"
        """
        ...

    def get_highlighted_dates(self) -> "calendar_date_t":
        """
        Get the highlighted dates

        :returns: pointer to an
        :retval: "calendar_date_t"
        """
        ...

    def get_highlighted_dates_num(self) -> int:
        """
        Get the number of the highlighted dates

        :returns: number of highlighted days
        :retval: int
        """
        ...

    def get_pressed_date(self, date: "calendar_date_t", /) -> "res_t":
        """
        Get the currently pressed day

        :param date:
        :type date: "calendar_date_t"

        :returns: LV_RES_OK: there is a valid pressed date; LV_RES_INV: there is no pressed data
        :retval: "res_t"
        """
        ...


class _type_calendar_t(TypedDict):
    obj: NotRequired["obj_t"]
    btnm: NotRequired["obj_t"]
    today: NotRequired["calendar_date_t"]
    showed_date: NotRequired["calendar_date_t"]
    highlighted_dates: NotRequired["calendar_date_t"]
    highlighted_dates_num: NotRequired[int]
    map: NotRequired["opa_t"]
    nums: NotRequired[int]


class calendar_t(object):
    obj: "obj_t" = ...
    btnm: "obj_t" = ...
    today: "calendar_date_t" = ...
    showed_date: "calendar_date_t" = ...
    highlighted_dates: "calendar_date_t" = ...
    highlighted_dates_num: int = ...
    map: "opa_t" = ...
    nums: int = ...

    def __init__(self, fields: Optional[_type_calendar_t] = {}, /):
        ...


class _type_canvas_t(TypedDict):
    img: NotRequired["img_t"]
    dsc: NotRequired["draw_mask_common_dsc_t"]


# noinspection PyShadowingNames
class canvas_t(object):
    img: "img_t" = ...
    dsc: "draw_mask_common_dsc_t" = ...

    def __init__(self, fields: Optional[_type_canvas_t] = {}, /):
        ...

    def set_buffer(
            self,
            buf, w: "coord_t",
            h: "coord_t",
            cf: "color_format_t",
            /
    ) -> None:
        """
        Set a buffer for the canvas.

        :param buf:
        :type buf: None

        :param w:
        :type w: "coord_t"

        :param h:
        :type h: "coord_t"

        :param cf:
        :type cf: "color_format_t"

        :returns:
        :retval: None
        """
        ...

    def set_px(
            self,
            x: "coord_t",
            y: "coord_t",
            color: "color_t",
            opa: "opa_t",
            /
    ) -> None:
        """
        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param color:
        :type color: "color_t"

        :param opa:
        :type opa: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_palette(self, id: int, c: "color32_t", /) -> None:
        """
        Set the palette color of a canvas with index format. Valid only for

        :param id:
        :type id: int

        :param c:
        :type c: "color32_t"

        :returns:
        :retval: None
        """
        ...

    def get_px(
            self,
            x: "coord_t",
            y: "coord_t",
            color: "color_t",
            opa: "opa_t",
            /
    ) -> None:
        """
        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param color:
        :type color: "color_t"

        :param opa:
        :type opa: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def get_img(self) -> "img_dsc_t":
        """
        Get the image of the canvas as a pointer to an

        :returns:
        :retval: "img_dsc_t"
        """
        ...

    def copy_buf(
            self,
            to_copy,
            x: "coord_t",
            y: "coord_t",
            w: "coord_t",
            h: "coord_t",
            /
    ) -> None:
        """
        Copy a buffer to the canvas

        :param to_copy:
        :type to_copy: None

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param w:
        :type w: "coord_t"

        :param h:
        :type h: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def transform(
            self, img: "img_dsc_t", angle: int, zoom: int, offset_x: "coord_t",
            offset_y: "coord_t", pivot_x: int, pivot_y: int, antialias: bool, /
    ) -> None:
        """
        Transform and image and store the result on a canvas.

        :param img:
        :type img: "img_dsc_t"

        :param angle:
        :type angle: int

        :param zoom:
        :type zoom: int

        :param offset_x:
        :type offset_x: "coord_t"

        :param offset_y:
        :type offset_y: "coord_t"

        :param pivot_x:
        :type pivot_x: int

        :param pivot_y:
        :type pivot_y: int

        :param antialias:
        :type antialias: bool

        :returns:
        :retval: None
        """
        ...

    def blur_hor(self, area: "area_t", r: int, /) -> None:
        """
        Apply horizontal blur on the canvas

        :param area:
        :type area: "area_t"

        :param r:
        :type r: int

        :returns:
        :retval: None
        """
        ...

    def blur_ver(self, area: "area_t", r: int, /) -> None:
        """
        Apply vertical blur on the canvas

        :param area:
        :type area: "area_t"

        :param r:
        :type r: int

        :returns:
        :retval: None
        """
        ...

    def fill_bg(self, color: "color_t", opa: "opa_t", /) -> None:
        """
        Fill the canvas with color

        :param color:
        :type color: "color_t"

        :param opa:
        :type opa: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def draw_rect(
            self, x: "coord_t", y: "coord_t", w: "coord_t",
            h: "coord_t", draw_dsc: "draw_rect_dsc_t", /
    ) -> None:
        """
        Draw a rectangle on the canvas

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param w:
        :type w: "coord_t"

        :param h:
        :type h: "coord_t"

        :param draw_dsc:
        :type draw_dsc: "draw_rect_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def draw_text(
            self, x: "coord_t", y: "coord_t", max_w: "coord_t",
            draw_dsc: "draw_label_dsc_t", txt: str, /
    ) -> None:
        """
        Draw a text on the canvas.

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param max_w:
        :type max_w: "coord_t"

        :param draw_dsc:
        :type draw_dsc: "draw_label_dsc_t"

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def draw_img(
            self, x: "coord_t", y: "coord_t", src,
            draw_dsc: "draw_img_dsc_t", /
    ) -> None:
        """
        Draw an image on the canvas

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param src:
        :type src: None

        :param draw_dsc:
        :type draw_dsc: "draw_img_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def draw_line(
            self, points: Callable[["[]"], "point_t"],
            point_cnt: int, draw_dsc: "draw_line_dsc_t", /
    ) -> None:
        """
        Draw a line on the canvas

        :param points:
        :type points: Callable[["[]"], "point_t"]

        :param point_cnt:
        :type point_cnt: int

        :param draw_dsc:
        :type draw_dsc: "draw_line_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def draw_polygon(
            self, points: Callable[["[]"], "point_t"],
            point_cnt: int, draw_dsc: "draw_rect_dsc_t", /
    ) -> None:
        """
        Draw a polygon on the canvas

        :param points:
        :type points: Callable[["[]"], "point_t"]

        :param point_cnt:
        :type point_cnt: int

        :param draw_dsc:
        :type draw_dsc: "draw_rect_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def draw_arc(
            self, x: "coord_t", y: "coord_t", r: "coord_t", start_angle: int,
            end_angle: int, draw_dsc: "draw_arc_dsc_t", /
    ) -> None:
        """
        Draw an arc on the canvas

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param r:
        :type r: "coord_t"

        :param start_angle:
        :type start_angle: int

        :param end_angle:
        :type end_angle: int

        :param draw_dsc:
        :type draw_dsc: "draw_arc_dsc_t"

        :returns:
        :retval: None
        """
        ...


class _type_chart_cursor_t(TypedDict):
    pos: NotRequired["point_t"]
    point_id: NotRequired["coord_t"]
    color: NotRequired["color_t"]
    ser: NotRequired["chart_series_t"]
    dir: NotRequired["dir_t"]
    pos_set: NotRequired[bool]


class chart_cursor_t(object):
    pos: "point_t" = ...
    point_id: "coord_t" = ...
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    ser: "chart_series_t" = ...
    dir: "dir_t" = ...
    pos_set: bool = ...

    class TYPE:
        """
        Chart types
        """
        NONE: int = 0
        LINE: int = 1
        BAR: int = 2
        SCATTER: int = 3

    class UPDATE_MODE:
        """
        Chart update mode for
        """
        SHIFT: int = 0
        CIRCULAR: int = 1

    class AXIS:
        """
        Enumeration of the axis'
        """
        PRIMARY_Y: int = 0x00
        SECONDARY_Y: int = 0x01
        PRIMARY_X: int = 0x02
        SECONDARY_X: int = 0x04

    class DRAW_PART:
        DIV_LINE_INIT: int = 0
        DIV_LINE_HOR: int = 1
        DIV_LINE_VER: int = 2
        LINE_AND_POINT: int = 3
        BAR: int = 4
        CURSOR: int = 5
        TICK_LABEL: int = 6

    def __init__(self, fields: Optional[_type_chart_cursor_t] = {}, /):
        ...

    def set_type(self, type: "chart_type_t", /) -> None:
        """
        Set a new type for a chart

        :param type:
        :type type: "chart_type_t"

        :returns:
        :retval: None
        """
        ...

    def set_point_count(self, cnt: int, /) -> None:
        """
        Set the number of points on a data line on a chart

        :param cnt:
        :type cnt: int

        :returns:
        :retval: None
        """
        ...

    def set_range(
            self, axis: "chart_axis_t", min: "coord_t", max: "coord_t", /
    ) -> None:
        """
        Set the minimal and maximal y values on an axis

        :param axis:
        :type axis: "chart_axis_t"

        :param min:
        :type min: "coord_t"

        :param max:
        :type max: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_update_mode(self, update_mode: "chart_update_mode_t", /) -> None:
        """
        Set update mode of the chart object. Affects

        :param update_mode:
        :type update_mode: "chart_update_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_div_line_count(self, hdiv: int, vdiv: int, /) -> None:
        """
        Set the number of horizontal and vertical division lines

        :param hdiv:
        :type hdiv: int

        :param vdiv:
        :type vdiv: int

        :returns:
        :retval: None
        """
        ...

    def set_zoom_x(self, zoom_x: int, /) -> None:
        """
        Zoom into the chart in X direction

        :param zoom_x:
        :type zoom_x: int

        :returns:
        :retval: None
        """
        ...

    def set_zoom_y(self, zoom_y: int, /) -> None:
        """
        Zoom into the chart in Y direction

        :param zoom_y:
        :type zoom_y: int

        :returns:
        :retval: None
        """
        ...

    def get_zoom_x(self) -> int:
        """
        Get X zoom of a chart

        :returns: the X zoom value
        :retval: int
        """
        ...

    def get_zoom_y(self) -> int:
        """
        Get Y zoom of a chart

        :returns: the Y zoom value
        :retval: int
        """
        ...

    def set_axis_tick(
            self, axis: "chart_axis_t", major_len: "coord_t",
            minor_len: "coord_t", major_cnt: "coord_t", minor_cnt: "coord_t",
            label_en: bool, draw_size: "coord_t", /
    ) -> None:
        """
        Set the number of tick lines on an axis

        :param axis:
        :type axis: "chart_axis_t"

        :param major_len:
        :type major_len: "coord_t"

        :param minor_len:
        :type minor_len: "coord_t"

        :param major_cnt:
        :type major_cnt: "coord_t"

        :param minor_cnt:
        :type minor_cnt: "coord_t"

        :param label_en:
        :type label_en: bool

        :param draw_size:
        :type draw_size: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def get_type(self) -> "chart_type_t":
        """
        Get the type of a chart

        :returns: type of the chart (from '
        :retval: "chart_type_t"
        """
        ...

    def get_point_count(self) -> int:
        """
        Get the data point number per data line on chart

        :returns: point number on each data line
        :retval: int
        """
        ...

    def get_x_start_point(self, ser: "chart_series_t", /) -> int:
        """
        Get the current index of the x-axis start point in the data array

        :param ser:
        :type ser: "chart_series_t"

        :returns: the index of the current x start point in the data array
        :retval: int
        """
        ...

    def get_point_pos_by_id(
            self, ser: "chart_series_t", id: int, p_out: "point_t", /
    ) -> None:
        """
        Get the position of a point to the chart.

        :param ser:
        :type ser: "chart_series_t"

        :param id:
        :type id: int

        :param p_out:
        :type p_out: "point_t"

        :returns:
        :retval: None
        """
        ...

    def refresh(self) -> None:
        """
        Refresh a chart if its data line has changed

        :returns:
        :retval: None
        """
        ...

    def add_series(
            self, color: "color_t", axis: "chart_axis_t", /
    ) -> "chart_series_t":
        """
        Allocate and add a data series to the chart

        :param color:
        :type color: "color_t"

        :param axis:
        :type axis: "chart_axis_t"

        :returns: pointer to the allocated data series or NULL on failure
        :retval: "chart_series_t"
        """
        ...

    def remove_series(self, series: "chart_series_t", /) -> None:
        """
        Deallocate and remove a data series from a chart

        :param series:
        :type series: "chart_series_t"

        :returns:
        :retval: None
        """
        ...

    def hide_series(self, series: "chart_series_t", hide: bool, /) -> None:
        """
        Hide/Unhide a single series of a chart.

        :param series:
        :type series: "chart_series_t"

        :param hide:
        :type hide: bool

        :returns:
        :retval: None
        """
        ...

    def set_series_color(
            self, series: "chart_series_t", color: "color_t", /
    ) -> None:
        """
        Change the color of a series

        :param series:
        :type series: "chart_series_t"

        :param color:
        :type color: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_x_start_point(self, ser: "chart_series_t", id: int, /) -> None:
        """
        Set the index of the x-axis start point in the data array.
        This point will be considers the first (left) point and the other
        points will be drawn after it.

        :param ser:
        :type ser: "chart_series_t"

        :param id:
        :type id: int

        :returns:
        :retval: None
        """
        ...

    def get_series_next(self, ser: "chart_series_t", /) -> "chart_series_t":
        """
        Get the next series.

        :param ser:
        :type ser: "chart_series_t"

        :returns: the next series or NULL if there is no more.
        :retval: "chart_series_t"
        """
        ...

    def add_cursor(self, color: "color_t", dir: "dir_t", /) -> "chart_cursor_t":
        """
        Add a cursor with a given color

        :param color:
        :type color: "color_t"

        :param dir:
        :type dir: "dir_t"

        :returns: pointer to the created cursor
        :retval: "chart_cursor_t"
        """
        ...

    def set_cursor_pos(
            self, cursor: "chart_cursor_t", pos: "point_t", /
    ) -> None:
        """
        Set the coordinate of the cursor with respect to the paddings

        :param cursor:
        :type cursor: "chart_cursor_t"

        :param pos:
        :type pos: "point_t"

        :returns:
        :retval: None
        """
        ...

    def set_cursor_point(
            self, cursor: "chart_cursor_t", ser: "chart_series_t",
            point_id: int, /
    ) -> None:
        """
        Stick the cursor to a point

        :param cursor:
        :type cursor: "chart_cursor_t"

        :param ser:
        :type ser: "chart_series_t"

        :param point_id:
        :type point_id: int

        :returns:
        :retval: None
        """
        ...

    def get_cursor_point(self, cursor: "chart_cursor_t", /) -> "point_t":
        """
        Get the coordinate of the cursor with respect to the paddings

        :param cursor:
        :type cursor: "chart_cursor_t"

        :returns: coordinate of the cursor as
        :retval: "point_t"
        """
        ...

    def set_all_value(self, ser: "chart_series_t", value: "coord_t", /) -> None:
        """
        Initialize all data points of a series with a value

        :param ser:
        :type ser: "chart_series_t"

        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_next_value(
            self, ser: "chart_series_t", value: "coord_t", /
    ) -> None:
        """
        Set the next point's Y value according to the update mode policy.

        :param ser:
        :type ser: "chart_series_t"

        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_next_value2(
            self, ser: "chart_series_t", x_value: "coord_t",
            y_value: "coord_t", /
    ) -> None:
        """
        Set the next point's X and Y value according to the update mode policy.

        :param ser:
        :type ser: "chart_series_t"

        :param x_value:
        :type x_value: "coord_t"

        :param y_value:
        :type y_value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_value_by_id(
            self, ser: "chart_series_t", id: int, value: "coord_t", /
    ) -> None:
        """
        Set an individual point's y value of a chart's
        series directly based on its index

        :param ser:
        :type ser: "chart_series_t"

        :param id:
        :type id: int

        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_value_by_id2(
            self, ser: "chart_series_t", id: int,
            x_value: "coord_t", y_value: "coord_t", /
    ) -> None:
        """
        Set an individual point's x and y value of a chart's
        series directly based on its index Can be used only with

        :param ser:
        :type ser: "chart_series_t"

        :param id:
        :type id: int

        :param x_value:
        :type x_value: "coord_t"

        :param y_value:
        :type y_value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_ext_y_array(
            self, ser: "chart_series_t", array: Callable[["[]"], "coord_t"], /
    ) -> None:
        """
        Set an external array for the y data points to use for
        the chart NOTE: It is the users responsibility to make sure the

        :param ser:
        :type ser: "chart_series_t"

        :param array:
        :type array: Callable[["[]"], "coord_t"]

        :returns:
        :retval: None
        """
        ...

    def set_ext_x_array(
            self, ser: "chart_series_t",
            array: Callable[["[]"], "coord_t"], /
    ) -> None:
        """
        Set an external array for the x data points to use
        for the chart NOTE: It is the users responsibility to make sure the

        :param ser:
        :type ser: "chart_series_t"

        :param array:
        :type array: Callable[["[]"], "coord_t"]

        :returns:
        :retval: None
        """
        ...

    def get_y_array(self, ser: "chart_series_t", /) -> "coord_t":
        """
        Get the array of y values of a series

        :param ser:
        :type ser: "chart_series_t"

        :returns: the array of values with 'point_count' elements
        :retval: "coord_t"
        """
        ...

    def get_x_array(self, ser: "chart_series_t", /) -> "coord_t":
        """
        Get the array of x values of a series

        :param ser:
        :type ser: "chart_series_t"

        :returns: the array of values with 'point_count' elements
        :retval: "coord_t"
        """
        ...

    def get_pressed_point(self) -> int:
        """
        Get the index of the currently pressed point.
        It's the same for every series.

        :returns: the index of the point [0 .. point count] or
            LV_CHART_POINT_ID_NONE if no point is being pressed
        :retval: int
        """
        ...


class _type_chart_series_t(TypedDict):
    x_points: NotRequired["coord_t"]
    y_points: NotRequired["coord_t"]
    color: NotRequired["color_t"]
    start_point: NotRequired[int]
    hidden: NotRequired[bool]
    x_ext_buf_assigned: NotRequired[bool]
    y_ext_buf_assigned: NotRequired[bool]
    x_axis_sec: NotRequired[bool]
    y_axis_sec: NotRequired[bool]


class chart_series_t(object):
    """
    Descriptor a chart series
    """

    x_points: "coord_t" = ...
    y_points: "coord_t" = ...
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    start_point: int = ...
    hidden: bool = ...
    x_ext_buf_assigned: bool = ...
    y_ext_buf_assigned: bool = ...
    x_axis_sec: bool = ...
    y_axis_sec: bool = ...

    def __init__(self, fields: Optional[_type_chart_series_t] = {}, /):
        ...


class _type_chart_t(TypedDict):
    obj: NotRequired["obj_t"]
    series_ll: NotRequired["ll_t"]
    cursor_ll: NotRequired["ll_t"]
    tick: NotRequired["chart_tick_dsc_t"]
    ymin: NotRequired["coord_t"]
    ymax: NotRequired["coord_t"]
    xmin: NotRequired["coord_t"]
    xmax: NotRequired["coord_t"]
    pressed_point_id: NotRequired["coord_t"]
    hdiv_cnt: NotRequired[int]
    vdiv_cnt: NotRequired[int]
    point_cnt: NotRequired[int]
    zoom_x: NotRequired[int]
    zoom_y: NotRequired[int]
    type: NotRequired["draw_mask_type_t"]
    update_mode: NotRequired[bool]


class chart_t(object):
    obj: "obj_t" = ...
    """Linked list for the series (stores"""
    series_ll: "ll_t" = ...
    """Linked list for the cursors (stores"""
    cursor_ll: "ll_t" = ...
    tick: "chart_tick_dsc_t" = ...
    ymin: "coord_t" = ...
    ymax: "coord_t" = ...
    xmin: "coord_t" = ...
    xmax: "coord_t" = ...
    pressed_point_id: "coord_t" = ...
    """Number of horizontal division lines"""
    hdiv_cnt: int = ...
    """Number of vertical division lines"""
    vdiv_cnt: int = ...
    """Point number in a data line"""
    point_cnt: int = ...
    zoom_x: int = ...
    zoom_y: int = ...
    type: "draw_mask_type_t" = ...
    update_mode: bool = ...

    def __init__(self, fields: Optional[_type_chart_t] = {}, /):
        ...


class _type_chart_tick_dsc_t(TypedDict):
    major_len: NotRequired["coord_t"]
    minor_len: NotRequired["coord_t"]
    draw_size: NotRequired["coord_t"]
    minor_cnt: NotRequired[int]
    major_cnt: NotRequired[int]
    label_en: NotRequired[bool]


class chart_tick_dsc_t(object):
    major_len: "coord_t" = ...
    minor_len: "coord_t" = ...
    draw_size: "coord_t" = ...
    minor_cnt: int = ...
    major_cnt: int = ...
    label_en: bool = ...

    def __init__(self, fields: Optional[_type_chart_tick_dsc_t] = {}, /):
        ...


class _type_checkbox_t(TypedDict):
    obj: NotRequired["obj_t"]
    txt: NotRequired[int]
    static_txt: NotRequired[bool]


class checkbox_t(object):
    obj: "obj_t" = ...
    txt: int = ...
    static_txt: bool = ...

    class DRAW_PART_BOX:
        CHECKBOX_DRAW_PART_BOX: int = 0

    def __init__(self, fields: Optional[_type_checkbox_t] = {}, /):
        ...

    def set_text(self, txt: str, /) -> None:
        """
        Set the text of a check box.

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def set_text_static(self, txt: str, /) -> None:
        """
        Set the text of a check box.

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def get_text(self) -> str:
        """
        Get the text of a check box

        :returns: pointer to the text of the check box
        :retval: str
        """
        ...


class _type_color16_t(TypedDict):
    blue: NotRequired[int]
    green: NotRequired[int]
    red: NotRequired[int]


class color16_t(object):
    blue: int = ...
    green: int = ...
    red: int = ...

    def __init__(self, fields: Optional[_type_color16_t] = {}, /):
        ...

    def set_int(self, v: int, /) -> None:
        """
        :param v:
        :type v: int

        :returns:
        :retval: None
        """
        ...

    def to_int(self) -> int:
        """
        :returns:
        :retval: int
        """
        ...


class _type_color1_t(TypedDict):
    blue: NotRequired[int]
    green: NotRequired[int]
    red: NotRequired[int]


class color1_t(object):
    blue: int = ...
    green: int = ...
    red: int = ...

    def __init__(self, fields: Optional[_type_color1_t] = {}, /):
        ...


class _type_color24_t(TypedDict):
    blue: NotRequired[int]
    green: NotRequired[int]
    red: NotRequired[int]


class color24_t(object):
    blue: int = ...
    green: int = ...
    red: int = ...

    def __init__(self, fields: Optional[_type_color24_t] = {}, /):
        ...

    def set_int(self, v: int, /) -> None:
        """
        :param v:
        :type v: int

        :returns:
        :retval: None
        """
        ...

    def to_int(self) -> int:
        """
        :returns:
        :retval: int
        """
        ...


class _type_color32_t(TypedDict):
    blue: NotRequired[int]
    green: NotRequired[int]
    red: NotRequired[int]
    alpha: NotRequired[int]


class color32_t(object):
    blue: int = ...
    green: int = ...
    red: int = ...
    alpha: int = ...

    def __init__(self, fields: Optional[_type_color32_t] = {}, /):
        ...

    def set_int(self, v: int, /) -> None:
        """
        :param v:
        :type v: int

        :returns:
        :retval: None
        """
        ...

    def to_int(self) -> int:
        """
        :returns:
        :retval: int
        """
        ...


class _type_color8_t(TypedDict):
    blue: NotRequired[int]
    green: NotRequired[int]
    red: NotRequired[int]
    level: NotRequired[int]


class color8_t(object):
    blue: int = ...
    green: int = ...
    red: int = ...
    level: int = ...

    def __init__(self, fields: Optional[_type_color8_t] = {}, /):
        ...

    def set_int(self, v: int, /) -> None:
        """
        :param v:
        :type v: int

        :returns:
        :retval: None
        """
        ...

    def to_int(self) -> int:
        """
        :returns:
        :retval: int
        """
        ...


class _type_color_hsv_t(TypedDict):
    h: NotRequired[int]
    s: NotRequired[int]
    v: NotRequired[int]


class color_hsv_t(object):
    h: int = ...
    s: int = ...
    v: int = ...

    def __init__(self, fields: Optional[_type_color_hsv_t] = {}, /):
        ...


class _type_colorwheel_t(TypedDict):
    obj: NotRequired["obj_t"]
    hsv: NotRequired["color_hsv_t"]
    pos: NotRequired["point_t"]
    recolor: NotRequired[bool]
    knob: NotRequired["colorwheel_t"]
    last_click_time: NotRequired[int]
    last_change_time: NotRequired[int]
    last_press_point: NotRequired["point_t"]
    mode: NotRequired["bar_mode_t"]
    mode_fixed: NotRequired[bool]


class colorwheel_t(object):
    obj: "obj_t" = ...
    hsv: "color_hsv_t" = ...
    pos: "point_t" = ...
    recolor: bool = ...
    knob: "colorwheel_t" = ...
    last_click_time: int = ...
    last_change_time: int = ...
    last_press_point: "point_t" = ...
    """Type of bar"""
    mode: "bar_mode_t" = ...
    mode_fixed: bool = ...

    class MODE:
        HUE: int = 0
        SATURATION: int = 1
        VALUE: int = 2

    def __init__(self, fields: Optional[_type_colorwheel_t] = {}, /):
        ...

    def set_hsv(self, hsv: "color_hsv_t", /) -> bool:
        """
        Set the current hsv of a color wheel.

        :param hsv:
        :type hsv: "color_hsv_t"

        :returns: true if changed, otherwise false
        :retval: bool
        """
        ...

    def set_rgb(self, color: "color_t", /) -> bool:
        """
        Set the current color of a color wheel.

        :param color:
        :type color: "color_t"

        :returns: true if changed, otherwise false
        :retval: bool
        """
        ...

    def set_mode(self, mode: "colorwheel_mode_t", /) -> None:
        """
        Set the current color mode.

        :param mode:
        :type mode: "colorwheel_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_mode_fixed(self, fixed: bool, /) -> None:
        """
        Set if the color mode is changed on long press on center

        :param fixed:
        :type fixed: bool

        :returns:
        :retval: None
        """
        ...

    def get_hsv(self) -> "color_hsv_t":
        """
        Get the current selected hsv of a color wheel.

        :returns: current selected hsv
        :retval: "color_hsv_t"
        """
        ...

    def get_rgb(self) -> "color_t":
        """
        Get the current selected color of a color wheel.

        :returns: color current selected color
        :retval: "color_t"
        """
        ...

    def get_color_mode(self) -> "colorwheel_mode_t":
        """
        Get the current color mode.

        :returns: color mode (hue/sat/val)
        :retval: "colorwheel_mode_t"
        """
        ...

    def get_color_mode_fixed(self) -> bool:
        """
        Get if the color mode is changed on long press on center

        :returns: mode cannot be changed on long press
        :retval: bool
        """
        ...


class _type_cover_check_info_t(TypedDict):
    res: NotRequired["cover_res_t"]
    area: NotRequired["area_t"]


class cover_check_info_t(object):
    """
    Used as the event parameter of
    """

    res: "cover_res_t" = ...
    area: "area_t" = ...

    def __init__(self, fields: Optional[_type_cover_check_info_t] = {}, /):
        ...


class _type_draw_arc_dsc_t(TypedDict):
    color: NotRequired["color_t"]
    width: NotRequired["coord_t"]
    start_angle: NotRequired[int]
    end_angle: NotRequired[int]
    img_src: NotRequired[None]
    opa: NotRequired["opa_t"]
    blend_mode: NotRequired["blend_mode_t"]
    rounded: NotRequired[bool]


class draw_arc_dsc_t(object):
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    width: "coord_t" = ...
    start_angle: int = ...
    end_angle: int = ...
    img_src: None = ...
    opa: "opa_t" = ...
    blend_mode: "blend_mode_t" = ...
    rounded: bool = ...

    class LAYER_FLAG:
        NONE: int = 0
        HAS_ALPHA: int = 1
        CAN_SUBDIVIDE: int = 2

    class SDL_COMPOSITE_TEXTURE_ID:
        STREAM0: int = 0
        STREAM1: int = 1
        TARGET0: int = 2
        TARGET1: int = 3
        TRANSFORM0: int = 4

    def __init__(self, fields: Optional[_type_draw_arc_dsc_t] = {}, /):
        ...

    def init(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...


class _type_draw_img_dsc_t(TypedDict):
    angle: NotRequired[int]
    zoom: NotRequired[int]
    pivot: NotRequired["point_t"]
    chroma_key_color: NotRequired["color_t"]
    recolor: NotRequired[bool]
    recolor_opa: NotRequired["opa_t"]
    opa: NotRequired["opa_t"]
    blend_mode: NotRequired["blend_mode_t"]
    frame_id: NotRequired[int]
    antialias: NotRequired[bool]
    sup: NotRequired["draw_img_sup_t"]


class draw_img_dsc_t(object):
    angle: int = ...
    zoom: int = ...
    pivot: "point_t" = ...
    chroma_key_color: "color_t" = ...
    recolor: bool = ...
    recolor_opa: "opa_t" = ...
    opa: "opa_t" = ...
    blend_mode: "blend_mode_t" = ...
    """Frame of the image, using with animated images"""
    frame_id: int = ...
    antialias: bool = ...
    sup: "draw_img_sup_t" = ...

    def __init__(self, fields: Optional[_type_draw_img_dsc_t] = {}, /):
        ...

    def init(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...


class _type_draw_img_sup_t(TypedDict):
    chroma_key_color: NotRequired["color_t"]
    alpha_color: NotRequired["color_t"]
    palette: NotRequired["color32_t"]
    palette_size: NotRequired[int]
    chroma_keyed: NotRequired[bool]


class draw_img_sup_t(object):
    chroma_key_color: "color_t" = ...
    alpha_color: "color_t" = ...
    palette: "color32_t" = ...
    palette_size: int = ...
    chroma_keyed: bool = ...

    def __init__(self, fields: Optional[_type_draw_img_sup_t] = {}, /):
        ...


class _type_draw_label_dsc_t(TypedDict):
    font: NotRequired["font_t"]
    sel_start: NotRequired[int]
    sel_end: NotRequired[int]
    color: NotRequired["color_t"]
    sel_color: NotRequired["color_t"]
    sel_bg_color: NotRequired["color_t"]
    line_space: NotRequired["coord_t"]
    letter_space: NotRequired["coord_t"]
    ofs_x: NotRequired["coord_t"]
    ofs_y: NotRequired["coord_t"]
    opa: NotRequired["opa_t"]
    bidi_dir: NotRequired["base_dir_t"]
    align: NotRequired["text_align_t"]
    flag: NotRequired["text_flag_t"]
    decor: NotRequired["text_decor_t"]
    blend_mode: NotRequired["blend_mode_t"]


class draw_label_dsc_t(object):
    font: "font_t" = ...
    sel_start: int = ...
    sel_end: int = ...
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    sel_color: "color_t" = ...
    sel_bg_color: "color_t" = ...
    line_space: "coord_t" = ...
    letter_space: "coord_t" = ...
    ofs_x: "coord_t" = ...
    ofs_y: "coord_t" = ...
    opa: "opa_t" = ...
    bidi_dir: "base_dir_t" = ...
    align: "text_align_t" = ...
    flag: "text_flag_t" = ...
    decor: "text_decor_t" = ...
    blend_mode: "blend_mode_t" = ...

    def __init__(self, fields: Optional[_type_draw_label_dsc_t] = {}, /):
        ...

    def init(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...


class _type_draw_line_dsc_t(TypedDict):
    color: NotRequired["color_t"]
    width: NotRequired["coord_t"]
    dash_width: NotRequired["coord_t"]
    dash_gap: NotRequired["coord_t"]
    opa: NotRequired["opa_t"]
    blend_mode: NotRequired["blend_mode_t"]
    round_start: NotRequired[bool]
    round_end: NotRequired[bool]
    raw_end: NotRequired[bool]


class draw_line_dsc_t(object):
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    width: "coord_t" = ...
    dash_width: "coord_t" = ...
    dash_gap: "coord_t" = ...
    opa: "opa_t" = ...
    blend_mode: "blend_mode_t" = ...
    round_start: bool = ...
    round_end: bool = ...
    raw_end: bool = ...

    def __init__(self, fields: Optional[_type_draw_line_dsc_t] = {}, /):
        ...

    def init(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...


class _type_draw_mask_angle_param_t(TypedDict):
    dsc: NotRequired["draw_mask_common_dsc_t"]
    vertex_p: NotRequired["point_t"]
    start_angle: NotRequired[int]
    end_angle: NotRequired[int]
    cfg: NotRequired["draw_mask_map_param_t"]
    start_line: NotRequired["draw_mask_line_param_t"]
    end_line: NotRequired["draw_mask_line_param_t"]
    delta_deg: NotRequired[int]


class draw_mask_angle_param_t(object):
    dsc: "draw_mask_common_dsc_t" = ...
    vertex_p: "point_t" = ...
    start_angle: int = ...
    end_angle: int = ...
    cfg: "draw_mask_map_param_t" = ...
    start_line: "draw_mask_line_param_t" = ...
    end_line: "draw_mask_line_param_t" = ...
    delta_deg: int = ...

    class RES:
        TRANSP: int = 0
        FULL_COVER: int = 1
        CHANGED: int = 2
        UNKNOWN: int = 3

    class TYPE:
        LINE: int = 0
        ANGLE: int = 1
        RADIUS: int = 2
        FADE: int = 3
        MAP: int = 4
        POLYGON: int = 5

    def __init__(self, fields: Optional[_type_draw_mask_angle_param_t] = {}, /):
        ...

    def init(
            self, vertex_x: "coord_t", vertex_y: "coord_t",
            start_angle: "coord_t", end_angle: "coord_t", /
    ) -> None:
        """
        Initialize an angle mask.

        :param vertex_x:
        :type vertex_x: "coord_t"

        :param vertex_y:
        :type vertex_y: "coord_t"

        :param start_angle:
        :type start_angle: "coord_t"

        :param end_angle:
        :type end_angle: "coord_t"

        :returns:
        :retval: None
        """
        ...


class _type_draw_mask_fade_param_t(TypedDict):
    dsc: NotRequired["draw_mask_common_dsc_t"]
    coords: NotRequired["area_t"]
    y_top: NotRequired["coord_t"]
    y_bottom: NotRequired["coord_t"]
    opa_top: NotRequired["opa_t"]
    opa_bottom: NotRequired["opa_t"]
    cfg: NotRequired["draw_mask_map_param_t"]


class draw_mask_fade_param_t(object):
    dsc: "draw_mask_common_dsc_t" = ...
    coords: "area_t" = ...
    y_top: "coord_t" = ...
    y_bottom: "coord_t" = ...
    opa_top: "opa_t" = ...
    opa_bottom: "opa_t" = ...
    cfg: "draw_mask_map_param_t" = ...

    def __init__(self, fields: Optional[_type_draw_mask_fade_param_t] = {}, /):
        ...

    def init(
            self, coords: "area_t", opa_top: "opa_t", y_top: "coord_t",
            opa_bottom: "opa_t", y_bottom: "coord_t", /
    ) -> None:
        """
        Initialize a fade mask.

        :param coords:
        :type coords: "area_t"

        :param opa_top:
        :type opa_top: "opa_t"

        :param y_top:
        :type y_top: "coord_t"

        :param opa_bottom:
        :type opa_bottom: "opa_t"

        :param y_bottom:
        :type y_bottom: "coord_t"

        :returns:
        :retval: None
        """
        ...


class _type_draw_mask_line_param_t(TypedDict):
    dsc: NotRequired["draw_mask_common_dsc_t"]
    p1: NotRequired["point_t"]
    p2: NotRequired["point_t"]
    side: NotRequired["draw_mask_line_side_t"]
    cfg: NotRequired["draw_mask_map_param_t"]
    origo: NotRequired["point_t"]
    xy_steep: NotRequired[int]
    yx_steep: NotRequired[int]
    steep: NotRequired[int]
    spx: NotRequired[int]
    flat: NotRequired[bool]
    inv: NotRequired[bool]


class draw_mask_line_param_t(object):
    dsc: "draw_mask_common_dsc_t" = ...
    p1: "point_t" = ...
    p2: "point_t" = ...
    side: "draw_mask_line_side_t" = ...
    cfg: "draw_mask_map_param_t" = ...
    origo: "point_t" = ...
    xy_steep: int = ...
    yx_steep: int = ...
    steep: int = ...
    spx: int = ...
    flat: bool = ...
    inv: bool = ...

    class SIDE:
        LEFT: int = 0
        RIGHT: int = 1
        TOP: int = 2
        BOTTOM: int = 3

    def __init__(self, fields: Optional[_type_draw_mask_line_param_t] = {}, /):
        ...

    def points_init(
            self, p1x: "coord_t", p1y: "coord_t", p2x: "coord_t",
            p2y: "coord_t", side: "draw_mask_line_side_t", /
    ) -> None:
        """
        Initialize a line mask from two points.

        :param p1x:
        :type p1x: "coord_t"

        :param p1y:
        :type p1y: "coord_t"

        :param p2x:
        :type p2x: "coord_t"

        :param p2y:
        :type p2y: "coord_t"

        :param side:
        :type side: "draw_mask_line_side_t"

        :returns:
        :retval: None
        """
        ...

    def angle_init(
            self, p1x: "coord_t", py: "coord_t", angle: int,
            side: "draw_mask_line_side_t", /
    ) -> None:
        """
        Initialize a line mask from a point and an angle.

        :param p1x:
        :type p1x: "coord_t"

        :param py:
        :type py: "coord_t"

        :param angle:
        :type angle: int

        :param side:
        :type side: "draw_mask_line_side_t"

        :returns:
        :retval: None
        """
        ...


class _type_draw_mask_polygon_param_t(TypedDict):
    dsc: NotRequired["draw_mask_common_dsc_t"]
    points: NotRequired["point_t"]
    point_cnt: NotRequired[int]
    cfg: NotRequired["draw_mask_map_param_t"]


class draw_mask_polygon_param_t(object):
    dsc: "draw_mask_common_dsc_t" = ...
    points: "point_t" = ...
    """Point number in a data line"""
    point_cnt: int = ...
    cfg: "draw_mask_map_param_t" = ...

    def __init__(
            self, fields: Optional[_type_draw_mask_polygon_param_t] = {}, /
    ):
        ...

    def init(self, points: "point_t", point_cnt: int, /) -> None:
        """
        :param points:
        :type points: "point_t"

        :param point_cnt:
        :type point_cnt: int

        :returns:
        :retval: None
        """
        ...


class _type_draw_mask_radius_param_t(TypedDict):
    dsc: NotRequired["draw_mask_common_dsc_t"]
    rect: NotRequired["area_t"]
    radius: NotRequired["coord_t"]
    outer: NotRequired[bool]
    cfg: NotRequired["draw_mask_map_param_t"]
    circle: NotRequired["draw_mask_radius_circle_dsc_t"]


class draw_mask_radius_param_t(object):
    dsc: "draw_mask_common_dsc_t" = ...
    rect: "area_t" = ...
    radius: "coord_t" = ...
    outer: bool = ...
    cfg: "draw_mask_map_param_t" = ...
    circle: "draw_mask_radius_circle_dsc_t" = ...

    def __init__(
            self, fields: Optional[_type_draw_mask_radius_param_t] = {}, /
    ):
        ...

    def init(self, rect: "area_t", radius: "coord_t", inv: bool, /) -> None:
        """
        Initialize a fade mask.

        :param rect:
        :type rect: "area_t"

        :param radius:
        :type radius: "coord_t"

        :param inv:
        :type inv: bool

        :returns:
        :retval: None
        """
        ...


class _type_draw_mask_t(TypedDict):
    user_data: NotRequired[None]


class draw_mask_t(object):
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type_draw_mask_t] = {}, /):
        ...


class _type_draw_rect_dsc_t(TypedDict):
    radius: NotRequired["coord_t"]
    blend_mode: NotRequired["blend_mode_t"]
    bg_opa: NotRequired["opa_t"]
    bg_color: NotRequired["color_t"]
    bg_grad: NotRequired["grad_dsc_t"]
    bg_img_src: NotRequired[None]
    bg_img_symbol_font: NotRequired[None]
    bg_img_recolor: NotRequired["color_t"]
    bg_img_opa: NotRequired["opa_t"]
    bg_img_recolor_opa: NotRequired["opa_t"]
    bg_img_tiled: NotRequired[int]
    border_color: NotRequired["color_t"]
    border_width: NotRequired["coord_t"]
    border_opa: NotRequired["opa_t"]
    border_post: NotRequired[bool]
    border_side: NotRequired["border_side_t"]
    outline_color: NotRequired["color_t"]
    outline_width: NotRequired["coord_t"]
    outline_pad: NotRequired["coord_t"]
    outline_opa: NotRequired["opa_t"]
    shadow_color: NotRequired["color_t"]
    shadow_width: NotRequired["coord_t"]
    shadow_ofs_x: NotRequired["coord_t"]
    shadow_ofs_y: NotRequired["coord_t"]
    shadow_spread: NotRequired["coord_t"]
    shadow_opa: NotRequired["opa_t"]


class draw_rect_dsc_t(object):
    radius: "coord_t" = ...
    blend_mode: "blend_mode_t" = ...
    bg_opa: "opa_t" = ...
    """First element of a gradient is a color, so it maps well here"""
    bg_color: "color_t" = ...
    bg_grad: "grad_dsc_t" = ...
    bg_img_src: None = ...
    bg_img_symbol_font: None = ...
    bg_img_recolor: "color_t" = ...
    bg_img_opa: "opa_t" = ...
    bg_img_recolor_opa: "opa_t" = ...
    bg_img_tiled: int = ...
    border_color: "color_t" = ...
    border_width: "coord_t" = ...
    border_opa: "opa_t" = ...
    border_post: bool = ...
    border_side: "border_side_t" = ...
    outline_color: "color_t" = ...
    outline_width: "coord_t" = ...
    outline_pad: "coord_t" = ...
    outline_opa: "opa_t" = ...
    shadow_color: "color_t" = ...
    shadow_width: "coord_t" = ...
    shadow_ofs_x: "coord_t" = ...
    shadow_ofs_y: "coord_t" = ...
    shadow_spread: "coord_t" = ...
    shadow_opa: "opa_t" = ...

    def __init__(self, fields: Optional[_type_draw_rect_dsc_t] = {}, /):
        ...

    def init(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...


class _type_draw_sw_blend_dsc_t(TypedDict):
    blend_area: NotRequired["area_t"]
    src_buf: NotRequired["color_t"]
    color: NotRequired["color_t"]
    mask_buf: NotRequired["opa_t"]
    mask_res: NotRequired["draw_mask_res_t"]
    mask_area: NotRequired["area_t"]
    opa: NotRequired["opa_t"]
    blend_mode: NotRequired["blend_mode_t"]


class draw_sw_blend_dsc_t(object):
    """The area with absolute coordinates to draw on"""
    blend_area: "area_t" = ...
    """Pointer to an image to blend. If set"""
    src_buf: "color_t" = ...
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    """NULL if ignored, or an alpha mask to apply on"""
    mask_buf: "opa_t" = ...
    """The result of the previous mask operation"""
    mask_res: "draw_mask_res_t" = ...
    """The area of"""
    mask_area: "area_t" = ...
    opa: "opa_t" = ...
    blend_mode: "blend_mode_t" = ...

    def __init__(self, fields: Optional[_type_draw_sw_blend_dsc_t] = {}, /):
        ...


class _type_draw_sw_ctx_t(TypedDict):
    base_draw: NotRequired["draw_ctx_t"]
    blend: NotRequired[Callable[["draw_ctx_t", "draw_sw_blend_dsc_t"], None]]


class draw_sw_ctx_t(object):
    base_draw: "draw_ctx_t" = ...
    """Fill an area of the destination buffer with a color"""
    blend: Callable[["draw_ctx_t", "draw_sw_blend_dsc_t"], None]

    def __init__(self, fields: Optional[_type_draw_sw_ctx_t] = {}, /):
        ...


class _type_draw_sw_layer_ctx_t(TypedDict):
    base_draw: NotRequired["draw_ctx_t"]
    buf_size_bytes: NotRequired[int]


class draw_sw_layer_ctx_t(object):
    base_draw: "draw_ctx_t" = ...
    buf_size_bytes: int = ...

    def __init__(self, fields: Optional[_type_draw_sw_layer_ctx_t] = {}, /):
        ...


class _type_dropdown_list_t(TypedDict):
    obj: NotRequired["obj_t"]
    dropdown: NotRequired["obj_t"]


class dropdown_list_t(object):
    obj: "obj_t" = ...
    dropdown: "obj_t" = ...

    def __init__(self, fields: Optional[_type_dropdown_list_t] = {}, /):
        ...

    def set_text(self, txt: str, /) -> None:
        """
        Set text of the drop-down list's button. If set to

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def set_options(self, options: str, /) -> None:
        """
        Set the options in a drop-down list from a string.
        The options will be copied and saved in the object so the

        :param options:
        :type options: str

        :returns:
        :retval: None
        """
        ...

    def set_options_static(self, options: str, /) -> None:
        """
        Set the options in a drop-down list from a static string
        (global, static or dynamically allocated). Only the pointer
        of the option string will be saved.

        :param options:
        :type options: str

        :returns:
        :retval: None
        """
        ...

    def add_option(self, option: str, pos: int, /) -> None:
        """
        Add an options to a drop-down list from a string.
        Only works for non-static options.

        :param option:
        :type option: str

        :param pos:
        :type pos: int

        :returns:
        :retval: None
        """
        ...

    def clear_options(self) -> None:
        """
        Clear all options in a drop-down list.
        Works with both static and dynamic options.

        :returns:
        :retval: None
        """
        ...

    def set_selected(self, sel_opt: int, /) -> None:
        """
        Set the selected option

        :param sel_opt:
        :type sel_opt: int

        :returns:
        :retval: None
        """
        ...

    def set_dir(self, dir: "dir_t", /) -> None:
        """
        Set the direction of the a drop-down list

        :param dir:
        :type dir: "dir_t"

        :returns:
        :retval: None
        """
        ...

    def set_symbol(self, symbol, /) -> None:
        """
        Set an arrow or other symbol to display when on drop-down
        list's button. Typically a down caret or arrow.

        :param symbol:
        :type symbol: None

        :returns: angle and zoom transformation can be applied if the
            symbol is an image. E.g. when drop down is checked (opened)
            rotate the symbol by 180 degree
        :retval: None
        """
        ...

    def set_selected_highlight(self, en: bool, /) -> None:
        """
        Set whether the selected option in the list should be
        highlighted or not

        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def get_list(self) -> "obj_t":
        """
        Get the list of a drop-down to allow styling or other modifications

        :returns: pointer to the list of the drop-down
        :retval: "obj_t"
        """
        ...

    def get_text(self) -> str:
        """
        Get text of the drop-down list's button.

        :returns: the text as string,
        :retval: str
        """
        ...

    def get_options(self) -> str:
        """
        Get the options of a drop-down list

        :returns: the options separated by '
        :retval: str
        """
        ...

    def get_selected(self) -> int:
        """
        Get the index of the selected option

        :returns: index of the selected option (0 ... number of option - 1);
        :retval: int
        """
        ...

    def get_option_cnt(self) -> int:
        """
        Get the total number of options

        :returns: the total number of options in the list
        :retval: int
        """
        ...

    def get_selected_str(self, buf: int, buf_size: int, /) -> None:
        """
        Get the current selected option as a string

        :param buf:
        :type buf: int

        :param buf_size:
        :type buf_size: int

        :returns:
        :retval: None
        """
        ...

    def get_option_index(self, option: str, /) -> int:
        """
        Get the index of an option.

        :param option:
        :type option: str

        :returns: index of
        :retval: int
        """
        ...

    def get_symbol(self) -> str:
        """
        Get the symbol on the drop-down list. Typically a down caret or arrow.

        :returns: the symbol or NULL if not enabled
        :retval: str
        """
        ...

    def get_selected_highlight(self) -> bool:
        """
        Get whether the selected option in the list should be
        highlighted or not

        :returns: true: highlight enabled; false: disabled
        :retval: bool
        """
        ...

    def get_dir(self) -> "dir_t":
        """
        Get the direction of the drop-down list

        :returns: LV_DIR_LEF/RIGHT/TOP/BOTTOM
        :retval: "dir_t"
        """
        ...

    def open(self) -> None:
        """
        Open the drop.down list

        :returns:
        :retval: None
        """
        ...

    def close(self) -> None:
        """
        Close (Collapse) the drop-down list

        :returns:
        :retval: None
        """
        ...

    def is_open(self) -> bool:
        """
        Tells whether the list is opened or not

        :returns: true if the list os opened
        :retval: bool
        """
        ...


class _type_dropdown_t(TypedDict):
    obj: NotRequired["obj_t"]
    list: NotRequired["obj_t"]
    text: NotRequired[str]
    symbol: NotRequired[None]
    options: NotRequired[int]
    option_cnt: NotRequired[int]
    sel_opt_id: NotRequired[int]
    sel_opt_id_orig: NotRequired[int]
    pr_opt_id: NotRequired[int]
    dir: NotRequired["dir_t"]
    static_txt: NotRequired[bool]
    selected_highlight: NotRequired[bool]


class dropdown_t(object):
    obj: "obj_t" = ...
    """The dropped down list"""
    list: "obj_t" = ...
    """Text to display on the dropdown's button"""
    text: str = ...
    """Arrow or other icon when the drop-down list is closed"""
    symbol: None = ...
    """Options in a '"""
    options: int = ...
    """Number of options"""
    option_cnt: int = ...
    """Index of the currently selected option"""
    sel_opt_id: int = ...
    """Store the original index on focus"""
    sel_opt_id_orig: int = ...
    """Index of the currently pressed option"""
    pr_opt_id: int = ...
    dir: "dir_t" = ...
    static_txt: bool = ...
    """1: Make the selected option highlighted in the list"""
    selected_highlight: bool = ...

    def __init__(self, fields: Optional[_type_dropdown_t] = {}, /):
        ...


class _type_event_list_t(TypedDict):
    dsc: NotRequired["draw_mask_common_dsc_t"]
    cnt: NotRequired[int]
        
        
        

def event_send(e_list: "event_list_t", e: "event_t", prerpocess: bool, /) -> "res_t":
    """
    :param e:
    :type e: "event_t"

    :param prerpocess:
    :type prerpocess: bool

    :returns:
    :retval: "res_t"
    """
    ...


class event_list_t(object):
    dsc: "draw_mask_common_dsc_t" = ...
    cnt: int = ...

    def __init__(self, fields: Optional[_type_event_list_t] = {}, /):
        ...

    def add(
            self, cb: "event_cb_t", filter: "event_code_t", user_data, /
    ) -> None:
        """
        :param cb:
        :type cb: "event_cb_t"

        :param filter:
        :type filter: "event_code_t"

        :param user_data:
        :type user_data: None

        :returns:
        :retval: None
        """
        ...

    def get_count(self) -> int:
        """
        :returns:
        :retval: int
        """
        ...

    def get_dsc(self, index: int, /) -> "event_dsc_t":
        """
        :param index:
        :type index: int

        :returns:
        :retval: "event_dsc_t"
        """
        ...

    def remove(self, index: int, /) -> bool:
        """
        :param index:
        :type index: int

        :returns:
        :retval: bool
        """
        ...


class _type_font_fmt_txt_cmap_t(TypedDict):
    range_start: NotRequired[int]
    range_length: NotRequired[int]
    glyph_id_start: NotRequired[int]
    unicode_list: NotRequired[int]
    glyph_id_ofs_list: NotRequired[None]
    list_length: NotRequired[int]
    type: NotRequired["draw_mask_type_t"]


class font_fmt_txt_cmap_t(object):
    """
    Map codepoints to a
    """

    """First Unicode character for this range"""
    range_start: int = ...
    """
    Number of Unicode characters related to this range. 
    Last Unicode character = range_start + range_length - 1
    """
    range_length: int = ...
    """First glyph ID (array index of"""
    glyph_id_start: int = ...
    unicode_list: int = ...
    """if(type == LV_FONT_FMT_TXT_CMAP_FORMAT0_...) it's"""
    glyph_id_ofs_list: None = ...
    """Length of"""
    list_length: int = ...
    type: "draw_mask_type_t" = ...

    class SUBPX:
        """
        The bitmaps might be upscaled by 3 to achieve subpixel rendering.
        """
        NONE: int = 0
        HOR: int = 1
        VER: int = 2
        BOTH: int = 3

    class FONT_FMT_TXT_CMAP:
        """
        Format of font character map.
        """
        FORMAT0_FULL: int = 0
        SPARSE_FULL: int = 1
        FORMAT0_TINY: int = 2
        SPARSE_TINY: int = 3

    class FONT_FMT_TXT:
        """
        Bitmap formats
        """
        PLAIN: int = 0
        COMPRESSED: int = 1
        COMPRESSED_NO_PREFILTER: int = 1

    def __init__(self, fields: Optional[_type_font_fmt_txt_cmap_t] = {}, /):
        ...


class _type_font_fmt_txt_dsc_t(TypedDict):
    glyph_bitmap: NotRequired[int]
    glyph_dsc: NotRequired["font_fmt_txt_glyph_dsc_t"]
    cmaps: NotRequired["font_fmt_txt_cmap_t"]
    kern_dsc: NotRequired[None]
    kern_scale: NotRequired[int]
    cmap_num: NotRequired[int]
    bpp: NotRequired[int]
    kern_classes: NotRequired[bool]
    bitmap_format: NotRequired[int]
    cache: NotRequired["font_fmt_txt_glyph_cache_t"]


class font_fmt_txt_dsc_t(object):
    glyph_bitmap: int = ...
    glyph_dsc: "font_fmt_txt_glyph_dsc_t" = ...
    cmaps: "font_fmt_txt_cmap_t" = ...
    """Store kerning values. Can be"""
    kern_dsc: None = ...
    kern_scale: int = ...
    cmap_num: int = ...
    bpp: int = ...
    kern_classes: bool = ...
    bitmap_format: int = ...
    cache: "font_fmt_txt_glyph_cache_t" = ...

    def __init__(self, fields: Optional[_type_font_fmt_txt_dsc_t] = {}, /):
        ...


class _type_font_fmt_txt_glyph_cache_t(TypedDict):
    last_letter: NotRequired[int]
    last_glyph_id: NotRequired[int]


class font_fmt_txt_glyph_cache_t(object):
    last_letter: int = ...
    last_glyph_id: int = ...

    def __init__(
            self, fields: Optional[_type_font_fmt_txt_glyph_cache_t] = {}, /
    ):
        ...


class _type_font_fmt_txt_glyph_dsc_t(TypedDict):
    bitmap_index: NotRequired[int]
    adv_w: NotRequired[int]
    box_w: NotRequired[int]
    box_h: NotRequired[int]
    ofs_x: NotRequired["coord_t"]
    ofs_y: NotRequired["coord_t"]


class font_fmt_txt_glyph_dsc_t(object):
    """
    This describes a glyph.
    """

    """Start index of the bitmap. A font can be max 1 MB."""
    bitmap_index: int = ...
    """
    Draw the next glyph after this width. 8.4 format 
    (real_value * 16 is stored).
    """
    adv_w: int = ...
    """Width of the glyph's bounding box"""
    box_w: int = ...
    """Height of the glyph's bounding box"""
    box_h: int = ...
    ofs_x: "coord_t" = ...
    ofs_y: "coord_t" = ...

    def __init__(
            self,
            fields: Optional[_type_font_fmt_txt_glyph_dsc_t] = {},
            /
    ):
        ...


class _type_font_fmt_txt_kern_classes_t(TypedDict):
    class_pair_values: NotRequired[int]
    left_class_mapping: NotRequired[int]
    right_class_mapping: NotRequired[int]
    left_class_cnt: NotRequired[int]
    right_class_cnt: NotRequired[int]


class font_fmt_txt_kern_classes_t(object):
    """
    More complex but more optimal class based kern value storage
    """
    class_pair_values: int = ...
    left_class_mapping: int = ...
    right_class_mapping: int = ...
    left_class_cnt: int = ...
    right_class_cnt: int = ...

    def __init__(
            self, fields: Optional[_type_font_fmt_txt_kern_classes_t] = {}, /
    ):
        ...


class _type_font_fmt_txt_kern_pair_t(TypedDict):
    glyph_ids: NotRequired[None]
    values: NotRequired[int]
    pair_cnt: NotRequired[int]
    glyph_ids_size: NotRequired[int]


class font_fmt_txt_kern_pair_t(object):
    """
    A simple mapping of kern values from pairs
    """

    glyph_ids: None = ...
    values: int = ...
    pair_cnt: int = ...
    glyph_ids_size: int = ...

    def __init__(
            self, fields: Optional[_type_font_fmt_txt_kern_pair_t] = {}, /
    ):
        ...


class _type_font_glyph_dsc_t(TypedDict):
    resolved_font: NotRequired["font_t"]
    adv_w: NotRequired[int]
    box_w: NotRequired[int]
    box_h: NotRequired[int]
    ofs_x: NotRequired["coord_t"]
    ofs_y: NotRequired["coord_t"]
    bpp: NotRequired[int]
    is_placeholder: NotRequired[bool]


class font_glyph_dsc_t(object):
    """
    Describes the properties of a glyph.
    """

    """
    Pointer to a font where the glyph was actually
     found after handling fallbacks
     """
    resolved_font: "font_t" = ...
    """
    Draw the next glyph after this width. 
    8.4 format (real_value * 16 is stored).
    """
    adv_w: int = ...
    """Width of the glyph's bounding box"""
    box_w: int = ...
    """Height of the glyph's bounding box"""
    box_h: int = ...
    ofs_x: "coord_t" = ...
    ofs_y: "coord_t" = ...
    bpp: int = ...
    is_placeholder: bool = ...

    def __init__(self, fields: Optional[_type_font_glyph_dsc_t] = {}, /):
        ...


class _type_fs_dir_t(TypedDict):
    dir_d: NotRequired[None]
    drv: NotRequired["fs_drv_t"]


class fs_dir_t(object):
    dir_d: None = ...
    drv: "fs_drv_t" = ...

    class RES:
        """
        Errors in the file system module.
        """
        OK: int = 0
        HW_ERR: int = 1
        FS_ERR: int = 2
        NOT_EX: int = 3
        FULL: int = 4
        LOCKED: int = 5
        DENIED: int = 6
        BUSY: int = 7
        TOUT: int = 8
        NOT_IMP: int = 9
        OUT_OF_MEM: int = 10
        INV_PARAM: int = 11
        UNKNOWN: int = 12

    class MODE:
        """
        File open mode.
        """
        WR: int = 0x01
        RD: int = 0x02

    class SEEK:
        """
        Seek modes.
        """
        SET: int = 0x00
        CUR: int = 0x01
        END: int = 0x02

    def __init__(self, fields: Optional[_type_fs_dir_t] = {}, /):
        ...

    def open(self, path: str, /) -> "fs_res_t":
        """
        Initialize a 'fs_dir_t' variable for directory reading

        :param path:
        :type path: str

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum
        :retval: "fs_res_t"
        """
        ...

    def read(self, fn: int, /) -> "fs_res_t":
        """
        Read the next filename form a directory.
        The name of the directories will begin with '/'

        :param fn:
        :type fn: int

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum
        :retval: "fs_res_t"
        """
        ...

    def close(self) -> "fs_res_t":
        """
        Close the directory reading

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum
        :retval: "fs_res_t"
        """
        ...


class _type_fs_file_cache_t(TypedDict):
    start: NotRequired[int]
    end: NotRequired[int]
    file_position: NotRequired[int]
    buffer: NotRequired[None]


class fs_file_cache_t(object):
    start: int = ...
    end: int = ...
    file_position: int = ...
    buffer: None = ...

    def __init__(self, fields: Optional[_type_fs_file_cache_t] = {}, /):
        ...


class _type_fs_file_t(TypedDict):
    file_d: NotRequired[None]
    drv: NotRequired["fs_drv_t"]
    cache: NotRequired["font_fmt_txt_glyph_cache_t"]


class fs_file_t(object):
    file_d: None = ...
    drv: "fs_drv_t" = ...
    cache: "font_fmt_txt_glyph_cache_t" = ...

    def __init__(self, fields: Optional[_type_fs_file_t] = {}, /):
        ...

    def open(self, path: str, mode: "fs_mode_t", /) -> "fs_res_t":
        """
        Open a file

        :param path:
        :type path: str

        :param mode:
        :type mode: "fs_mode_t"

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum
        :retval: "fs_res_t"
        """
        ...

    def close(self) -> "fs_res_t":
        """
        Close an already opened file

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum
        :retval: "fs_res_t"
        """
        ...

    def read(self, buf, btr: int, br: int, /) -> "fs_res_t":
        """
        Read from a file

        :param buf:
        :type buf: None

        :param btr:
        :type btr: int

        :param br:
        :type br: int

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum
        :retval: "fs_res_t"
        """
        ...

    def write(self, buf, btw: int, bw: int, /) -> "fs_res_t":
        """
        Write into a file

        :param buf:
        :type buf: None

        :param btw:
        :type btw: int

        :param bw:
        :type bw: int

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum
        :retval: "fs_res_t"
        """
        ...

    def seek(self, pos: int, whence: "fs_whence_t", /) -> "fs_res_t":
        """
        Set the position of the 'cursor' (read write pointer) in a file

        :param pos:
        :type pos: int

        :param whence:
        :type whence: "fs_whence_t"

        :returns: LV_FS_RES_OK or any error from lv_fs_res_t enum
        :retval: "fs_res_t"
        """
        ...

    def tell(self, pos: int, /) -> "fs_res_t":
        """
        Give the position of the read write pointer

        :param pos:
        :type pos: int

        :returns: LV_FS_RES_OK or any error from 'fs_res_t'
        :retval: "fs_res_t"
        """
        ...


class _type_grad_dsc_t(TypedDict):
    stops: NotRequired["gradient_stop_t"]
    stops_count: NotRequired[int]
    dir: NotRequired["dir_t"]
    dither: NotRequired["dither_mode_t"]


class grad_dsc_t(object):
    """
    A descriptor of a gradient.
    """

    """A gradient stop array"""
    stops: "gradient_stop_t" = ...
    """The number of used stops in the array"""
    stops_count: int = ...
    dir: "dir_t" = ...
    """
    Whether to dither the gradient or not. 
    Any of LV_DITHER_NONE, LV_DITHER_ORDERED, LV_DITHER_ERR_DIFF
    """
    dither: "dither_mode_t" = ...

    def __init__(self, fields: Optional[_type_grad_dsc_t] = {}, /):
        ...


class _type_gradient_stop_t(TypedDict):
    color: NotRequired["color_t"]
    frac: NotRequired[int]


class gradient_stop_t(object):
    """
    A gradient stop definition.
    This matches a color and a position in a virtual 0-255 scale.
    """

    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    """The stop position in 1/255 unit"""
    frac: int = ...

    def __init__(self, fields: Optional[_type_gradient_stop_t] = {}, /):
        ...


class _type_hit_test_info_t(TypedDict):
    point: NotRequired["point_t"]
    res: NotRequired["cover_res_t"]


class hit_test_info_t(object):
    """
    Used as the event parameter of
    """
    """A point relative to screen to check if it can click the object or not"""
    point: "point_t" = ...
    res: "cover_res_t" = ...

    def __init__(self, fields: Optional[_type_hit_test_info_t] = {}, /):
        ...


class _type_img_cache_manager_t(TypedDict):
    open_cb: NotRequired[Callable[[Any, "color_t", int], "img_cache_entry_t"]]


class img_cache_manager_t(object):
    open_cb: Callable[[Any, "color_t", int], "img_cache_entry_t"]

    class SRC:
        """
        Source of image.
        """
        VARIABLE: int = 0
        FILE: int = 1
        SYMBOL: int = 2
        UNKNOWN: int = 3

    class SIZE_MODE:
        """
        Image size mode, when image size and object size is different
        """
        VIRTUAL: int = 0
        REAL: int = 1

    def __init__(self, fields: Optional[_type_img_cache_manager_t] = {}, /):
        ...

    def init(self) -> None:
        """
        Initialize the img cache manager

        :returns:
        :retval: None
        """
        ...

    def apply(self) -> None:
        """
        Apply the img cache manager

        :returns:
        :retval: None
        """
        ...

    def set_src(self, src, /) -> None:
        """
        Set the image data to display on the object

        :param src:
        :type src: None

        :returns:
        :retval: None
        """
        ...

    def set_offset_x(self, x: "coord_t", /) -> None:
        """
        Set an offset for the source of an image so the
        image will be displayed from the new origin.

        :param x:
        :type x: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_offset_y(self, y: "coord_t", /) -> None:
        """
        Set an offset for the source of an image. so
        the image will be displayed from the new origin.

        :param y:
        :type y: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_angle(self, angle: int, /) -> None:
        """
        Set the rotation angle of the image. The image
        will be rotated around the set pivot set by

        :param angle:
        :type angle: int

        :returns:
        :retval: None
        """
        ...

    def set_pivot(self, x: "coord_t", y: "coord_t", /) -> None:
        """
        Set the rotation center of the image. The
        image will be rotated around this point.

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_zoom(self, zoom: int, /) -> None:
        """
        :param zoom:
        :type zoom: int

        :returns:
        :retval: None
        """
        ...

    def set_antialias(self, antialias: bool, /) -> None:
        """
        Enable/disable anti-aliasing for the transformations
        (rotate, zoom) or not. The quality is better with
        anti-aliasing looks better but slower.

        :param antialias:
        :type antialias: bool

        :returns:
        :retval: None
        """
        ...

    def set_size_mode(self, mode: "img_size_mode_t", /) -> None:
        """
        Set the image object size mode.

        :param mode:
        :type mode: "img_size_mode_t"

        :returns:
        :retval: None
        """
        ...

    def get_src(self) -> None:
        """
        Get the source of the image

        :returns: the image source
            (symbol, file name or ::lv-img_dsc_t for C arrays)
        :retval: None
        """
        ...

    def get_offset_x(self) -> "coord_t":
        """
        Get the offset's x attribute of the image object.

        :returns: offset X value.
        :retval: "coord_t"
        """
        ...

    def get_offset_y(self) -> "coord_t":
        """
        Get the offset's y attribute of the image object.

        :returns: offset Y value.
        :retval: "coord_t"
        """
        ...

    def get_angle(self) -> int:
        """
        Get the rotation angle of the image.

        :returns: rotation angle in 0.1 degrees (0..3600)
        :retval: int
        """
        ...

    def get_pivot(self, pivot: "point_t", /) -> None:
        """
        Get the pivot (rotation center) of the image.

        :param pivot:
        :type pivot: "point_t"

        :returns:
        :retval: None
        """
        ...

    def get_zoom(self) -> int:
        """
        Get the zoom factor of the image.

        :returns: zoom factor (256: no zoom)
        :retval: int
        """
        ...

    def get_antialias(self) -> bool:
        """
        Get whether the transformations (rotate, zoom) are anti-aliased or not

        :returns: true: anti-aliased; false: not anti-aliased
        :retval: bool
        """
        ...

    def get_size_mode(self) -> "img_size_mode_t":
        """
        Get the size mode of the image

        :returns: element of
        :retval: "img_size_mode_t"
        """
        ...


class _type_img_dsc_t(TypedDict):
    header: NotRequired["img_header_t"]
    data_size: NotRequired[int]
    data: NotRequired[int]


class img_dsc_t(object):
    """
    Image header it is compatible with the result from image converter utility
    """

    """Info about the opened image: color format, size, etc. MUST be set in"""
    header: "img_header_t" = ...
    """Size of the image in bytes"""
    data_size: int = ...
    """Pointer to the data of the image"""
    data: int = ...

    def __init__(self, fields: Optional[_type_img_dsc_t] = {}, /):
        ...

    def buf_set_palette(self, id: int, c: "color32_t", /) -> None:
        """
        Set the palette color of an indexed image. Valid only for

        :param id:
        :type id: int

        :param c:
        :type c: "color32_t"

        :returns:
        :retval: None
        """
        ...

    def buf_free(self) -> None:
        """
        Free an allocated image buffer

        :returns:
        :retval: None
        """
        ...


class _type_img_header_t(TypedDict):
    cf: NotRequired[int]
    always_zero: NotRequired[int]
    reserved: NotRequired[bool]
    chroma_keyed: NotRequired[bool]
    w: NotRequired[int]
    h: NotRequired[int]


class img_header_t(object):
    """
    The first 8 bit is very important to distinguish
    the different source types. For more info see
    """
    cf: int = ...
    always_zero: int = ...
    reserved: bool = ...
    chroma_keyed: bool = ...
    w: int = ...
    h: int = ...

    def __init__(self, fields: Optional[_type_img_header_t] = {}, /):
        ...


class _type_img_t(TypedDict):
    obj: NotRequired["obj_t"]
    src: NotRequired[None]
    offset: NotRequired["point_t"]
    w: NotRequired[int]
    h: NotRequired[int]
    angle: NotRequired[int]
    pivot: NotRequired["point_t"]
    zoom: NotRequired[int]
    src_type: NotRequired["img_src_t"]
    cf: NotRequired[int]
    antialias: NotRequired[bool]
    obj_size_mode: NotRequired[int]


class img_t(object):
    """
    Data of image
    """
    obj: "obj_t" = ...
    """The image source. A file path like "S:my_img.png" or pointer to an"""
    src: None = ...
    offset: "point_t" = ...
    w: int = ...
    h: int = ...
    angle: int = ...
    pivot: "point_t" = ...
    zoom: int = ...
    """Type of the source: file or variable. Can be set in"""
    src_type: "img_src_t" = ...
    cf: int = ...
    antialias: bool = ...
    obj_size_mode: int = ...

    def __init__(self, fields: Optional[_type_img_t] = {}, /):
        ...


class _type_imgbtn_src_info_t(TypedDict):
    img_src: NotRequired[None]
    header: NotRequired["img_header_t"]


class imgbtn_src_info_t(object):
    img_src: None = ...
    """Info about the opened image: color format, size, etc. MUST be set in"""
    header: "img_header_t" = ...

    class STATE:
        RELEASED: int = 0
        PRESSED: int = 1
        DISABLED: int = 2
        CHECKED_RELEASED: int = 3
        CHECKED_PRESSED: int = 4
        CHECKED_DISABLED: int = 5

    def __init__(self, fields: Optional[_type_imgbtn_src_info_t] = {}, /):
        ...

    def set_src(
            self, state: "imgbtn_state_t", src_left, src_mid, src_right, /
    ) -> None:
        """
        Set images for a state of the image button

        :param state:
        :type state: "imgbtn_state_t"

        :param src_left:
        :type src_left: None

        :param src_mid:
        :type src_mid: None

        :param src_right:
        :type src_right: None

        :returns:
        :retval: None
        """
        ...

    def set_state(self, state: "imgbtn_state_t", /) -> None:
        """
        Use this function instead of

        :param state:
        :type state: "imgbtn_state_t"

        :returns:
        :retval: None
        """
        ...

    def get_src_left(self, state: "imgbtn_state_t", /) -> None:
        """
        Get the left image in a given state

        :param state:
        :type state: "imgbtn_state_t"

        :returns: pointer to the left image source (a C array or path to a file)
        :retval: None
        """
        ...

    def get_src_middle(self, state: "imgbtn_state_t", /) -> None:
        """
        Get the middle image in a given state

        :param state:
        :type state: "imgbtn_state_t"

        :returns: pointer to the middle image source
            (a C array or path to a file)
        :retval: None
        """
        ...

    def get_src_right(self, state: "imgbtn_state_t", /) -> None:
        """
        Get the right image in a given state

        :param state:
        :type state: "imgbtn_state_t"

        :returns: pointer to the left image source (a C array or path to a file)
        :retval: None
        """
        ...


class _type_imgbtn_t(TypedDict):
    obj: NotRequired["obj_t"]
    src_mid: NotRequired["imgbtn_src_info_t"]
    src_left: NotRequired["imgbtn_src_info_t"]
    src_right: NotRequired["imgbtn_src_info_t"]


class imgbtn_t(object):
    obj: "obj_t" = ...
    src_mid: "imgbtn_src_info_t" = ...
    src_left: "imgbtn_src_info_t" = ...
    src_right: "imgbtn_src_info_t" = ...

    def __init__(self, fields: Optional[_type_imgbtn_t] = {}, /):
        ...


class _type_indev_data_t(TypedDict):
    point: NotRequired["point_t"]
    key: NotRequired[int]
    btn_id: NotRequired[int]
    enc_diff: NotRequired[int]
    state: NotRequired["indev_state_t"]
    continue_reading: NotRequired[bool]


class indev_data_t(object):
    """
    Data structure passed to an input driver to fill
    """

    """A point relative to screen to check if it can click the object or not"""
    point: "point_t" = ...
    """
    A discriminating key that's built from the drawing operation. 
    If the key does not match, the cache item is not used
    """
    key: int = ...
    """For LV_INDEV_TYPE_BUTTON the currently pressed button"""
    btn_id: int = ...
    """For LV_INDEV_TYPE_ENCODER number of steps since the previous read"""
    enc_diff: int = ...
    """Current state of the input device."""
    state: "indev_state_t" = ...
    """If set to true, the read callback is invoked again"""
    continue_reading: bool = ...


    def __init__(self, fields: Optional[_type_indev_data_t] = {}, /):
        ...

    def search_obj(self, point: "point_t", /) -> "obj_t":
        """
        Search the most top, clickable object by a point

        :param point:
        :type point: "point_t"

        :returns: pointer to the found object or NULL if
            there was no suitable object
        :retval: "obj_t"
        """
        ...

    def scroll_get_snap_dist(self, p: "point_t", /) -> None:
        """
        Get the distance of the nearest snap point

        :param p:
        :type p: "point_t"

        :returns:
        :retval: None
        """
        ...


class _type_keyboard_t(TypedDict):
    btnm: NotRequired["obj_t"]
    ta: NotRequired["obj_t"]
    mode: NotRequired["bar_mode_t"]
    popovers: NotRequired[bool]


class keyboard_t(object):
    btnm: "obj_t" = ...
    ta: "obj_t" = ...
    """Type of bar"""
    mode: "bar_mode_t" = ...
    popovers: bool = ...

    class MODE:
        """
        Current keyboard mode.
        """
        TEXT_LOWER: int = 0
        TEXT_UPPER: int = 1
        SPECIAL: int = 2
        NUMBER: int = 3
        USER_1: int = 4
        USER_2: int = 5
        USER_3: int = 6
        USER_4: int = 7

    def __init__(self, fields: Optional[_type_keyboard_t] = {}, /):
        ...

    def set_textarea(self, ta: "obj_t", /) -> None:
        """
        Assign a Text Area to the Keyboard.
        The pressed characters will be put there.

        :param ta:
        :type ta: "obj_t"

        :returns:
        :retval: None
        """
        ...

    def set_mode(self, mode: "keyboard_mode_t", /) -> None:
        """
        Set a new a mode (text or number map)

        :param mode:
        :type mode: "keyboard_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_popovers(self, en: bool, /) -> None:
        """
        Show the button title in a popover when pressed.

        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def set_map(
            self, mode: "keyboard_mode_t", map: Callable[["[]"], str],
            ctrl_map: Callable[["[]"], "btnmatrix_ctrl_t"], /
    ) -> None:
        """
        Set a new map for the keyboard

        :param mode:
        :type mode: "keyboard_mode_t"

        :param map:
        :type map: Callable[["[]"], str]

        :param ctrl_map:
        :type ctrl_map: Callable[["[]"], "btnmatrix_ctrl_t"]

        :returns:
        :retval: None
        """
        ...

    def get_textarea(self) -> "obj_t":
        """
        Assign a Text Area to the Keyboard.
        The pressed characters will be put there.

        :returns: pointer to the assigned Text Area object
        :retval: "obj_t"
        """
        ...

    def get_mode(self) -> "keyboard_mode_t":
        """
        Set a new a mode (text or number map)

        :returns: the current mode from 'lv_keyboard_mode_t'
        :retval: "keyboard_mode_t"
        """
        ...

    def get_map_array(self) -> str:
        """
        Get the current map of a keyboard

        :returns: the current map
        :retval: str
        """
        ...

    def get_selected_btn(self) -> int:
        """
        Get the index of the lastly "activated" button by the user
        (pressed, released, focused etc) Useful in the

        :returns:
        :retval: int
        """
        ...

    def get_btn_text(self, btn_id: int, /) -> str:
        """
        Get the button's text

        :param btn_id:
        :type btn_id: int

        :returns: text of btn_index` button
        :retval: str
        """
        ...


class _type_label_t(TypedDict):
    obj: NotRequired["obj_t"]
    text: NotRequired[str]
    tmp_ptr: NotRequired[int]
    tmp: NotRequired[int]
    dot: NotRequired["label_t"]
    dot_end: NotRequired[int]
    hint: NotRequired["draw_label_hint_t"]
    sel_start: NotRequired[int]
    sel_end: NotRequired[int]
    size_cache: NotRequired["point_t"]
    offset: NotRequired["point_t"]
    long_mode: NotRequired["label_long_mode_t"]
    static_txt: NotRequired[bool]
    recolor: NotRequired[bool]
    expand: NotRequired[bool]
    dot_tmp_alloc: NotRequired[bool]
    invalid_size_cache: NotRequired[bool]


class label_t(object):
    obj: "obj_t" = ...
    """Text to display on the dropdown's button"""
    text: str = ...
    tmp_ptr: int = ...
    tmp: int = ...
    dot: "label_t" = ...
    dot_end: int = ...
    hint: "draw_label_hint_t" = ...
    sel_start: int = ...
    sel_end: int = ...
    size_cache: "point_t" = ...
    offset: "point_t" = ...
    long_mode: "label_long_mode_t" = ...
    static_txt: bool = ...
    recolor: bool = ...
    expand: bool = ...
    dot_tmp_alloc: bool = ...
    invalid_size_cache: bool = ...

    class LONG:
        """
        Long mode behaviors. Used in 'lv_label_ext_t'
        """
        WRAP: int = 0
        DOT: int = 1
        SCROLL: int = 2
        SCROLL_CIRCULAR: int = 3
        CLIP: int = 4

    def __init__(self, fields: Optional[_type_label_t] = {}, /):
        ...

    def set_text(self, text: str, /) -> None:
        """
        Set a new text for a label.
        Memory will be allocated to store the text by the label.

        :param text:
        :type text: str

        :returns:
        :retval: None
        """
        ...

    def set_text_fmt(self, fmt: str, /) -> None:
        """
        :param fmt:
        :type fmt: str

        :returns:
        :retval: None
        """
        ...

    def set_text_static(self, text: str, /) -> None:
        """
        Set a static text. It will not be saved by the label
        so the 'text' variable has to be 'alive' while the label exists.

        :param text:
        :type text: str

        :returns:
        :retval: None
        """
        ...

    def set_long_mode(self, long_mode: "label_long_mode_t", /) -> None:
        """
        Set the behavior of the label with text longer than the object size

        :param long_mode:
        :type long_mode: "label_long_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_recolor(self, en: bool, /) -> None:
        """
        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def set_text_selection_start(self, index: int, /) -> None:
        """
        Set where text selection should start

        :param index:
        :type index: int

        :returns:
        :retval: None
        """
        ...

    def set_text_selection_end(self, index: int, /) -> None:
        """
        Set where text selection should end

        :param index:
        :type index: int

        :returns:
        :retval: None
        """
        ...

    def get_text(self) -> int:
        """
        Get the text of a label

        :returns: the text of the label
        :retval: int
        """
        ...

    def get_long_mode(self) -> "label_long_mode_t":
        """
        Get the long mode of a label

        :returns: the current long mode
        :retval: "label_long_mode_t"
        """
        ...

    def get_recolor(self) -> bool:
        """
        Get the recoloring attribute

        :returns: true: recoloring is enabled, false: disable
        :retval: bool
        """
        ...

    def get_letter_pos(self, char_id: int, pos: "point_t", /) -> None:
        """
        Get the relative x and y coordinates of a letter

        :param char_id:
        :type char_id: int

        :param pos:
        :type pos: "point_t"

        :returns:
        :retval: None
        """
        ...

    def get_letter_on(self, pos_in: "point_t", /) -> int:
        """
        Get the index of letter on a relative point of a label.

        :param pos_in:
        :type pos_in: "point_t"

        :returns: The index of the letter on the 'pos_p'
            point (E.g. on 0;0 is the 0. letter if aligned to the left)
            Expressed in character index and not byte index (different in UTF-8)
        :retval: int
        """
        ...

    def is_char_under_pos(self, pos: "point_t", /) -> bool:
        """
        Check if a character is drawn under a point.

        :param pos:
        :type pos: "point_t"

        :returns: whether a character is drawn under the point
        :retval: bool
        """
        ...

    def get_text_selection_start(self) -> int:
        """
        :returns: selection start index.
        :retval: int
        """
        ...

    def get_text_selection_end(self) -> int:
        """
        :returns: selection end index.
        :retval: int
        """
        ...

    def ins_text(self, pos: int, txt: str, /) -> None:
        """
        Insert a text to a label. The label text can not be static.

        :param pos:
        :type pos: int

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def cut_text(self, pos: int, cnt: int, /) -> None:
        """
        Delete characters from a label. The label text can not be static.

        :param pos:
        :type pos: int

        :param cnt:
        :type cnt: int

        :returns:
        :retval: None
        """
        ...


class _type_layout_dsc_t(TypedDict):
    cb: NotRequired["draw_mask_xcb_t"]
    user_data: NotRequired[None]


class layout_dsc_t(object):
    cb: "draw_mask_xcb_t" = ...
    """Custom user data"""
    user_data: None = ...

    def __init__(self, fields: Optional[_type_layout_dsc_t] = {}, /):
        ...


class _type_led_t(TypedDict):
    obj: NotRequired["obj_t"]
    color: NotRequired["color_t"]
    bright: NotRequired[int]


class led_t(object):
    obj: "obj_t" = ...
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    """Current brightness of the LED (0..255)"""
    bright: int = ...

    class DRAW_PART_RECTANGLE:
        LED_DRAW_PART_RECTANGLE: int = 0

    def __init__(self, fields: Optional[_type_led_t] = {}, /):
        ...

    def set_color(self, color: "color_t", /) -> None:
        """
        Set the color of the LED

        :param color:
        :type color: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_brightness(self, bright: int, /) -> None:
        """
        Set the brightness of a LED object

        :param bright:
        :type bright: int

        :returns:
        :retval: None
        """
        ...

    def on(self) -> None:
        """
        Light on a LED

        :returns:
        :retval: None
        """
        ...

    def off(self) -> None:
        """
        Light off a LED

        :returns:
        :retval: None
        """
        ...

    def toggle(self) -> None:
        """
        Toggle the state of a LED

        :returns:
        :retval: None
        """
        ...

    def get_brightness(self) -> int:
        """
        Get the brightness of a LEd object

        :returns: bright 0 (max. dark) ... 255 (max. light)
        :retval: int
        """
        ...


class _type_line_t(TypedDict):
    obj: NotRequired["obj_t"]
    point_array: NotRequired["point_t"]
    point_num: NotRequired[int]
    y_inv: NotRequired[bool]


class line_t(object):
    obj: "obj_t" = ...
    """Pointer to an array with the points of the line"""
    point_array: "point_t" = ...
    """Number of points in 'point_array'"""
    point_num: int = ...
    """1: y == 0 will be on the bottom"""
    y_inv: bool = ...

    def __init__(self, fields: Optional[_type_line_t] = {}, /):
        ...

    def set_points(
            self, points: Callable[["[]"], "point_t"],
            point_num: int, /
    ) -> None:
        """
        Set an array of points. The line object will connect these points.

        :param points:
        :type points: Callable[["[]"], "point_t"]

        :param point_num:
        :type point_num: int

        :returns:
        :retval: None
        """
        ...

    def set_y_invert(self, en: bool, /) -> None:
        """
        Enable (or disable) the y coordinate inversion.
        If enabled then y will be subtracted from the height of the object,
        therefore the y = 0 coordinate will be on the bottom.

        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def get_y_invert(self) -> bool:
        """
        Get the y inversion attribute

        :returns: true: y inversion is enabled, false: disabled
        :retval: bool
        """
        ...


class _type_ll_t(TypedDict):
    n_size: NotRequired[int]
    head: NotRequired["ll_node_t"]
    tail: NotRequired["ll_node_t"]


class ll_t(object):
    """
    Description of a linked list
    """
    n_size: int = ...
    head: "ll_node_t" = ...
    tail: "ll_node_t" = ...

    def __init__(self, fields: Optional[_type_ll_t] = {}, /):
        ...


class _type_lru_t(TypedDict):
    items: NotRequired["lru_item_t"]
    access_count: NotRequired[int]
    free_memory: NotRequired[int]
    total_memory: NotRequired[int]
    average_item_length: NotRequired[int]
    hash_table_size: NotRequired[int]
    seed: NotRequired[int]
    value_free: NotRequired["lru_free_t"]
    key_free: NotRequired["lru_free_t"]
    free_items: NotRequired["lru_item_t"]


class lru_t(object):
    items: "lru_item_t" = ...
    access_count: int = ...
    free_memory: int = ...
    total_memory: int = ...
    average_item_length: int = ...
    hash_table_size: int = ...
    seed: int = ...
    value_free: "lru_free_t" = ...
    key_free: "lru_free_t" = ...
    free_items: "lru_item_t" = ...

    class LRU:
        OK: int = 0
        MISSING_CACHE: int = 1
        MISSING_KEY: int = 2
        MISSING_VALUE: int = 3
        LOCK_ERROR: int = 4
        VALUE_TOO_LARGE: int = 5

    def __init__(self, fields: Optional[_type_lru_t] = {}, /):
        ...

    def _del(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...

    def set(
            self, key, key_length: int, value, value_length: int, /
    ) -> "lru_res_t":
        """
        :param key:
        :type key: None

        :param key_length:
        :type key_length: int

        :param value:
        :type value: None

        :param value_length:
        :type value_length: int

        :returns:
        :retval: "lru_res_t"
        """
        ...

    def get(self, key, key_size: int, value, /) -> "lru_res_t":
        """
        :param key:
        :type key: None

        :param key_size:
        :type key_size: int

        :param value:
        :type value: None

        :returns:
        :retval: "lru_res_t"
        """
        ...

    def remove(self, key, key_size: int, /) -> "lru_res_t":
        """
        :param key:
        :type key: None

        :param key_size:
        :type key_size: int

        :returns:
        :retval: "lru_res_t"
        """
        ...

    def remove_item(self) -> None:
        """
        remove the least recently used item

        :returns:
        :retval: None
        """
        ...


class _type_mem_monitor_t(TypedDict):
    total_size: NotRequired[int]
    free_cnt: NotRequired[int]
    free_size: NotRequired[int]
    free_biggest_size: NotRequired[int]
    used_cnt: NotRequired[int]
    max_used: NotRequired[int]
    used_pct: NotRequired[int]
    frag_pct: NotRequired[int]


class mem_monitor_t(object):
    """
    Heap information structure.
    """

    """Total heap size"""
    total_size: int = ...
    free_cnt: int = ...
    """Size of available memory"""
    free_size: int = ...
    free_biggest_size: int = ...
    used_cnt: int = ...
    """Max size of Heap memory used"""
    max_used: int = ...
    """Percentage used"""
    used_pct: int = ...
    """Amount of fragmentation"""
    frag_pct: int = ...

    def __init__(self, fields: Optional[_type_mem_monitor_t] = {}, /):
        ...

    def builtin(self) -> None:
        """
        Give information about the work memory of dynamic allocation

        :returns:
        :retval: None
        """
        ...

    def mem_monitor(self) -> None:
        """
        Give information about the work memory of dynamic allocation

        :returns:
        :retval: None
        """
        ...


class _type_menu_history_t(TypedDict):
    page: NotRequired["obj_t"]


# noinspection PyShadowingNames
class menu_history_t(object):
    page: "obj_t" = ...

    class HEADER:
        TOP_FIXED: int = 0
        TOP_UNFIXED: int = 1
        BOTTOM_FIXED: int = 2

    class ROOT_BACK_BTN:
        DISABLED: int = 0
        ENABLED: int = 1

    def __init__(self, fields: Optional[_type_menu_history_t] = {}, /):
        ...

    def set_page(self, page: "obj_t", /) -> None:
        """
        Set menu page to display in main

        :param page:
        :type page: "obj_t"

        :returns:
        :retval: None
        """
        ...

    def set_page_title(self, title: str, /) -> None:
        """
        Set menu page title

        :param title:
        :type title: str

        :returns:
        :retval: None
        """
        ...

    def set_page_title_static(self, title: str, /) -> None:
        """
        Set menu page title with a static text. It will not be saved by the
        label so the 'text' variable has to be 'alive' while the page exists.

        :param title:
        :type title: str

        :returns:
        :retval: None
        """
        ...

    def set_sidebar_page(self, page: "obj_t", /) -> None:
        """
        Set menu page to display in sidebar

        :param page:
        :type page: "obj_t"

        :returns:
        :retval: None
        """
        ...

    def set_mode_header(self, mode_header: "menu_mode_header_t", /) -> None:
        """
        Set the how the header should behave and its position

        :param mode_header:
        :type mode_header: "menu_mode_header_t"

        :returns:
        :retval: None
        """
        ...

    def set_mode_root_back_btn(
            self, mode_root_back_btn: "menu_mode_root_back_btn_t", /
    ) -> None:
        """
        Set whether back button should appear at root

        :param mode_root_back_btn:
        :type mode_root_back_btn: "menu_mode_root_back_btn_t"

        :returns:
        :retval: None
        """
        ...

    def set_load_page_event(self, obj: "obj_t", page: "obj_t", /) -> None:
        """
        Add menu to the menu item

        :param obj:
        :type obj: "obj_t"

        :param page:
        :type page: "obj_t"

        :returns:
        :retval: None
        """
        ...

    def get_cur_main_page(self) -> "obj_t":
        """
        Get a pointer to menu page that is currently displayed in main

        :returns: pointer to current page
        :retval: "obj_t"
        """
        ...

    def get_cur_sidebar_page(self) -> "obj_t":
        """
        Get a pointer to menu page that is currently displayed in sidebar

        :returns: pointer to current page
        :retval: "obj_t"
        """
        ...

    def get_main_header(self) -> "obj_t":
        """
        Get a pointer to main header obj

        :returns: pointer to main header obj
        :retval: "obj_t"
        """
        ...

    def get_main_header_back_btn(self) -> "obj_t":
        """
        Get a pointer to main header back btn obj

        :returns: pointer to main header back btn obj
        :retval: "obj_t"
        """
        ...

    def get_sidebar_header(self) -> "obj_t":
        """
        Get a pointer to sidebar header obj

        :returns: pointer to sidebar header obj
        :retval: "obj_t"
        """
        ...

    def get_sidebar_header_back_btn(self) -> "obj_t":
        """
        Get a pointer to sidebar header obj

        :returns: pointer to sidebar header back btn obj
        :retval: "obj_t"
        """
        ...

    def back_btn_is_root(self, obj: "obj_t", /) -> bool:
        """
        Check if an obj is a root back btn

        :param obj:
        :type obj: "obj_t"

        :returns: true if it is a root back btn
        :retval: bool
        """
        ...

    def clear_history(self) -> None:
        """
        Clear menu history

        :returns:
        :retval: None
        """
        ...


class _type_menu_load_page_event_data_t(TypedDict):
    menu: NotRequired["obj_t"]
    page: NotRequired["obj_t"]


class menu_load_page_event_data_t(object):
    menu: "obj_t" = ...
    page: "obj_t" = ...

    def __init__(
            self, fields: Optional[_type_menu_load_page_event_data_t] = {}, /
    ):
        ...


class _type_menu_page_t(TypedDict):
    obj: NotRequired["obj_t"]
    title: NotRequired[int]
    static_title: NotRequired[bool]


class menu_page_t(object):
    obj: "obj_t" = ...
    title: int = ...
    static_title: bool = ...

    def __init__(self, fields: Optional[_type_menu_page_t] = {}, /):
        ...


class _type_menu_t(TypedDict):
    obj: NotRequired["obj_t"]
    storage: NotRequired["obj_t"]
    main: NotRequired["obj_t"]
    main_page: NotRequired["obj_t"]
    main_header: NotRequired["obj_t"]
    main_header_back_btn: NotRequired["obj_t"]
    main_header_title: NotRequired["obj_t"]
    sidebar: NotRequired["obj_t"]
    sidebar_page: NotRequired["obj_t"]
    sidebar_header: NotRequired["obj_t"]
    sidebar_header_back_btn: NotRequired["obj_t"]
    sidebar_header_title: NotRequired["obj_t"]
    selected_tab: NotRequired["obj_t"]
    history_ll: NotRequired["ll_t"]
    cur_depth: NotRequired[int]
    prev_depth: NotRequired[int]
    sidebar_generated: NotRequired[bool]
    mode_header: NotRequired["menu_mode_header_t"]
    mode_root_back_btn: NotRequired[bool]


class menu_t(object):
    obj: "obj_t" = ...
    storage: "obj_t" = ...
    main: "obj_t" = ...
    main_page: "obj_t" = ...
    main_header: "obj_t" = ...
    main_header_back_btn: "obj_t" = ...
    main_header_title: "obj_t" = ...
    sidebar: "obj_t" = ...
    sidebar_page: "obj_t" = ...
    sidebar_header: "obj_t" = ...
    sidebar_header_back_btn: "obj_t" = ...
    sidebar_header_title: "obj_t" = ...
    selected_tab: "obj_t" = ...
    history_ll: "ll_t" = ...
    cur_depth: int = ...
    prev_depth: int = ...
    sidebar_generated: bool = ...
    mode_header: "menu_mode_header_t" = ...
    mode_root_back_btn: bool = ...

    def __init__(self, fields: Optional[_type_menu_t] = {}, /):
        ...


class _type_meter_indicator_t(TypedDict):
    type: NotRequired["draw_mask_type_t"]
    opa: NotRequired["opa_t"]
    start_value: NotRequired[int]
    end_value: NotRequired[int]
    src: NotRequired[None]
    pivot: NotRequired["point_t"]
    needle_img: NotRequired["meter_indicator_t"]
    width: NotRequired["coord_t"]
    r_mod: NotRequired[int]
    color: NotRequired["color_t"]
    needle_line: NotRequired["meter_indicator_t"]
    arc: NotRequired["meter_indicator_t"]
    width_mod: NotRequired[int]
    color_start: NotRequired["color_t"]
    color_end: NotRequired["color_t"]
    local_grad: NotRequired[bool]
    scale_lines: NotRequired["meter_indicator_t"]
    type_data: NotRequired["meter_indicator_t"]


class meter_indicator_t(object):
    type: "draw_mask_type_t" = ...
    opa: "opa_t" = ...
    """Start value"""
    start_value: int = ...
    """End value"""
    end_value: int = ...
    """The image source. A file path like "S:my_img.png" or pointer to an"""
    src: None = ...
    pivot: "point_t" = ...
    needle_img: "meter_indicator_t" = ...
    width: "coord_t" = ...
    r_mod: int = ...
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...
    needle_line: "meter_indicator_t" = ...
    arc: "meter_indicator_t" = ...
    width_mod: int = ...
    color_start: "color_t" = ...
    color_end: "color_t" = ...
    local_grad: bool = ...
    scale_lines: "meter_indicator_t" = ...
    type_data: "meter_indicator_t" = ...

    class TYPE:
        NEEDLE_IMG: int = 0
        NEEDLE_LINE: int = 1
        SCALE_LINES: int = 2
        ARC: int = 3

    class DRAW_PART:
        ARC: int = 0
        NEEDLE_LINE: int = 1
        NEEDLE_IMG: int = 2
        TICK: int = 3

    def __init__(self, fields: Optional[_type_meter_indicator_t] = {}, /):
        ...

    def set_scale_ticks(
            self, cnt: int, width: int, len: int, color: "color_t", /
    ) -> None:
        """
        Set the properties of the ticks of a scale

        :param cnt:
        :type cnt: int

        :param width:
        :type width: int

        :param len:
        :type len: int

        :param color:
        :type color: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_scale_major_ticks(
            self, nth: int, width: int, len: int, color: "color_t",
            label_gap: int, /
    ) -> None:
        """
        Make some "normal" ticks major ticks and set their attributes.
        Texts with the current value are also added to the major ticks.

        :param nth:
        :type nth: int

        :param width:
        :type width: int

        :param len:
        :type len: int

        :param color:
        :type color: "color_t"

        :param label_gap:
        :type label_gap: int

        :returns:
        :retval: None
        """
        ...

    def set_scale_range(
            self, min: int, max: int, angle_range: int, rotation: int, /
    ) -> None:
        """
        Set the value and angular range of a scale.

        :param min:
        :type min: int

        :param max:
        :type max: int

        :param angle_range:
        :type angle_range: int

        :param rotation:
        :type rotation: int

        :returns:
        :retval: None
        """
        ...

    def add_needle_line(
            self, width: int, color: "color_t", r_mod: int, /
    ) -> "meter_indicator_t":
        """
        Add a needle line indicator the scale

        :param width:
        :type width: int

        :param color:
        :type color: "color_t"

        :param r_mod:
        :type r_mod: int

        :returns: the new indicator
        :retval: "meter_indicator_t"
        """
        ...

    def add_needle_img(
            self, src, pivot_x: "coord_t", pivot_y: "coord_t", /
    ) -> "meter_indicator_t":
        """
        Add a needle image indicator the scale

        :param src:
        :type src: None

        :param pivot_x:
        :type pivot_x: "coord_t"

        :param pivot_y:
        :type pivot_y: "coord_t"

        :returns: the new indicator
        :retval: "meter_indicator_t"
        """
        ...

    def add_arc(
            self, width: int, color: "color_t", r_mod: int, /
    ) -> "meter_indicator_t":
        """
        Add an arc indicator the scale

        :param width:
        :type width: int

        :param color:
        :type color: "color_t"

        :param r_mod:
        :type r_mod: int

        :returns: the new indicator
        :retval: "meter_indicator_t"
        """
        ...

    def add_scale_lines(
            self, color_start: "color_t", color_end: "color_t",
            local: bool, width_mod: int, /
    ) -> "meter_indicator_t":
        """
        Add a scale line indicator the scale. It will modify the ticks.

        :param color_start:
        :type color_start: "color_t"

        :param color_end:
        :type color_end: "color_t"

        :param local:
        :type local: bool

        :param width_mod:
        :type width_mod: int

        :returns: the new indicator
        :retval: "meter_indicator_t"
        """
        ...

    def set_indicator_value(
            self, indic: "meter_indicator_t", value: int, /
    ) -> None:
        """
        Set the value of the indicator.
        It will set start and and value to the same value

        :param indic:
        :type indic: "meter_indicator_t"

        :param value:
        :type value: int

        :returns:
        :retval: None
        """
        ...

    def set_indicator_start_value(
            self, indic: "meter_indicator_t", value: int, /
    ) -> None:
        """
        Set the start value of the indicator.

        :param indic:
        :type indic: "meter_indicator_t"

        :param value:
        :type value: int

        :returns:
        :retval: None
        """
        ...

    def set_indicator_end_value(
            self, indic: "meter_indicator_t", value: int, /
    ) -> None:
        """
        Set the start value of the indicator.

        :param indic:
        :type indic: "meter_indicator_t"

        :param value:
        :type value: int

        :returns:
        :retval: None
        """
        ...


class _type_meter_t(TypedDict):
    obj: NotRequired["obj_t"]
    tick_color: NotRequired["color_t"]
    tick_cnt: NotRequired[int]
    tick_length: NotRequired[int]
    tick_width: NotRequired[int]
    tick_major_color: NotRequired["color_t"]
    tick_major_nth: NotRequired[int]
    tick_major_length: NotRequired[int]
    tick_major_width: NotRequired[int]
    label_gap: NotRequired[int]
    label_color: NotRequired[int]
    min: NotRequired[int]
    max: NotRequired[int]
    r_mod: NotRequired[int]
    angle_range: NotRequired[int]
    rotation: NotRequired[int]
    scale: NotRequired["meter_t"]
    indicator_ll: NotRequired["ll_t"]


class meter_t(object):
    obj: "obj_t" = ...
    tick_color: "color_t" = ...
    tick_cnt: int = ...
    tick_length: int = ...
    tick_width: int = ...
    tick_major_color: "color_t" = ...
    tick_major_nth: int = ...
    tick_major_length: int = ...
    tick_major_width: int = ...
    label_gap: int = ...
    label_color: int = ...
    min: int = ...
    max: int = ...
    r_mod: int = ...
    angle_range: int = ...
    """Element of @lv_disp_rotation_t The theme assigned to the screen"""
    rotation: int = ...
    scale: "meter_t" = ...
    indicator_ll: "ll_t" = ...

    def __init__(self, fields: Optional[_type_meter_t] = {}, /):
        ...


class _type_msgbox_t(TypedDict):
    obj: NotRequired["obj_t"]
    title: NotRequired[int]
    close_btn: NotRequired["obj_t"]
    content: NotRequired["obj_t"]
    text: NotRequired[str]
    btns: NotRequired["obj_t"]


class msgbox_t(object):
    obj: "obj_t" = ...
    title: int = ...
    close_btn: "obj_t" = ...
    content: "obj_t" = ...
    """Text to display on the dropdown's button"""
    text: str = ...
    btns: "obj_t" = ...

    def __init__(self, fields: Optional[_type_msgbox_t] = {}, /):
        ...

    def get_title(self) -> "obj_t":
        """
        :returns:
        :retval: "obj_t"
        """
        ...

    def get_close_btn(self) -> "obj_t":
        """
        :returns:
        :retval: "obj_t"
        """
        ...

    def get_text(self) -> "obj_t":
        """
        :returns:
        :retval: "obj_t"
        """
        ...

    def get_content(self) -> "obj_t":
        """
        :returns:
        :retval: "obj_t"
        """
        ...

    def get_btns(self) -> "obj_t":
        """
        :returns:
        :retval: "obj_t"
        """
        ...

    def get_active_btn(self) -> int:
        """
        Get the index of the selected button

        :returns: index of the button (LV_BTNMATRIX_BTN_NONE: if unset)
        :retval: int
        """
        ...

    def get_active_btn_text(self) -> str:
        """
        :returns:
        :retval: str
        """
        ...

    def close(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...

    def close_async(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...


class _type_obj_draw_part_dsc_t(TypedDict):
    draw_ctx: NotRequired["draw_ctx_t"]
    class_p: NotRequired["obj_class_t"]
    type: NotRequired["draw_mask_type_t"]
    draw_area: NotRequired["area_t"]
    rect_dsc: NotRequired["draw_rect_dsc_t"]
    label_dsc: NotRequired["draw_label_dsc_t"]
    line_dsc: NotRequired["draw_line_dsc_t"]
    img_dsc: NotRequired["draw_img_dsc_t"]
    arc_dsc: NotRequired["draw_arc_dsc_t"]
    p1: NotRequired["point_t"]
    p2: NotRequired["point_t"]
    text: NotRequired[str]
    text_length: NotRequired[int]
    part: NotRequired[int]
    id: NotRequired[int]
    radius: NotRequired["coord_t"]
    value: NotRequired[int]
    sub_part_ptr: NotRequired[None]


class obj_draw_part_dsc_t(object):
    draw_ctx: "draw_ctx_t" = ...
    class_p: "obj_class_t" = ...
    type: "draw_mask_type_t" = ...
    """The area of the part being drawn"""
    draw_area: "area_t" = ...
    """
    A draw descriptor that can be modified to changed what LVGL will draw. 
    Set only for rectangle-like parts
    """
    rect_dsc: "draw_rect_dsc_t" = ...
    """
    A draw descriptor that can be modified to changed what LVGL will draw. 
    Set only for text-like parts
    """
    label_dsc: "draw_label_dsc_t" = ...
    """
    A draw descriptor that can be modified to changed what LVGL will draw. 
    Set only for line-like parts
    """
    line_dsc: "draw_line_dsc_t" = ...
    """
    A draw descriptor that can be modified to changed what LVGL will draw. 
    Set only for image-like parts
    """
    img_dsc: "draw_img_dsc_t" = ...
    """
    A draw descriptor that can be modified to changed what LVGL will draw. 
    Set only for arc-like parts
    """
    arc_dsc: "draw_arc_dsc_t" = ...
    p1: "point_t" = ...
    p2: "point_t" = ...
    """Text to display on the dropdown's button"""
    text: str = ...
    """
    Size of the text buffer containing null-terminated text string 
    calculated during drawing.
    """
    text_length: int = ...
    """The current part for which the event is sent"""
    part: int = ...
    """
    The index of the part. E.g. a button's index on button matrix 
    or table cell index.
    """
    id: int = ...
    radius: "coord_t" = ...
    value: int = ...
    """A pointer the identifies something in the part. E.g. chart series."""
    sub_part_ptr: None = ...

    class FLAG:
        """
        On/Off features controlling the object's behavior.
        OR-ed values are possible
        """
        HIDDEN: int = 0
        CLICKABLE: int = 1
        CLICK_FOCUSABLE: int = 2
        CHECKABLE: int = 3
        SCROLLABLE: int = 4
        SCROLL_ELASTIC: int = 5
        SCROLL_MOMENTUM: int = 6
        SCROLL_ONE: int = 7
        SCROLL_CHAIN_HOR: int = 8
        SCROLL_CHAIN_VER: int = 9
        SCROLL_CHAIN: int = SCROLL_CHAIN_VER
        SCROLL_ON_FOCUS: int = 10
        SCROLL_WITH_ARROW: int = 11
        SNAPPABLE: int = 12
        PRESS_LOCK: int = 13
        EVENT_BUBBLE: int = 14
        GESTURE_BUBBLE: int = 15
        ADV_HITTEST: int = 16
        IGNORE_LAYOUT: int = 17
        FLOATING: int = 18
        OVERFLOW_VISIBLE: int = 19
        LAYOUT_1: int = 23
        LAYOUT_2: int = 24
        WIDGET_1: int = 25
        WIDGET_2: int = 26
        USER_1: int = 27
        USER_2: int = 28
        USER_3: int = 29
        USER_4: int = 30

    class OBJ_DRAW_PART:
        RECTANGLE: int = 0
        BORDER_POST: int = 1
        SCROLLBAR: int = 2

    class CLASS_EDITABLE:
        INHERIT: int = 0
        TRUE: int = 1
        FALSE: int = 2

    class CLASS_GROUP_DEF:
        INHERIT: int = 0
        TRUE: int = 1
        FALSE: int = 2

    class CLASS_THEME_INHERITABLE:
        FALSE: int = 0
        TRUE: int = 1

    class TREE_WALK:
        NEXT: int = 0
        SKIP_CHILDREN: int = 1
        END: int = 2

    def __init__(self, fields: Optional[_type_obj_draw_part_dsc_t] = {}, /):
        ...

    def add_flag(self, f: "obj_flag_t", /) -> None:
        """
        Set one or more flags

        :param f:
        :type f: "obj_flag_t"

        :returns:
        :retval: None
        """
        ...

    def clear_flag(self, f: "obj_flag_t", /) -> None:
        """
        Clear one or more flags

        :param f:
        :type f: "obj_flag_t"

        :returns:
        :retval: None
        """
        ...

    def add_state(self, state: "state_t", /) -> None:
        """
        Add one or more states to the object. The other state bits will
        remain unchanged. If specified in the styles, transition animation
        will be started from the previous state to the current.

        :param state:
        :type state: "state_t"

        :returns:
        :retval: None
        """
        ...

    def clear_state(self, state: "state_t", /) -> None:
        """
        Remove one or more states to the object. The other state bits will
        remain unchanged. If specified in the styles, transition animation
        will be started from the previous state to the current.

        :param state:
        :type state: "state_t"

        :returns:
        :retval: None
        """
        ...

    def set_user_data(self, user_data, /) -> None:
        """
        Set the user_data field of the object

        :param user_data:
        :type user_data: None

        :returns:
        :retval: None
        """
        ...

    def has_flag(self, f: "obj_flag_t", /) -> bool:
        """
        Check if a given flag or all the given flags are set on an object.

        :param f:
        :type f: "obj_flag_t"

        :returns: true: all flags are set; false: not all flags are set
        :retval: bool
        """
        ...

    def has_flag_any(self, f: "obj_flag_t", /) -> bool:
        """
        Check if a given flag or any of the flags are set on an object.

        :param f:
        :type f: "obj_flag_t"

        :returns: true: at lest one flag flag is set; false:
            none of the flags are set
        :retval: bool
        """
        ...

    def get_state(self) -> "state_t":
        """
        Get the state of an object

        :returns: the state (OR-ed values from
        :retval: "state_t"
        """
        ...

    def has_state(self, state: "state_t", /) -> bool:
        """
        Check if the object is in a given state or not.

        :param state:
        :type state: "state_t"

        :returns: true:
        :retval: bool
        """
        ...

    def get_group(self) -> "group_t":
        """
        Get the group of the object

        :returns: the pointer to group of the object
        :retval: "group_t"
        """
        ...

    def get_user_data(self) -> None:
        """
        Get the user_data field of the object

        :returns: the pointer to the user_data of the object
        :retval: None
        """
        ...

    def allocate_spec_attr(self) -> None:
        """
        Allocate special data for an object if not allocated yet.

        :returns:
        :retval: None
        """
        ...

    def check_type(self, class_p: "obj_class_t", /) -> bool:
        """
        Check the type of obj.

        :param class_p:
        :type class_p: "obj_class_t"

        :returns: true:
        :retval: bool
        """
        ...

    def has_class(self, class_p: "obj_class_t", /) -> bool:
        """
        Check if any object has a given class (type).
        It checks the ancestor classes too.

        :param class_p:
        :type class_p: "obj_class_t"

        :returns: true:
        :retval: bool
        """
        ...

    def get_class(self) -> "obj_class_t":
        """
        Get the class (type) of the object

        :returns: the class (type) of the object
        :retval: "obj_class_t"
        """
        ...

    def is_valid(self) -> bool:
        """
        Check if any object is still "alive".

        :returns: true: valid
        :retval: bool
        """
        ...

    def class_init_obj(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...

    def is_editable(self) -> bool:
        """
        :returns:
        :retval: bool
        """
        ...

    def is_group_def(self) -> bool:
        """
        :returns:
        :retval: bool
        """
        ...

    def init_draw_rect_dsc(
            self, part: int, draw_dsc: "draw_rect_dsc_t", /
    ) -> None:
        """
        Initialize a rectangle draw descriptor from an
        object's styles in its current state

        :param part:
        :type part: int

        :param draw_dsc:
        :type draw_dsc: "draw_rect_dsc_t"

        :returns: Only the relevant fields will be set. E.g. if
        :retval: None
        """
        ...

    def init_draw_label_dsc(
            self, part: int, draw_dsc: "draw_label_dsc_t", /
    ) -> None:
        """
        Initialize a label draw descriptor
        from an object's styles in its current state

        :param part:
        :type part: int

        :param draw_dsc:
        :type draw_dsc: "draw_label_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def init_draw_img_dsc(
            self, part: int, draw_dsc: "draw_img_dsc_t", /
    ) -> None:
        """
        Initialize an image draw descriptor
        from an object's styles in its current state

        :param part:
        :type part: int

        :param draw_dsc:
        :type draw_dsc: "draw_img_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def init_draw_line_dsc(
            self, part: int, draw_dsc: "draw_line_dsc_t", /
    ) -> None:
        """
        Initialize a line draw descriptor from an
        object's styles in its current state

        :param part:
        :type part: int

        :param draw_dsc:
        :type draw_dsc: "draw_line_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def init_draw_arc_dsc(
            self, part: int, draw_dsc: "draw_arc_dsc_t", /
    ) -> None:
        """
        Initialize an arc draw descriptor from an
        object's styles in its current state

        :param part:
        :type part: int

        :param draw_dsc:
        :type draw_dsc: "draw_arc_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def calculate_ext_draw_size(self, part: int, /) -> "coord_t":
        """
        Get the required extra size (around the object's part) to
        draw shadow, outline, value etc.

        :param part:
        :type part: int

        :returns: the extra size required around the object
        :retval: "coord_t"
        """
        ...

    def dsc_init(self, draw_ctx: "draw_ctx_t", /) -> None:
        """
        Initialize a draw descriptor used in events.

        :param draw_ctx:
        :type draw_ctx: "draw_ctx_t"

        :returns:
        :retval: None
        """
        ...

    def check_type(self, class_p: "obj_class_t", type: int, /) -> bool:
        """
        Check the type obj a part draw descriptor

        :param class_p:
        :type class_p: "obj_class_t"

        :param type:
        :type type: int

        :returns: true if ::dsc is related to ::class_p and ::type
        :retval: bool
        """
        ...

    def refresh_ext_draw_size(self) -> None:
        """
        Send a 'LV_EVENT_REFR_EXT_DRAW_SIZE' Call the ancestor's event
        handler to the object to refresh the value of the extended draw size.
        The result will be saved in

        :returns:
        :retval: None
        """
        ...

    def send_event(self, event_code: "event_code_t", param, /) -> "res_t":
        """
        Send an event to the object

        :param event_code:
        :type event_code: "event_code_t"

        :param param:
        :type param: None

        :returns: LV_RES_OK:
        :retval: "res_t"
        """
        ...

    def add_event(
            self, event_cb: "event_cb_t", filter: "event_code_t", user_data, /
    ) -> None:
        """
        Add an event handler function for an object. Used by the user to
        react on event which happens with the object. An object can have
        multiple event handler. They will be called in the same order
        as they were added.

        :param event_cb:
        :type event_cb: "event_cb_t"

        :param filter:
        :type filter: "event_code_t"

        :param user_data:
        :type user_data: None

        :returns:
        :retval: None
        """
        ...

    def get_event_count(self) -> int:
        """
        :returns:
        :retval: int
        """
        ...

    def get_event_dsc(self, index: int, /) -> "event_dsc_t":
        """
        :param index:
        :type index: int

        :returns:
        :retval: "event_dsc_t"
        """
        ...

    def remove_event(self, index: int, /) -> bool:
        """
        :param index:
        :type index: int

        :returns:
        :retval: bool
        """
        ...

    def set_pos(self, x: "coord_t", y: "coord_t", /) -> None:
        """
        Set the position of an object relative to the set alignment.

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :returns: With default alignment it's the
            distance from the top left corner
        :retval: None
        """
        ...

    def set_x(self, x: "coord_t", /) -> None:
        """
        Set the x coordinate of an object

        :param x:
        :type x: "coord_t"

        :returns: With default alignment it's the
            distance from the top left corner
        :retval: None
        """
        ...

    def set_y(self, y: "coord_t", /) -> None:
        """
        Set the y coordinate of an object

        :param y:
        :type y: "coord_t"

        :returns: With default alignment it's the
            distance from the top left corner
        :retval: None
        """
        ...

    def set_size(self, w: "coord_t", h: "coord_t", /) -> None:
        """
        Set the size of an object.

        :param w:
        :type w: "coord_t"

        :param h:
        :type h: "coord_t"

        :returns: possible values are: pixel simple set the size
            accordingly LV_SIZE_CONTENT set the size to involve all
            children in the given direction LV_SIZE_PCT(x) to set size in
            percentage of the parent's content area size (the size
            without paddings). x should be in [0..1000]% range
        :retval: None
        """
        ...

    def refr_size(self) -> bool:
        """
        Recalculate the size of the object

        :returns: true: the size has been changed
        :retval: bool
        """
        ...

    def set_width(self, w: "coord_t", /) -> None:
        """
        Set the width of an object

        :param w:
        :type w: "coord_t"

        :returns: possible values are: pixel simple set the size
            accordingly LV_SIZE_CONTENT set the size to involve all children
            in the given direction lv_pct(x) to set size in percentage of
            the parent's content area size (the size without paddings). x
            should be in [0..1000]% range
        :retval: None
        """
        ...

    def set_height(self, h: "coord_t", /) -> None:
        """
        Set the height of an object

        :param h:
        :type h: "coord_t"

        :returns: possible values are: pixel simple set the size
            accordingly LV_SIZE_CONTENT set the size to involve all children
            in the given direction lv_pct(x) to set size in percentage of the
            parent's content area size (the size without paddings). x should
            be in [0..1000]% range
        :retval: None
        """
        ...

    def set_content_width(self, w: "coord_t", /) -> None:
        """
        Set the width reduced by the
        left and right padding and the border width.

        :param w:
        :type w: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_content_height(self, h: "coord_t", /) -> None:
        """
        Set the height reduced by the top and bottom
        padding and the border width.

        :param h:
        :type h: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_layout(self, layout: int, /) -> None:
        """
        Set a layout for an object

        :param layout:
        :type layout: int

        :returns:
        :retval: None
        """
        ...

    def is_layout_positioned(self) -> bool:
        """
        Test whether the and object is positioned by a layout or not

        :returns: true: positioned by a layout; false:
            not positioned by a layout
        :retval: bool
        """
        ...

    def mark_layout_as_dirty(self) -> None:
        """
        Mark the object for layout update.

        :returns:
        :retval: None
        """
        ...

    def update_layout(self) -> None:
        """
        Update the layout of an object.

        :returns:
        :retval: None
        """
        ...

    def set_align(self, align: "align_t", /) -> None:
        """
        Change the alignment of an object.

        :param align:
        :type align: "align_t"

        :returns:
        :retval: None
        """
        ...

    def align(
            self, align: "align_t", x_ofs: "coord_t", y_ofs: "coord_t", /
    ) -> None:
        """
        Change the alignment of an object and set new coordinates.
        Equivalent to: lv_obj_set_align(obj, align);
        lv_obj_set_pos(obj, x_ofs, y_ofs);

        :param align:
        :type align: "align_t"

        :param x_ofs:
        :type x_ofs: "coord_t"

        :param y_ofs:
        :type y_ofs: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def align_to(
            self, base: "obj_t", align: "align_t",
            x_ofs: "coord_t", y_ofs: "coord_t", /
    ) -> None:
        """
        Align an object to an other object.

        :param base:
        :type base: "obj_t"

        :param align:
        :type align: "align_t"

        :param x_ofs:
        :type x_ofs: "coord_t"

        :param y_ofs:
        :type y_ofs: "coord_t"

        :returns: if the position or size of
        :retval: None
        """
        ...

    def center(self) -> None:
        """
        Align an object to the center on its parent.

        :returns: if the parent size changes
        :retval: None
        """
        ...

    def get_coords(self, coords: "area_t", /) -> None:
        """
        Copy the coordinates of an object to an area

        :param coords:
        :type coords: "area_t"

        :returns:
        :retval: None
        """
        ...

    def get_x(self) -> "coord_t":
        """
        Get the x coordinate of object.

        :returns: distance of
        :retval: "coord_t"
        """
        ...

    def get_x2(self) -> "coord_t":
        """
        Get the x2 coordinate of object.

        :returns: distance of
        :retval: "coord_t"
        """
        ...

    def get_y(self) -> "coord_t":
        """
        Get the y coordinate of object.

        :returns: distance of
        :retval: "coord_t"
        """
        ...

    def get_y2(self) -> "coord_t":
        """
        Get the y2 coordinate of object.

        :returns: distance of
        :retval: "coord_t"
        """
        ...

    def get_x_aligned(self) -> "coord_t":
        """
        Get the actually set x coordinate of object,
        i.e. the offset form the set alignment

        :returns: the set x coordinate
        :retval: "coord_t"
        """
        ...

    def get_y_aligned(self) -> "coord_t":
        """
        Get the actually set y coordinate of object,
        i.e. the offset form the set alignment

        :returns: the set y coordinate
        :retval: "coord_t"
        """
        ...

    def get_width(self) -> "coord_t":
        """
        Get the width of an object

        :returns: The position of the object is recalculated
            only on the next redraw. To force coordinate recalculation call
        :retval: "coord_t"
        """
        ...

    def get_height(self) -> "coord_t":
        """
        Get the height of an object

        :returns: The position of the object is recalculated only on
            the next redraw. To force coordinate recalculation call
        :retval: "coord_t"
        """
        ...

    def get_content_width(self) -> "coord_t":
        """
        Get the width reduced by the left and right
        padding and the border width.

        :returns: The position of the object is recalculated only on the
            next redraw. To force coordinate recalculation call
        :retval: "coord_t"
        """
        ...

    def get_content_height(self) -> "coord_t":
        """
        Get the height reduced by the top and bottom
        padding and the border width.

        :returns: The position of the object is recalculated only on
            the next redraw. To force coordinate recalculation call
        :retval: "coord_t"
        """
        ...

    def get_content_coords(self, area: "area_t", /) -> None:
        """
        Get the area reduced by the paddings and the border width.

        :param area:
        :type area: "area_t"

        :returns: The position of the object is recalculated only on
            the next redraw. To force coordinate recalculation call
        :retval: None
        """
        ...

    def get_self_width(self) -> "coord_t":
        """
        Get the width occupied by the "parts" of the widget.
        E.g. the width of all columns of a table.

        :returns: the width of the virtually drawn content
        :retval: "coord_t"
        """
        ...

    def get_self_height(self) -> "coord_t":
        """
        Get the height occupied by the "parts" of the widget.
        E.g. the height of all rows of a table.

        :returns: the width of the virtually drawn content
        :retval: "coord_t"
        """
        ...

    def refresh_self_size(self) -> bool:
        """
        Handle if the size of the internal ("virtual")
        content of an object has changed.

        :returns: false: nothing happened; true: refresh happened
        :retval: bool
        """
        ...

    def refr_pos(self) -> None:
        """
        :returns:
        :retval: None
        """
        ...

    def move_to(self, x: "coord_t", y: "coord_t", /) -> None:
        """
        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def move_children_by(
            self, x_diff: "coord_t", y_diff: "coord_t",
            ignore_floating: bool, /
    ) -> None:
        """
        :param x_diff:
        :type x_diff: "coord_t"

        :param y_diff:
        :type y_diff: "coord_t"

        :param ignore_floating:
        :type ignore_floating: bool

        :returns:
        :retval: None
        """
        ...

    def transform_point(
            self, p: "point_t", recursive: bool, inv: bool, /
    ) -> None:
        """
        Transform a point using the angle and zoom style properties of an object

        :param p:
        :type p: "point_t"

        :param recursive:
        :type recursive: bool

        :param inv:
        :type inv: bool

        :returns:
        :retval: None
        """
        ...

    def get_transformed_area(
            self, area: "area_t", recursive: bool, inv: bool, /
    ) -> None:
        """
        Transform an area using the angle and zoom style properties of an object

        :param area:
        :type area: "area_t"

        :param recursive:
        :type recursive: bool

        :param inv:
        :type inv: bool

        :returns:
        :retval: None
        """
        ...

    def invalidate_area(self, area: "area_t", /) -> None:
        """
        Mark an area of an object as invalid.
        The area will be truncated to the object's area and marked for redraw.

        :param area:
        :type area: "area_t"

        :returns:
        :retval: None
        """
        ...

    def invalidate(self) -> None:
        """
        Mark the object as invalid to redrawn its area

        :returns:
        :retval: None
        """
        ...

    def area_is_visible(self, area: "area_t", /) -> bool:
        """
        Tell whether an area of an object is visible (even partially) now or not

        :param area:
        :type area: "area_t"

        :returns: true visible; false not visible
            (hidden, out of parent, on other screen, etc)
        :retval: bool
        """
        ...

    def is_visible(self) -> bool:
        """
        Tell whether an object is visible (even partially) now or not

        :returns: true: visible; false not visible (hidden,
            out of parent, on other screen, etc)
        :retval: bool
        """
        ...

    def set_ext_click_area(self, size: "coord_t", /) -> None:
        """
        Set the size of an extended clickable area

        :param size:
        :type size: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def get_click_area(self, area: "area_t", /) -> None:
        """
        Get the an area where to object can be clicked.
        It's the object's normal area plus the extended click area.

        :param area:
        :type area: "area_t"

        :returns:
        :retval: None
        """
        ...

    def hit_test(self, point: "point_t", /) -> bool:
        """
        Hit-test an object given a particular point in screen space.

        :param point:
        :type point: "point_t"

        :returns: true: if the object is considered under the point
        :retval: bool
        """
        ...

    def set_scrollbar_mode(self, mode: "scrollbar_mode_t", /) -> None:
        """
        Set how the scrollbars should behave.

        :param mode:
        :type mode: "scrollbar_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_scroll_dir(self, dir: "dir_t", /) -> None:
        """
        Set the object in which directions can be scrolled

        :param dir:
        :type dir: "dir_t"

        :returns:
        :retval: None
        """
        ...

    def set_scroll_snap_x(self, align: "scroll_snap_t", /) -> None:
        """
        Set where to snap the children when scrolling ends horizontally

        :param align:
        :type align: "scroll_snap_t"

        :returns:
        :retval: None
        """
        ...

    def set_scroll_snap_y(self, align: "scroll_snap_t", /) -> None:
        """
        Set where to snap the children when scrolling ends vertically

        :param align:
        :type align: "scroll_snap_t"

        :returns:
        :retval: None
        """
        ...

    def get_scrollbar_mode(self) -> "scrollbar_mode_t":
        """
        Get the current scroll mode (when to hide the scrollbars)

        :returns: the current scroll mode from
        :retval: "scrollbar_mode_t"
        """
        ...

    def get_scroll_dir(self) -> "dir_t":
        """
        Get the object in which directions can be scrolled

        :returns:
        :retval: "dir_t"
        """
        ...

    def get_scroll_snap_x(self) -> "scroll_snap_t":
        """
        Get where to snap the children when scrolling ends horizontally

        :returns: the current snap align from
        :retval: "scroll_snap_t"
        """
        ...

    def get_scroll_snap_y(self) -> "scroll_snap_t":
        """
        Get where to snap the children when scrolling ends vertically

        :returns: the current snap align from
        :retval: "scroll_snap_t"
        """
        ...

    def get_scroll_x(self) -> "coord_t":
        """
        Get current X scroll position.

        :returns: the current scroll position from the left edge.
            If the object is not scrolled return 0 If scrolled return > 0
            If scrolled in (elastic scroll) return < 0
        :retval: "coord_t"
        """
        ...

    def get_scroll_y(self) -> "coord_t":
        """
        Get current Y scroll position.

        :returns: the current scroll position from the top edge.
            If the object is not scrolled return 0 If scrolled return > 0
            If scrolled inside return < 0
        :retval: "coord_t"
        """
        ...

    def get_scroll_top(self) -> "coord_t":
        """
        Return the height of the area above the object.
        That is the number of pixels the object can be scrolled down.
        Normally positive but can be negative when scrolled inside.

        :returns: the scrollable area above the object in pixels
        :retval: "coord_t"
        """
        ...

    def get_scroll_bottom(self) -> "coord_t":
        """
        Return the height of the area below the object.
        That is the number of pixels the object can be scrolled down.
        Normally positive but can be negative when scrolled inside.

        :returns: the scrollable area below the object in pixels
        :retval: "coord_t"
        """
        ...

    def get_scroll_left(self) -> "coord_t":
        """
        Return the width of the area on the left the object.
        That is the number of pixels the object can be scrolled down.
         Normally positive but can be negative when scrolled inside.

        :returns: the scrollable area on the left the object in pixels
        :retval: "coord_t"
        """
        ...

    def get_scroll_right(self) -> "coord_t":
        """
        Return the width of the area on the right the object.
        That is the number of pixels the object can be scrolled down.
        Normally positive but can be negative when scrolled inside.

        :returns: the scrollable area on the right the object in pixels
        :retval: "coord_t"
        """
        ...

    def get_scroll_end(self, end: "point_t", /) -> None:
        """
        Get the X and Y coordinates where the scrolling will end for
        this object if a scrolling animation is in progress.
        If no scrolling animation, give the current

        :param end:
        :type end: "point_t"

        :returns:
        :retval: None
        """
        ...

    def scroll_by(
            self, x: "coord_t", y: "coord_t", anim_en: "anim_enable_t", /
    ) -> None:
        """
        Scroll by a given amount of pixels

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns: > 0 value means scroll right/bottom
            (show the more content on the right/bottom)
        :retval: None
        """
        ...

    def scroll_by_bounded(
            self, dx: "coord_t", dy: "coord_t", anim_en: "anim_enable_t", /
    ) -> None:
        """
        Scroll by a given amount of pixels.

        :param dx:
        :type dx: "coord_t"

        :param dy:
        :type dy: "coord_t"

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def scroll_to(
            self, x: "coord_t", y: "coord_t", anim_en: "anim_enable_t", /
    ) -> None:
        """
        Scroll to a given coordinate on an object.

        :param x:
        :type x: "coord_t"

        :param y:
        :type y: "coord_t"

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def scroll_to_x(self, x: "coord_t", anim_en: "anim_enable_t", /) -> None:
        """
        Scroll to a given X coordinate on an object.

        :param x:
        :type x: "coord_t"

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def scroll_to_y(self, y: "coord_t", anim_en: "anim_enable_t", /) -> None:
        """
        Scroll to a given Y coordinate on an object

        :param y:
        :type y: "coord_t"

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def scroll_to_view(self, anim_en: "anim_enable_t", /) -> None:
        """
        Scroll to an object until it becomes visible on its parent

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def scroll_to_view_recursive(self, anim_en: "anim_enable_t", /) -> None:
        """
        Scroll to an object until it becomes visible on its parent.
        Do the same on the parent's parent, and so on. Therefore the
        object will be scrolled into view even it has nested scrollable parents

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def is_scrolling(self) -> bool:
        """
        Tell whether an object is being scrolled or not at this moment

        :returns: true:
        :retval: bool
        """
        ...

    def update_snap(self, anim_en: "anim_enable_t", /) -> None:
        """
        Check the children of

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def get_scrollbar_area(self, hor: "area_t", ver: "area_t", /) -> None:
        """
        Get the area of the scrollbars

        :param hor:
        :type hor: "area_t"

        :param ver:
        :type ver: "area_t"

        :returns:
        :retval: None
        """
        ...

    def scrollbar_invalidate(self) -> None:
        """
        Invalidate the area of the scrollbars

        :returns:
        :retval: None
        """
        ...

    def readjust_scroll(self, anim_en: "anim_enable_t", /) -> None:
        """
        Checked if the content is scrolled "in"
        and adjusts it to a normal position.

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def add_style(
            self, style: "style_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param style:
        :type style: "style_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def replace_style(
            self, old_style: "style_t", new_style: "style_t",
            selector: "style_selector_t", /
    ) -> bool:
        """
        :param old_style:
        :type old_style: "style_t"

        :param new_style:
        :type new_style: "style_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: bool
        """
        ...

    def remove_style(
            self, style: "style_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param style:
        :type style: "style_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def remove_style_all(self) -> None:
        """
        Remove all styles from an object

        :returns:
        :retval: None
        """
        ...

    def refresh_style(self, part: "part_t", prop: "style_prop_t", /) -> None:
        """
        Notify an object and its children about its style is modified.

        :param part:
        :type part: "part_t"

        :param prop:
        :type prop: "style_prop_t"

        :returns:
        :retval: None
        """
        ...

    def get_style_prop(
            self, part: "part_t", prop: "style_prop_t", /
    ) -> "style_value_t":
        """
        Get the value of a style property. The current state of the
        object will be considered. Inherited properties will be inherited.
        If a property is not set a default value will be returned.

        :param part:
        :type part: "part_t"

        :param prop:
        :type prop: "style_prop_t"

        :returns: the value of the property.
            Should be read from the correct field of the
        :retval: "style_value_t"
        """
        ...

    def set_local_style_prop(
            self, prop: "style_prop_t", value: "style_value_t",
            selector: "style_selector_t", /
    ) -> None:
        """
        Set local style property on an object's part and state.

        :param prop:
        :type prop: "style_prop_t"

        :param value:
        :type value: "style_value_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_local_style_prop_meta(
            self, prop: "style_prop_t", meta: int,
            selector: "style_selector_t", /
    ) -> None:
        """
        :param prop:
        :type prop: "style_prop_t"

        :param meta:
        :type meta: int

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def get_local_style_prop(
            self, prop: "style_prop_t", value: "style_value_t",
            selector: "style_selector_t", /
    ) -> "style_res_t":
        """
        :param prop:
        :type prop: "style_prop_t"

        :param value:
        :type value: "style_value_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: "style_res_t"
        """
        ...

    def remove_local_style_prop(
            self, prop: "style_prop_t", selector: "style_selector_t", /
    ) -> bool:
        """
        Remove a local style property from a part of an object with a given state.

        :param prop:
        :type prop: "style_prop_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns: true the property was found and removed;
            false: the property was not found
        :retval: bool
        """
        ...

    def fade_in(self, time: int, delay: int, /) -> None:
        """
        Fade in an an object and all its children.

        :param time:
        :type time: int

        :param delay:
        :type delay: int

        :returns:
        :retval: None
        """
        ...

    def fade_out(self, time: int, delay: int, /) -> None:
        """
        Fade out an an object and all its children.

        :param time:
        :type time: int

        :param delay:
        :type delay: int

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_all(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_hor(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_ver(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_margin_all(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_margin_hor(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_margin_ver(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_gap(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
         :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_size(
            self, width: "coord_t", height: "coord_t",
            selector: "style_selector_t", /
    ) -> None:
        """
        :param width:
        :type width: "coord_t"

        :param height:
        :type height: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def get_style_space_left(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_space_right(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_space_top(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_space_bottom(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def calculate_style_text_align(
            self, part: "part_t", txt: str, /
    ) -> "text_align_t":
        """
        :param part:
        :type part: "part_t"

        :param txt:
        :type txt: str

        :returns:
        :retval: "text_align_t"
        """
        ...

    def get_style_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_min_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_max_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_height(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_min_height(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_max_height(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_x(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_y(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_align(self, part: int, /) -> "align_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "align_t"
        """
        ...

    def get_style_transform_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_transform_height(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_translate_x(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_translate_y(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_transform_zoom(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_transform_angle(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_transform_pivot_x(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_transform_pivot_y(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_pad_top(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_pad_bottom(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_pad_left(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_pad_right(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_pad_row(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_pad_column(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_margin_top(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_margin_bottom(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_margin_left(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_margin_right(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_bg_color(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_bg_color_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_bg_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_bg_grad_color(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_bg_grad_color_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_bg_grad_dir(self, part: int, /) -> "grad_dir_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "grad_dir_t"
        """
        ...

    def get_style_bg_main_stop(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_bg_grad_stop(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_bg_grad(self, part: int, /) -> "grad_dsc_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "grad_dsc_t"
        """
        ...

    def get_style_bg_dither_mode(self, part: int, /) -> "dither_mode_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "dither_mode_t"
        """
        ...

    def get_style_bg_img_src(self, part: int, /) -> None:
        """
        :param part:
        :type part: int

        :returns:
        :retval: None
        """
        ...

    def get_style_bg_img_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_bg_img_recolor(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_bg_img_recolor_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_bg_img_recolor_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_bg_img_tiled(self, part: int, /) -> bool:
        """
        :param part:
        :type part: int

        :returns:
        :retval: bool
        """
        ...

    def get_style_border_color(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_border_color_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_border_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_border_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_border_side(self, part: int, /) -> "border_side_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "border_side_t"
        """
        ...

    def get_style_border_post(self, part: int, /) -> bool:
        """
        :param part:
        :type part: int

        :returns:
        :retval: bool
        """
        ...

    def get_style_outline_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_outline_color(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_outline_color_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_outline_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_outline_pad(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_shadow_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_shadow_ofs_x(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_shadow_ofs_y(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_shadow_spread(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_shadow_color(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_shadow_color_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_shadow_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_img_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_img_recolor(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_img_recolor_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_img_recolor_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_line_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_line_dash_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_line_dash_gap(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_line_rounded(self, part: int, /) -> bool:
        """
        :param part:
        :type part: int

        :returns:
        :retval: bool
        """
        ...

    def get_style_line_color(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_line_color_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_line_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_arc_width(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_arc_rounded(self, part: int, /) -> bool:
        """
        :param part:
        :type part: int

        :returns:
        :retval: bool
        """
        ...

    def get_style_arc_color(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_arc_color_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_arc_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_arc_img_src(self, part: int, /) -> None:
        """
        :param part:
        :type part: int

        :returns:
        :retval: None
        """
        ...

    def get_style_text_color(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_text_color_filtered(self, part: int, /) -> "color_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_t"
        """
        ...

    def get_style_text_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_text_font(self, part: int, /) -> "font_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "font_t"
        """
        ...

    def get_style_text_letter_space(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_text_line_space(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_text_decor(self, part: int, /) -> "text_decor_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "text_decor_t"
        """
        ...

    def get_style_text_align(self, part: int, /) -> "text_align_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "text_align_t"
        """
        ...

    def get_style_radius(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_clip_corner(self, part: int, /) -> bool:
        """
        :param part:
        :type part: int

        :returns:
        :retval: bool
        """
        ...

    def get_style_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_color_filter_dsc(self, part: int, /) -> "color_filter_dsc_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "color_filter_dsc_t"
        """
        ...

    def get_style_color_filter_opa(self, part: int, /) -> "opa_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "opa_t"
        """
        ...

    def get_style_anim(self, part: int, /) -> "anim_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "anim_t"
        """
        ...

    def get_style_anim_time(self, part: int, /) -> int:
        """
        :param part:
        :type part: int

        :returns:
        :retval: int
        """
        ...

    def get_style_anim_speed(self, part: int, /) -> int:
        """
        :param part:
        :type part: int

        :returns:
        :retval: int
        """
        ...

    def get_style_transition(self, part: int, /) -> "style_transition_dsc_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "style_transition_dsc_t"
        """
        ...

    def get_style_blend_mode(self, part: int, /) -> "blend_mode_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "blend_mode_t"
        """
        ...

    def get_style_layout(self, part: int, /) -> int:
        """
        :param part:
        :type part: int

        :returns:
        :retval: int
        """
        ...

    def get_style_base_dir(self, part: int, /) -> "base_dir_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "base_dir_t"
        """
        ...

    def set_style_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_min_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_max_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_height(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_min_height(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_max_height(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_x(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_y(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_align(
            self, value: "align_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "align_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_transform_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_transform_height(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_translate_x(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_translate_y(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_transform_zoom(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_transform_angle(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_transform_pivot_x(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_transform_pivot_y(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_top(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_bottom(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_left(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_right(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_row(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_pad_column(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_margin_top(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_margin_bottom(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_margin_left(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_margin_right(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_color(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_grad_color(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_grad_dir(
            self, value: "grad_dir_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "grad_dir_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_main_stop(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_grad_stop(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_grad(
            self, value: "grad_dsc_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "grad_dsc_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_dither_mode(
            self, value: "dither_mode_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "dither_mode_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_img_src(
            self, value, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: None

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_img_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_img_recolor(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_img_recolor_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_bg_img_tiled(
            self, value: bool, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: bool

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_border_color(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_border_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_border_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_border_side(
            self, value: "border_side_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "border_side_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_border_post(
            self, value: bool, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: bool

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_outline_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_outline_color(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_outline_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_outline_pad(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_shadow_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_shadow_ofs_x(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_shadow_ofs_y(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_shadow_spread(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_shadow_color(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_shadow_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_img_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_img_recolor(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_img_recolor_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_line_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_line_dash_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_line_dash_gap(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_line_rounded(
            self, value: bool, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: bool

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_line_color(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_line_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_arc_width(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_arc_rounded(
            self, value: bool, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: bool

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_arc_color(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_arc_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_arc_img_src(
            self, value, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: None

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_text_color(
            self, value: "color_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_text_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_text_font(
            self, value: "font_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "font_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_text_letter_space(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_text_line_space(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_text_decor(
            self, value: "text_decor_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "text_decor_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_text_align(
            self, value: "text_align_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "text_align_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_radius(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_clip_corner(
            self, value: bool, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: bool

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_color_filter_dsc(
            self, value: "color_filter_dsc_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "color_filter_dsc_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_color_filter_opa(
            self, value: "opa_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "opa_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_anim(
            self, value: "anim_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "anim_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_anim_time(
            self, value: int, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: int

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_anim_speed(
            self, value: int, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: int

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_transition(
            self, value: "style_transition_dsc_t",
            selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "style_transition_dsc_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_blend_mode(
            self, value: "blend_mode_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "blend_mode_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_layout(
            self, value: int, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: int

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_base_dir(
            self, value: "base_dir_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "base_dir_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def _del(self) -> None:
        """
        Delete an object and all of its children. Also remove the objects
        from their group and remove all animations (if any). Send

        :returns:
        :retval: None
        """
        ...

    def clean(self) -> None:
        """
        Delete all children of an object. Also remove the objects from
        their group and remove all animations (if any). Send

        :returns:
        :retval: None
        """
        ...

    def del_delayed(self, delay_ms: int, /) -> None:
        """
        Delete an object after some delay

        :param delay_ms:
        :type delay_ms: int

        :returns:
        :retval: None
        """
        ...

    def del_async(self) -> None:
        """
        Helper function for asynchronously deleting objects. Useful for
        cases where you can't delete an object directly in an

        :returns:
        :retval: None
        """
        ...

    def set_parent(self, parent: "obj_t", /) -> None:
        """
        Move the parent of an object. The relative coordinates will be kept.

        :param parent:
        :type parent: "obj_t"

        :returns:
        :retval: None
        """
        ...

    def swap(self, obj2: "obj_t", /) -> None:
        """
        Swap the positions of two objects. When used in listboxes,
        it can be used to sort the listbox items.

        :param obj2:
        :type obj2: "obj_t"

        :returns:
        :retval: None
        """
        ...

    def move_to_index(self, index: int, /) -> None:
        """
        moves the object to the given index in its parent. When used in
        listboxes, it can be used to sort the listbox items.

        :param index:
        :type index: int

        :returns: to move to the background: lv_obj_move_to_index(obj, 0)
        :retval: None
        """
        ...

    def get_screen(self) -> "obj_t":
        """
        Get the screen of an object

        :returns: pointer to the object's screen
        :retval: "obj_t"
        """
        ...

    def get_disp(self) -> "disp_t":
        """
        Get the display of the object

        :returns: pointer to the object's display
        :retval: "disp_t"
        """
        ...

    def get_parent(self) -> "obj_t":
        """
        Get the parent of an object

        :returns: the parent of the object. (NULL if
        :retval: "obj_t"
        """
        ...

    def get_child(self, id: int, /) -> "obj_t":
        """
        Get the child of an object by the child's index.

        :param id:
        :type id: int

        :returns: pointer to the child or NULL if the index was invalid
        :retval: "obj_t"
        """
        ...

    def get_child_cnt(self) -> int:
        """
        Get the number of children

        :returns: the number of children
        :retval: int
        """
        ...

    def get_index(self) -> int:
        """
        Get the index of a child.

        :returns: the child index of the object. E.g. 0: the oldest
            (firstly created child)
        :retval: int
        """
        ...

    def tree_walk(self, cb: "obj_tree_walk_cb_t", user_data, /) -> None:
        """
        Iterate through all children of any object.

        :param cb:
        :type cb: "obj_tree_walk_cb_t"

        :param user_data:
        :type user_data: None

        :returns:
        :retval: None
        """
        ...

    def set_flex_flow(self, flow: "flex_flow_t", /) -> None:
        """
        Set how the item should flow

        :param flow:
        :type flow: "flex_flow_t"

        :returns:
        :retval: None
        """
        ...

    def set_flex_align(
            self, main_place: "flex_align_t", cross_place: "flex_align_t",
            track_cross_place: "flex_align_t", /
    ) -> None:
        """
        Set how to place (where to align) the items and tracks

        :param main_place:
        :type main_place: "flex_align_t"

        :param cross_place:
        :type cross_place: "flex_align_t"

        :param track_cross_place:
        :type track_cross_place: "flex_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_flex_grow(self, grow: int, /) -> None:
        """
        Sets the width or height (on main axis) to grow the object
        in order fill the free space

        :param grow:
        :type grow: int

        :returns:
        :retval: None
        """
        ...

    def set_style_flex_flow(
            self, value: "flex_flow_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "flex_flow_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_flex_main_place(
            self, value: "flex_align_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "flex_align_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_flex_cross_place(
            self, value: "flex_align_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "flex_align_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_flex_track_place(
            self, value: "flex_align_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "flex_align_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_flex_grow(
            self, value: int, selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: int

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def get_style_flex_flow(self, part: int, /) -> "flex_flow_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "flex_flow_t"
        """
        ...

    def get_style_flex_main_place(self, part: int, /) -> "flex_align_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "flex_align_t"
        """
        ...

    def get_style_flex_cross_place(self, part: int, /) -> "flex_align_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "flex_align_t"
        """
        ...

    def get_style_flex_track_place(self, part: int, /) -> "flex_align_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "flex_align_t"
        """
        ...

    def get_style_flex_grow(self, part: int, /) -> int:
        """
        :param part:
        :type part: int

        :returns:
        :retval: int
        """
        ...

    def set_grid_dsc_array(
            self, col_dsc: Callable[["[]"], "coord_t"],
            row_dsc: Callable[["[]"], "coord_t"], /
    ) -> None:
        """
        :param col_dsc:
        :type col_dsc: Callable[["[]"], "coord_t"]

        :param row_dsc:
        :type row_dsc: Callable[["[]"], "coord_t"]

        :returns:
        :retval: None
        """
        ...

    def set_grid_align(
            self, column_align: "grid_align_t", row_align: "grid_align_t", /
    ) -> None:
        """
        :param column_align:
        :type column_align: "grid_align_t"

        :param row_align:
        :type row_align: "grid_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_grid_cell(
            self, column_align: "grid_align_t", col_pos: int,
            col_span: int, row_align: "grid_align_t",
            row_pos: int, row_span: int, /
    ) -> None:
        """
        Set the cell of an object. The object's parent needs to have
        grid layout, else nothing will happen

        :param column_align:
        :type column_align: "grid_align_t"

        :param col_pos:
        :type col_pos: int

        :param col_span:
        :type col_span: int

        :param row_align:
        :type row_align: "grid_align_t"

        :param row_pos:
        :type row_pos: int

        :param row_span:
        :type row_span: int

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_row_dsc_array(
            self, value: Callable[["[]"], "coord_t"],
            selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: Callable[["[]"], "coord_t"]

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_column_dsc_array(
            self, value: Callable[["[]"], "coord_t"],
            selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: Callable[["[]"], "coord_t"]

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_row_align(
            self, value: "grid_align_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "grid_align_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_column_align(
            self, value: "grid_align_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "grid_align_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_cell_column_pos(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_cell_column_span(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_cell_row_pos(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_cell_row_span(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_cell_x_align(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def set_style_grid_cell_y_align(
            self, value: "coord_t", selector: "style_selector_t", /
    ) -> None:
        """
        :param value:
        :type value: "coord_t"

        :param selector:
        :type selector: "style_selector_t"

        :returns:
        :retval: None
        """
        ...

    def get_style_grid_row_dsc_array(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_grid_column_dsc_array(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_grid_row_align(self, part: int, /) -> "grid_align_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "grid_align_t"
        """
        ...

    def get_style_grid_column_align(self, part: int, /) -> "grid_align_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "grid_align_t"
        """
        ...

    def get_style_grid_cell_column_pos(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_grid_cell_column_span(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_grid_cell_row_pos(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_grid_cell_row_span(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_grid_cell_x_align(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_style_grid_cell_y_align(self, part: int, /) -> "coord_t":
        """
        :param part:
        :type part: int

        :returns:
        :retval: "coord_t"
        """
        ...

    def move_foreground(self) -> None:
        """
        Move the object to the foreground. It will look like if it was
        created as the last child of its parent. It also means it can
        cover any of the siblings.

        :returns:
        :retval: None
        """
        ...

    def move_background(self) -> None:
        """
        Move the object to the background. It will look like if it was
        created as the first child of its parent. It also means any
        of the siblings can cover the object.

        :returns:
        :retval: None
        """
        ...

    def get_child_id(self) -> int:
        """
                :returns:
        :retval: int
        """
        ...

    def set_tile(self, tile_obj: "obj_t", anim_en: "anim_enable_t", /) -> None:
        """
        :param tile_obj:
        :type tile_obj: "obj_t"

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def set_tile_id(
            self, col_id: int, row_id: int, anim_en: "anim_enable_t", /
    ) -> None:
        """
        :param col_id:
        :type col_id: int

        :param row_id:
        :type row_id: int

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...


class _type_point_t(TypedDict):
    x: NotRequired["coord_t"]
    y: NotRequired[int]


class point_t(object):
    """
    Represents a point on the screen.
    """

    x: "coord_t" = ...
    """Give the"""
    y: int = ...

    def __init__(self, fields: Optional[_type_point_t] = {}, /):
        ...

    def transform(self, angle: int, zoom: int, pivot: "point_t", /) -> None:
        """
        :param angle:
        :type angle: int

        :param zoom:
        :type zoom: int

        :param pivot:
        :type pivot: "point_t"

        :returns:
        :retval: None
        """
        ...


class _type_roller_t(TypedDict):
    obj: NotRequired["obj_t"]
    option_cnt: NotRequired[int]
    sel_opt_id: NotRequired[int]
    sel_opt_id_ori: NotRequired[int]
    inf_page_cnt: NotRequired[int]
    mode: NotRequired["bar_mode_t"]
    moved: NotRequired[bool]


class roller_t(object):
    obj: "obj_t" = ...
    """Number of options"""
    option_cnt: int = ...
    """Index of the currently selected option"""
    sel_opt_id: int = ...
    """Store the original index on focus"""
    sel_opt_id_ori: int = ...
    """Number of extra pages added to make the roller look infinite"""
    inf_page_cnt: int = ...
    """Type of bar"""
    mode: "bar_mode_t" = ...
    moved: bool = ...

    class MODE:
        """
        Roller mode.
        """
        NORMAL: int = 0
        INFINITE: int = 1

    def __init__(self, fields: Optional[_type_roller_t] = {}, /):
        ...

    def set_options(self, options: str, mode: "roller_mode_t", /) -> None:
        """
        Set the options on a roller

        :param options:
        :type options: str

        :param mode:
        :type mode: "roller_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_selected(self, sel_opt: int, anim: "anim_enable_t", /) -> None:
        """
        Set the selected option

        :param sel_opt:
        :type sel_opt: int

        :param anim:
        :type anim: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def set_visible_row_count(self, row_cnt: int, /) -> None:
        """
        Set the height to show the given number of rows (options)

        :param row_cnt:
        :type row_cnt: int

        :returns:
        :retval: None
        """
        ...

    def get_selected(self) -> int:
        """
        Get the index of the selected option

        :returns: index of the selected option (0 ... number of option - 1);
        :retval: int
        """
        ...

    def get_selected_str(self, buf: int, buf_size: int, /) -> None:
        """
        Get the current selected option as a string.

        :param buf:
        :type buf: int

        :param buf_size:
        :type buf_size: int

        :returns:
        :retval: None
        """
        ...

    def get_options(self) -> str:
        """
        Get the options of a roller

        :returns: the options separated by '
        :retval: str
        """
        ...

    def get_option_cnt(self) -> int:
        """
        Get the total number of options

        :returns: the total number of options
        :retval: int
        """
        ...


class _type_slider_t(TypedDict):
    bar: NotRequired["obj_t"]
    left_knob_area: NotRequired["area_t"]
    right_knob_area: NotRequired["area_t"]
    pressed_point: NotRequired["point_t"]
    value_to_set: NotRequired[int]
    dragging: NotRequired[bool]
    left_knob_focus: NotRequired[bool]


class slider_t(object):
    bar: "obj_t" = ...
    left_knob_area: "area_t" = ...
    right_knob_area: "area_t" = ...
    pressed_point: "point_t" = ...
    value_to_set: int = ...
    dragging: bool = ...
    left_knob_focus: bool = ...

    class MODE:
        NORMAL: int = ...
        SYMMETRICAL: int = ...
        RANGE: int = ...

    class DRAW_PART_KNOB:
        SLIDER_DRAW_PART_KNOB: int = 0
        LEFT: int = 1

    def __init__(self, fields: Optional[_type_slider_t] = {}, /):
        ...

    def set_value(self, value: int, anim: "anim_enable_t", /) -> None:
        """
        Set a new value on the slider

        :param value:
        :type value: int

        :param anim:
        :type anim: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def set_left_value(self, value: int, anim: "anim_enable_t", /) -> None:
        """
        Set a new value for the left knob of a slider

        :param value:
        :type value: int

        :param anim:
        :type anim: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def set_range(self, min: int, max: int, /) -> None:
        """
        Set minimum and the maximum values of a bar

        :param min:
        :type min: int

        :param max:
        :type max: int

        :returns:
        :retval: None
        """
        ...

    def set_mode(self, mode: "slider_mode_t", /) -> None:
        """
        Set the mode of slider.

        :param mode:
        :type mode: "slider_mode_t"

        :returns:
        :retval: None
        """
        ...

    def get_value(self) -> int:
        """
        Get the value of the main knob of a slider

        :returns: the value of the main knob of the slider
        :retval: int
        """
        ...

    def get_left_value(self) -> int:
        """
        Get the value of the left knob of a slider

        :returns: the value of the left knob of the slider
        :retval: int
        """
        ...

    def get_min_value(self) -> int:
        """
        Get the minimum value of a slider

        :returns: the minimum value of the slider
        :retval: int
        """
        ...

    def get_max_value(self) -> int:
        """
        Get the maximum value of a slider

        :returns: the maximum value of the slider
        :retval: int
        """
        ...

    def is_dragged(self) -> bool:
        """
        Give the slider is being dragged or not

        :returns: true: drag in progress false: not dragged
        :retval: bool
        """
        ...

    def get_mode(self) -> "slider_mode_t":
        """
        Get the mode of the slider.

        :returns: see lv_slider_mode_t
        :retval: "slider_mode_t"
        """
        ...


class _type_span_t(TypedDict):
    txt: NotRequired[int]
    spangroup: NotRequired["obj_t"]
    style: NotRequired["style_t"]
    static_flag: NotRequired[bool]


class span_t(object):
    txt: int = ...
    spangroup: "obj_t" = ...
    style: "style_t" = ...
    static_flag: bool = ...

    class OVERFLOW:
        CLIP: int = 0
        ELLIPSIS: int = 1

    class MODE:
        FIXED: int = 0
        EXPAND: int = 1
        BREAK: int = 2

    def __init__(self, fields: Optional[_type_span_t] = {}, /):
        ...

    def set_text(self, text: str, /) -> None:
        """
        Set a new text for a span. Memory will be
        allocated to store the text by the span.

        :param text:
        :type text: str

        :returns:
        :retval: None
        """
        ...

    def set_text_static(self, text: str, /) -> None:
        """
        Set a static text. It will not be saved by the span so the
        'text' variable has to be 'alive' while the span exist.

        :param text:
        :type text: str

        :returns:
        :retval: None
        """
        ...


class _type_spangroup_t(TypedDict):
    obj: NotRequired["obj_t"]
    lines: NotRequired[int]
    indent: NotRequired["coord_t"]
    cache_w: NotRequired["coord_t"]
    cache_h: NotRequired["coord_t"]
    child_ll: NotRequired["ll_t"]
    mode: NotRequired["bar_mode_t"]
    overflow: NotRequired[bool]
    refresh: NotRequired[bool]


class spangroup_t(object):
    obj: "obj_t" = ...
    lines: int = ...
    indent: "coord_t" = ...
    cache_w: "coord_t" = ...
    cache_h: "coord_t" = ...
    child_ll: "ll_t" = ...
    """Type of bar"""
    mode: "bar_mode_t" = ...
    overflow: bool = ...
    refresh: bool = ...

    def __init__(self, fields: Optional[_type_spangroup_t] = {}, /):
        ...

    def new_span(self) -> "span_t":
        """
        Create a span string descriptor and add to spangroup.

        :returns: pointer to the created span.
        :retval: "span_t"
        """
        ...

    def del_span(self, span: "span_t", /) -> None:
        """
        Remove the span from the spangroup and free memory.

        :param span:
        :type span: "span_t"

        :returns:
        :retval: None
        """
        ...

    def set_align(self, align: "text_align_t", /) -> None:
        """
        Set the align of the spangroup.

        :param align:
        :type align: "text_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_overflow(self, overflow: "span_overflow_t", /) -> None:
        """
        Set the overflow of the spangroup.

        :param overflow:
        :type overflow: "span_overflow_t"

        :returns:
        :retval: None
        """
        ...

    def set_indent(self, indent: "coord_t", /) -> None:
        """
        Set the indent of the spangroup.

        :param indent:
        :type indent: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_mode(self, mode: "span_mode_t", /) -> None:
        """
        Set the mode of the spangroup.

        :param mode:
        :type mode: "span_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_lines(self, lines: int, /) -> None:
        """
        Set lines of the spangroup.

        :param lines:
        :type lines: int

        :returns:
        :retval: None
        """
        ...

    def get_child(self, id: int, /) -> "span_t":
        """
        Get a spangroup child by its index.

        :param id:
        :type id: int

        :returns:
        :retval: "span_t"
        """
        ...

    def get_child_cnt(self) -> int:
        """
                :returns: The span count of the spangroup.
        :retval: int
        """
        ...

    def get_align(self) -> "text_align_t":
        """
        get the align of the spangroup.

        :returns: the align value.
        :retval: "text_align_t"
        """
        ...

    def get_overflow(self) -> "span_overflow_t":
        """
        get the overflow of the spangroup.

        :returns: the overflow value.
        :retval: "span_overflow_t"
        """
        ...

    def get_indent(self) -> "coord_t":
        """
        get the indent of the spangroup.

        :returns: the indent value.
        :retval: "coord_t"
        """
        ...

    def get_mode(self) -> "span_mode_t":
        """
        get the mode of the spangroup.

        :returns:
        :retval: "span_mode_t"
        """
        ...

    def get_lines(self) -> int:
        """
        get lines of the spangroup.

        :returns: the lines value.
        :retval: int
        """
        ...

    def get_max_line_h(self) -> "coord_t":
        """
        get max line height of all span in the spangroup.

        :returns:
        :retval: "coord_t"
        """
        ...

    def get_expand_width(self, max_width: int, /) -> int:
        """
        get the text content width when all span of spangroup on a line.

        :param max_width:
        :type max_width: int

        :returns: text content width or max_width.
        :retval: int
        """
        ...

    def get_expand_height(self, width: "coord_t", /) -> "coord_t":
        """
        get the text content height with width fixed.

        :param width:
        :type width: "coord_t"

        :returns:
        :retval: "coord_t"
        """
        ...

    def refr_mode(self) -> None:
        """
        update the mode of the spangroup.

        :returns:
        :retval: None
        """
        ...


class _type_spinbox_t(TypedDict):
    ta: NotRequired["obj_t"]
    value: NotRequired[int]
    range_max: NotRequired[int]
    range_min: NotRequired[int]
    step: NotRequired[int]
    digit_count: NotRequired[int]
    dec_point_pos: NotRequired[int]
    rollover: NotRequired[bool]
    digit_step_dir: NotRequired[int]


class spinbox_t(object):
    ta: "obj_t" = ...
    value: int = ...
    range_max: int = ...
    range_min: int = ...
    step: int = ...
    digit_count: int = ...
    dec_point_pos: int = ...
    rollover: bool = ...
    digit_step_dir: int = ...

    def __init__(self, fields: Optional[_type_spinbox_t] = {}, /):
        ...

    def set_value(self, i: int, /) -> None:
        """
        Set spinbox value

        :param i:
        :type i: int

        :returns:
        :retval: None
        """
        ...

    def set_rollover(self, b: bool, /) -> None:
        """
        Set spinbox rollover function

        :param b:
        :type b: bool

        :returns:
        :retval: None
        """
        ...

    def set_digit_format(
            self, digit_count: int, separator_position: int, /
    ) -> None:
        """
        Set spinbox digit format (digit count and decimal format)

        :param digit_count:
        :type digit_count: int

        :param separator_position:
        :type separator_position: int

        :returns:
        :retval: None
        """
        ...

    def set_step(self, step: int, /) -> None:
        """
        Set spinbox step

        :param step:
        :type step: int

        :returns:
        :retval: None
        """
        ...

    def set_range(self, range_min: int, range_max: int, /) -> None:
        """
        Set spinbox value range

        :param range_min:
        :type range_min: int

        :param range_max:
        :type range_max: int

        :returns:
        :retval: None
        """
        ...

    def set_cursor_pos(self, pos: int, /) -> None:
        """
        Set cursor position to a specific digit for edition

        :param pos:
        :type pos: int

        :returns:
        :retval: None
        """
        ...

    def set_digit_step_direction(self, direction: "dir_t", /) -> None:
        """
        Set direction of digit step when
        licking an encoder button while in editing mode

        :param direction:
        :type direction: "dir_t"

        :returns:
        :retval: None
        """
        ...

    def get_rollover(self) -> bool:
        """
        Get spinbox rollover function status

        :returns:
        :retval: bool
        """
        ...

    def get_value(self) -> int:
        """
        Get the spinbox numeral value (user has to
        convert to float according to its digit format)

        :returns: value integer value of the spinbox
        :retval: int
        """
        ...

    def get_step(self) -> int:
        """
        Get the spinbox step value (user has to convert
        to float according to its digit format)

        :returns: value integer step value of the spinbox
        :retval: int
        """
        ...

    def step_next(self) -> None:
        """
        Select next lower digit for edition by dividing the step by 10

        :returns:
        :retval: None
        """
        ...

    def step_prev(self) -> None:
        """
        Select next higher digit for edition by multiplying the step by 10

        :returns:
        :retval: None
        """
        ...

    def increment(self) -> None:
        """
        Increment spinbox value by one step

        :returns:
        :retval: None
        """
        ...

    def decrement(self) -> None:
        """
        Decrement spinbox value by one step

        :returns:
        :retval: None
        """
        ...


class _type_sqrt_res_t(TypedDict):
    i: NotRequired[int]
    f: NotRequired[int]


class sqrt_res_t(object):
    i: int = ...
    f: int = ...

    def __init__(self, fields: Optional[_type_sqrt_res_t] = {}, /):
        ...


class _type_style_const_prop_t(TypedDict):
    prop_ptr: NotRequired["style_prop_t"]
    value: NotRequired[int]


class style_const_prop_t(object):
    """
    Descriptor of a constant style property.
    """
    prop_ptr: "style_prop_t" = ...
    value: int = ...

    class RES:
        NOT_FOUND: int = 0
        FOUND: int = 1
        INHERIT: int = 2

    def __init__(self, fields: Optional[_type_style_const_prop_t] = {}, /):
        ...


class _type_style_t(TypedDict):
    value1: NotRequired["style_value_t"]
    values_and_props: NotRequired[int]
    const_props: NotRequired["style_prop_t"]
    v_p: NotRequired["style_t"]
    prop1: NotRequired[int]
    has_group: NotRequired[int]
    prop_cnt: NotRequired[int]


class style_t(object):
    """
    Descriptor of a style (a collection of properties and values).
    """

    value1: "style_value_t" = ...
    values_and_props: int = ...
    const_props: "style_prop_t" = ...
    v_p: "style_t" = ...
    prop1: int = ...
    has_group: int = ...
    prop_cnt: int = ...

    def __init__(self, fields: Optional[_type_style_t] = {}, /):
        ...

    def set_flex_flow(self, value: "flex_flow_t", /) -> None:
        """
        :param value:
        :type value: "flex_flow_t"

        :returns:
        :retval: None
        """
        ...

    def set_flex_main_place(self, value: "flex_align_t", /) -> None:
        """
        :param value:
        :type value: "flex_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_flex_cross_place(self, value: "flex_align_t", /) -> None:
        """
        :param value:
        :type value: "flex_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_flex_track_place(self, value: "flex_align_t", /) -> None:
        """
        :param value:
        :type value: "flex_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_flex_grow(self, value: int, /) -> None:
        """
        :param value:
        :type value: int

        :returns:
        :retval: None
        """
        ...

    def set_grid_row_dsc_array(
            self, value: Callable[["[]"], "coord_t"], /
    ) -> None:
        """
        :param value:
        :type value: Callable[["[]"], "coord_t"]

        :returns:
        :retval: None
        """
        ...

    def set_grid_column_dsc_array(
            self, value: Callable[["[]"], "coord_t"], /
    ) -> None:
        """
        :param value:
        :type value: Callable[["[]"], "coord_t"]

        :returns:
        :retval: None
        """
        ...

    def set_grid_row_align(self, value: "grid_align_t", /) -> None:
        """
        :param value:
        :type value: "grid_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_grid_column_align(self, value: "grid_align_t", /) -> None:
        """
        :param value:
        :type value: "grid_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_grid_cell_column_pos(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_grid_cell_column_span(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_grid_cell_row_pos(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_grid_cell_row_span(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_grid_cell_x_align(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_grid_cell_y_align(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def init(self) -> None:
        """
        Initialize a style

        :returns: Do not call
        :retval: None
        """
        ...

    def reset(self) -> None:
        """
        Clear all properties from a style and free all allocated memories.

        :returns:
        :retval: None
        """
        ...

    def remove_prop(self, prop: "style_prop_t", /) -> bool:
        """
        Remove a property from a style

        :param prop:
        :type prop: "style_prop_t"

        :returns: true: the property was found and removed;
            false: the property wasn't found
        :retval: bool
        """
        ...

    def set_prop(self, prop: "style_prop_t", value: "style_value_t", /) -> None:
        """
        Set the value of property in a style.
        This function shouldn't be used directly by the user. Instead use

        :param prop:
        :type prop: "style_prop_t"

        :param value:
        :type value: "style_value_t"

        :returns:
        :retval: None
        """
        ...

    def set_prop_meta(self, prop: "style_prop_t", meta: int, /) -> None:
        """
        Set a special meta state for a property in a style. This
        function shouldn't be used directly by the user.

        :param prop:
        :type prop: "style_prop_t"

        :param meta:
        :type meta: int

        :returns:
        :retval: None
        """
        ...

    def get_prop(
            self, prop: "style_prop_t", value: "style_value_t", /
    ) -> "style_res_t":
        """
        Get the value of a property

        :param prop:
        :type prop: "style_prop_t"

        :param value:
        :type value: "style_value_t"

        :returns: LV_RES_INV: the property wasn't found in the style (
        :retval: "style_res_t"
        """
        ...

    def get_prop_inlined(
            self, prop: "style_prop_t", value: "style_value_t", /
    ) -> "style_res_t":
        """
        Get the value of a property

        :param prop:
        :type prop: "style_prop_t"

        :param value:
        :type value: "style_value_t"

        :returns: LV_RES_INV: the property wasn't found in the style (
        :retval: "style_res_t"
        """
        ...

    def is_empty(self) -> bool:
        """
        Checks if a style is empty (has no properties)

        :returns: true if the style is empty
        :retval: bool
        """
        ...

    def set_size(self, width: "coord_t", height: "coord_t", /) -> None:
        """
        :param width:
        :type width: "coord_t"

        :param height:
        :type height: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_all(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_hor(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_ver(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_gap(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_min_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_max_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_height(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_min_height(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_max_height(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_x(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_y(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_align(self, value: "align_t", /) -> None:
        """
        :param value:
        :type value: "align_t"

        :returns:
        :retval: None
        """
        ...

    def set_transform_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_transform_height(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_translate_x(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_translate_y(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_transform_zoom(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_transform_angle(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_transform_pivot_x(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_transform_pivot_y(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_top(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_bottom(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_left(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_right(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_row(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_pad_column(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_margin_top(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_margin_bottom(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_margin_left(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_margin_right(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_color(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_grad_color(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_grad_dir(self, value: "grad_dir_t", /) -> None:
        """
        :param value:
        :type value: "grad_dir_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_main_stop(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_grad_stop(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_grad(self, value: "grad_dsc_t", /) -> None:
        """
        :param value:
        :type value: "grad_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_dither_mode(self, value: "dither_mode_t", /) -> None:
        """
        :param value:
        :type value: "dither_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_img_src(self, value, /) -> None:
        """
        :param value:
        :type value: None

        :returns:
        :retval: None
        """
        ...

    def set_bg_img_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_img_recolor(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_img_recolor_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_bg_img_tiled(self, value: bool, /) -> None:
        """
        :param value:
        :type value: bool

        :returns:
        :retval: None
        """
        ...

    def set_border_color(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_border_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_border_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_border_side(self, value: "border_side_t", /) -> None:
        """
        :param value:
        :type value: "border_side_t"

        :returns:
        :retval: None
        """
        ...

    def set_border_post(self, value: bool, /) -> None:
        """
        :param value:
        :type value: bool

        :returns:
        :retval: None
        """
        ...

    def set_outline_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_outline_color(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_outline_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_outline_pad(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_shadow_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_shadow_ofs_x(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_shadow_ofs_y(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_shadow_spread(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_shadow_color(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_shadow_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_img_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_img_recolor(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_img_recolor_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_line_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_line_dash_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_line_dash_gap(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_line_rounded(self, value: bool, /) -> None:
        """
        :param value:
        :type value: bool

        :returns:
        :retval: None
        """
        ...

    def set_line_color(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_line_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_arc_width(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_arc_rounded(self, value: bool, /) -> None:
        """
        :param value:
        :type value: bool

        :returns:
        :retval: None
        """
        ...

    def set_arc_color(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_arc_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_arc_img_src(self, value, /) -> None:
        """
        :param value:
        :type value: None

        :returns:
        :retval: None
        """
        ...

    def set_text_color(self, value: "color_t", /) -> None:
        """
        :param value:
        :type value: "color_t"

        :returns:
        :retval: None
        """
        ...

    def set_text_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_text_font(self, value: "font_t", /) -> None:
        """
        :param value:
        :type value: "font_t"

        :returns:
        :retval: None
        """
        ...

    def set_text_letter_space(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_text_line_space(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_text_decor(self, value: "text_decor_t", /) -> None:
        """
        :param value:
        :type value: "text_decor_t"

        :returns:
        :retval: None
        """
        ...

    def set_text_align(self, value: "text_align_t", /) -> None:
        """
        :param value:
        :type value: "text_align_t"

        :returns:
        :retval: None
        """
        ...

    def set_radius(self, value: "coord_t", /) -> None:
        """
        :param value:
        :type value: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def set_clip_corner(self, value: bool, /) -> None:
        """
        :param value:
        :type value: bool

        :returns:
        :retval: None
        """
        ...

    def set_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_color_filter_dsc(self, value: "color_filter_dsc_t", /) -> None:
        """
        :param value:
        :type value: "color_filter_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def set_color_filter_opa(self, value: "opa_t", /) -> None:
        """
        :param value:
        :type value: "opa_t"

        :returns:
        :retval: None
        """
        ...

    def set_anim(self, value: "anim_t", /) -> None:
        """
        :param value:
        :type value: "anim_t"

        :returns:
        :retval: None
        """
        ...

    def set_anim_time(self, value: int, /) -> None:
        """
        :param value:
        :type value: int

        :returns:
        :retval: None
        """
        ...

    def set_anim_speed(self, value: int, /) -> None:
        """
        :param value:
        :type value: int

        :returns:
        :retval: None
        """
        ...

    def set_transition(self, value: "style_transition_dsc_t", /) -> None:
        """
        :param value:
        :type value: "style_transition_dsc_t"

        :returns:
        :retval: None
        """
        ...

    def set_blend_mode(self, value: "blend_mode_t", /) -> None:
        """
        :param value:
        :type value: "blend_mode_t"

        :returns:
        :retval: None
        """
        ...

    def set_layout(self, value: int, /) -> None:
        """
        :param value:
        :type value: int

        :returns:
        :retval: None
        """
        ...

    def set_base_dir(self, value: "base_dir_t", /) -> None:
        """
        :param value:
        :type value: "base_dir_t"

        :returns:
        :retval: None
        """
        ...


class _type_style_transition_dsc_t(TypedDict):
    props: NotRequired["style_prop_t"]
    user_data: NotRequired[None]
    path_xcb: NotRequired["anim_path_cb_t"]
    time: NotRequired[int]
    delay: NotRequired[int]


class style_transition_dsc_t(object):
    """
    Descriptor for style transitions
    """

    """An array with the properties to animate."""
    props: "style_prop_t" = ...
    """Custom user data"""
    user_data: None = ...
    """A path for the animation."""
    path_xcb: "anim_path_cb_t" = ...
    """Animation time in ms"""
    time: int = ...
    delay: int = ...

    def __init__(self, fields: Optional[_type_style_transition_dsc_t] = {}, /):
        ...

    def init(
            self, props: Callable[["[]"], "style_prop_t"],
            path_cb: "anim_path_cb_t", time: int, delay: int,
            user_data, /
    ) -> None:
        """
        :param props:
        :type props: Callable[["[]"], "style_prop_t"]

        :param path_cb:
        :type path_cb: "anim_path_cb_t"

        :param time:
        :type time: int

        :param delay:
        :type delay: int

        :param user_data:
        :type user_data: None

        :returns:
        :retval: None
        """
        ...


class _type_style_value_t(TypedDict):
    num: NotRequired[int]
    ptr: NotRequired[None]
    color: NotRequired["color_t"]


class style_value_t(object):
    """
    A common type to handle all the property types in the same way.
    """

    """Number integer number (opacity, enums, booleans or "normal" numbers)"""
    num: int = ...
    """Constant pointers (font, cone text, etc)"""
    ptr: None = ...
    """Color to draw the image. Used when the image has alpha channel only"""
    color: "color_t" = ...

    def __init__(self, fields: Optional[_type_style_value_t] = {}, /):
        ...


class _type_switch_t(TypedDict):
    obj: NotRequired["obj_t"]
    anim_state: NotRequired[int]


class switch_t(object):
    obj: "obj_t" = ...
    anim_state: int = ...

    def __init__(self, fields: Optional[_type_switch_t] = {}, /):
        ...


class _type_table_t(TypedDict):
    obj: NotRequired["obj_t"]
    col_cnt: NotRequired[int]
    row_cnt: NotRequired[int]
    cell_data: NotRequired[int]
    row_h: NotRequired["coord_t"]
    col_w: NotRequired["coord_t"]
    col_act: NotRequired[int]
    row_act: NotRequired[int]


class table_t(object):
    obj: "obj_t" = ...
    col_cnt: int = ...
    row_cnt: int = ...
    cell_data: int = ...
    row_h: "coord_t" = ...
    col_w: "coord_t" = ...
    col_act: int = ...
    row_act: int = ...

    class CELL_CTRL:
        MERGE_RIGHT: int = 0
        TEXT_CROP: int = 1
        CUSTOM_1: int = 4
        CUSTOM_2: int = 5
        CUSTOM_3: int = 6
        CUSTOM_4: int = 7

    class DRAW_PART_CELL:
        TABLE_DRAW_PART_CELL: int = 0

    def __init__(self, fields: Optional[_type_table_t] = {}, /):
        ...

    def set_cell_value(self, row: int, col: int, txt: str, /) -> None:
        """
        Set the value of a cell.

        :param row:
        :type row: int

        :param col:
        :type col: int

        :param txt:
        :type txt: str

        :returns: New roes/columns are added automatically if required
        :retval: None
        """
        ...

    def set_cell_value_fmt(self, row: int, col: int, fmt: str, /) -> None:
        """
        Set the value of a cell.
        Memory will be allocated to store the text by the table.

        :param row:
        :type row: int

        :param col:
        :type col: int

        :param fmt:
        :type fmt: str

        :returns: New roes/columns are added automatically if required
        :retval: None
        """
        ...

    def set_row_cnt(self, row_cnt: int, /) -> None:
        """
        Set the number of rows

        :param row_cnt:
        :type row_cnt: int

        :returns:
        :retval: None
        """
        ...

    def set_col_cnt(self, col_cnt: int, /) -> None:
        """
        Set the number of columns

        :param col_cnt:
        :type col_cnt: int

        :returns:
        :retval: None
        """
        ...

    def set_col_width(self, col_id: int, w: "coord_t", /) -> None:
        """
        Set the width of a column

        :param col_id:
        :type col_id: int

        :param w:
        :type w: "coord_t"

        :returns:
        :retval: None
        """
        ...

    def add_cell_ctrl(
            self, row: int, col: int, ctrl: "table_cell_ctrl_t", /
    ) -> None:
        """
        Add control bits to the cell.

        :param row:
        :type row: int

        :param col:
        :type col: int

        :param ctrl:
        :type ctrl: "table_cell_ctrl_t"

        :returns:
        :retval: None
        """
        ...

    def clear_cell_ctrl(
            self, row: int, col: int, ctrl: "table_cell_ctrl_t", /
    ) -> None:
        """
        Clear control bits of the cell.

        :param row:
        :type row: int

        :param col:
        :type col: int

        :param ctrl:
        :type ctrl: "table_cell_ctrl_t"

        :returns:
        :retval: None
        """
        ...

    def get_cell_value(self, row: int, col: int, /) -> str:
        """
        Get the value of a cell.

        :param row:
        :type row: int

        :param col:
        :type col: int

        :returns: text in the cell
        :retval: str
        """
        ...

    def get_row_cnt(self) -> int:
        """
        Get the number of rows.

        :returns: number of rows.
        :retval: int
        """
        ...

    def get_col_cnt(self) -> int:
        """
        Get the number of columns.

        :returns: number of columns.
        :retval: int
        """
        ...

    def get_col_width(self, col: int, /) -> "coord_t":
        """
        Get the width of a column

        :param col:
        :type col: int

        :returns: width of the column
        :retval: "coord_t"
        """
        ...

    def has_cell_ctrl(
            self, row: int, col: int, ctrl: "table_cell_ctrl_t", /
    ) -> bool:
        """
        Get whether a cell has the control bits

        :param row:
        :type row: int

        :param col:
        :type col: int

        :param ctrl:
        :type ctrl: "table_cell_ctrl_t"

        :returns: true: all control bits are set;
            false: not all control bits are set
        :retval: bool
        """
        ...

    def get_selected_cell(self, row: int, col: int, /) -> None:
        """
        Get the selected cell (pressed and or focused)

        :param row:
        :type row: int

        :param col:
        :type col: int

        :returns:
        :retval: None
        """
        ...


class _type_tabview_t(TypedDict):
    obj: NotRequired["obj_t"]
    map: NotRequired["opa_t"]
    tab_cnt: NotRequired[int]
    tab_cur: NotRequired[int]
    tab_pos: NotRequired["dir_t"]


class tabview_t(object):
    obj: "obj_t" = ...
    map: "opa_t" = ...
    tab_cnt: int = ...
    tab_cur: int = ...
    tab_pos: "dir_t" = ...

    def __init__(self, fields: Optional[_type_tabview_t] = {}, /):
        ...

    def add_tab(self, name: str, /) -> "obj_t":
        """
        :param name:
        :type name: str

        :returns:
        :retval: "obj_t"
        """
        ...

    def rename_tab(self, tab_id: int, new_name: str, /) -> None:
        """
        :param tab_id:
        :type tab_id: int

        :param new_name:
        :type new_name: str

        :returns:
        :retval: None
        """
        ...

    def get_content(self) -> "obj_t":
        """
                :returns:
        :retval: "obj_t"
        """
        ...

    def get_tab_btns(self) -> "obj_t":
        """
                :returns:
        :retval: "obj_t"
        """
        ...

    def set_act(self, id: int, anim_en: "anim_enable_t", /) -> None:
        """
        :param id:
        :type id: int

        :param anim_en:
        :type anim_en: "anim_enable_t"

        :returns:
        :retval: None
        """
        ...

    def get_tab_act(self) -> int:
        """
                :returns:
        :retval: int
        """
        ...


class _type_textarea_t(TypedDict):
    obj: NotRequired["obj_t"]
    label: NotRequired["obj_t"]
    placeholder_txt: NotRequired[int]
    pwd_tmp: NotRequired[int]
    pwd_bullet: NotRequired[int]
    accepted_chars: NotRequired[str]
    max_length: NotRequired[int]
    pwd_show_time: NotRequired[int]
    valid_x: NotRequired["coord_t"]
    pos: NotRequired["point_t"]
    area: NotRequired["area_t"]
    txt_byte_pos: NotRequired[int]
    show: NotRequired[bool]
    click_pos: NotRequired[bool]
    cursor: NotRequired["obj_t"]
    sel_start: NotRequired[int]
    sel_end: NotRequired[int]
    text_sel_in_prog: NotRequired[bool]
    text_sel_en: NotRequired[bool]
    pwd_mode: NotRequired[bool]
    one_line: NotRequired[bool]


# noinspection PyShadowingNames
class textarea_t(object):
    obj: "obj_t" = ...
    label: "obj_t" = ...
    placeholder_txt: int = ...
    pwd_tmp: int = ...
    pwd_bullet: int = ...
    accepted_chars: str = ...
    max_length: int = ...
    pwd_show_time: int = ...
    valid_x: "coord_t" = ...
    pos: "point_t" = ...
    area: "area_t" = ...
    txt_byte_pos: int = ...
    show: bool = ...
    click_pos: bool = ...
    """Cursor for LV_INPUT_TYPE_POINTER"""
    cursor: "obj_t" = ...
    sel_start: int = ...
    sel_end: int = ...
    text_sel_in_prog: bool = ...
    text_sel_en: bool = ...
    pwd_mode: bool = ...
    one_line: bool = ...

    def __init__(self, fields: Optional[_type_textarea_t] = {}, /):
        ...

    def add_char(self, c: int, /) -> None:
        """
        Insert a character to the current cursor position.
        To add a wide char, e.g. 'Á' use

        :param c:
        :type c: int

        :returns:
        :retval: None
        """
        ...

    def add_text(self, txt: str, /) -> None:
        """
        Insert a text to the current cursor position

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def del_char(self) -> None:
        """
        Delete a the left character from the current cursor position

        :returns:
        :retval: None
        """
        ...

    def del_char_forward(self) -> None:
        """
        Delete the right character from the current cursor position

        :returns:
        :retval: None
        """
        ...

    def set_text(self, txt: str, /) -> None:
        """
        Set the text of a text area

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def set_placeholder_text(self, txt: str, /) -> None:
        """
        Set the placeholder text of a text area

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def set_cursor_pos(self, pos: int, /) -> None:
        """
        Set the cursor position

        :param pos:
        :type pos: int

        :returns:
        :retval: None
        """
        ...

    def set_cursor_click_pos(self, en: bool, /) -> None:
        """
        Enable/Disable the positioning of the cursor
        by clicking the text on the text area.

        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def set_password_mode(self, en: bool, /) -> None:
        """
        Enable/Disable password mode

        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def set_password_bullet(self, bullet: str, /) -> None:
        """
        Set the replacement characters to show in password mode

        :param bullet:
        :type bullet: str

        :returns:
        :retval: None
        """
        ...

    def set_one_line(self, en: bool, /) -> None:
        """
        Configure the text area to one line or back to normal

        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def set_accepted_chars(self, list: str, /) -> None:
        """
        Set a list of characters. Only these characters
        will be accepted by the text area

        :param list:
        :type list: str

        :returns:
        :retval: None
        """
        ...

    def set_max_length(self, num: int, /) -> None:
        """
        Set max length of a Text Area.

        :param num:
        :type num: int

        :returns:
        :retval: None
        """
        ...

    def set_insert_replace(self, txt: str, /) -> None:
        """
        In

        :param txt:
        :type txt: str

        :returns:
        :retval: None
        """
        ...

    def set_text_selection(self, en: bool, /) -> None:
        """
        Enable/disable selection mode.

        :param en:
        :type en: bool

        :returns:
        :retval: None
        """
        ...

    def set_password_show_time(self, time: int, /) -> None:
        """
        Set how long show the password before changing it to '*'

        :param time:
        :type time: int

        :returns:
        :retval: None
        """
        ...

    def set_align(self, align: "text_align_t", /) -> None:
        """
        Deprecated: use the normal text_align style property
        instead Set the label's alignment. It sets where the label is
        aligned (in one line mode it can be smaller than the text area)
        and how the lines of the area align in case of multiline text area

        :param align:
        :type align: "text_align_t"

        :returns:
        :retval: None
        """
        ...

    def get_text(self) -> str:
        """
        Get the text of a text area.
        In password mode it gives the real text (not '*'s).

        :returns: pointer to the text
        :retval: str
        """
        ...

    def get_placeholder_text(self) -> str:
        """
        Get the placeholder text of a text area

        :returns: pointer to the text
        :retval: str
        """
        ...

    def get_label(self) -> "obj_t":
        """
        Get the label of a text area

        :returns: pointer to the label object
        :retval: "obj_t"
        """
        ...

    def get_cursor_pos(self) -> int:
        """
        Get the current cursor position in character index

        :returns: the cursor position
        :retval: int
        """
        ...

    def get_cursor_click_pos(self) -> bool:
        """
        Get whether the cursor click positioning is enabled or not.

        :returns: true: enable click positions; false: disable
        :retval: bool
        """
        ...

    def get_password_mode(self) -> bool:
        """
        Get the password mode attribute

        :returns: true: password mode is enabled, false: disabled
        :retval: bool
        """
        ...

    def get_password_bullet(self) -> str:
        """
        Get the replacement characters to show in password mode

        :returns: pointer to the replacement text
        :retval: str
        """
        ...

    def get_one_line(self) -> bool:
        """
        Get the one line configuration attribute

        :returns: true: one line configuration is enabled, false: disabled
        :retval: bool
        """
        ...

    def get_accepted_chars(self) -> str:
        """
        Get a list of accepted characters.

        :returns: list of accented characters.
        :retval: str
        """
        ...

    def get_max_length(self) -> int:
        """
        Get max length of a Text Area.

        :returns: the maximal number of characters to be add
        :retval: int
        """
        ...

    def text_is_selected(self) -> bool:
        """
        Find whether text is selected or not.

        :returns: whether text is selected or not
        :retval: bool
        """
        ...

    def get_text_selection(self) -> bool:
        """
        Find whether selection mode is enabled.

        :returns: true: selection mode is enabled, false: disabled
        :retval: bool
        """
        ...

    def get_password_show_time(self) -> int:
        """
        Set how long show the password before changing it to '*'

        :returns: show time in milliseconds. 0: hide immediately.
        :retval: int
        """
        ...

    def get_current_char(self) -> int:
        """
        Get a the character from the current cursor position

        :returns: a the character or 0
        :retval: int
        """
        ...

    def clear_selection(self) -> None:
        """
        Clear the selection on the text area.

        :returns:
        :retval: None
        """
        ...

    def cursor_right(self) -> None:
        """
        Move the cursor one character right

        :returns:
        :retval: None
        """
        ...

    def cursor_left(self) -> None:
        """
        Move the cursor one character left

        :returns:
        :retval: None
        """
        ...

    def cursor_down(self) -> None:
        """
        Move the cursor one line down

        :returns:
        :retval: None
        """
        ...

    def cursor_up(self) -> None:
        """
        Move the cursor one line up

        :returns:
        :retval: None
        """
        ...


class _type_tileview_t(TypedDict):
    obj: NotRequired["obj_t"]
    tile_act: NotRequired["obj_t"]


class tileview_t(object):
    obj: "obj_t" = ...
    tile_act: "obj_t" = ...

    def __init__(self, fields: Optional[_type_tileview_t] = {}, /):
        ...

    def add_tile(self, col_id: int, row_id: int, dir: "dir_t", /) -> "obj_t":
        """
        :param col_id:
        :type col_id: int

        :param row_id:
        :type row_id: int

        :param dir:
        :type dir: "dir_t"

        :returns:
        :retval: "obj_t"
        """
        ...

    def get_tile_act(self) -> "obj_t":
        """
                :returns:
        :retval: "obj_t"
        """
        ...


class _type_tileview_tile_t(TypedDict):
    obj: NotRequired["obj_t"]
    dir: NotRequired["dir_t"]


class tileview_tile_t(object):
    obj: "obj_t" = ...
    dir: "dir_t" = ...

    def __init__(self, fields: Optional[_type_tileview_tile_t] = {}, /):
        ...


class _type_vaformat_t(TypedDict):
    fmt: NotRequired[str]
    va: NotRequired[Any]


class vaformat_t(object):
    fmt: str = ...
    va: Any = ...

    def __init__(self, fields: Optional[_type_vaformat_t] = {}, /):
        ...


class _type_win_t(TypedDict):
    obj: NotRequired["obj_t"]


class win_t(object):
    obj: "obj_t" = ...

    def __init__(self, fields: Optional[_type_win_t] = {}, /):
        ...

    def add_title(self, txt: str, /) -> "obj_t":
        """
        :param txt:
        :type txt: str

        :returns:
        :retval: "obj_t"
        """
        ...

    def add_btn(self, icon, btn_w: "coord_t", /) -> "obj_t":
        """
        :param icon:
        :type icon: None

        :param btn_w:
        :type btn_w: "coord_t"

        :returns:
        :retval: "obj_t"
        """
        ...

    def get_header(self) -> "obj_t":
        """
                :returns:
        :retval: "obj_t"
        """
        ...

    def get_content(self) -> "obj_t":
        """
                :returns:
        :retval: "obj_t"
        """
        ...


class _type_qrcodegen_Segment(TypedDict):
    mode: NotRequired["bar_mode_t"]
    numChars: NotRequired[int]
    data: NotRequired[int]
    bitLength: NotRequired[int]


class qrcodegen_Segment(object):
    """Type of bar"""
    mode: "bar_mode_t" = ...
    numChars: int = ...
    """Pointer to the data of the image"""
    data: int = ...
    bitLength: int = ...

    class qrcodegen_Ecc:
        LOW: int = 0
        MEDIUM: int = 1
        QUARTILE: int = 2
        HIGH: int = 3

    class qrcodegen_Mask:
        AUTO: int = -1
        _0: int = 0
        _1: int = 1
        _2: int = 2
        _3: int = 3
        _4: int = 4
        _5: int = 5
        _6: int = 6
        _7: int = 7

    class qrcodegen_Mode:
        NUMERIC: int = 0x1
        ALPHANUMERIC: int = 0x2
        BYTE: int = 0x4
        KANJI: int = 0x8
        ECI: int = 0x7

    def __init__(self, fields: Optional[_type_qrcodegen_Segment] = {}, /):
        ...

    def encodeSegments(
            self, len: int, ecl: "qrcodegen_Ecc",
            tempBuffer: Callable[["[]"], int], qrcode: Callable[["[]"], int], /
    ) -> bool:
        """
        :param len:
        :type len: int

        :param ecl:
        :type ecl: "qrcodegen_Ecc"

        :param tempBuffer:
        :type tempBuffer: Callable[["[]"], int]

        :param qrcode:
        :type qrcode: Callable[["[]"], int]

        :returns:
        :retval: bool
        """
        ...

    def encodeSegmentsAdvanced(
            self, len: int, ecl: "qrcodegen_Ecc", minVersion: int,
            maxVersion: int, mask: int, boostEcl: bool,
            tempBuffer: Callable[["[]"], int],
            qrcode: Callable[["[]"], int], /
    ) -> bool:
        """
        :param len:
        :type len: int

        :param ecl:
        :type ecl: "qrcodegen_Ecc"

        :param minVersion:
        :type minVersion: int

        :param maxVersion:
        :type maxVersion: int

        :param mask:
        :type mask: int

        :param boostEcl:
        :type boostEcl: bool

        :param tempBuffer:
        :type tempBuffer: Callable[["[]"], int]

        :param qrcode:
        :type qrcode: Callable[["[]"], int]

        :returns:
        :retval: bool
        """
        ...


class _type_stbrp_context(TypedDict):
    width: NotRequired["coord_t"]
    height: NotRequired[int]
    align: NotRequired["text_align_t"]
    init_mode: NotRequired[int]
    heuristic: NotRequired[int]
    num_nodes: NotRequired[int]
    active_head: NotRequired["stbrp_node"]
    free_head: NotRequired["stbrp_node"]
    extra: NotRequired["stbrp_node"]


class stbrp_context(object):
    width: "coord_t" = ...
    height: int = ...
    align: "text_align_t" = ...
    init_mode: int = ...
    heuristic: int = ...
    num_nodes: int = ...
    active_head: "stbrp_node" = ...
    free_head: "stbrp_node" = ...
    extra: "stbrp_node" = ...

    class HEURISTIC_Skyline:
        default: int = 0
        BL_sortHeight: int = ...
        BF_sortHeight: int = 1

    def __init__(self, fields: Optional[_type_stbrp_context] = {}, /):
        ...

    def pack_rects(self, rects: "stbrp_rect", num_rects: int, /) -> int:
        """
        :param rects:
        :type rects: "stbrp_rect"

        :param num_rects:
        :type num_rects: int

        :returns:
        :retval: int
        """
        ...

    def init_target(
            self, width: int, height: int, nodes: "stbrp_node",
            num_nodes: int, /
    ) -> None:
        """
        :param width:
        :type width: int

        :param height:
        :type height: int

        :param nodes:
        :type nodes: "stbrp_node"

        :param num_nodes:
        :type num_nodes: int

        :returns:
        :retval: None
        """
        ...

    def setup_allow_out_of_mem(self, allow_out_of_mem: int, /) -> None:
        """
        :param allow_out_of_mem:
        :type allow_out_of_mem: int

        :returns:
        :retval: None
        """
        ...

    def setup_heuristic(self, heuristic: int, /) -> None:
        """
        :param heuristic:
        :type heuristic: int

        :returns:
        :retval: None
        """
        ...


class _type_stbrp_node(TypedDict):
    x: NotRequired["coord_t"]
    y: NotRequired[int]
    next: NotRequired["stbrp_node"]


class stbrp_node(object):
    x: "coord_t" = ...
    """Give the"""
    y: int = ...
    next: "stbrp_node" = ...

    def __init__(self, fields: Optional[_type_stbrp_node] = {}, /):
        ...


class _type_stbrp_rect(TypedDict):
    id: NotRequired[int]
    w: NotRequired[int]
    h: NotRequired[int]
    x: NotRequired["coord_t"]
    y: NotRequired[int]
    was_packed: NotRequired[int]


class stbrp_rect(object):
    """
    The index of the part.
    E.g. a button's index on button matrix or table cell index.
    """
    id: int = ...
    w: int = ...
    h: int = ...
    x: "coord_t" = ...
    """Give the"""
    y: int = ...
    was_packed: int = ...

    def __init__(self, fields: Optional[_type_stbrp_rect] = {}, /):
        ...


class _type_stbtt__bitmap(TypedDict):
    w: NotRequired[int]
    h: NotRequired[int]
    stride: NotRequired[int]
    pixels: NotRequired[int]


class stbtt__bitmap(object):
    w: int = ...
    h: int = ...
    stride: int = ...
    pixels: int = ...

    class STBTT:
        vmove: int = 1
        vline: int = 2
        vcurve: int = 3
        vcubic: int = 4

    class PLATFORM_ID:
        UNICODE: int = 0
        MAC: int = 1
        ISO: int = 2
        MICROSOFT: int = 3

    class UNICODE_EID:
        UNICODE_1_0: int = 0
        UNICODE_1_1: int = 1
        ISO_10646: int = 2
        UNICODE_2_0_BMP: int = 3
        UNICODE_2_0_FULL: int = 4

    class MS_EID:
        SYMBOL: int = 0
        UNICODE_BMP: int = 1
        SHIFTJIS: int = 2
        UNICODE_FULL: int = 10

    class MAC_EID:
        ROMAN: int = 0
        ARABIC: int = 4
        JAPANESE: int = 1
        HEBREW: int = 5
        CHINESE_TRAD: int = 2
        GREEK: int = 6
        KOREAN: int = 3
        RUSSIAN: int = 7

    class MS_LANG:
        ENGLISH: int = 0x0409
        ITALIAN: int = 0x0410
        CHINESE: int = 0x0804
        JAPANESE: int = 0x0411
        DUTCH: int = 0x0413
        KOREAN: int = 0x0412
        FRENCH: int = 0x040c
        RUSSIAN: int = 0x0419
        GERMAN: int = 0x0407
        SPANISH: int = 0x0409
        HEBREW: int = 0x040d
        SWEDISH: int = 0x041D

    class MAC_LANG:
        ENGLISH: int = 0
        JAPANESE: int = 11
        ARABIC: int = 12
        KOREAN: int = 23
        DUTCH: int = 4
        RUSSIAN: int = 32
        FRENCH: int = 1
        SPANISH: int = 6
        GERMAN: int = 2
        SWEDISH: int = 5
        HEBREW: int = 10
        CHINESE_SIMPLIFIED: int = 33
        ITALIAN: int = 3
        CHINESE_TRAD: int = 19

    def __init__(self, fields: Optional[_type_stbtt__bitmap] = {}, /):
        ...

    def Rasterize(
            self, flatness_in_pixels: float, vertices: "stbtt_vertex",
            num_verts: int, scale_x: float, scale_y: float,
            shift_x: float, shift_y: float, x_off: int, y_off: int,
            invert: int, userdata, /
    ) -> None:
        """
        :param flatness_in_pixels:
        :type flatness_in_pixels: float

        :param vertices:
        :type vertices: "stbtt_vertex"

        :param num_verts:
        :type num_verts: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param x_off:
        :type x_off: int

        :param y_off:
        :type y_off: int

        :param invert:
        :type invert: int

        :param userdata:
        :type userdata: None

        :returns:
        :retval: None
        """
        ...


class _type_stbtt__buf(TypedDict):
    data: NotRequired[int]
    cursor: NotRequired["obj_t"]
    size: NotRequired["coord_t"]


class stbtt__buf(object):
    """Pointer to the data of the image"""
    data: int = ...
    """Cursor for LV_INPUT_TYPE_POINTER"""
    cursor: "obj_t" = ...
    """The computed gradient color map size, in colors"""
    size: "coord_t" = ...

    def __init__(self, fields: Optional[_type_stbtt__buf] = {}, /):
        ...


class _type_stbtt_aligned_quad(TypedDict):
    x0: NotRequired[float]
    y0: NotRequired[float]
    s0: NotRequired[float]
    t0: NotRequired[float]
    x1: NotRequired["coord_t"]
    y1: NotRequired["coord_t"]
    s1: NotRequired[float]
    t1: NotRequired[float]


class stbtt_aligned_quad(object):
    x0: float = ...
    y0: float = ...
    s0: float = ...
    t0: float = ...
    x1: "coord_t" = ...
    y1: "coord_t" = ...
    s1: float = ...
    t1: float = ...

    def __init__(self, fields: Optional[_type_stbtt_aligned_quad] = {}, /):
        ...


class _type_stbtt_bakedchar(TypedDict):
    x0: NotRequired[float]
    y0: NotRequired[float]
    x1: NotRequired["coord_t"]
    y1: NotRequired["coord_t"]
    xoff: NotRequired[float]
    yoff: NotRequired[float]
    xadvance: NotRequired[float]


class stbtt_bakedchar(object):
    x0: float = ...
    y0: float = ...
    x1: "coord_t" = ...
    y1: "coord_t" = ...
    xoff: float = ...
    yoff: float = ...
    xadvance: float = ...

    def __init__(self, fields: Optional[_type_stbtt_bakedchar] = {}, /):
        ...

    def GetBakedQuad(
            self, pw: int, ph: int, char_index: int, xpos: float,
            ypos: float, q: "stbtt_aligned_quad", opengl_fillrule: int, /
    ) -> None:
        """
        :param pw:
        :type pw: int

        :param ph:
        :type ph: int

        :param char_index:
        :type char_index: int

        :param xpos:
        :type xpos: float

        :param ypos:
        :type ypos: float

        :param q:
        :type q: "stbtt_aligned_quad"

        :param opengl_fillrule:
        :type opengl_fillrule: int

        :returns:
        :retval: None
        """
        ...


class _type_stbtt_fontinfo(TypedDict):
    userdata: NotRequired[None]
    data: NotRequired[int]
    fontstart: NotRequired[int]
    numGlyphs: NotRequired[int]
    loca: NotRequired[int]
    head: NotRequired["ll_node_t"]
    glyf: NotRequired[int]
    hhea: NotRequired[int]
    hmtx: NotRequired[int]
    kern: NotRequired[int]
    gpos: NotRequired[int]
    svg: NotRequired[int]
    index_map: NotRequired[int]
    indexToLocFormat: NotRequired[int]
    cff: NotRequired["stbtt__buf"]
    charstrings: NotRequired["stbtt__buf"]
    gsubrs: NotRequired["stbtt__buf"]
    subrs: NotRequired["stbtt__buf"]
    fontdicts: NotRequired["stbtt__buf"]
    fdselect: NotRequired["stbtt__buf"]


# noinspection PyShadowingNames
class stbtt_fontinfo(object):
    userdata: None = ...
    """Pointer to the data of the image"""
    data: int = ...
    fontstart: int = ...
    numGlyphs: int = ...
    loca: int = ...
    head: "ll_node_t" = ...
    glyf: int = ...
    hhea: int = ...
    hmtx: int = ...
    kern: int = ...
    gpos: int = ...
    svg: int = ...
    index_map: int = ...
    indexToLocFormat: int = ...
    cff: "stbtt__buf" = ...
    charstrings: "stbtt__buf" = ...
    gsubrs: "stbtt__buf" = ...
    subrs: "stbtt__buf" = ...
    fontdicts: "stbtt__buf" = ...
    fdselect: "stbtt__buf" = ...

    def __init__(self, fields: Optional[_type_stbtt_fontinfo] = {}, /):
        ...

    def InitFont(self, data: str, offset: int, /) -> int:
        """
        :param data:
        :type data: str

        :param offset:
        :type offset: int

        :returns:
        :retval: int
        """
        ...

    def FindGlyphIndex(self, unicode_codepoint: int, /) -> int:
        """
        :param unicode_codepoint:
        :type unicode_codepoint: int

        :returns:
        :retval: int
        """
        ...

    def ScaleForPixelHeight(self, pixels: float, /) -> float:
        """
        :param pixels:
        :type pixels: float

        :returns:
        :retval: float
        """
        ...

    def ScaleForMappingEmToPixels(self, pixels: float, /) -> float:
        """
        :param pixels:
        :type pixels: float

        :returns:
        :retval: float
        """
        ...

    def GetFontVMetrics(
            self, ascent: int, descent: int, lineGap: int, /
    ) -> None:
        """
        :param ascent:
        :type ascent: int

        :param descent:
        :type descent: int

        :param lineGap:
        :type lineGap: int

        :returns:
        :retval: None
        """
        ...

    def GetFontVMetricsOS2(
            self, typoAscent: int, typoDescent: int, typoLineGap: int, /
    ) -> int:
        """
        :param typoAscent:
        :type typoAscent: int

        :param typoDescent:
        :type typoDescent: int

        :param typoLineGap:
        :type typoLineGap: int

        :returns:
        :retval: int
        """
        ...

    def GetFontBoundingBox(self, x0: int, y0: int, x1: int, y1: int, /) -> None:
        """
        :param x0:
        :type x0: int

        :param y0:
        :type y0: int

        :param x1:
        :type x1: int

        :param y1:
        :type y1: int

        :returns:
        :retval: None
        """
        ...

    def GetCodepointHMetrics(
            self, codepoint: int, advanceWidth: int, leftSideBearing: int, /
    ) -> None:
        """
        :param codepoint:
        :type codepoint: int

        :param advanceWidth:
        :type advanceWidth: int

        :param leftSideBearing:
        :type leftSideBearing: int

        :returns:
        :retval: None
        """
        ...

    def GetCodepointKernAdvance(self, ch1: int, ch2: int, /) -> int:
        """
        :param ch1:
        :type ch1: int

        :param ch2:
        :type ch2: int

        :returns:
        :retval: int
        """
        ...

    def GetCodepointBox(
            self, codepoint: int, x0: int, y0: int, x1: int, y1: int, /
    ) -> int:
        """
        :param codepoint:
        :type codepoint: int

        :param x0:
        :type x0: int

        :param y0:
        :type y0: int

        :param x1:
        :type x1: int

        :param y1:
        :type y1: int

        :returns:
        :retval: int
        """
        ...

    def GetGlyphHMetrics(
            self, glyph_index: int, advanceWidth: int, leftSideBearing: int, /
    ) -> None:
        """
        :param glyph_index:
        :type glyph_index: int

        :param advanceWidth:
        :type advanceWidth: int

        :param leftSideBearing:
        :type leftSideBearing: int

        :returns:
        :retval: None
        """
        ...

    def GetGlyphKernAdvance(self, glyph1: int, glyph2: int, /) -> int:
        """
        :param glyph1:
        :type glyph1: int

        :param glyph2:
        :type glyph2: int

        :returns:
        :retval: int
        """
        ...

    def GetGlyphBox(
            self, glyph_index: int, x0: int, y0: int, x1: int, y1: int, /
    ) -> int:
        """
        :param glyph_index:
        :type glyph_index: int

        :param x0:
        :type x0: int

        :param y0:
        :type y0: int

        :param x1:
        :type x1: int

        :param y1:
        :type y1: int

        :returns:
        :retval: int
        """
        ...

    def GetKerningTableLength(self) -> int:
        """
                :returns:
        :retval: int
        """
        ...

    def GetKerningTable(
            self, table: "stbtt_kerningentry", table_length: int, /
    ) -> int:
        """
        :param table:
        :type table: "stbtt_kerningentry"

        :param table_length:
        :type table_length: int

        :returns:
        :retval: int
        """
        ...

    def IsGlyphEmpty(self, glyph_index: int, /) -> int:
        """
        :param glyph_index:
        :type glyph_index: int

        :returns:
        :retval: int
        """
        ...

    def GetCodepointShape(
            self, unicode_codepoint: int, vertices: "stbtt_vertex", /
    ) -> int:
        """
        :param unicode_codepoint:
        :type unicode_codepoint: int

        :param vertices:
        :type vertices: "stbtt_vertex"

        :returns:
        :retval: int
        """
        ...

    def GetGlyphShape(
            self, glyph_index: int, vertices: "stbtt_vertex", /
    ) -> int:
        """
        :param glyph_index:
        :type glyph_index: int

        :param vertices:
        :type vertices: "stbtt_vertex"

        :returns:
        :retval: int
        """
        ...

    def FreeShape(self, vertices: "stbtt_vertex", /) -> None:
        """
        :param vertices:
        :type vertices: "stbtt_vertex"

        :returns:
        :retval: None
        """
        ...

    def FindSVGDoc(self, gl: int, /) -> "int":
        """
        :param gl:
        :type gl: int

        :returns:
        :retval: "int"
        """
        ...

    def GetCodepointSVG(
            self, unicode_codepoint: int, svgOfs: "int", /
    ) -> int:
        """
        :param unicode_codepoint:
        :type unicode_codepoint: int

        :param svgOfs:
        :type svgOfs: "int"

        :returns:
        :retval: int
        """
        ...

    def GetGlyphSVG(self, gl: int, svgOfs: "int", /) -> int:
        """
        :param gl:
        :type gl: int

        :param svgOfs:
        :type svgOfs: "int"

        :returns:
        :retval: int
        """
        ...

    def GetCodepointBitmap(
            self, scale_x: float, scale_y: float, codepoint: int, width: int,
            height: int, xoff: int, yoff: int, /
    ) -> int:
        """
        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param codepoint:
        :type codepoint: int

        :param width:
        :type width: int

        :param height:
        :type height: int

        :param xoff:
        :type xoff: int

        :param yoff:
        :type yoff: int

        :returns:
        :retval: int
        """
        ...

    def GetCodepointBitmapSubpixel(
            self, scale_x: float, scale_y: float, shift_x: float,
            shift_y: float, codepoint: int, width: int,
            height: int, xoff: int, yoff: int, /
    ) -> int:
        """
        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param codepoint:
        :type codepoint: int

        :param width:
        :type width: int

        :param height:
        :type height: int

        :param xoff:
        :type xoff: int

        :param yoff:
        :type yoff: int

        :returns:
        :retval: int
        """
        ...

    def MakeCodepointBitmap(
            self, output: int, out_w: int, out_h: int, out_stride: int,
            scale_x: float, scale_y: float, codepoint: int, /
    ) -> None:
        """
        :param output:
        :type output: int

        :param out_w:
        :type out_w: int

        :param out_h:
        :type out_h: int

        :param out_stride:
        :type out_stride: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param codepoint:
        :type codepoint: int

        :returns:
        :retval: None
        """
        ...

    def MakeCodepointBitmapSubpixel(
            self, output: int, out_w: int, out_h: int, out_stride: int,
            scale_x: float, scale_y: float, shift_x: float,
            shift_y: float, codepoint: int, /
    ) -> None:
        """
        :param output:
        :type output: int

        :param out_w:
        :type out_w: int

        :param out_h:
        :type out_h: int

        :param out_stride:
        :type out_stride: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param codepoint:
        :type codepoint: int

        :returns:
        :retval: None
        """
        ...

    def MakeCodepointBitmapSubpixelPrefilter(
            self, output: int, out_w: int, out_h: int, out_stride: int,
            scale_x: float, scale_y: float, shift_x: float, shift_y: float,
            oversample_x: int, oversample_y: int, sub_x: float,
            sub_y: float, codepoint: int, /
    ) -> None:
        """
        :param output:
        :type output: int

        :param out_w:
        :type out_w: int

        :param out_h:
        :type out_h: int

        :param out_stride:
        :type out_stride: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param oversample_x:
        :type oversample_x: int

        :param oversample_y:
        :type oversample_y: int

        :param sub_x:
        :type sub_x: float

        :param sub_y:
        :type sub_y: float

        :param codepoint:
        :type codepoint: int

        :returns:
        :retval: None
        """
        ...

    def GetCodepointBitmapBox(
            self, codepoint: int, scale_x: float, scale_y: float,
            ix0: int, iy0: int, ix1: int, iy1: int, /
    ) -> None:
        """
        :param codepoint:
        :type codepoint: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param ix0:
        :type ix0: int

        :param iy0:
        :type iy0: int

        :param ix1:
        :type ix1: int

        :param iy1:
        :type iy1: int

        :returns:
        :retval: None
        """
        ...

    def GetCodepointBitmapBoxSubpixel(
            self, codepoint: int, scale_x: float, scale_y: float,
            shift_x: float, shift_y: float, ix0: int, iy0: int,
            ix1: int, iy1: int, /
    ) -> None:
        """
        :param codepoint:
        :type codepoint: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param ix0:
        :type ix0: int

        :param iy0:
        :type iy0: int

        :param ix1:
        :type ix1: int

        :param iy1:
        :type iy1: int

        :returns:
        :retval: None
        """
        ...

    def GetGlyphBitmap(
            self, scale_x: float, scale_y: float, glyph: int, width: int,
            height: int, xoff: int, yoff: int, /
    ) -> int:
        """
        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param glyph:
        :type glyph: int

        :param width:
        :type width: int

        :param height:
        :type height: int

        :param xoff:
        :type xoff: int

        :param yoff:
        :type yoff: int

        :returns:
        :retval: int
        """
        ...

    def GetGlyphBitmapSubpixel(
            self, scale_x: float, scale_y: float, shift_x: float,
            shift_y: float, glyph: int, width: int, height: int,
            xoff: int, yoff: int, /
    ) -> int:
        """
        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param glyph:
        :type glyph: int

        :param width:
        :type width: int

        :param height:
        :type height: int

        :param xoff:
        :type xoff: int

        :param yoff:
        :type yoff: int

        :returns:
        :retval: int
        """
        ...

    def MakeGlyphBitmap(
            self, output: int, out_w: int, out_h: int, out_stride: int,
            scale_x: float, scale_y: float, glyph: int, /
    ) -> None:
        """
        :param output:
        :type output: int

        :param out_w:
        :type out_w: int

        :param out_h:
        :type out_h: int

        :param out_stride:
        :type out_stride: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param glyph:
        :type glyph: int

        :returns:
        :retval: None
        """
        ...

    def MakeGlyphBitmapSubpixel(
            self, output: int, out_w: int, out_h: int, out_stride: int,
            scale_x: float, scale_y: float, shift_x: float,
            shift_y: float, glyph: int, /
    ) -> None:
        """
        :param output:
        :type output: int

        :param out_w:
        :type out_w: int

        :param out_h:
        :type out_h: int

        :param out_stride:
        :type out_stride: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param glyph:
        :type glyph: int

        :returns:
        :retval: None
        """
        ...

    def MakeGlyphBitmapSubpixelPrefilter(
            self, output: int, out_w: int, out_h: int, out_stride: int,
            scale_x: float, scale_y: float, shift_x: float, shift_y: float,
            oversample_x: int, oversample_y: int, sub_x: float,
            sub_y: float, glyph: int, /
    ) -> None:
        """
        :param output:
        :type output: int

        :param out_w:
        :type out_w: int

        :param out_h:
        :type out_h: int

        :param out_stride:
        :type out_stride: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param oversample_x:
        :type oversample_x: int

        :param oversample_y:
        :type oversample_y: int

        :param sub_x:
        :type sub_x: float

        :param sub_y:
        :type sub_y: float

        :param glyph:
        :type glyph: int

        :returns:
        :retval: None
        """
        ...

    def GetGlyphBitmapBox(
            self, glyph: int, scale_x: float, scale_y: float, ix0: int,
            iy0: int, ix1: int, iy1: int, /
    ) -> None:
        """
        :param glyph:
        :type glyph: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param ix0:
        :type ix0: int

        :param iy0:
        :type iy0: int

        :param ix1:
        :type ix1: int

        :param iy1:
        :type iy1: int

        :returns:
        :retval: None
        """
        ...

    def GetGlyphBitmapBoxSubpixel(
            self, glyph: int, scale_x: float, scale_y: float,
            shift_x: float, shift_y: float, ix0: int, iy0: int,
            ix1: int, iy1: int, /
    ) -> None:
        """
        :param glyph:
        :type glyph: int

        :param scale_x:
        :type scale_x: float

        :param scale_y:
        :type scale_y: float

        :param shift_x:
        :type shift_x: float

        :param shift_y:
        :type shift_y: float

        :param ix0:
        :type ix0: int

        :param iy0:
        :type iy0: int

        :param ix1:
        :type ix1: int

        :param iy1:
        :type iy1: int

        :returns:
        :retval: None
        """
        ...

    def GetGlyphSDF(
            self, scale: float, glyph: int, padding: int,
            onedge_value: int, pixel_dist_scale: float, width: int,
            height: int, xoff: int, yoff: int, /
    ) -> int:
        """
        :param scale:
        :type scale: float

        :param glyph:
        :type glyph: int

        :param padding:
        :type padding: int

        :param onedge_value:
        :type onedge_value: int

        :param pixel_dist_scale:
        :type pixel_dist_scale: float

        :param width:
        :type width: int

        :param height:
        :type height: int

        :param xoff:
        :type xoff: int

        :param yoff:
        :type yoff: int

        :returns:
        :retval: int
        """
        ...

    def GetCodepointSDF(
            self, scale: float, codepoint: int, padding: int,
            onedge_value: int, pixel_dist_scale: float, width: int,
            height: int, xoff: int, yoff: int, /
    ) -> int:
        """
        :param scale:
        :type scale: float

        :param codepoint:
        :type codepoint: int

        :param padding:
        :type padding: int

        :param onedge_value:
        :type onedge_value: int

        :param pixel_dist_scale:
        :type pixel_dist_scale: float

        :param width:
        :type width: int

        :param height:
        :type height: int

        :param xoff:
        :type xoff: int

        :param yoff:
        :type yoff: int

        :returns:
        :retval: int
        """
        ...

    def GetFontNameString(
            self, length: int, platformID: int, encodingID: int,
            languageID: int, nameID: int, /
    ) -> "int":
        """
        :param length:
        :type length: int

        :param platformID:
        :type platformID: int

        :param encodingID:
        :type encodingID: int

        :param languageID:
        :type languageID: int

        :param nameID:
        :type nameID: int

        :returns:
        :retval: "int"
        """
        ...


class _type_stbtt_pack_context(TypedDict):
    user_allocator_context: NotRequired[None]
    pack_info: NotRequired[None]
    width: NotRequired["coord_t"]
    height: NotRequired[int]
    stride_in_bytes: NotRequired[int]
    padding: NotRequired[int]
    skip_missing: NotRequired[int]
    h_oversample: NotRequired[int]
    v_oversample: NotRequired[int]
    pixels: NotRequired[int]
    nodes: NotRequired[None]


class stbtt_pack_context(object):
    user_allocator_context: None = ...
    pack_info: None = ...
    width: "coord_t" = ...
    height: int = ...
    stride_in_bytes: int = ...
    padding: int = ...
    skip_missing: int = ...
    h_oversample: int = ...
    v_oversample: int = ...
    pixels: int = ...
    nodes: None = ...

    def __init__(self, fields: Optional[_type_stbtt_pack_context] = {}, /):
        ...

    def PackBegin(
            self, pixels: int, width: int, height: int,
            stride_in_bytes: int, padding: int, alloc_context, /
    ) -> int:
        """
        :param pixels:
        :type pixels: int

        :param width:
        :type width: int

        :param height:
        :type height: int

        :param stride_in_bytes:
        :type stride_in_bytes: int

        :param padding:
        :type padding: int

        :param alloc_context:
        :type alloc_context: None

        :returns:
        :retval: int
        """
        ...

    def PackEnd(self) -> None:
        """
                :returns:
        :retval: None
        """
        ...

    def PackSetOversampling(
            self, h_oversample: int, v_oversample: int, /
    ) -> None:
        """
        :param h_oversample:
        :type h_oversample: int

        :param v_oversample:
        :type v_oversample: int

        :returns:
        :retval: None
        """
        ...

    def PackSetSkipMissingCodepoints(self, skip: int, /) -> None:
        """
        :param skip:
        :type skip: int

        :returns:
        :retval: None
        """
        ...

    def PackFontRangesGatherRects(
            self, info: "stbtt_fontinfo", ranges: "stbtt_pack_range",
            num_ranges: int, rects: "stbrp_rect", /
    ) -> int:
        """
        :param info:
        :type info: "stbtt_fontinfo"

        :param ranges:
        :type ranges: "stbtt_pack_range"

        :param num_ranges:
        :type num_ranges: int

        :param rects:
        :type rects: "stbrp_rect"

        :returns:
        :retval: int
        """
        ...

    def PackFontRangesPackRects(
            self, rects: "stbrp_rect", num_rects: int, /
    ) -> None:
        """
        :param rects:
        :type rects: "stbrp_rect"

        :param num_rects:
        :type num_rects: int

        :returns:
        :retval: None
        """
        ...

    def PackFontRangesRenderIntoRects(
            self, info: "stbtt_fontinfo", ranges: "stbtt_pack_range",
            num_ranges: int, rects: "stbrp_rect", /
    ) -> int:
        """
        :param info:
        :type info: "stbtt_fontinfo"

        :param ranges:
        :type ranges: "stbtt_pack_range"

        :param num_ranges:
        :type num_ranges: int

        :param rects:
        :type rects: "stbrp_rect"

        :returns:
        :retval: int
        """
        ...


class _type_stbtt_pack_range(TypedDict):
    font_size: NotRequired[float]
    first_unicode_codepoint_in_range: NotRequired[int]
    array_of_unicode_codepoints: NotRequired[int]
    num_chars: NotRequired[int]
    chardata_for_range: NotRequired["stbtt_packedchar"]
    h_oversample: NotRequired[int]
    v_oversample: NotRequired[int]


class stbtt_pack_range(object):
    font_size: float = ...
    first_unicode_codepoint_in_range: int = ...
    array_of_unicode_codepoints: int = ...
    num_chars: int = ...
    chardata_for_range: "stbtt_packedchar" = ...
    h_oversample: int = ...
    v_oversample: int = ...

    def __init__(self, fields: Optional[_type_stbtt_pack_range] = {}, /):
        ...


class _type_stbtt_packedchar(TypedDict):
    x0: NotRequired[float]
    y0: NotRequired[float]
    x1: NotRequired["coord_t"]
    y1: NotRequired["coord_t"]
    xoff: NotRequired[float]
    yoff: NotRequired[float]
    xadvance: NotRequired[float]
    xoff2: NotRequired[float]
    yoff2: NotRequired[float]


class stbtt_packedchar(object):
    x0: float = ...
    y0: float = ...
    x1: "coord_t" = ...
    y1: "coord_t" = ...
    xoff: float = ...
    yoff: float = ...
    xadvance: float = ...
    xoff2: float = ...
    yoff2: float = ...

    def __init__(self, fields: Optional[_type_stbtt_packedchar] = {}, /):
        ...

    def GetPackedQuad(
            self, pw: int, ph: int, char_index: int, xpos: float,
            ypos: float, q: "stbtt_aligned_quad", align_to_integer: int, /
    ) -> None:
        """
        :param pw:
        :type pw: int

        :param ph:
        :type ph: int

        :param char_index:
        :type char_index: int

        :param xpos:
        :type xpos: float

        :param ypos:
        :type ypos: float

        :param q:
        :type q: "stbtt_aligned_quad"

        :param align_to_integer:
        :type align_to_integer: int

        :returns:
        :retval: None
        """
        ...


class _type_stbtt_vertex(TypedDict):
    x: NotRequired["coord_t"]
    y: NotRequired[int]
    cx: NotRequired[int]
    cy: NotRequired[int]
    cx1: NotRequired[int]
    cy1: NotRequired[int]
    type: NotRequired["draw_mask_type_t"]
    padding: NotRequired[int]


class stbtt_vertex(object):
    x: "coord_t" = ...
    """Give the"""
    y: int = ...
    cx: int = ...
    cy: int = ...
    cx1: int = ...
    cy1: int = ...
    type: "draw_mask_type_t" = ...
    padding: int = ...

    def __init__(self, fields: Optional[_type_stbtt_vertex] = {}, /):
        ...


disp_rotation_t = int
disp_render_mode_t = int
scr_load_anim_t = int
disp_t = disp_t
group_refocus_policy_t = int
key_t = int
group_focus_cb_t = None
group_edge_cb_t = None
group_t = group_t
indev_type_t = int
indev_state_t = int
indev_t = indev_t
obj_flag_t = int
obj_draw_part_type_t = int
state_t = int
part_t = int
obj_t = obj_t
obj_class_editable_t = int
obj_class_group_def_t = int
obj_class_theme_inheritable_t = int
obj_class_event_cb_t = None
obj_class_t = obj_class_t
cover_res_t = int
layer_type_t = int
layout_update_cb_t = None
scroll_snap_t = int
style_state_cmp_t = int
obj_tree_walk_res_t = int
obj_tree_walk_cb_t = obj_tree_walk_res_t
theme_apply_cb_t = None
theme_t = theme_t
draw_layer_ctx_t = draw_layer_ctx_t
draw_ctx_t = draw_ctx_t
draw_label_hint_t = draw_label_hint_t
draw_layer_flags_t = int
draw_mask_res_t = int
# _draw_mask_saved_arr_t = draw_mask_saved_t
draw_mask_type_t = int
draw_mask_line_side_t = int
_draw_mask_radius_circle_dsc_arr_t = draw_mask_radius_circle_dsc_t
draw_mask_map_param_t = draw_mask_map_param_t
img_src_t = int
img_decoder_t = img_decoder_t
img_decoder_dsc_t = img_decoder_dsc_t
_draw_sdl_composite_texture_id_t = int
draw_sdl_composite_texture_id_t = draw_sdl_composite_texture_id_t
draw_sdl_layer_ctx_t = draw_sdl_layer_ctx_t
grad_color_t = color_t
grad_t = _gradient_cache_t
font_subpx_t = int
font_t = font_t
font_fmt_txt_bitmap_format_t = int
font_fmt_txt_cmap_type_t = int
flex_align_t = int
flex_flow_t = int
grid_align_t = int
qrcodegen_Ecc = int
qrcodegen_Mask = int
qrcodegen_Mode = int
stbrp_coord = int
stbtt_kerningentry = stbtt_kerningentry
anim_enable_t = int
anim_path_cb_t = int
anim_exec_xcb_t = None
anim_custom_exec_cb_t = None
anim_ready_cb_t = None
anim_start_cb_t = None
anim_get_value_cb_t = int
anim_deleted_cb_t = None
anim_t = anim_t
anim_timeline_t = anim_timeline_t
coord_t = int
align_t = int
dir_t = int
async_cb_t = None
base_dir_t = int
color_format_t = int
palette_t = int
opa_t = int
color_t = color16_t
color_filter_cb_t = color_t
color_filter_dsc_t = color_filter_dsc_t
event_code_t = int
event_dsc_t = event_dsc_t
event_t = event_t
event_cb_t = None
fs_whence_t = int
fs_res_t = int
fs_mode_t = int
fs_drv_t = fs_drv_t
ll_node_t = int
log_level_t = int
lru_res_t = int
lru_free_t = None
lru_item_t = lru_item_t
mem_builtin_pool_t = None
blend_mode_t = int
text_decor_t = int
border_side_t = int
grad_dir_t = int
dither_mode_t = int
style_prop_t = int
style_res_t = int
timer_cb_t = None
timer_t = timer_t
tlsf_t = None
pool_t = None
text_flag_t = int
text_cmd_state_t = int
text_align_t = int
res_t = int
uintptr_t = int
intptr_t = int
_keep_pedantic_happy = int
animimg_part_t = animimg_part_t
arc_draw_part_type_t = int
arc_mode_t = int
bar_draw_part_type_t = int
bar_mode_t = int
btnmatrix_draw_part_type_t = int
btnmatrix_ctrl_t = int
btnmatrix_btn_draw_cb_t = bool
chart_draw_part_type_t = int
chart_type_t = int
chart_update_mode_t = int
chart_axis_t = int
checkbox_draw_part_type_t = int
colorwheel_mode_t = int
img_size_mode_t = int
imgbtn_state_t = int
keyboard_mode_t = int
label_long_mode_t = int
led_draw_part_type_t = int
menu_mode_header_t = int
menu_mode_root_back_btn_t = int
meter_draw_part_type_t = int
meter_indicator_type_t = int
roller_mode_t = int
slider_draw_part_type_t = int
slider_mode_t = int
span_overflow_t = int
span_mode_t = int
table_draw_part_type_t = int
table_cell_ctrl_t = int
style_selector_t = int
draw_mask_common_dsc_t = _draw_mask_common_dsc_t
draw_mask_radius_circle_dsc_t = _draw_mask_radius_circle_dsc_t
obj_style_t = int
img_decoder_info_f_t = _img_decoder_info_f_t
tlsf_walker = _tlsf_walker
bar_anim_t = _bar_anim_t
img_decoder_open_f_t = _img_decoder_open_f_t
img_decoder_read_line_f_t = _img_decoder_read_line_f_t
img_decoder_close_f_t = _img_decoder_close_f_t
obj_spec_attr_t = _obj_spec_attr_t
img_cache_entry_t = _img_cache_entry_t


def disp_create(hor_res: "coord_t", ver_res: "coord_t", /) -> "disp_t":
    """
    Create a new display with the given resolution

    :param hor_res:
    :type hor_res: "coord_t"

    :param ver_res:
    :type ver_res: "coord_t"

    :returns: pointer to a display object or
    :retval: "disp_t"
    """
    ...


def disp_remove(disp: "disp_t", /) -> None:
    """
    Remove a display

    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: None
    """
    ...


def disp_set_default(disp: "disp_t", /) -> None:
    """
    Set a default display. The new screens will be created on it by default.

    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: None
    """
    ...


def disp_get_default() -> "disp_t":
    """
    Get the default display

    :returns:
    :retval: "disp_t"
    """
    ...


def disp_get_next(disp: "disp_t", /) -> "disp_t":
    """
    Get the next display.

    :param disp:
    :type disp: "disp_t"

    :returns: the next display or NULL if no more.
        Gives the first display when the parameter is NULL.
    :retval: "disp_t"
    """
    ...


def disp_set_res(
        disp: "disp_t", hor_res: "coord_t", ver_res: "coord_t", /
) -> None:
    """
    Sets the resolution of a display.

    :param disp:
    :type disp: "disp_t"

    :param hor_res:
    :type hor_res: "coord_t"

    :param ver_res:
    :type ver_res: "coord_t"

    :returns:
    :retval: None
    """
    ...


def disp_set_physical_res(
        disp: "disp_t", hor_res: "coord_t", ver_res: "coord_t", /
) -> None:
    """
    It's not mandatory to use the whole display for LVGL,
    however in some cases physical resolution is important. For example
    the touchpad still sees whole resolution and the values needs
    to be converted to the active LVGL display area.

    :param disp:
    :type disp: "disp_t"

    :param hor_res:
    :type hor_res: "coord_t"

    :param ver_res:
    :type ver_res: "coord_t"

    :returns:
    :retval: None
    """
    ...


def disp_set_offset(disp: "disp_t", x: "coord_t", y: "coord_t", /) -> None:
    """
    If physical resolution is not the same as the normal resolution the
    offset of the active display area can be set here.

    :param disp:
    :type disp: "disp_t"

    :param x:
    :type x: "coord_t"

    :param y:
    :type y: "coord_t"

    :returns:
    :retval: None
    """
    ...


def disp_set_rotation(
        disp: "disp_t", rotation: "disp_rotation_t", sw_rotate: bool, /
) -> None:
    """
    Set the rotation of this display. LVGL will swap the
    horizontal and vertical resolutions internally.

    :param disp:
    :type disp: "disp_t"

    :param rotation:
    :type rotation: "disp_rotation_t"

    :param sw_rotate:
    :type sw_rotate: bool

    :returns:
    :retval: None
    """
    ...


def disp_set_dpi(disp: "disp_t", dpi: "coord_t", /) -> None:
    """
    Set the DPI (dot per inch) of the display.
    dpi = sqrt(hor_res^2 + ver_res^2) / diagonal"

    :param disp:
    :type disp: "disp_t"

    :param dpi:
    :type dpi: "coord_t"

    :returns:
    :retval: None
    """
    ...


def disp_get_hor_res(disp: "disp_t", /) -> "coord_t":
    """
    Get the horizontal resolution of a display.

    :param disp:
    :type disp: "disp_t"

    :returns: the horizontal resolution of the display.
    :retval: "coord_t"
    """
    ...


def disp_get_ver_res(disp: "disp_t", /) -> "coord_t":
    """
    Get the vertical resolution of a display

    :param disp:
    :type disp: "disp_t"

    :returns: the vertical resolution of the display
    :retval: "coord_t"
    """
    ...


def disp_get_physical_hor_res(disp: "disp_t", /) -> "coord_t":
    """
    Get the physical horizontal resolution of a display

    :param disp:
    :type disp: "disp_t"

    :returns: the physical horizontal resolution of the display
    :retval: "coord_t"
    """
    ...


def disp_get_physical_ver_res(disp: "disp_t", /) -> "coord_t":
    """
    Get the physical vertical resolution of a display

    :param disp:
    :type disp: "disp_t"

    :returns: the physical vertical resolution of the display
    :retval: "coord_t"
    """
    ...


def disp_get_offset_x(disp: "disp_t", /) -> "coord_t":
    """
    Get the horizontal offset from the full / physical display

    :param disp:
    :type disp: "disp_t"

    :returns: the horizontal offset from the physical display
    :retval: "coord_t"
    """
    ...


def disp_get_offset_y(disp: "disp_t", /) -> "coord_t":
    """
    Get the vertical offset from the full / physical display

    :param disp:
    :type disp: "disp_t"

    :returns: the horizontal offset from the physical display
    :retval: "coord_t"
    """
    ...


def disp_get_rotation(disp: "disp_t", /) -> "disp_rotation_t":
    """
    Get the current rotation of this display.

    :param disp:
    :type disp: "disp_t"

    :returns: the current rotation
    :retval: "disp_rotation_t"
    """
    ...


def disp_get_dpi(disp: "disp_t", /) -> "coord_t":
    """
    Get the DPI of the display

    :param disp:
    :type disp: "disp_t"

    :returns: dpi of the display
    :retval: "coord_t"
    """
    ...


def disp_set_draw_buffers(
        disp: "disp_t", buf1, buf2, buf_size_px: int,
        render_mode: "disp_render_mode_t", /
) -> None:
    """
    Set the buffers for a display

    :param disp:
    :type disp: "disp_t"

    :param buf1:
    :type buf1: None

    :param buf2:
    :type buf2: None

    :param buf_size_px:
    :type buf_size_px: int

    :param render_mode:
    :type render_mode: "disp_render_mode_t"

    :returns:
    :retval: None
    """
    ...


def disp_set_flush_cb(
        disp: "disp_t",
        flush_cb: Callable[
            ["disp_t disp", "area_t area", "color_t color_p"], None],
        /
) -> None:
    """
    Set the flush callback whcih will be
    called to copy the rendered image to the display.

    :param disp:
    :type disp: "disp_t"

    :param flush_cb:
    :type flush_cb: Callable[["disp_t disp", "area_t area", "color_t color_p"], None]

    :returns:
    :retval: None
    """
    ...


def disp_set_color_format(
        disp: "disp_t", color_format: "color_format_t", /
) -> None:
    """
    Set the color format of the display. If set to other than

    :param disp:
    :type disp: "disp_t"

    :param color_format:
    :type color_format: "color_format_t"

    :returns:
    :retval: None
    """
    ...


def disp_get_color_format(disp: "disp_t", /) -> "color_format_t":
    """
    Get the color format of the display

    :param disp:
    :type disp: "disp_t"

    :returns: the color format
    :retval: "color_format_t"
    """
    ...


def disp_set_antialaising(disp: "disp_t", en: bool, /) -> None:
    """
    Enable anti-aliasing for the render engine

    :param disp:
    :type disp: "disp_t"

    :param en:
    :type en: bool

    :returns:
    :retval: None
    """
    ...


def disp_get_antialiasing(disp: "disp_t", /) -> bool:
    """
    Get if anti-aliasing is enabled for a display or not

    :param disp:
    :type disp: "disp_t"

    :returns: true/false
    :retval: bool
    """
    ...


def disp_is_double_buffered(disp: "disp_t", /) -> bool:
    """
        :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: bool
    """
    ...


def disp_set_draw_ctx(
        disp: "disp_t", draw_ctx_init: "disp_t", draw_ctx_deinit: "disp_t",
        draw_ctx_size: int, /
) -> None:
    """
    Initialize a new draw context for the display

    :param disp:
    :type disp: "disp_t"

    :param draw_ctx_init:
    :type draw_ctx_init: "disp_t"

    :param draw_ctx_deinit:
    :type draw_ctx_deinit: "disp_t"

    :param draw_ctx_size:
    :type draw_ctx_size: int

    :returns:
    :retval: None
    """
    ...


def disp_get_scr_act(disp: "disp_t", /) -> "obj_t":
    """
    Return a pointer to the active screen on a display

    :param disp:
    :type disp: "disp_t"

    :returns: pointer to the active screen object (loaded by '
    :retval: "obj_t"
    """
    ...


def disp_get_scr_prev(disp: "disp_t", /) -> "obj_t":
    """
    Return with a pointer to the previous screen.
    Only used during screen transitions.

    :param disp:
    :type disp: "disp_t"

    :returns: pointer to the previous screen object or NULL if not used now
    :retval: "obj_t"
    """
    ...


def disp_load_scr(scr: "obj_t", /) -> None:
    """
    Make a screen active

    :param scr:
    :type scr: "obj_t"

    :returns:
    :retval: None
    """
    ...


def disp_get_layer_top(disp: "disp_t", /) -> "obj_t":
    """
    Return the top layer. The top layer is the same on all
    screens and it is above the normal screen layer.

    :param disp:
    :type disp: "disp_t"

    :returns: pointer to the top layer object
    :retval: "obj_t"
    """
    ...


def disp_get_layer_sys(disp: "disp_t", /) -> "obj_t":
    """
    Return the sys. layer. The system layer is the same on all
    screen and it is above the normal screen and the top layer.

    :param disp:
    :type disp: "disp_t"

    :returns: pointer to the sys layer object
    :retval: "obj_t"
    """
    ...


def disp_get_layer_bottom(disp: "disp_t", /) -> "obj_t":
    """
    Return the bottom layer. The bottom layer is the same on all
    screen and it is under the normal screen layer.
    It's visble only if the the screen is transparent.

    :param disp:
    :type disp: "disp_t"

    :returns: pointer to the bottom layer object
    :retval: "obj_t"
    """
    ...


def scr_load_anim(
        scr: "obj_t", anim_type: "scr_load_anim_t", time: int,
        delay: int, auto_del: bool, /
) -> None:
    """
    Switch screen with animation

    :param scr:
    :type scr: "obj_t"

    :param anim_type:
    :type anim_type: "scr_load_anim_t"

    :param time:
    :type time: int

    :param delay:
    :type delay: int

    :param auto_del:
    :type auto_del: bool

    :returns:
    :retval: None
    """
    ...


def scr_act() -> "obj_t":
    """
    Get the active screen of the default display

    :returns:
    :retval: "obj_t"
    """
    ...


def layer_top() -> "obj_t":
    """
    Get the top layer of the default display

    :returns:
    :retval: "obj_t"
    """
    ...


def layer_sys() -> "obj_t":
    """
    Get the system layer of the default display

    :returns:
    :retval: "obj_t"
    """
    ...


def layer_bottom() -> "obj_t":
    """
    Get the bottom layer of the default display

    :returns:
    :retval: "obj_t"
    """
    ...


def scr_load(scr: "obj_t", /) -> None:
    """
    Load a screen on the default display

    :param scr:
    :type scr: "obj_t"

    :returns:
    :retval: None
    """
    ...


def disp_add_event(
        disp: "disp_t", event_cb: "event_cb_t",
        filter: "event_code_t", user_data, /
) -> None:
    """
    Add an event handler to the display

    :param disp:
    :type disp: "disp_t"

    :param event_cb:
    :type event_cb: "event_cb_t"

    :param filter:
    :type filter: "event_code_t"

    :param user_data:
    :type user_data: None

    :returns:
    :retval: None
    """
    ...


def disp_get_event_count(disp: "disp_t", /) -> int:
    """
    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: int
    """
    ...


def disp_get_event_dsc(disp: "disp_t", index: int, /) -> "event_dsc_t":
    """
    :param disp:
    :type disp: "disp_t"

    :param index:
    :type index: int

    :returns:
    :retval: "event_dsc_t"
    """
    ...


def disp_remove_event(disp: "disp_t", index: int, /) -> bool:
    """
    :param disp:
    :type disp: "disp_t"

    :param index:
    :type index: int

    :returns:
    :retval: bool
    """
    ...


def disp_send_event(
        disp: "disp_t", code: "event_code_t", user_data, /
) -> "res_t":
    """
    Send amn event to a display

    :param disp:
    :type disp: "disp_t"

    :param code:
    :type code: "event_code_t"

    :param user_data:
    :type user_data: None

    :returns: LV_RES_OK: disp wasn't deleted in the event.
    :retval: "res_t"
    """
    ...


def disp_set_theme(disp: "disp_t", th: "theme_t", /) -> None:
    """
    Set the theme of a display. If there are no user created
    widgets yet the screens' theme will be updated

    :param disp:
    :type disp: "disp_t"

    :param th:
    :type th: "theme_t"

    :returns:
    :retval: None
    """
    ...


def disp_get_theme(disp: "disp_t", /) -> "theme_t":
    """
    Get the theme of a display

    :param disp:
    :type disp: "disp_t"

    :returns: the display's theme (can be NULL)
    :retval: "theme_t"
    """
    ...


def disp_get_inactive_time(disp: "disp_t", /) -> int:
    """
    Get elapsed time since last user activity on a display (e.g. click)

    :param disp:
    :type disp: "disp_t"

    :returns: elapsed ticks (milliseconds) since the last activity
    :retval: int
    """
    ...


def disp_trig_activity(disp: "disp_t", /) -> None:
    """
    Manually trigger an activity on a display

    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: None
    """
    ...


def disp_enable_invalidation(disp: "disp_t", en: bool, /) -> None:
    """
    Temporarily enable and disable the invalidation of the display.

    :param disp:
    :type disp: "disp_t"

    :param en:
    :type en: bool

    :returns:
    :retval: None
    """
    ...


def disp_is_invalidation_enabled(disp: "disp_t", /) -> bool:
    """
    Get display invalidation is enabled.

    :param disp:
    :type disp: "disp_t"

    :returns: return true if invalidation is enabled
    :retval: bool
    """
    ...


def disp_get_chroma_key_color(disp: "disp_t", /) -> "color_t":
    """
    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: "color_t"
    """
    ...


def disp_set_user_data(disp: "disp_t", user_data, /) -> None:
    """
    :param disp:
    :type disp: "disp_t"

    :param user_data:
    :type user_data: None

    :returns:
    :retval: None
    """
    ...


def disp_set_driver_data(disp: "disp_t", driver_data, /) -> None:
    """
    :param disp:
    :type disp: "disp_t"

    :param driver_data:
    :type driver_data: None

    :returns:
    :retval: None
    """
    ...


def disp_get_user_data(disp: "disp_t", /) -> None:
    """
    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: None
    """
    ...


def disp_get_driver_data(disp: "disp_t", /) -> None:
    """
    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: None
    """
    ...


def dpx(n: "coord_t", /) -> "coord_t":
    """
    Scale the given number of pixels (a distance or size)
    relative to a 160 DPI display considering the DPI of
    the default display. It ensures that e.g.

    :param n:
    :type n: "coord_t"

    :returns:
    :retval: "coord_t"
    """
    ...


def disp_dpx(disp: "disp_t", n: "coord_t", /) -> "coord_t":
    """
    Scale the given number of pixels (a distance or size) relative to a
    160 DPI display considering the DPI of the given display.
    It ensures that e.g.

    :param disp:
    :type disp: "disp_t"

    :param n:
    :type n: "coord_t"

    :returns:
    :retval: "coord_t"
    """
    ...


def group_create() -> "group_t":
    """
    Create a new object group

    :returns:
    :retval: "group_t"
    """
    ...


def group_del(group: "group_t", /) -> None:
    """
    Delete a group object

    :param group:
    :type group: "group_t"

    :returns:
    :retval: None
    """
    ...


def group_set_default(group: "group_t", /) -> None:
    """
    Set a default group. New object are added to this group
    if it's enabled in their class with

    :param group:
    :type group: "group_t"

    :returns:
    :retval: None
    """
    ...


def group_get_default() -> "group_t":
    """
    Get the default group

    :returns:
    :retval: "group_t"
    """
    ...


# noinspection PyShadowingNames
def group_add_obj(group: "group_t", obj: "obj_t", /) -> None:
    """
    Add an object to a group

    :param group:
    :type group: "group_t"

    :param obj:
    :type obj: "obj_t"

    :returns:
    :retval: None
    """
    ...


def group_swap_obj(obj1: "obj_t", obj2: "obj_t", /) -> None:
    """
    Swap 2 object in a group. The object must be in the same group

    :param obj1:
    :type obj1: "obj_t"

    :param obj2:
    :type obj2: "obj_t"

    :returns:
    :retval: None
    """
    ...


# noinspection PyShadowingNames
def group_remove_obj(obj: "obj_t", /) -> None:
    """
    Remove an object from its group

    :param obj:
    :type obj: "obj_t"

    :returns:
    :retval: None
    """
    ...


def group_remove_all_objs(group: "group_t", /) -> None:
    """
    Remove all objects from a group

    :param group:
    :type group: "group_t"

    :returns:
    :retval: None
    """
    ...


# noinspection PyShadowingNames
def group_focus_obj(obj: "obj_t", /) -> None:
    """
    Focus on an object (defocus the current)

    :param obj:
    :type obj: "obj_t"

    :returns:
    :retval: None
    """
    ...


def group_focus_next(group: "group_t", /) -> None:
    """
    Focus the next object in a group (defocus the current)

    :param group:
    :type group: "group_t"

    :returns:
    :retval: None
    """
    ...


def group_focus_prev(group: "group_t", /) -> None:
    """
    Focus the previous object in a group (defocus the current)

    :param group:
    :type group: "group_t"

    :returns:
    :retval: None
    """
    ...


def group_focus_freeze(group: "group_t", en: bool, /) -> None:
    """
    Do not let to change the focus from the current object

    :param group:
    :type group: "group_t"

    :param en:
    :type en: bool

    :returns:
    :retval: None
    """
    ...


def group_send_data(group: "group_t", c: int, /) -> "res_t":
    """
    Send a control character to the focuses object of a group

    :param group:
    :type group: "group_t"

    :param c:
    :type c: int

    :returns: result of focused object in group.
    :retval: "res_t"
    """
    ...


def group_set_focus_cb(
        group: "group_t",
        focus_cb: "group_focus_cb_t",
        /
) -> None:
    """
    Set a function for a group which will be called when a new object is focused

    :param group:
    :type group: "group_t"

    :param focus_cb:
    :type focus_cb: "group_focus_cb_t"

    :returns:
    :retval: None
    """
    ...


def group_set_edge_cb(group: "group_t", edge_cb: "group_edge_cb_t", /) -> None:
    """
    Set a function for a group which will be called when a focus edge is reached

    :param group:
    :type group: "group_t"

    :param edge_cb:
    :type edge_cb: "group_edge_cb_t"

    :returns:
    :retval: None
    """
    ...


def group_set_refocus_policy(
        group: "group_t", policy: "group_refocus_policy_t", /
) -> None:
    """
    Set whether the next or previous item in a group is
    focused if the currently focused obj is deleted.

    :param group:
    :type group: "group_t"

    :param policy:
    :type policy: "group_refocus_policy_t"

    :returns:
    :retval: None
    """
    ...


def group_set_editing(group: "group_t", edit: bool, /) -> None:
    """
    Manually set the current mode (edit or navigate).

    :param group:
    :type group: "group_t"

    :param edit:
    :type edit: bool

    :returns:
    :retval: None
    """
    ...


def group_set_wrap(group: "group_t", en: bool, /) -> None:
    """
    Set whether focus next/prev will allow wrapping
    from first->last or last->first object.

    :param group:
    :type group: "group_t"

    :param en:
    :type en: bool

    :returns:
    :retval: None
    """
    ...


def group_get_focused(group: "group_t", /) -> "obj_t":
    """
    Get the focused object or NULL if there isn't one

    :param group:
    :type group: "group_t"

    :returns: pointer to the focused object
    :retval: "obj_t"
    """
    ...


def group_get_focus_cb(group: "group_t", /) -> "group_focus_cb_t":
    """
    Get the focus callback function of a group

    :param group:
    :type group: "group_t"

    :returns: the call back function or NULL if not set
    :retval: "group_focus_cb_t"
    """
    ...


def group_get_edge_cb(group: "group_t", /) -> "group_edge_cb_t":
    """
    Get the edge callback function of a group

    :param group:
    :type group: "group_t"

    :returns: the call back function or NULL if not set
    :retval: "group_edge_cb_t"
    """
    ...


def group_get_editing(group: "group_t", /) -> bool:
    """
    Get the current mode (edit or navigate).

    :param group:
    :type group: "group_t"

    :returns: true: edit mode; false: navigate mode
    :retval: bool
    """
    ...


def group_get_wrap(group: "group_t", /) -> bool:
    """
    Get whether focus next/prev will allow wrapping
    from first->last or last->first object.

    :param group:
    :type group: "group_t"

    :returns:
    :retval: bool
    """
    ...


def group_get_obj_count(group: "group_t", /) -> int:
    """
    Get the number of object in the group

    :param group:
    :type group: "group_t"

    :returns: number of objects in the group
    :retval: int
    """
    ...


def indev_create() -> "indev_t":
    """
    :returns:
    :retval: "indev_t"
    """
    ...


def indev_delete(indev: "indev_t", /) -> None:
    """
    Remove the provided input device. Make sure not to use the
    provided input device afterwards anymore.

    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: None
    """
    ...


def indev_get_next(indev: "indev_t", /) -> "indev_t":
    """
    Get the next input device.

    :param indev:
    :type indev: "indev_t"

    :returns: the next input device or NULL if there are no more.
        Provide the first input device when the parameter is NULL
    :retval: "indev_t"
    """
    ...


def indev_read_timer_cb(timer: "timer_t", /) -> None:
    """
    Called periodically to read the input devices

    :param timer:
    :type timer: "timer_t"

    :returns:
    :retval: None
    """
    ...


def indev_enable(indev: "indev_t", en: bool, /) -> None:
    """
    Enable or disable one or all input devices (default enabled)

    :param indev:
    :type indev: "indev_t"

    :param en:
    :type en: bool

    :returns:
    :retval: None
    """
    ...


def indev_get_act() -> "indev_t":
    """
    Get the currently processed input device.
    Can be used in action functions too.

    :returns:
    :retval: "indev_t"
    """
    ...


def indev_set_type(indev: "indev_t", indev_type: "indev_type_t", /) -> None:
    """
    Set the type of an input device

    :param indev:
    :type indev: "indev_t"

    :param indev_type:
    :type indev_type: "indev_type_t"

    :returns:
    :retval: None
    """
    ...


def indev_set_read_cb(
        indev: "indev_t",
        read_cb: Callable[["indev_t indev", "indev_data_t data"], None], /
) -> None:
    """
    :param indev:
    :type indev: "indev_t"

    :param read_cb:
    :type read_cb: Callable[["indev_t indev", "indev_data_t data"], None]

    :returns:
    :retval: None
    """
    ...


def indev_set_user_data(indev: "indev_t", user_data, /) -> None:
    """
    :param indev:
    :type indev: "indev_t"

    :param user_data:
    :type user_data: None

    :returns:
    :retval: None
    """
    ...


def indev_set_driver_data(indev: "indev_t", driver_data, /) -> None:
    """
    :param indev:
    :type indev: "indev_t"

    :param driver_data:
    :type driver_data: None

    :returns:
    :retval: None
    """
    ...


def indev_get_type(indev: "indev_t", /) -> "indev_type_t":
    """
    Get the type of an input device

    :param indev:
    :type indev: "indev_t"

    :returns: the type of the input device from
    :retval: "indev_type_t"
    """
    ...


def indev_get_state(indev: "indev_t", /) -> "indev_state_t":
    """
    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: "indev_state_t"
    """
    ...


def indev_get_group(indev: "indev_t", /) -> "group_t":
    """
    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: "group_t"
    """
    ...


def indev_get_disp(indev: "indev_t", /) -> "disp_t":
    """
    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: "disp_t"
    """
    ...


def indev_set_disp(indev: "indev_t", disp: "disp_t", /) -> None:
    """
    :param indev:
    :type indev: "indev_t"

    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: None
    """
    ...


def indev_get_user_data(indev: "indev_t", /) -> None:
    """
    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: None
    """
    ...


def indev_get_driver_data(indev: "indev_t", /) -> None:
    """
    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: None
    """
    ...


# noinspection PyShadowingNames
def indev_reset(indev: "indev_t", obj: "obj_t", /) -> None:
    """
    Reset one or all input devices

    :param indev:
    :type indev: "indev_t"

    :param obj:
    :type obj: "obj_t"

    :returns:
    :retval: None
    """
    ...


def indev_reset_long_press(indev: "indev_t", /) -> None:
    """
    Reset the long press state of an input device

    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: None
    """
    ...


def indev_set_cursor(indev: "indev_t", cur_obj: "obj_t", /) -> None:
    """
    Set a cursor for a pointer input device
    (for LV_INPUT_TYPE_POINTER and LV_INPUT_TYPE_BUTTON)

    :param indev:
    :type indev: "indev_t"

    :param cur_obj:
    :type cur_obj: "obj_t"

    :returns:
    :retval: None
    """
    ...


def indev_set_group(indev: "indev_t", group: "group_t", /) -> None:
    """
    Set a destination group for a keypad input device (for LV_INDEV_TYPE_KEYPAD)

    :param indev:
    :type indev: "indev_t"

    :param group:
    :type group: "group_t"

    :returns:
    :retval: None
    """
    ...


def indev_set_button_points(
        indev: "indev_t", points: Callable[["[]"], "point_t"], /
) -> None:
    """
    Set the an array of points for LV_INDEV_TYPE_BUTTON.
    These points will be assigned to the buttons to press a
    specific point on the screen

    :param indev:
    :type indev: "indev_t"

    :param points:
    :type points: Callable[["[]"], "point_t"]

    :returns:
    :retval: None
    """
    ...


def indev_get_point(indev: "indev_t", point: "point_t", /) -> None:
    """
    Get the last point of an input device
    (for LV_INDEV_TYPE_POINTER and LV_INDEV_TYPE_BUTTON)

    :param indev:
    :type indev: "indev_t"

    :param point:
    :type point: "point_t"

    :returns:
    :retval: None
    """
    ...


def indev_get_gesture_dir(indev: "indev_t", /) -> "dir_t":
    """
    Get the current gesture direct

    :param indev:
    :type indev: "indev_t"

    :returns: current gesture direct
    :retval: "dir_t"
    """
    ...


def indev_get_key(indev: "indev_t", /) -> int:
    """
    Get the last pressed key of an input device (for LV_INDEV_TYPE_KEYPAD)

    :param indev:
    :type indev: "indev_t"

    :returns: the last pressed key (0 on error)
    :retval: int
    """
    ...


def indev_get_scroll_dir(indev: "indev_t", /) -> "dir_t":
    """
    Check the current scroll direction of an input device
    (for LV_INDEV_TYPE_POINTER and LV_INDEV_TYPE_BUTTON)

    :param indev:
    :type indev: "indev_t"

    :returns: LV_DIR_NONE: no scrolling now LV_DIR_HOR/VER
    :retval: "dir_t"
    """
    ...


def indev_get_scroll_obj(indev: "indev_t", /) -> "obj_t":
    """
    Get the currently scrolled object
    (for LV_INDEV_TYPE_POINTER and LV_INDEV_TYPE_BUTTON)

    :param indev:
    :type indev: "indev_t"

    :returns: pointer to the currently scrolled object or
        NULL if no scrolling by this indev
    :retval: "obj_t"
    """
    ...


def indev_get_vect(indev: "indev_t", point: "point_t", /) -> None:
    """
    Get the movement vector of an input device
    (for LV_INDEV_TYPE_POINTER and LV_INDEV_TYPE_BUTTON)

    :param indev:
    :type indev: "indev_t"

    :param point:
    :type point: "point_t"

    :returns:
    :retval: None
    """
    ...


def indev_wait_release(indev: "indev_t", /) -> None:
    """
    Do nothing until the next release

    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: None
    """
    ...


def indev_get_obj_act() -> "obj_t":
    """
    Gets a pointer to the currently active object in the
    currently processed input device.

    :returns:
    :retval: "obj_t"
    """
    ...


def indev_get_read_timer(indev: "indev_t", /) -> "timer_t":
    """
    Get a pointer to the indev read timer to modify its parameters with

    :param indev:
    :type indev: "indev_t"

    :returns:
    :retval: "timer_t"
    """
    ...


def indev_scroll_throw_predict(indev: "indev_t", dir: "dir_t", /) -> "coord_t":
    """
    Predict where would a scroll throw end

    :param indev:
    :type indev: "indev_t"

    :param dir:
    :type dir: "dir_t"

    :returns: the difference compared to the current
        position when the throw would be finished
    :retval: "coord_t"
    """
    ...


def init() -> None:
    """
    Initialize LVGL library.
    Should be called before any other LVGL related function.

    :returns:
    :retval: None
    """
    ...


def deinit() -> None:
    """
    Deinit the 'lv' library Currently only implemented when not
    using custom allocators, or GC is enabled.

    :returns:
    :retval: None
    """
    ...


def is_initialized() -> bool:
    """
    Returns whether the 'lv' library is currently initialized

    :returns:
    :retval: bool
    """
    ...


def obj_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a base object (a rectangle)

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the new object
    :retval: "obj_t"
    """
    ...


def obj_class_create_obj(class_p: "obj_class_t", parent: "obj_t", /) -> "obj_t":
    """
    Create an object form a class descriptor

    :param class_p:
    :type class_p: "obj_class_t"

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created object
    :retval: "obj_t"
    """
    ...


def obj_event_base(class_p: "obj_class_t", e: "event_t", /) -> "res_t":
    """
    Used by the widgets internally to call the ancestor widget types's
    event handler

    :param class_p:
    :type class_p: "obj_class_t"

    :param e:
    :type e: "event_t"

    :returns: LV_RES_OK: the target object was not deleted in the event;
        LV_RES_INV: it was deleted in the event_code
    :retval: "res_t"
    """
    ...


def event_get_target_obj(e: "event_t", /) -> "obj_t":
    """
    Get the object originally targeted by the event.
    It's the same even if the event is bubbled.

    :param e:
    :type e: "event_t"

    :returns: the target of the event_code
    :retval: "obj_t"
    """
    ...


def event_get_current_target_obj(e: "event_t", /) -> "obj_t":
    """
    Get the current target of the event. It's the object which event handler
    being called. If the event is not bubbled it's the same as "normal" target.

    :param e:
    :type e: "event_t"

    :returns: pointer to the current target of the event_code
    :retval: "obj_t"
    """
    ...


def event_get_indev(e: "event_t", /) -> "indev_t":
    """
    Get the input device passed as parameter to indev related events.

    :param e:
    :type e: "event_t"

    :returns: the indev that triggered the event or NULL if
        called on a not indev related event
    :retval: "indev_t"
    """
    ...


def event_get_draw_part_dsc(e: "event_t", /) -> "obj_draw_part_dsc_t":
    """
    Get the part draw descriptor passed as parameter to

    :param e:
    :type e: "event_t"

    :returns:
    :retval: "obj_draw_part_dsc_t"
    """
    ...


def event_get_draw_ctx(e: "event_t", /) -> "draw_ctx_t":
    """
    Get the draw context which should be the
    first parameter of the draw functions. Namely:

    :param e:
    :type e: "event_t"

    :returns:
    :retval: "draw_ctx_t"
    """
    ...


def event_get_old_size(e: "event_t", /) -> "area_t":
    """
    Get the old area of the object before its size was changed. Can be used in

    :param e:
    :type e: "event_t"

    :returns:
    :retval: "area_t"
    """
    ...


def event_get_key(e: "event_t", /) -> int:
    """
    Get the key passed as parameter to an event. Can be used in

    :param e:
    :type e: "event_t"

    :returns:
    :retval: int
    """
    ...


def event_get_scroll_anim(e: "event_t", /) -> "anim_t":
    """
    Get the animation descriptor of a scrolling. Can be used in

    :param e:
    :type e: "event_t"

    :returns:
    :retval: "anim_t"
    """
    ...


def event_set_ext_draw_size(e: "event_t", size: "coord_t", /) -> None:
    """
    Set the new extra draw size. Can be used in

    :param e:
    :type e: "event_t"

    :param size:
    :type size: "coord_t"

    :returns:
    :retval: None
    """
    ...


def event_get_self_size_info(e: "event_t", /) -> "point_t":
    """
    Get a pointer to an

    :param e:
    :type e: "event_t"

    :returns:
    :retval: "point_t"
    """
    ...


def event_get_hit_test_info(e: "event_t", /) -> "hit_test_info_t":
    """
    Get a pointer to an

    :param e:
    :type e: "event_t"

    :returns:
    :retval: "hit_test_info_t"
    """
    ...


def event_get_cover_area(e: "event_t", /) -> "area_t":
    """
    Get a pointer to an area which should be examined whether
    the object fully covers it or not. Can be used in

    :param e:
    :type e: "event_t"

    :returns:
    :retval: "area_t"
    """
    ...


def event_set_cover_res(e: "event_t", res: "cover_res_t", /) -> None:
    """
    Set the result of cover checking. Can be used in

    :param e:
    :type e: "event_t"

    :param res:
    :type res: "cover_res_t"

    :returns:
    :retval: None
    """
    ...


def layout_register(cb: "layout_update_cb_t", user_data, /) -> int:
    """
    Register a new layout

    :param cb:
    :type cb: "layout_update_cb_t"

    :param user_data:
    :type user_data: None

    :returns: the ID of the new layout
    :retval: int
    """
    ...


def clamp_width(
        width: "coord_t", min_width: "coord_t",
        max_width: "coord_t", ref_width: "coord_t", /
) -> "coord_t":
    """
    Clamp a width between min and max width.
    If the min/max width is in percentage value use the ref_width

    :param width:
    :type width: "coord_t"

    :param min_width:
    :type min_width: "coord_t"

    :param max_width:
    :type max_width: "coord_t"

    :param ref_width:
    :type ref_width: "coord_t"

    :returns: the clamped width
    :retval: "coord_t"
    """
    ...


def clamp_height(
        height: "coord_t", min_height: "coord_t",
        max_height: "coord_t", ref_height: "coord_t", /
) -> "coord_t":
    """
    Clamp a height between min and max height.
    If the min/max height is in percentage value use the ref_height

    :param height:
    :type height: "coord_t"

    :param min_height:
    :type min_height: "coord_t"

    :param max_height:
    :type max_height: "coord_t"

    :param ref_height:
    :type ref_height: "coord_t"

    :returns: the clamped height
    :retval: "coord_t"
    """
    ...


def obj_report_style_change(style: "style_t", /) -> None:
    """
    Notify all object if a style is modified

    :param style:
    :type style: "style_t"

    :returns:
    :retval: None
    """
    ...


def obj_enable_style_refresh(en: bool, /) -> None:
    """
    Enable or disable automatic style refreshing when a new
    style is added/removed to/from an object or any other style change happens.

    :param en:
    :type en: bool

    :returns:
    :retval: None
    """
    ...


def obj_style_get_selector_state(selector: "style_selector_t", /) -> "state_t":
    """
    :param selector:
    :type selector: "style_selector_t"

    :returns:
    :retval: "state_t"
    """
    ...


def obj_style_get_selector_part(selector: "style_selector_t", /) -> "part_t":
    """
    :param selector:
    :type selector: "style_selector_t"

    :returns:
    :retval: "part_t"
    """
    ...


def obj_del_anim_ready_cb(a: "anim_t", /) -> None:
    """
    A function to be easily used in animation ready callback to
    delete an object when the animation is ready

    :param a:
    :type a: "anim_t"

    :returns:
    :retval: None
    """
    ...


def refr_now(disp: "disp_t", /) -> None:
    """
    Redraw the invalidated areas now. Normally the
    redrawing is periodically executed in

    :param disp:
    :type disp: "disp_t"

    :returns:
    :retval: None
    """
    ...


# noinspection PyShadowingNames
def obj_redraw(draw_ctx: "draw_ctx_t", obj: "obj_t", /) -> None:
    """
    Redrawn on object an all its children using the passed draw context

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param obj:
    :type obj: "obj_t"

    :returns:
    :retval: None
    """
    ...


# noinspection PyShadowingNames
def theme_get_from_obj(obj: "obj_t", /) -> "theme_t":
    """
    Get the theme assigned to the display of the object

    :param obj:
    :type obj: "obj_t"

    :returns: the theme of the object's display (can be NULL)
    :retval: "theme_t"
    """
    ...


# noinspection PyShadowingNames
def theme_apply(obj: "obj_t", /) -> None:
    """
    Apply the active theme on an object

    :param obj:
    :type obj: "obj_t"

    :returns:
    :retval: None
    """
    ...


def theme_set_parent(new_theme: "theme_t", parent: "theme_t", /) -> None:
    """
    Set a base theme for a theme. The styles from the base
    them will be added before the styles of the current theme.
    Arbitrary long chain of themes can be created by setting base themes.

    :param new_theme:
    :type new_theme: "theme_t"

    :param parent:
    :type parent: "theme_t"

    :returns:
    :retval: None
    """
    ...


def theme_set_apply_cb(
        theme: "theme_t", apply_cb: "theme_apply_cb_t", /
) -> None:
    """
    Set an apply callback for a theme.
    The apply callback is used to add styles to different objects

    :param theme:
    :type theme: "theme_t"

    :param apply_cb:
    :type apply_cb: "theme_apply_cb_t"

    :returns:
    :retval: None
    """
    ...


# noinspection PyShadowingNames
def theme_get_font_small(obj: "obj_t", /) -> "font_t":
    """
    Get the small font of the theme

    :param obj:
    :type obj: "obj_t"

    :returns: pointer to the font
    :retval: "font_t"
    """
    ...


# noinspection PyShadowingNames
def theme_get_font_normal(obj: "obj_t", /) -> "font_t":
    """
    Get the normal font of the theme

    :param obj:
    :type obj: "obj_t"

    :returns: pointer to the font
    :retval: "font_t"
    """
    ...


# noinspection PyShadowingNames
def theme_get_font_large(obj: "obj_t", /) -> "font_t":
    """
    Get the subtitle font of the theme

    :param obj:
    :type obj: "obj_t"

    :returns: pointer to the font
    :retval: "font_t"
    """
    ...


# noinspection PyShadowingNames
def theme_get_color_primary(obj: "obj_t", /) -> "color_t":
    """
    Get the primary color of the theme

    :param obj:
    :type obj: "obj_t"

    :returns: the color
    :retval: "color_t"
    """
    ...


# noinspection PyShadowingNames
def theme_get_color_secondary(obj: "obj_t", /) -> "color_t":
    """
    Get the secondary color of the theme

    :param obj:
    :type obj: "obj_t"

    :returns: the color
    :retval: "color_t"
    """
    ...


def draw_init() -> None:
    """
        :returns:
    :retval: None
    """
    ...


def draw_wait_for_finish(draw_ctx: "draw_ctx_t", /) -> None:
    """
        :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :returns:
    :retval: None
    """
    ...


def draw_arc(
        draw_ctx: "draw_ctx_t", dsc: "draw_arc_dsc_t", center: "point_t",
        radius: int, start_angle: int, end_angle: int, /
) -> None:
    """
    Draw an arc. (Can draw pie too with great thickness.)

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param dsc:
    :type dsc: "draw_arc_dsc_t"

    :param center:
    :type center: "point_t"

    :param radius:
    :type radius: int

    :param start_angle:
    :type start_angle: int

    :param end_angle:
    :type end_angle: int

    :returns:
    :retval: None
    """
    ...


def draw_arc_get_area(
        x: "coord_t", y: "coord_t", radius: int, start_angle: int,
        end_angle: int, w: "coord_t", rounded: bool, area: "area_t", /
) -> None:
    """
    Get an area the should be invalidated when the arcs angle
    changed between start_angle and end_ange

    :param x:
    :type x: "coord_t"

    :param y:
    :type y: "coord_t"

    :param radius:
    :type radius: int

    :param start_angle:
    :type start_angle: int

    :param end_angle:
    :type end_angle: int

    :param w:
    :type w: "coord_t"

    :param rounded:
    :type rounded: bool

    :param area:
    :type area: "area_t"

    :returns:
    :retval: None
    """
    ...


def draw_img(
        draw_ctx: "draw_ctx_t", dsc: "draw_img_dsc_t",
        coords: "area_t", src, /
) -> None:
    """
    Draw an image

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param dsc:
    :type dsc: "draw_img_dsc_t"

    :param coords:
    :type coords: "area_t"

    :param src:
    :type src: None

    :returns:
    :retval: None
    """
    ...


def draw_img_decoded(
        draw_ctx: "draw_ctx_t", dsc: "draw_img_dsc_t", coords: "area_t",
        map_p: int, sup: "draw_img_sup_t", color_format: "color_format_t", /
) -> None:
    """
    Draw a decoded image

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param dsc:
    :type dsc: "draw_img_dsc_t"

    :param coords:
    :type coords: "area_t"

    :param map_p:
    :type map_p: int

    :param sup:
    :type sup: "draw_img_sup_t"

    :param color_format:
    :type color_format: "color_format_t"

    :returns:
    :retval: None
    """
    ...


def img_src_get_type(src, /) -> "img_src_t":
    """
    Get the type of an image source

    :param src:
    :type src: None

    :returns: type of the image source LV_IMG_SRC_VARIABLE/FILE/SYMBOL/UNKNOWN
    :retval: "img_src_t"
    """
    ...


def draw_label(
        draw_ctx: "draw_ctx_t", dsc: "draw_label_dsc_t",
        coords: "area_t", txt: str, hint: "draw_label_hint_t", /
) -> None:
    """
    Write a text

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param dsc:
    :type dsc: "draw_label_dsc_t"

    :param coords:
    :type coords: "area_t"

    :param txt:
    :type txt: str

    :param hint:
    :type hint: "draw_label_hint_t"

    :returns:
    :retval: None
    """
    ...


def draw_letter(
        draw_ctx: "draw_ctx_t", dsc: "draw_label_dsc_t",
        pos_p: "point_t", letter: int, /
) -> None:
    """
    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param dsc:
    :type dsc: "draw_label_dsc_t"

    :param pos_p:
    :type pos_p: "point_t"

    :param letter:
    :type letter: int

    :returns:
    :retval: None
    """
    ...


def draw_layer_create(
        draw_ctx: "draw_ctx_t", layer_area: "area_t",
        flags: "draw_layer_flags_t", /
) -> "draw_layer_ctx_t":
    """
    Create a new layer context.
    It is used to start and independent rendering
    session with the current draw_ctx

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param layer_area:
    :type layer_area: "area_t"

    :param flags:
    :type flags: "draw_layer_flags_t"

    :returns: pointer to the layer context, or NULL on error
    :retval: "draw_layer_ctx_t"
    """
    ...


def draw_layer_adjust(
        draw_ctx: "draw_ctx_t", layer_ctx: "draw_layer_ctx_t",
        flags: "draw_layer_flags_t", /
) -> None:
    """
    Adjust the layer_ctx and/or draw_ctx based on the

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param layer_ctx:
    :type layer_ctx: "draw_layer_ctx_t"

    :param flags:
    :type flags: "draw_layer_flags_t"

    :returns:
    :retval: None
    """
    ...


def draw_layer_blend(
        draw_ctx: "draw_ctx_t", layer_ctx: "draw_layer_ctx_t",
        draw_dsc: "draw_img_dsc_t", /
) -> None:
    """
    Blend a rendered layer to

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param layer_ctx:
    :type layer_ctx: "draw_layer_ctx_t"

    :param draw_dsc:
    :type draw_dsc: "draw_img_dsc_t"

    :returns:
    :retval: None
    """
    ...


def draw_layer_destroy(
        draw_ctx: "draw_ctx_t", layer_ctx: "draw_layer_ctx_t", /
) -> None:
    """
    Destroy a layer context.

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param layer_ctx:
    :type layer_ctx: "draw_layer_ctx_t"

    :returns:
    :retval: None
    """
    ...


def draw_line(
        draw_ctx: "draw_ctx_t", dsc: "draw_line_dsc_t",
        point1: "point_t", point2: "point_t", /
) -> None:
    """
    Draw a line

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param dsc:
    :type dsc: "draw_line_dsc_t"

    :param point1:
    :type point1: "point_t"

    :param point2:
    :type point2: "point_t"

    :returns:
    :retval: None
    """
    ...


def draw_mask_add(param, custom_id, /) -> int:
    """
    Add a draw mask. Everything drawn after it
    (until removing the mask) will be affected by the mask.

    :param param:
    :type param: None

    :param custom_id:
    :type custom_id: None

    :returns: the an integer, the ID of the mask. Can be used in
    :retval: int
    """
    ...


def draw_mask_remove_id(id: int, /) -> None:
    """
    Remove a mask with a given ID

    :param id:
    :type id: int

    :returns: the parameter of the removed mask. If more masks have
    :retval: None
    """
    ...


def draw_mask_remove_custom(custom_id, /) -> None:
    """
    Remove all mask with a given custom ID

    :param custom_id:
    :type custom_id: None

    :returns: return the parameter of the removed mask. If more masks have
    :retval: None
    """
    ...


def draw_mask_free_param(p, /) -> None:
    """
    Free the data from the parameter. It's called inside

    :param p:
    :type p: None

    :returns:
    :retval: None
    """
    ...


def draw_mask_map_init(
        param: "draw_mask_map_param_t", coords: "area_t", map: "opa_t", /
) -> None:
    """
    Initialize a map mask.

    :param param:
    :type param: "draw_mask_map_param_t"

    :param coords:
    :type coords: "area_t"

    :param map:
    :type map: "opa_t"

    :returns:
    :retval: None
    """
    ...


def draw_rect(
        draw_ctx: "draw_ctx_t", dsc: "draw_rect_dsc_t", coords: "area_t", /
) -> None:
    """
    Draw a rectangle

    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param dsc:
    :type dsc: "draw_rect_dsc_t"

    :param coords:
    :type coords: "area_t"

    :returns:
    :retval: None
    """
    ...


def draw_transform(
        draw_ctx: "draw_ctx_t", dest_area: "area_t", src_buf,
        src_w: "coord_t", src_h: "coord_t", src_stride: "coord_t",
        draw_dsc: "draw_img_dsc_t", sup: "draw_img_sup_t",
        cf: "color_format_t", cbuf: "color_t", abuf: "opa_t", /
) -> None:
    """
    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param dest_area:
    :type dest_area: "area_t"

    :param src_buf:
    :type src_buf: None

    :param src_w:
    :type src_w: "coord_t"

    :param src_h:
    :type src_h: "coord_t"

    :param src_stride:
    :type src_stride: "coord_t"

    :param draw_dsc:
    :type draw_dsc: "draw_img_dsc_t"

    :param sup:
    :type sup: "draw_img_sup_t"

    :param cf:
    :type cf: "color_format_t"

    :param cbuf:
    :type cbuf: "color_t"

    :param abuf:
    :type abuf: "opa_t"

    :returns:
    :retval: None
    """
    ...


def draw_polygon(
        draw_ctx: "draw_ctx_t", draw_dsc: "draw_rect_dsc_t",
        points: Callable[["[]"], "point_t"], point_cnt: int, /
) -> None:
    """
    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param draw_dsc:
    :type draw_dsc: "draw_rect_dsc_t"

    :param points:
    :type points: Callable[["[]"], "point_t"]

    :param point_cnt:
    :type point_cnt: int

    :returns:
    :retval: None
    """
    ...


def draw_triangle(
        draw_ctx: "draw_ctx_t", draw_dsc: "draw_rect_dsc_t",
        points: Callable[["[]"], "point_t"], /
) -> None:
    """
    :param draw_ctx:
    :type draw_ctx: "draw_ctx_t"

    :param draw_dsc:
    :type draw_dsc: "draw_rect_dsc_t"

    :param points:
    :type points: Callable[["[]"], "point_t"]

    :returns:
    :retval: None
    """
    ...


def img_cache_set_size(new_entry_cnt: int, /) -> None:
    """
    Set the number of images to be cached. More cached images mean more
    opened image at same time which might mean more memory usage.
    E.g. if 20 PNG or JPG images are open in the RAM they consume
    memory while opened in the cache.

    :param new_entry_cnt:
    :type new_entry_cnt: int

    :returns:
    :retval: None
    """
    ...


def img_cache_invalidate_src(src, /) -> None:
    """
    Invalidate an image source in the cache. Useful if the
    image source is updated therefore it needs to be cached again.

    :param src:
    :type src: None

    :returns:
    :retval: None
    """
    ...


def img_decoder_get_info(src, header: "img_header_t", /) -> "res_t":
    """
    Get information about an image. Try the created image decoder one
    by one. Once one is able to get info that info will be used.

    :param src:
    :type src: None

    :param header:
    :type header: "img_header_t"

    :returns: LV_RES_OK: success; LV_RES_INV: wasn't
        able to get info about the image
    :retval: "res_t"
    """
    ...


def img_decoder_open(
        dsc: "img_decoder_dsc_t", src, color: "color_t", frame_id: int, /
) -> "res_t":
    """
    Open an image. Try the created image decoders one by one.
    Once one is able to open the image that decoder is saved in

    :param dsc:
    :type dsc: "img_decoder_dsc_t"

    :param src:
    :type src: None

    :param color:
    :type color: "color_t"

    :param frame_id:
    :type frame_id: int

    :returns:
    :retval: "res_t"
    """
    ...


def img_decoder_read_line(
        dsc: "img_decoder_dsc_t", x: "coord_t", y: "coord_t",
        len: "coord_t", buf: int, /
) -> "res_t":
    """
    Read a line from an opened image

    :param dsc:
    :type dsc: "img_decoder_dsc_t"

    :param x:
    :type x: "coord_t"

    :param y:
    :type y: "coord_t"

    :param len:
    :type len: "coord_t"

    :param buf:
    :type buf: int

    :returns: LV_RES_OK: success; LV_RES_INV: an error occurred
    :retval: "res_t"
    """
    ...


def img_decoder_close(dsc: "img_decoder_dsc_t", /) -> None:
    """
    Close a decoding session

    :param dsc:
    :type dsc: "img_decoder_dsc_t"

    :returns:
    :retval: None
    """
    ...


def img_decoder_create() -> "img_decoder_t":
    """
    Create a new image decoder

    :returns:
    :retval: "img_decoder_t"
    """
    ...


def img_decoder_delete(decoder: "img_decoder_t", /) -> None:
    """
    Delete an image decoder

    :param decoder:
    :type decoder: "img_decoder_t"

    :returns:
    :retval: None
    """
    ...


def img_decoder_set_info_cb(
        decoder: "img_decoder_t", info_cb: "img_decoder_info_f_t", /
) -> None:
    """
    Set a callback to get information about the image

    :param decoder:
    :type decoder: "img_decoder_t"

    :param info_cb:
    :type info_cb: "img_decoder_info_f_t"

    :returns:
    :retval: None
    """
    ...


def img_decoder_set_open_cb(
        decoder: "img_decoder_t", open_cb: "img_decoder_open_f_t", /
) -> None:
    """
    Set a callback to open an image

    :param decoder:
    :type decoder: "img_decoder_t"

    :param open_cb:
    :type open_cb: "img_decoder_open_f_t"

    :returns:
    :retval: None
    """
    ...


def img_decoder_set_read_line_cb(
        decoder: "img_decoder_t",
        read_line_cb: "img_decoder_read_line_f_t", /
) -> None:
    """
    Set a callback to a decoded line of an image

    :param decoder:
    :type decoder: "img_decoder_t"

    :param read_line_cb:
    :type read_line_cb: "img_decoder_read_line_f_t"

    :returns:
    :retval: None
    """
    ...


def img_decoder_set_close_cb(
        decoder: "img_decoder_t",
        close_cb: "img_decoder_close_f_t", /
) -> None:
    """
    Set a callback to close a decoding session. E.g.
    close files and free other resources.

    :param decoder:
    :type decoder: "img_decoder_t"

    :param close_cb:
    :type close_cb: "img_decoder_close_f_t"

    :returns:
    :retval: None
    """
    ...


def img_decoder_built_in_info(
        decoder: "img_decoder_t", src, header: "img_header_t", /
) -> "res_t":
    """
    Get info about a built-in image

    :param decoder:
    :type decoder: "img_decoder_t"

    :param src:
    :type src: None

    :param header:
    :type header: "img_header_t"

    :returns: LV_RES_OK: the info is successfully stored in
    :retval: "res_t"
    """
    ...


def img_decoder_built_in_open(
        decoder: "img_decoder_t", dsc: "img_decoder_dsc_t", /
) -> "res_t":
    """
    Open a built in image

    :param decoder:
    :type decoder: "img_decoder_t"

    :param dsc:
    :type dsc: "img_decoder_dsc_t"

    :returns: LV_RES_OK: the info is successfully stored in
    :retval: "res_t"
    """
    ...


def img_decoder_built_in_close(
        decoder: "img_decoder_t", dsc: "img_decoder_dsc_t", /
) -> None:
    """
    Close the pending decoding. Free resources etc.

    :param decoder:
    :type decoder: "img_decoder_t"

    :param dsc:
    :type dsc: "img_decoder_dsc_t"

    :returns:
    :retval: None
    """
    ...


def gradient_calculate(
        dsc: "grad_dsc_t", range: "coord_t", frac: "coord_t", /
) -> "grad_color_t":
    """
    Compute the color in the given gradient and fraction Gradient are
    specified in a virtual [0-255] range, so this function scales the
    virtual range to the given range

    :param dsc:
    :type dsc: "grad_dsc_t"

    :param range:
    :type range: "coord_t"

    :param frac:
    :type frac: "coord_t"

    :returns:
    :retval: "grad_color_t"
    """
    ...


def gradient_set_cache_size(max_bytes: int, /) -> None:
    """
    Set the gradient cache size

    :param max_bytes:
    :type max_bytes: int

    :returns:
    :retval: None
    """
    ...


def gradient_free_cache() -> None:
    """
    Free the gradient cache

    :returns:
    :retval: None
    """
    ...


def gradient_get(
        gradient: "grad_dsc_t", w: "coord_t", h: "coord_t", /
) -> "grad_t":
    """
    Get a gradient cache from the given parameters

    :param gradient:
    :type gradient: "grad_dsc_t"

    :param w:
    :type w: "coord_t"

    :param h:
    :type h: "coord_t"

    :returns:
    :retval: "grad_t"
    """
    ...


def gradient_cleanup(grad: "grad_t", /) -> None:
    """
    Clean up the gradient item after it was get with

    :param grad:
    :type grad: "grad_t"

    :returns:
    :retval: None
    """
    ...


def font_get_glyph_bitmap(font_p: "font_t", letter: int, /) -> int:
    """
    Return with the bitmap of a font.

    :param font_p:
    :type font_p: "font_t"

    :param letter:
    :type letter: int

    :returns: pointer to the bitmap of the letter
    :retval: int
    """
    ...


def font_get_glyph_dsc(
        font_p: "font_t", dsc_out: "font_glyph_dsc_t",
        letter: int, letter_next: int, /
) -> bool:
    """
    Get the descriptor of a glyph

    :param font_p:
    :type font_p: "font_t"

    :param dsc_out:
    :type dsc_out: "font_glyph_dsc_t"

    :param letter:
    :type letter: int

    :param letter_next:
    :type letter_next: int

    :returns: true: descriptor is successfully loaded into
    :retval: bool
    """
    ...


def font_get_glyph_width(
        font: "font_t", letter: int, letter_next: int, /
) -> int:
    """
    Get the width of a glyph with kerning

    :param font:
    :type font: "font_t"

    :param letter:
    :type letter: int

    :param letter_next:
    :type letter_next: int

    :returns: the width of the glyph
    :retval: int
    """
    ...


def font_get_line_height(font_p: "font_t", /) -> "coord_t":
    """
    Get the line height of a font. All characters fit into this height

    :param font_p:
    :type font_p: "font_t"

    :returns: the height of a font
    :retval: "coord_t"
    """
    ...


def font_default() -> "font_t":
    """
    Just a wrapper around LV_FONT_DEFAULT because it might
    be more convenient to use a function in some cases

    :returns:
    :retval: "font_t"
    """
    ...


def font_get_bitmap_fmt_txt(font: "font_t", letter: int, /) -> int:
    """
    Used as

    :param font:
    :type font: "font_t"

    :param letter:
    :type letter: int

    :returns:
    :retval: int
    """
    ...


def font_get_glyph_dsc_fmt_txt(
        font: "font_t", dsc_out: "font_glyph_dsc_t",
        unicode_letter: int, unicode_letter_next: int, /
) -> bool:
    """
    Used as

    :param font:
    :type font: "font_t"

    :param dsc_out:
    :type dsc_out: "font_glyph_dsc_t"

    :param unicode_letter:
    :type unicode_letter: int

    :param unicode_letter_next:
    :type unicode_letter_next: int

    :returns:
    :retval: bool
    """
    ...


def font_load(fontName: str, /) -> "font_t":
    """
    :param fontName:
    :type fontName: str

    :returns:
    :retval: "font_t"
    """
    ...


def font_free(font: "font_t", /) -> None:
    """
    :param font:
    :type font: "font_t"

    :returns:
    :retval: None
    """
    ...


def tick_get() -> int:
    """
    Get the elapsed milliseconds since start up

    :returns:
    :retval: int
    """
    ...


def tick_elaps(prev_tick: int, /) -> int:
    """
    Get the elapsed milliseconds since a previous time stamp

    :param prev_tick:
    :type prev_tick: int

    :returns: the elapsed milliseconds since 'prev_tick'
    :retval: int
    """
    ...


def flex_init() -> None:
    """
    Initialize a flex layout the default values

    :returns:
    :retval: None
    """
    ...


def grid_init() -> None:
    """
        :returns:
    :retval: None
    """
    ...


def grid_fr(x: int, /) -> "coord_t":
    """
    Just a wrapper to

    :param x:
    :type x: int

    :returns:
    :retval: "coord_t"
    """
    ...


def code128_estimate_len(s: str, /) -> int:
    """
    :param s:
    :type s: str

    :returns:
    :retval: int
    """
    ...


def code128_encode_gs1(s: str, out: int, maxlength: int, /) -> int:
    """
    :param s:
    :type s: str

    :param out:
    :type out: int

    :param maxlength:
    :type maxlength: int

    :returns:
    :retval: int
    """
    ...


def code128_encode_raw(s: str, out: int, maxlength: int, /) -> int:
    """
    :param s:
    :type s: str

    :param out:
    :type out: int

    :param maxlength:
    :type maxlength: int

    :returns:
    :retval: int
    """
    ...


def qrcodegen_encodeText(
        text: str, tempBuffer: Callable[["[]"], int],
        qrcode: Callable[["[]"], int], ecl: "qrcodegen_Ecc",
        minVersion: int, maxVersion: int, mask: "qrcodegen_Mask",
        boostEcl: bool, /
) -> bool:
    """
    :param text:
    :type text: str

    :param tempBuffer:
    :type tempBuffer: Callable[["[]"], int]

    :param qrcode:
    :type qrcode: Callable[["[]"], int]

    :param ecl:
    :type ecl: "qrcodegen_Ecc"

    :param minVersion:
    :type minVersion: int

    :param maxVersion:
    :type maxVersion: int

    :param mask:
    :type mask: "qrcodegen_Mask"

    :param boostEcl:
    :type boostEcl: bool

    :returns:
    :retval: bool
    """
    ...


def qrcodegen_encodeBinary(
        dataAndTemp: Callable[["[]"], int], dataLen: int,
        qrcode: Callable[["[]"], int], ecl: "qrcodegen_Ecc",
        minVersion: int, maxVersion: int, mask: "qrcodegen_Mask",
        boostEcl: bool, /
) -> bool:
    """
    :param dataAndTemp:
    :type dataAndTemp: Callable[["[]"], int]

    :param dataLen:
    :type dataLen: int

    :param qrcode:
    :type qrcode: Callable[["[]"], int]

    :param ecl:
    :type ecl: "qrcodegen_Ecc"

    :param minVersion:
    :type minVersion: int

    :param maxVersion:
    :type maxVersion: int

    :param mask:
    :type mask: "qrcodegen_Mask"

    :param boostEcl:
    :type boostEcl: bool

    :returns:
    :retval: bool
    """
    ...


def qrcodegen_isAlphanumeric(text: str, /) -> bool:
    """
    :param text:
    :type text: str

    :returns:
    :retval: bool
    """
    ...


def qrcodegen_isNumeric(text: str, /) -> bool:
    """
    :param text:
    :type text: str

    :returns:
    :retval: bool
    """
    ...


def qrcodegen_calcSegmentBufferSize(
        mode: "qrcodegen_Mode", numChars: int, /
) -> int:
    """
    :param mode:
    :type mode: "qrcodegen_Mode"

    :param numChars:
    :type numChars: int

    :returns:
    :retval: int
    """
    ...


def qrcodegen_makeBytes(
        data: Callable[["[]"], int], len: int, buf: Callable[["[]"], int], /
) -> "qrcodegen_Segment":
    """
    :param data:
    :type data: Callable[["[]"], int]

    :param len:
    :type len: int

    :param buf:
    :type buf: Callable[["[]"], int]

    :returns:
    :retval: "qrcodegen_Segment"
    """
    ...


def qrcodegen_makeNumeric(
        digits: str, buf: Callable[["[]"], int], /
) -> "qrcodegen_Segment":
    """
    :param digits:
    :type digits: str

    :param buf:
    :type buf: Callable[["[]"], int]

    :returns:
    :retval: "qrcodegen_Segment"
    """
    ...


def qrcodegen_makeAlphanumeric(
        text: str, buf: Callable[["[]"], int], /
) -> "qrcodegen_Segment":
    """
    :param text:
    :type text: str

    :param buf:
    :type buf: Callable[["[]"], int]

    :returns:
    :retval: "qrcodegen_Segment"
    """
    ...


def qrcodegen_makeEci(
        assignVal: int, buf: Callable[["[]"], int], /
) -> "qrcodegen_Segment":
    """
    :param assignVal:
    :type assignVal: int

    :param buf:
    :type buf: Callable[["[]"], int]

    :returns:
    :retval: "qrcodegen_Segment"
    """
    ...


def qrcodegen_getSize(qrcode: Callable[["[]"], int], /) -> int:
    """
    :param qrcode:
    :type qrcode: Callable[["[]"], int]

    :returns:
    :retval: int
    """
    ...


def qrcodegen_getModule(
        qrcode: Callable[["[]"], int], x: int, y: int, /
) -> bool:
    """
    :param qrcode:
    :type qrcode: Callable[["[]"], int]

    :param x:
    :type x: int

    :param y:
    :type y: int

    :returns:
    :retval: bool
    """
    ...


def qrcodegen_version2size(version: int, /) -> int:
    """
    :param version:
    :type version: int

    :returns:
    :retval: int
    """
    ...


def qrcodegen_getMinFitVersion(ecl: "qrcodegen_Ecc", dataLen: int, /) -> int:
    """
    :param ecl:
    :type ecl: "qrcodegen_Ecc"

    :param dataLen:
    :type dataLen: int

    :returns:
    :retval: int
    """
    ...


def stbtt_GetNumberOfFonts(data: str, /) -> int:
    """
    :param data:
    :type data: str

    :returns:
    :retval: int
    """
    ...


def stbtt_GetFontOffsetForIndex(data: str, index: int, /) -> int:
    """
    :param data:
    :type data: str

    :param index:
    :type index: int

    :returns:
    :retval: int
    """
    ...


def stbtt_FreeBitmap(bitmap: int, userdata, /) -> None:
    """
    :param bitmap:
    :type bitmap: int

    :param userdata:
    :type userdata: None

    :returns:
    :retval: None
    """
    ...


def stbtt_FreeSDF(bitmap: int, userdata, /) -> None:
    """
    :param bitmap:
    :type bitmap: int

    :param userdata:
    :type userdata: None

    :returns:
    :retval: None
    """
    ...


def stbtt_FindMatchingFont(fontdata: str, name: str, flags: int, /) -> int:
    """
    :param fontdata:
    :type fontdata: str

    :param name:
    :type name: str

    :param flags:
    :type flags: int

    :returns:
    :retval: int
    """
    ...


def stbtt_CompareUTF8toUTF16_bigendian(
        s1: str, len1: int, s2: str, s2offs: "int", len2: int, /
) -> int:
    """
    :param s1:
    :type s1: str

    :param len1:
    :type len1: int

    :param s2:
    :type s2: str

    :param s2offs:
    :type s2offs: "int"

    :param len2:
    :type len2: int

    :returns:
    :retval: int
    """
    ...


def task_handler() -> int:
    """
    :returns:
    :retval: int
    """
    ...


def anim_init(a: "anim_t", /) -> None:
    """
    Initialize an animation variable. E.g.: lv_anim_t a;
    lv_anim_init(&a); lv_anim_set_...(&a); lv_anim_start(&a);

    :param a:
    :type a: "anim_t"

    :returns:
    :retval: None
    """
    ...


def anim_set_var(a: "anim_t", var, /) -> None:
    """
    Set a variable to animate

    :param a:
    :type a: "anim_t"

    :param var:
    :type var: None

    :returns:
    :retval: None
    """
    ...


def anim_set_exec_cb(a: "anim_t", exec_cb: "anim_exec_xcb_t", /) -> None:
    """
    Set a function to animate

    :param a:
    :type a: "anim_t"

    :param exec_cb:
    :type exec_cb: "anim_exec_xcb_t"

    :returns:
    :retval: None
    """
    ...


def anim_set_time(a: "anim_t", duration: int, /) -> None:
    """
    Set the duration of an animation

    :param a:
    :type a: "anim_t"

    :param duration:
    :type duration: int

    :returns:
    :retval: None
    """
    ...


def anim_set_delay(a: "anim_t", delay: int, /) -> None:
    """
    Set a delay before starting the animation

    :param a:
    :type a: "anim_t"

    :param delay:
    :type delay: int

    :returns:
    :retval: None
    """
    ...


def anim_set_values(a: "anim_t", start: int, end: int, /) -> None:
    """
    Set the start and end values of an animation

    :param a:
    :type a: "anim_t"

    :param start:
    :type start: int

    :param end:
    :type end: int

    :returns:
    :retval: None
    """
    ...


def anim_set_custom_exec_cb(
        a: "anim_t", exec_cb: "anim_custom_exec_cb_t", /
) -> None:
    """
    Similar to

    :param a:
    :type a: "anim_t"

    :param exec_cb:
    :type exec_cb: "anim_custom_exec_cb_t"

    :returns:
    :retval: None
    """
    ...


def anim_set_path_cb(a: "anim_t", path_cb: "anim_path_cb_t", /) -> None:
    """
    Set the path (curve) of the animation.

    :param a:
    :type a: "anim_t"

    :param path_cb:
    :type path_cb: "anim_path_cb_t"

    :returns:
    :retval: None
    """
    ...


def anim_set_start_cb(a: "anim_t", start_cb: "anim_start_cb_t", /) -> None:
    """
    Set a function call when the animation really starts (considering

    :param a:
    :type a: "anim_t"

    :param start_cb:
    :type start_cb: "anim_start_cb_t"

    :returns:
    :retval: None
    """
    ...


def anim_set_get_value_cb(
        a: "anim_t", get_value_cb: "anim_get_value_cb_t", /
) -> None:
    """
    Set a function to use the current value of the variable
    and make start and end value relative to the returned current value.

    :param a:
    :type a: "anim_t"

    :param get_value_cb:
    :type get_value_cb: "anim_get_value_cb_t"

    :returns:
    :retval: None
    """
    ...


def anim_set_ready_cb(a: "anim_t", ready_cb: "anim_ready_cb_t", /) -> None:
    """
    Set a function call when the animation is ready

    :param a:
    :type a: "anim_t"

    :param ready_cb:
    :type ready_cb: "anim_ready_cb_t"

    :returns:
    :retval: None
    """
    ...


def anim_set_deleted_cb(
        a: "anim_t", deleted_cb: "anim_deleted_cb_t", /
) -> None:
    """
    Set a function call when the animation is deleted.

    :param a:
    :type a: "anim_t"

    :param deleted_cb:
    :type deleted_cb: "anim_deleted_cb_t"

    :returns:
    :retval: None
    """
    ...


def anim_set_playback_time(a: "anim_t", time: int, /) -> None:
    """
    Make the animation to play back to when the forward direction is ready

    :param a:
    :type a: "anim_t"

    :param time:
    :type time: int

    :returns:
    :retval: None
    """
    ...


def anim_set_playback_delay(a: "anim_t", delay: int, /) -> None:
    """
    Make the animation to play back to when the forward direction is ready

    :param a:
    :type a: "anim_t"

    :param delay:
    :type delay: int

    :returns:
    :retval: None
    """
    ...


def anim_set_repeat_count(a: "anim_t", cnt: int, /) -> None:
    """
    Make the animation repeat itself.

    :param a:
    :type a: "anim_t"

    :param cnt:
    :type cnt: int

    :returns:
    :retval: None
    """
    ...


def anim_set_repeat_delay(a: "anim_t", delay: int, /) -> None:
    """
    Set a delay before repeating the animation.

    :param a:
    :type a: "anim_t"

    :param delay:
    :type delay: int

    :returns:
    :retval: None
    """
    ...


def anim_set_early_apply(a: "anim_t", en: bool, /) -> None:
    """
    Set a whether the animation's should be applied
    immediately or only when the delay expired.

    :param a:
    :type a: "anim_t"

    :param en:
    :type en: bool

    :returns:
    :retval: None
    """
    ...


def anim_set_user_data(a: "anim_t", user_data, /) -> None:
    """
    Set the custom user data field of the animation.

    :param a:
    :type a: "anim_t"

    :param user_data:
    :type user_data: None

    :returns:
    :retval: None
    """
    ...


def anim_get_delay(a: "anim_t", /) -> int:
    """
    Get a delay before starting the animation

    :param a:
    :type a: "anim_t"

    :returns: delay before the animation in milliseconds
    :retval: int
    """
    ...


def anim_get_playtime(a: "anim_t", /) -> int:
    """
    Get the time used to play the animation.

    :param a:
    :type a: "anim_t"

    :returns: the play time in milliseconds.
    :retval: int
    """
    ...


def anim_get_time(a: "anim_t", /) -> int:
    """
    Get the duration of an animation

    :param a:
    :type a: "anim_t"

    :returns: the duration of the animation in milliseconds
    :retval: int
    """
    ...


def anim_get_repeat_count(a: "anim_t", /) -> int:
    """
    Get the repeat count of the animation.

    :param a:
    :type a: "anim_t"

    :returns: the repeat count or
    :retval: int
    """
    ...


def anim_get_user_data(a: "anim_t", /) -> None:
    """
    Get the user_data field of the animation

    :param a:
    :type a: "anim_t"

    :returns: the pointer to the custom user_data of the animation
    :retval: None
    """
    ...


def anim_del(var, exec_cb: "anim_exec_xcb_t", /) -> bool:
    """
    Delete an animation of a variable with a given animator function

    :param var:
    :type var: None

    :param exec_cb:
    :type exec_cb: "anim_exec_xcb_t"

    :returns: true: at least 1 animation is deleted,
        false: no animation is deleted
    :retval: bool
    """
    ...


def anim_del_all() -> None:
    """
    Delete all the animations

    :returns:
    :retval: None
    """
    ...


def anim_get(var, exec_cb: "anim_exec_xcb_t", /) -> "anim_t":
    """
    Get the animation of a variable and its

    :param var:
    :type var: None

    :param exec_cb:
    :type exec_cb: "anim_exec_xcb_t"

    :returns:
    :retval: "anim_t"
    """
    ...


def anim_get_timer() -> "timer_t":
    """
    Get global animation refresher timer.

    :returns:
    :retval: "timer_t"
    """
    ...


def anim_custom_del(a: "anim_t", exec_cb: "anim_custom_exec_cb_t", /) -> bool:
    """
    Delete an animation by getting the animated variable from

    :param a:
    :type a: "anim_t"

    :param exec_cb:
    :type exec_cb: "anim_custom_exec_cb_t"

    :returns:
    :retval: bool
    """
    ...


def anim_custom_get(
        a: "anim_t", exec_cb: "anim_custom_exec_cb_t", /
) -> "anim_t":
    """
    Get the animation of a variable and its

    :param a:
    :type a: "anim_t"

    :param exec_cb:
    :type exec_cb: "anim_custom_exec_cb_t"

    :returns:
    :retval: "anim_t"
    """
    ...


def anim_count_running() -> int:
    """
    Get the number of currently running animations

    :returns:
    :retval: int
    """
    ...


def anim_speed_to_time(speed: int, start: int, end: int, /) -> int:
    """
    Calculate the time of an animation with a given
    speed and the start and end values

    :param speed:
    :type speed: int

    :param start:
    :type start: int

    :param end:
    :type end: int

    :returns: the required time [ms] for the
        animation with the given parameters
    :retval: int
    """
    ...


def anim_refr_now() -> None:
    """
    Manually refresh the state of the animations.
    Useful to make the animations running in a blocking process where

    :returns: lv_refr_now()
    :retval: None
    """
    ...


def anim_path_linear(a: "anim_t", /) -> int:
    """
    Calculate the current value of an animation applying linear characteristic

    :param a:
    :type a: "anim_t"

    :returns: the current value to set
    :retval: int
    """
    ...


def anim_path_ease_in(a: "anim_t", /) -> int:
    """
    Calculate the current value of an animation slowing down the start phase

    :param a:
    :type a: "anim_t"

    :returns: the current value to set
    :retval: int
    """
    ...


def anim_path_ease_out(a: "anim_t", /) -> int:
    """
    Calculate the current value of an animation slowing down the end phase

    :param a:
    :type a: "anim_t"

    :returns: the current value to set
    :retval: int
    """
    ...


def anim_path_ease_in_out(a: "anim_t", /) -> int:
    """
    Calculate the current value of an animation applying
    an "S" characteristic (cosine)

    :param a:
    :type a: "anim_t"

    :returns: the current value to set
    :retval: int
    """
    ...


def anim_path_overshoot(a: "anim_t", /) -> int:
    """
    Calculate the current value of an animation with overshoot at the end

    :param a:
    :type a: "anim_t"

    :returns: the current value to set
    :retval: int
    """
    ...


def anim_path_bounce(a: "anim_t", /) -> int:
    """
    Calculate the current value of an animation with 3 bounces

    :param a:
    :type a: "anim_t"

    :returns: the current value to set
    :retval: int
    """
    ...


def anim_path_step(a: "anim_t", /) -> int:
    """
    Calculate the current value of an animation applying step characteristic.
    (Set end value on the end of the animation)

    :param a:
    :type a: "anim_t"

    :returns: the current value to set
    :retval: int
    """
    ...


def anim_timeline_create() -> "anim_timeline_t":
    """
    Create an animation timeline.

    :returns:
    :retval: "anim_timeline_t"
    """
    ...


def anim_timeline_del(at: "anim_timeline_t", /) -> None:
    """
    Delete animation timeline.

    :param at:
    :type at: "anim_timeline_t"

    :returns:
    :retval: None
    """
    ...


def anim_timeline_add(
        at: "anim_timeline_t", start_time: int, a: "anim_t", /
) -> None:
    """
    Add animation to the animation timeline.

    :param at:
    :type at: "anim_timeline_t"

    :param start_time:
    :type start_time: int

    :param a:
    :type a: "anim_t"

    :returns:
    :retval: None
    """
    ...


def anim_timeline_start(at: "anim_timeline_t", /) -> int:
    """
    Start the animation timeline.

    :param at:
    :type at: "anim_timeline_t"

    :returns: total time spent in animation timeline.
    :retval: int
    """
    ...


def anim_timeline_stop(at: "anim_timeline_t", /) -> None:
    """
    Stop the animation timeline.

    :param at:
    :type at: "anim_timeline_t"

    :returns:
    :retval: None
    """
    ...


def anim_timeline_set_reverse(at: "anim_timeline_t", reverse: bool, /) -> None:
    """
    Set the playback direction of the animation timeline.

    :param at:
    :type at: "anim_timeline_t"

    :param reverse:
    :type reverse: bool

    :returns:
    :retval: None
    """
    ...


def anim_timeline_set_progress(at: "anim_timeline_t", progress: int, /) -> None:
    """
    Set the progress of the animation timeline.

    :param at:
    :type at: "anim_timeline_t"

    :param progress:
    :type progress: int

    :returns:
    :retval: None
    """
    ...


def anim_timeline_get_playtime(at: "anim_timeline_t", /) -> int:
    """
    Get the time used to play the animation timeline.

    :param at:
    :type at: "anim_timeline_t"

    :returns: total time spent in animation timeline.
    :retval: int
    """
    ...


def anim_timeline_get_reverse(at: "anim_timeline_t", /) -> bool:
    """
    Get whether the animation timeline is played in reverse.

    :param at:
    :type at: "anim_timeline_t"

    :returns: return true if it is reverse playback.
    :retval: bool
    """
    ...


def pct(x: "coord_t", /) -> "coord_t":
    """
    Convert a percentage value to

    :param x:
    :type x: "coord_t"

    :returns:
    :retval: "coord_t"
    """
    ...


def async_call(async_xcb: "async_cb_t", user_data, /) -> "res_t":
    """
    Call an asynchronous function the next time lv_timer_handler() is run.
    This function is likely to return

    :param async_xcb:
    :type async_xcb: "async_cb_t"

    :param user_data:
    :type user_data: None

    :returns:
    :retval: "res_t"
    """
    ...


def async_call_cancel(async_xcb: "async_cb_t", user_data, /) -> "res_t":
    """
    Cancel an asynchronous function call

    :param async_xcb:
    :type async_xcb: "async_cb_t"

    :param user_data:
    :type user_data: None

    :returns:
    :retval: "res_t"
    """
    ...


def bidi_calculate_align(
        align: "text_align_t", base_dir: "base_dir_t", txt: str, /
) -> None:
    """
    For compatibility if LV_USE_BIDI = 0 Get the real text alignment
    from the a text alignment, base direction and a text.

    :param align:
    :type align: "text_align_t"

    :param base_dir:
    :type base_dir: "base_dir_t"

    :param txt:
    :type txt: str

    :returns:
    :retval: None
    """
    ...


def color_to_native(
        src_buf: int, src_cf: "color_format_t", c_out: "color_t",
        a_out: "opa_t", alpha_color: "color_t", px_cnt: int, /
) -> None:
    """
    :param src_buf:
    :type src_buf: int

    :param src_cf:
    :type src_cf: "color_format_t"

    :param c_out:
    :type c_out: "color_t"

    :param a_out:
    :type a_out: "opa_t"

    :param alpha_color:
    :type alpha_color: "color_t"

    :param px_cnt:
    :type px_cnt: int

    :returns:
    :retval: None
    """
    ...


def color_from_native(
        src_buf: "color_t", dest_buf: int, dest_cf: "color_format_t",
        px_cnt: int, /
) -> None:
    """
    :param src_buf:
    :type src_buf: "color_t"

    :param dest_buf:
    :type dest_buf: int

    :param dest_cf:
    :type dest_cf: "color_format_t"

    :param px_cnt:
    :type px_cnt: int

    :returns:
    :retval: None
    """
    ...


def color_from_native_alpha(
        src_buf: int, dest_buf: int, dest_cf: "color_format_t",
        px_cnt: int, /
) -> None:
    """
    :param src_buf:
    :type src_buf: int

    :param dest_buf:
    :type dest_buf: int

    :param dest_cf:
    :type dest_cf: "color_format_t"

    :param px_cnt:
    :type px_cnt: int

    :returns:
    :retval: None
    """
    ...


def color_format_get_size(src_cf: "color_format_t", /) -> int:
    """
    Get the pixel size of a color format in bits

    :param src_cf:
    :type src_cf: "color_format_t"

    :returns: the pixel size in bits
    :retval: int
    """
    ...


def color_format_has_alpha(src_cf: "color_format_t", /) -> bool:
    """
    Check if a color format has alpha channel or not

    :param src_cf:
    :type src_cf: "color_format_t"

    :returns: true: has alpha channel; false: doesn't have alpha channel
    :retval: bool
    """
    ...


def color_set_int(c: "color_t", v: int, /) -> None:
    """
    :param c:
    :type c: "color_t"

    :param v:
    :type v: int

    :returns:
    :retval: None
    """
    ...


def color_to_int(c: "color_t", /) -> int:
    """
    :param c:
    :type c: "color_t"

    :returns:
    :retval: int
    """
    ...


def color8_from_buf(buf: int, /) -> "color8_t":
    """
    :param buf:
    :type buf: int

    :returns:
    :retval: "color8_t"
    """
    ...


def color16_from_buf(buf: int, /) -> "color16_t":
    """
    :param buf:
    :type buf: int

    :returns:
    :retval: "color16_t"
    """
    ...


def color24_from_buf(buf: int, /) -> "color24_t":
    """
    :param buf:
    :type buf: int

    :returns:
    :retval: "color24_t"
    """
    ...


def color32_from_buf(buf: int, /) -> "color32_t":
    """
    :param buf:
    :type buf: int

    :returns:
    :retval: "color32_t"
    """
    ...


def color_from_buf(buf: int, /) -> "color_t":
    """
    :param buf:
    :type buf: int

    :returns:
    :retval: "color_t"
    """
    ...


def color_eq(c1: "color_t", c2: "color_t", /) -> bool:
    """
    :param c1:
    :type c1: "color_t"

    :param c2:
    :type c2: "color_t"

    :returns:
    :retval: bool
    """
    ...


def color_to8(color: "color_t", /) -> "color8_t":
    """
    :param color:
    :type color: "color_t"

    :returns:
    :retval: "color8_t"
    """
    ...


def color_to16(color: "color_t", /) -> "color16_t":
    """
    :param color:
    :type color: "color_t"

    :returns:
    :retval: "color16_t"
    """
    ...


def color_to24(color: "color_t", /) -> "color24_t":
    """
    :param color:
    :type color: "color_t"

    :returns:
    :retval: "color24_t"
    """
    ...


def color_to32(color: "color_t", /) -> "color32_t":
    """
    :param color:
    :type color: "color_t"

    :returns:
    :retval: "color32_t"
    """
    ...


def color_brightness(color: "color_t", /) -> int:
    """
    Get the brightness of a color

    :param color:
    :type color: "color_t"

    :returns: the brightness [0..255]
    :retval: int
    """
    ...


def color_make(r: int, g: int, b: int, /) -> "color_t":
    """
    :param r:
    :type r: int

    :param g:
    :type g: int

    :param b:
    :type b: int

    :returns:
    :retval: "color_t"
    """
    ...


def color_hex(c: int, /) -> "color_t":
    """
    :param c:
    :type c: int

    :returns:
    :retval: "color_t"
    """
    ...


def color_hex3(c: int, /) -> "color_t":
    """
    :param c:
    :type c: int

    :returns:
    :retval: "color_t"
    """
    ...


def color_filter_dsc_init(
        dsc: "color_filter_dsc_t", cb: "color_filter_cb_t", /
) -> None:
    """
    :param dsc:
    :type dsc: "color_filter_dsc_t"

    :param cb:
    :type cb: "color_filter_cb_t"

    :returns:
    :retval: None
    """
    ...


def color_lighten(c: "color_t", lvl: "opa_t", /) -> "color_t":
    """
    :param c:
    :type c: "color_t"

    :param lvl:
    :type lvl: "opa_t"

    :returns:
    :retval: "color_t"
    """
    ...


def color_darken(c: "color_t", lvl: "opa_t", /) -> "color_t":
    """
    :param c:
    :type c: "color_t"

    :param lvl:
    :type lvl: "opa_t"

    :returns:
    :retval: "color_t"
    """
    ...


def color_change_lightness(c: "color_t", lvl: "opa_t", /) -> "color_t":
    """
    :param c:
    :type c: "color_t"

    :param lvl:
    :type lvl: "opa_t"

    :returns:
    :retval: "color_t"
    """
    ...


def color_hsv_to_rgb(h: int, s: int, v: int, /) -> "color_t":
    """
    Convert a HSV color to RGB

    :param h:
    :type h: int

    :param s:
    :type s: int

    :param v:
    :type v: int

    :returns: the given RGB color in RGB (with LV_COLOR_DEPTH depth)
    :retval: "color_t"
    """
    ...


def color_rgb_to_hsv(r8: int, g8: int, b8: int, /) -> "color_hsv_t":
    """
    Convert a 32-bit RGB color to HSV

    :param r8:
    :type r8: int

    :param g8:
    :type g8: int

    :param b8:
    :type b8: int

    :returns: the given RGB color in HSV
    :retval: "color_hsv_t"
    """
    ...


def color_to_hsv(color: "color_t", /) -> "color_hsv_t":
    """
    Convert a color to HSV

    :param color:
    :type color: "color_t"

    :returns: the given color in HSV
    :retval: "color_hsv_t"
    """
    ...


def palette_main(p: "palette_t", /) -> "color_t":
    """
    :param p:
    :type p: "palette_t"

    :returns:
    :retval: "color_t"
    """
    ...


def color_white() -> "color_t":
    """
    :returns:
    :retval: "color_t"
    """
    ...


def color_black() -> "color_t":
    """
    :returns:
    :retval: "color_t"
    """
    ...


def palette_lighten(p: "palette_t", lvl: int, /) -> "color_t":
    """
    :param p:
    :type p: "palette_t"

    :param lvl:
    :type lvl: int

    :returns:
    :retval: "color_t"
    """
    ...


def palette_darken(p: "palette_t", lvl: int, /) -> "color_t":
    """
    :param p:
    :type p: "palette_t"

    :param lvl:
    :type lvl: int

    :returns:
    :retval: "color_t"
    """
    ...


def event_dsc_get_cb(dsc: "event_dsc_t", /) -> "event_cb_t":
    """
    :param dsc:
    :type dsc: "event_dsc_t"

    :returns:
    :retval: "event_cb_t"
    """
    ...


def event_dsc_get_user_data(dsc: "event_dsc_t", /) -> None:
    """
    :param dsc:
    :type dsc: "event_dsc_t"

    :returns:
    :retval: None
    """
    ...


def event_get_target(e: "event_t", /) -> None:
    """
    Get the object originally targeted by the event.
    It's the same even if the event is bubbled.

    :param e:
    :type e: "event_t"

    :returns: the target of the event_code
    :retval: None
    """
    ...


def event_get_current_target(e: "event_t", /) -> None:
    """
    Get the current target of the event. It's the object
     which event handler being called. If the event is not
     bubbled it's the same as "normal" target.

    :param e:
    :type e: "event_t"

    :returns: pointer to the current target of the event_code
    :retval: None
    """
    ...


def event_get_code(e: "event_t", /) -> "event_code_t":
    """
    Get the event code of an event

    :param e:
    :type e: "event_t"

    :returns: the event code. (E.g.
    :retval: "event_code_t"
    """
    ...


def event_get_param(e: "event_t", /) -> None:
    """
    Get the parameter passed when the event was sent

    :param e:
    :type e: "event_t"

    :returns: pointer to the parameter
    :retval: None
    """
    ...


def event_get_user_data(e: "event_t", /) -> None:
    """
    Get the user_data passed when the event was registered on the object

    :param e:
    :type e: "event_t"

    :returns: pointer to the user_data
    :retval: None
    """
    ...


def event_stop_bubbling(e: "event_t", /) -> None:
    """
    Stop the event from bubbling. This is only valid when
    called in the middle of an event processing chain.

    :param e:
    :type e: "event_t"

    :returns:
    :retval: None
    """
    ...


def event_stop_processing(e: "event_t", /) -> None:
    """
    Stop processing this event. This is only valid when
    called in the middle of an event processing chain.

    :param e:
    :type e: "event_t"

    :returns:
    :retval: None
    """
    ...


def event_register_id() -> int:
    """
    :returns:
    :retval: int
    """
    ...


def fs_drv_init(drv: "fs_drv_t", /) -> None:
    """
    Initialize a file system driver with default values.
    It is used to ensure all fields have known values and not
    memory junk. After it you can set the fields.

    :param drv:
    :type drv: "fs_drv_t"

    :returns:
    :retval: None
    """
    ...


def fs_drv_register(drv: "fs_drv_t", /) -> None:
    """
    Add a new drive

    :param drv:
    :type drv: "fs_drv_t"

    :returns:
    :retval: None
    """
    ...


def fs_get_drv(letter: int, /) -> "fs_drv_t":
    """
    Give a pointer to a driver from its letter

    :param letter:
    :type letter: int

    :returns: pointer to a driver or NULL if not found
    :retval: "fs_drv_t"
    """
    ...


def fs_is_ready(letter: int, /) -> bool:
    """
    Test if a drive is ready or not. If the

    :param letter:
    :type letter: int

    :returns:
    :retval: bool
    """
    ...


def fs_get_letters(buf: int, /) -> int:
    """
    Fill a buffer with the letters of existing drivers

    :param buf:
    :type buf: int

    :returns: the buffer
    :retval: int
    """
    ...


def fs_get_ext(fn: str, /) -> str:
    """
    Return with the extension of the filename

    :param fn:
    :type fn: str

    :returns: pointer to the beginning extension or empty string if no extension
    :retval: str
    """
    ...


def fs_up(path: int, /) -> int:
    """
    Step up one level

    :param path:
    :type path: int

    :returns: the truncated file name
    :retval: int
    """
    ...


def fs_get_last(path: str, /) -> str:
    """
    Get the last element of a path (e.g. U:/folder/file -> file)

    :param path:
    :type path: str

    :returns: pointer to the beginning of the last element in the path
    :retval: str
    """
    ...


def lru_create(
        cache_size: int, average_length: int, value_free: "lru_free_t",
        key_free: "lru_free_t", /
) -> "lru_t":
    """
    :param cache_size:
    :type cache_size: int

    :param average_length:
    :type average_length: int

    :param value_free:
    :type value_free: "lru_free_t"

    :param key_free:
    :type key_free: "lru_free_t"

    :returns:
    :retval: "lru_t"
    """
    ...


def mem_init_builtin() -> None:
    """
    Initialize the dyn_mem module (work memory and other variables)

    :returns:
    :retval: None
    """
    ...


def mem_deinit_builtin() -> None:
    """
    Clean up the memory buffer which frees all the allocated memories.

    :returns:
    :retval: None
    """
    ...


def mem_builtin_add_pool(mem, bytes: int, /) -> "mem_builtin_pool_t":
    """
    Add a new memory block to the builtin memory pool.

    :param mem:
    :type mem: None

    :param bytes:
    :type bytes: int

    :returns: pointer to lv_mem_builtin_pool handle
    :retval: "mem_builtin_pool_t"
    """
    ...


def mem_builtin_remove_pool(pool: "mem_builtin_pool_t", /) -> None:
    """
    Remove the memory pool.

    :param pool:
    :type pool: "mem_builtin_pool_t"

    :returns:
    :retval: None
    """
    ...


def malloc_builtin(size: int, /) -> None:
    """
    :param size:
    :type size: int

    :returns:
    :retval: None
    """
    ...


def realloc_builtin(p, new_size: int, /) -> None:
    """
    :param p:
    :type p: None

    :param new_size:
    :type new_size: int

    :returns:
    :retval: None
    """
    ...


def free_builtin(p, /) -> None:
    """
    :param p:
    :type p: None

    :returns:
    :retval: None
    """
    ...


def mem_test_builtin() -> "res_t":
    """
    :returns:
    :retval: "res_t"
    """
    ...


def bezier3(t: int, u0: int, u1: int, u2: int, u3: int, /) -> int:
    """
    Calculate a value of a Cubic Bezier function.

    :param t:
    :type t: int

    :param u0:
    :type u0: int

    :param u1:
    :type u1: int

    :param u2:
    :type u2: int

    :param u3:
    :type u3: int

    :returns: the value calculated from the given
        parameters in range of [0..LV_BEZIER_VAL_MAX]
    :retval: int
    """
    ...


def atan2(x: int, y: int, /) -> int:
    """
    Calculate the atan2 of a vector.

    :param x:
    :type x: int

    :param y:
    :type y: int

    :returns: the angle in degree calculated from the
        given parameters in range of [0..360]
    :retval: int
    """
    ...


def pow(base: int, exp: int, /) -> int:
    """
    Calculate the integer exponents.

    :param base:
    :type base: int

    :param exp:
    :type exp: int

    :returns: base raised to the power exponent
    :retval: int
    """
    ...


def rand(min: int, max: int, /) -> int:
    """
    Get a pseudo random number in the given range

    :param min:
    :type min: int

    :param max:
    :type max: int

    :returns: return the random number. min <= return_value <= max
    :retval: int
    """
    ...


def malloc(size: int, /) -> None:
    """
    Allocate a memory dynamically

    :param size:
    :type size: int

    :returns: pointer to the allocated memory
    :retval: None
    """
    ...


def free(data, /) -> None:
    """
    Free an allocated data

    :param data:
    :type data: None

    :returns:
    :retval: None
    """
    ...


def realloc(data_p, new_size: int, /) -> None:
    """
    Reallocate a memory with a new size. The old content will be kept.

    :param data_p:
    :type data_p: None

    :param new_size:
    :type new_size: int

    :returns: pointer to the new memory, NULL on failure
    :retval: None
    """
    ...


def memcpy(dst, src, len: int, /) -> None:
    """
        :param dst:
    :type dst: None

    :param src:
    :type src: None

    :param len:
    :type len: int

    :returns:
    :retval: None
    """
    ...


def memset(dst, v: int, len: int, /) -> None:
    """
        :param dst:
    :type dst: None

    :param v:
    :type v: int

    :param len:
    :type len: int

    :returns:
    :retval: None
    """
    ...


def memzero(dst, len: int, /) -> None:
    """
    Same as

    :param dst:
    :type dst: None

    :param len:
    :type len: int

    :returns:
    :retval: None
    """
    ...


def strlen(str: str, /) -> int:
    """
    :param str:
    :type str: str

    :returns:
    :retval: int
    """
    ...


def strncpy(dst: int, src: str, dest_size: int, /) -> int:
    """
    :param dst:
    :type dst: int

    :param src:
    :type src: str

    :param dest_size:
    :type dest_size: int

    :returns:
    :retval: int
    """
    ...


def mem_test() -> "res_t":
    """
    :returns:
    :retval: "res_t"
    """
    ...


def memcpy_builtin(dst, src, len: int, /) -> None:
    """
    Same as

    :param dst:
    :type dst: None

    :param src:
    :type src: None

    :param len:
    :type len: int

    :returns:
    :retval: None
    """
    ...


def memset_builtin(dst, v: int, len: int, /) -> None:
    """
    Same as

    :param dst:
    :type dst: None

    :param v:
    :type v: int

    :param len:
    :type len: int

    :returns:
    :retval: None
    """
    ...


def strlen_builtin(str: str, /) -> int:
    """
        :param str:
    :type str: str

    :returns:
    :retval: int
    """
    ...


def strncpy_builtin(dst: int, src: str, dest_size: int, /) -> int:
    """
    :param dst:
    :type dst: int

    :param src:
    :type src: str

    :param dest_size:
    :type dest_size: int

    :returns:
    :retval: int
    """
    ...


def snprintf_builtin(buffer: int, count: int, format: str, /) -> int:
    """
    :param buffer:
    :type buffer: int

    :param count:
    :type count: int

    :param format:
    :type format: str

    :returns:
    :retval: int
    """
    ...


def vsnprintf_builtin(buffer: int, count: int, format: str, va: Any, /) -> int:
    """
    :param buffer:
    :type buffer: int

    :param count:
    :type count: int

    :param format:
    :type format: str

    :param va:
    :type va: Any

    :returns:
    :retval: int
    """
    ...


def style_register_prop(flag: int, /) -> "style_prop_t":
    """
    :param flag:
    :type flag: int

    :returns:
    :retval: "style_prop_t"
    """
    ...


def style_get_num_custom_props() -> "style_prop_t":
    """
    Get the number of custom properties that have been registered thus far.

    :returns:
    :retval: "style_prop_t"
    """
    ...


def style_prop_get_default(prop: "style_prop_t", /) -> "style_value_t":
    """
    Get the default value of a property

    :param prop:
    :type prop: "style_prop_t"

    :returns: the default value
    :retval: "style_value_t"
    """
    ...


def style_prop_has_flag(prop: "style_prop_t", flag: int, /) -> bool:
    """
    Do not pass multiple flags to this function as
    backwards-compatibility is not guaranteed for that.

    :param prop:
    :type prop: "style_prop_t"

    :param flag:
    :type flag: int

    :returns:
    :retval: bool
    """
    ...


def timer_handler_run_in_period(ms: int, /) -> int:
    """
    Call it in the super-loop of main() or threads.
    It will run lv_timer_handler() with a given period in ms.
    You can use it with sleep or delay in OS environment.
    This function is used to simplify the porting.

    :param ms:
    :type ms: int

    :returns:
    :retval: int
    """
    ...


def timer_create_basic() -> "timer_t":
    """
    Create an "empty" timer. It needs to be initialized with at least

    :returns:
    :retval: "timer_t"
    """
    ...


def timer_create(
        timer_xcb: "timer_cb_t", period: int, user_data, /
) -> "timer_t":
    """
    Create a new lv_timer

    :param timer_xcb:
    :type timer_xcb: "timer_cb_t"

    :param period:
    :type period: int

    :param user_data:
    :type user_data: None

    :returns: pointer to the new timer
    :retval: "timer_t"
    """
    ...


def timer_del(timer: "timer_t", /) -> None:
    """
    Delete a lv_timer

    :param timer:
    :type timer: "timer_t"

    :returns:
    :retval: None
    """
    ...


def timer_pause(timer: "timer_t", /) -> None:
    """
    Pause/resume a timer.

    :param timer:
    :type timer: "timer_t"

    :returns:
    :retval: None
    """
    ...


def timer_resume(timer: "timer_t", /) -> None:
    """
    :param timer:
    :type timer: "timer_t"

    :returns:
    :retval: None
    """
    ...


def timer_set_cb(timer: "timer_t", timer_cb: "timer_cb_t", /) -> None:
    """
    Set the callback to the timer (the function to call periodically)

    :param timer:
    :type timer: "timer_t"

    :param timer_cb:
    :type timer_cb: "timer_cb_t"

    :returns:
    :retval: None
    """
    ...


def timer_set_period(timer: "timer_t", period: int, /) -> None:
    """
    Set new period for a lv_timer

    :param timer:
    :type timer: "timer_t"

    :param period:
    :type period: int

    :returns:
    :retval: None
    """
    ...


def timer_ready(timer: "timer_t", /) -> None:
    """
    Make a lv_timer ready. It will not wait its period.

    :param timer:
    :type timer: "timer_t"

    :returns:
    :retval: None
    """
    ...


def timer_set_repeat_count(timer: "timer_t", repeat_count: int, /) -> None:
    """
    Set the number of times a timer will repeat.

    :param timer:
    :type timer: "timer_t"

    :param repeat_count:
    :type repeat_count: int

    :returns:
    :retval: None
    """
    ...


def timer_reset(timer: "timer_t", /) -> None:
    """
    Reset a lv_timer. It will be called the previously set period milliseconds later.

    :param timer:
    :type timer: "timer_t"

    :returns:
    :retval: None
    """
    ...


def timer_enable(en: bool, /) -> None:
    """
    Enable or disable the whole lv_timer handling

    :param en:
    :type en: bool

    :returns:
    :retval: None
    """
    ...


def timer_get_idle() -> int:
    """
    Get idle percentage

    :returns:
    :retval: int
    """
    ...


def timer_get_next(timer: "timer_t", /) -> "timer_t":
    """
    Iterate through the timers

    :param timer:
    :type timer: "timer_t"

    :returns: the next timer or NULL if there is no more timer
    :retval: "timer_t"
    """
    ...


def timer_get_user_data(timer: "timer_t", /) -> None:
    """
    Get the user_data passed when the timer was created

    :param timer:
    :type timer: "timer_t"

    :returns: pointer to the user_data
    :retval: None
    """
    ...


def tlsf_create(mem, /) -> "tlsf_t":
    """
        :param mem:
    :type mem: None

    :returns:
    :retval: "tlsf_t"
    """
    ...


def tlsf_create_with_pool(mem, bytes: int, /) -> "tlsf_t":
    """
    :param mem:
    :type mem: None

    :param bytes:
    :type bytes: int

    :returns:
    :retval: "tlsf_t"
    """
    ...


def tlsf_destroy(tlsf: "tlsf_t", /) -> None:
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :returns:
    :retval: None
    """
    ...


def tlsf_get_pool(tlsf: "tlsf_t", /) -> "pool_t":
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :returns:
    :retval: "pool_t"
    """
    ...


def tlsf_add_pool(tlsf: "tlsf_t", mem, bytes: int, /) -> "pool_t":
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :param mem:
    :type mem: None

    :param bytes:
    :type bytes: int

    :returns:
    :retval: "pool_t"
    """
    ...


def tlsf_remove_pool(tlsf: "tlsf_t", pool: "pool_t", /) -> None:
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :param pool:
    :type pool: "pool_t"

    :returns:
    :retval: None
    """
    ...


def tlsf_malloc(tlsf: "tlsf_t", bytes: int, /) -> None:
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :param bytes:
    :type bytes: int

    :returns:
    :retval: None
    """
    ...


def tlsf_memalign(tlsf: "tlsf_t", align: int, bytes: int, /) -> None:
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :param align:
    :type align: int

    :param bytes:
    :type bytes: int

    :returns:
    :retval: None
    """
    ...


def tlsf_realloc(tlsf: "tlsf_t", ptr, size: int, /) -> None:
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :param ptr:
    :type ptr: None

    :param size:
    :type size: int

    :returns:
    :retval: None
    """
    ...


def tlsf_free(tlsf: "tlsf_t", ptr, /) -> int:
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :param ptr:
    :type ptr: None

    :returns:
    :retval: int
    """
    ...


def tlsf_block_size(ptr, /) -> int:
    """
    :param ptr:
    :type ptr: None

    :returns:
    :retval: int
    """
    ...


def tlsf_size() -> int:
    """
    :returns:
    :retval: int
    """
    ...


def tlsf_align_size() -> int:
    """
    :returns:
    :retval: int
    """
    ...


def tlsf_block_size_min() -> int:
    """
    :returns:
    :retval: int
    """
    ...


def tlsf_block_size_max() -> int:
    """
    :returns:
    :retval: int
    """
    ...


def tlsf_pool_overhead() -> int:
    """
    :returns:
    :retval: int
    """
    ...


def tlsf_alloc_overhead() -> int:
    """
    :returns:
    :retval: int
    """
    ...


def tlsf_walk_pool(pool: "pool_t", walker: "tlsf_walker", user, /) -> None:
    """
    :param pool:
    :type pool: "pool_t"

    :param walker:
    :type walker: "tlsf_walker"

    :param user:
    :type user: None

    :returns:
    :retval: None
    """
    ...


def tlsf_check(tlsf: "tlsf_t", /) -> int:
    """
    :param tlsf:
    :type tlsf: "tlsf_t"

    :returns:
    :retval: int
    """
    ...


def tlsf_check_pool(pool: "pool_t", /) -> int:
    """
    :param pool:
    :type pool: "pool_t"

    :returns:
    :retval: int
    """
    ...


def txt_get_size(
        size_res: "point_t", text: str, font: "font_t",
        letter_space: "coord_t", line_space: "coord_t",
        max_width: "coord_t", flag: "text_flag_t", /
) -> None:
    """
    Get size of a text

    :param size_res:
    :type size_res: "point_t"

    :param text:
    :type text: str

    :param font:
    :type font: "font_t"

    :param letter_space:
    :type letter_space: "coord_t"

    :param line_space:
    :type line_space: "coord_t"

    :param max_width:
    :type max_width: "coord_t"

    :param flag:
    :type flag: "text_flag_t"

    :returns:
    :retval: None
    """
    ...


def txt_get_width(
        txt: str, length: int, font: "font_t",
        letter_space: "coord_t", flag: "text_flag_t", /
) -> "coord_t":
    """
    Give the length of a text with a given font

    :param txt:
    :type txt: str

    :param length:
    :type length: int

    :param font:
    :type font: "font_t"

    :param letter_space:
    :type letter_space: "coord_t"

    :param flag:
    :type flag: "text_flag_t"

    :returns: length of a char_num long text
    :retval: "coord_t"
    """
    ...


def theme_basic_init(disp: "disp_t", /) -> "theme_t":
    """
    Initialize the theme

    :param disp:
    :type disp: "disp_t"

    :returns: a pointer to reference this theme later
    :retval: "theme_t"
    """
    ...


def theme_basic_is_inited() -> bool:
    """
    Check if the theme is initialized

    :returns:
    :retval: bool
    """
    ...


def theme_default_init(
        disp: "disp_t", color_primary: "color_t",
        color_secondary: "color_t", dark: bool, font: "font_t", /
) -> "theme_t":
    """
    Initialize the theme

    :param disp:
    :type disp: "disp_t"

    :param color_primary:
    :type color_primary: "color_t"

    :param color_secondary:
    :type color_secondary: "color_t"

    :param dark:
    :type dark: bool

    :param font:
    :type font: "font_t"

    :returns: a pointer to reference this theme later
    :retval: "theme_t"
    """
    ...


def theme_default_get() -> "theme_t":
    """
    Get default theme

    :returns:
    :retval: "theme_t"
    """
    ...


def theme_default_is_inited() -> bool:
    """
    Check if default theme is initialized

    :returns:
    :retval: bool
    """
    ...


def theme_mono_init(
        disp: "disp_t", dark_bg: bool, font: "font_t", /
) -> "theme_t":
    """
    Initialize the theme

    :param disp:
    :type disp: "disp_t"

    :param dark_bg:
    :type dark_bg: bool

    :param font:
    :type font: "font_t"

    :returns: a pointer to reference this theme later
    :retval: "theme_t"
    """
    ...


def theme_mono_is_inited() -> bool:
    """
    Check if the theme is initialized

    :returns:
    :retval: bool
    """
    ...


def animimg_create(parent: "obj_t", /) -> "obj_t":
    """
    Create an animation image objects

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created animation image object
    :retval: "obj_t"
    """
    ...


def arc_create(parent: "obj_t", /) -> "obj_t":
    """
    Create an arc object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created arc
    :retval: "obj_t"
    """
    ...


def bar_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a bar object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created bar
    :retval: "obj_t"
    """
    ...


def btn_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a button object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created button
    :retval: "obj_t"
    """
    ...


def btnmatrix_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a button matrix object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created button matrix
    :retval: "obj_t"
    """
    ...


def calendar_create(parent: "obj_t", /) -> "obj_t":
    """
    :param parent:
    :type parent: "obj_t"

    :returns:
    :retval: "obj_t"
    """
    ...


def calendar_header_arrow_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a calendar header with drop-drowns to select the year and month

    :param parent:
    :type parent: "obj_t"

    :returns: the created header
    :retval: "obj_t"
    """
    ...


def calendar_header_dropdown_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a calendar header with drop-drowns to select the year and month

    :param parent:
    :type parent: "obj_t"

    :returns: the created header
    :retval: "obj_t"
    """
    ...


def canvas_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a canvas object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created canvas
    :retval: "obj_t"
    """
    ...


def chart_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a chart object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created chart
    :retval: "obj_t"
    """
    ...


def checkbox_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a check box object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created check box
    :retval: "obj_t"
    """
    ...


def colorwheel_create(parent: "obj_t", knob_recolor: bool, /) -> "obj_t":
    """
    Create a color picker object with disc shape

    :param parent:
    :type parent: "obj_t"

    :param knob_recolor:
    :type knob_recolor: bool

    :returns: pointer to the created color picker
    :retval: "obj_t"
    """
    ...


def dropdown_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a drop-down list object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created drop-down list
    :retval: "obj_t"
    """
    ...


def img_create(parent: "obj_t", /) -> "obj_t":
    """
    Create an image object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created image
    :retval: "obj_t"
    """
    ...


def imgbtn_create(parent: "obj_t", /) -> "obj_t":
    """
    Create an image button object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created image button
    :retval: "obj_t"
    """
    ...


def keyboard_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a Keyboard object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created keyboard
    :retval: "obj_t"
    """
    ...


def keyboard_def_event_cb(e: "event_t", /) -> None:
    """
    Default keyboard event to add characters to the
    Text area and change the map. If a custom

    :param e:
    :type e: "event_t"

    :returns:
    :retval: None
    """
    ...


def label_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a label object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created button
    :retval: "obj_t"
    """
    ...


def led_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a led object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created led
    :retval: "obj_t"
    """
    ...


def line_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a line object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created line
    :retval: "obj_t"
    """
    ...


def list_create(parent: "obj_t", /) -> "obj_t":
    """
        :param parent:
    :type parent: "obj_t"

    :returns:
    :retval: "obj_t"
    """
    ...


def menu_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a menu object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created menu
    :retval: "obj_t"
    """
    ...


def menu_page_create(parent: "obj_t", title: str, /) -> "obj_t":
    """
    Create a menu page object

    :param parent:
    :type parent: "obj_t"

    :param title:
    :type title: str

    :returns: pointer to the created menu page
    :retval: "obj_t"
    """
    ...


def menu_cont_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a menu cont object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created menu cont
    :retval: "obj_t"
    """
    ...


def menu_section_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a menu section object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created menu section
    :retval: "obj_t"
    """
    ...


def menu_separator_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a menu separator object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created menu separator
    :retval: "obj_t"
    """
    ...


def meter_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a Meter object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created meter
    :retval: "obj_t"
    """
    ...


def msgbox_create(
        parent: "obj_t", title: str, txt: str,
        btn_txts: Callable[["[]"], str], add_close_btn: bool, /
) -> "obj_t":
    """
    Create a message box object

    :param parent:
    :type parent: "obj_t"

    :param title:
    :type title: str

    :param txt:
    :type txt: str

    :param btn_txts:
    :type btn_txts: Callable[["[]"], str]

    :param add_close_btn:
    :type add_close_btn: bool

    :returns: pointer to the message box object
    :retval: "obj_t"
    """
    ...


def roller_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a roller object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created roller
    :retval: "obj_t"
    """
    ...


def slider_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a slider object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created slider
    :retval: "obj_t"
    """
    ...


def spangroup_create(par: "obj_t", /) -> "obj_t":
    """
    Create a spangroup object

    :param par:
    :type par: "obj_t"

    :returns: pointer to the created spangroup
    :retval: "obj_t"
    """
    ...


def spinbox_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a Spinbox object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created spinbox
    :retval: "obj_t"
    """
    ...


def spinner_create(parent: "obj_t", time: int, arc_length: int, /) -> "obj_t":
    """
    :param parent:
    :type parent: "obj_t"

    :param time:
    :type time: int

    :param arc_length:
    :type arc_length: int

    :returns:
    :retval: "obj_t"
    """
    ...


def switch_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a switch object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created switch
    :retval: "obj_t"
    """
    ...


def table_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a table object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created table
    :retval: "obj_t"
    """
    ...


def tabview_create(
        parent: "obj_t", tab_pos: "dir_t", tab_size: "coord_t", /
) -> "obj_t":
    """
    :param parent:
    :type parent: "obj_t"

    :param tab_pos:
    :type tab_pos: "dir_t"

    :param tab_size:
    :type tab_size: "coord_t"

    :returns:
    :retval: "obj_t"
    """
    ...


def textarea_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a text area object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created text area
    :retval: "obj_t"
    """
    ...


def tileview_create(parent: "obj_t", /) -> "obj_t":
    """
    Create a Tileview object

    :param parent:
    :type parent: "obj_t"

    :returns: pointer to the created tileview
    :retval: "obj_t"
    """
    ...


def win_create(parent: "obj_t", header_height: "coord_t", /) -> "obj_t":
    """
    :param parent:
    :type parent: "obj_t"

    :param header_height:
    :type header_height: "coord_t"

    :returns:
    :retval: "obj_t"
    """
    ...


obj_class: _obj_class_t = ...
scrollbar_mode_t: int = ...
font_montserrat_8: font_t = ...
font_montserrat_10: font_t = ...
font_montserrat_12: font_t = ...
font_montserrat_14: font_t = ...
font_montserrat_16: font_t = ...
font_montserrat_18: font_t = ...
font_montserrat_20: font_t = ...
font_montserrat_22: font_t = ...
font_montserrat_24: font_t = ...
font_montserrat_26: font_t = ...
font_montserrat_28: font_t = ...
font_montserrat_30: font_t = ...
font_montserrat_32: font_t = ...
SIZE_CONTENT: int = ...
LV_LAYOUT_FLEX: int = ...
LV_STYLE_FLEX_FLOW: style_prop_t = ...
LV_STYLE_FLEX_MAIN_PLACE: style_prop_t = ...
LV_STYLE_FLEX_CROSS_PLACE: style_prop_t = ...
LV_STYLE_FLEX_TRACK_PLACE: style_prop_t = ...
LV_STYLE_FLEX_GROW: style_prop_t = ...
LV_LAYOUT_GRID: int = ...
LV_STYLE_GRID_COLUMN_DSC_ARRAY: style_prop_t = ...
LV_STYLE_GRID_COLUMN_ALIGN: style_prop_t = ...
LV_STYLE_GRID_ROW_DSC_ARRAY: style_prop_t = ...
LV_STYLE_GRID_ROW_ALIGN: style_prop_t = ...
LV_STYLE_GRID_CELL_COLUMN_POS: style_prop_t = ...
LV_STYLE_GRID_CELL_COLUMN_SPAN: style_prop_t = ...
LV_STYLE_GRID_CELL_X_ALIGN: style_prop_t = ...
LV_STYLE_GRID_CELL_ROW_POS: style_prop_t = ...
LV_STYLE_GRID_CELL_ROW_SPAN: style_prop_t = ...
LV_STYLE_GRID_CELL_Y_ALIGN: style_prop_t = ...
_timer_ll: ll_t = ...
_disp_ll: ll_t = ...
_indev_ll: ll_t = ...
_fsdrv_ll: ll_t = ...
_anim_ll: ll_t = ...
_group_ll: ll_t = ...
_img_decoder_ll: ll_t = ...
_obj_style_trans_ll: ll_t = ...
_layout_list: layout_dsc_t = ...
_img_cache_single: _img_cache_entry_t = ...
_timer_act: timer_t = ...
_circle_cache: _draw_mask_radius_circle_dsc_arr_t = ...
_draw_mask_list: _draw_mask_saved_arr_t = ...
_theme_default_styles: None = ...
_theme_basic_styles: None = ...
_grad_cache_mem: int = ...
_style_custom_prop_flag_lookup_table: int = ...
_subs_ll: ll_t = ...

"""Give the size of an encoded character"""
_txt_encoded_size: Callable[[str], int]
"""Convert a Unicode letter to encoded"""
_txt_unicode_to_encoded: Callable[[int], int]
"""
Convert a wide character, e.g. 'Á' little endian 
to be compatible with the encoded format.
"""
_txt_encoded_conv_wc: Callable[[int], int]
"""Decode the next encoded character from a string."""
_txt_encoded_next: Callable[[str, list[int]], int]
"""Get the previous encoded character form a string."""
_txt_encoded_prev: Callable[[str, list[int]], int]
"""
Convert a letter index (in the encoded text) to byte index. 
E.g. in UTF-8 "AÁRT" index of 'R' is 2 but start at byte 3 
because 'Á' is 2 bytes long
"""
_txt_encoded_get_byte_id: Callable[[str, int], int]
"""
Convert a byte index (in an encoded text) to character index. 
E.g. in UTF-8 "AÁRT" index of 'R' is 2 but start at byte 3 
because 'Á' is 2 bytes long
"""
_txt_encoded_get_char_id: Callable[[str, int], int]
"""
Get the number of characters (and NOT bytes) in a string. 
E.g. in UTF-8 "ÁBC" is 3 characters (but 4 bytes)
"""
_txt_get_encoded_length: Callable[[str], int]

animimg_class: _obj_class_t = ...
_animimg_part_t: int = ...
arc_class: _obj_class_t = ...
bar_class: _obj_class_t = ...
btn_class: _obj_class_t = ...
btnmatrix_class: _obj_class_t = ...
calendar_class: _obj_class_t = ...
calendar_header_arrow_class: _obj_class_t = ...
calendar_header_dropdown_class: _obj_class_t = ...
canvas_class: _obj_class_t = ...
chart_class: _obj_class_t = ...
checkbox_class: _obj_class_t = ...
colorwheel_class: _obj_class_t = ...
dropdown_class: _obj_class_t = ...
dropdownlist_class: _obj_class_t = ...
img_class: _obj_class_t = ...
imgbtn_class: _obj_class_t = ...
keyboard_class: _obj_class_t = ...
label_class: _obj_class_t = ...
led_class: _obj_class_t = ...
line_class: _obj_class_t = ...
list_class: _obj_class_t = ...
list_text_class: _obj_class_t = ...
list_btn_class: _obj_class_t = ...
menu_class: _obj_class_t = ...
menu_page_class: _obj_class_t = ...
menu_cont_class: _obj_class_t = ...
menu_section_class: _obj_class_t = ...
menu_separator_class: _obj_class_t = ...
menu_sidebar_cont_class: _obj_class_t = ...
menu_main_cont_class: _obj_class_t = ...
menu_sidebar_header_cont_class: _obj_class_t = ...
menu_main_header_cont_class: _obj_class_t = ...
meter_class: _obj_class_t = ...
msgbox_class: _obj_class_t = ...
msgbox_content_class: _obj_class_t = ...
msgbox_backdrop_class: _obj_class_t = ...
roller_class: _obj_class_t = ...
slider_class: _obj_class_t = ...
spangroup_class: _obj_class_t = ...
spinbox_class: _obj_class_t = ...
spinner_class: _obj_class_t = ...
switch_class: _obj_class_t = ...
table_class: _obj_class_t = ...
tabview_class: _obj_class_t = ...
textarea_class: _obj_class_t = ...
tileview_class: _obj_class_t = ...
tileview_tile_class: _obj_class_t = ...
win_class: _obj_class_t = ...


class obj(obj_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a base object (a rectangle)

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class animimg(obj_t, animimg_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create an animation image objects

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class arc(obj_t, arc_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create an arc object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class bar(obj_t, bar_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a bar object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class btn(obj_t, btn_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a button object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class btnmatrix(obj_t, btnmatrix_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a button matrix object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class calendar(obj_t, calendar_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class calendar_header_arrow(obj_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a calendar header with drop-drowns to select the year and month

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class calendar_header_dropdown(obj_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a calendar header with drop-drowns to select the year and month

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class canvas(obj_t, canvas_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a canvas object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class chart(obj_t, chart_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a chart object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class checkbox(obj_t, checkbox_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a check box object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class colorwheel(obj_t, colorwheel_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a color picker object with disc shape

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class dropdown(obj_t, dropdown_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a drop-down list object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class img(obj_t, img_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create an image object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class imgbtn(obj_t, imgbtn_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create an image button object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class keyboard(obj_t, keyboard_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a Keyboard object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class label(obj_t, label_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a label object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class led(obj_t, led_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a led object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class line(obj_t, line_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a line object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


# noinspection PyShadowingNames
class list(obj_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...

    def add_text(self, txt: str, /) -> "obj_t":
        """
        :param txt:
        :type txt: str

        :returns:
        :retval: "obj_t"
        """
        ...

    def add_btn(self, icon, txt: str, /) -> "obj_t":
        """
        :param icon:
        :type icon: None

        :param txt:
        :type txt: str

        :returns:
        :retval: "obj_t"
        """
        ...

    def get_btn_text(self, btn: "obj_t", /) -> str:
        """
        :param btn:
        :type btn: "obj_t"

        :returns:
        :retval: str
        """
        ...


class menu(obj_t, menu_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a menu object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class menu_page(obj_t, menu_page_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a menu page object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class menu_cont(obj_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a menu cont object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class menu_section(obj_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a menu section object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class menu_separator(obj_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a menu separator object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class meter(obj_t, meter_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a Meter object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class msgbox(obj_t, msgbox_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a message box object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class roller(obj_t, roller_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a roller object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class slider(obj_t, slider_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a slider object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class spangroup(obj_t, spangroup_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a spangroup object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class spinbox(obj_t, spinbox_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a Spinbox object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class spinner(obj_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class switch(obj_t, switch_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a switch object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class table(obj_t, table_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a table object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class tabview(obj_t, tabview_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class textarea(obj_t, textarea_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a text area object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class tileview(obj_t, tileview_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        Create a Tileview object

        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...


class win(obj_t, win_t):

    def __init__(self, parent: "obj_t" = None, /):
        """
        :param parent: parent object, Default=None
        :type parent: obj_t
        """
        ...
