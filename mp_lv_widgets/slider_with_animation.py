##### startup script #####

# !/opt/bin/lv_micropython -i

import lvgl as lv
import display_driver


slider = lv.slider(lv.scr_act())
slider.set_value(70, lv.ANIM.OFF)
slider.set_size(300, 20)
slider.center()

slider.set_style_bg_color(lv.color_hex(0x0F1215), lv.PART.MAIN)
slider.set_style_bg_opa(255, lv.PART.MAIN)
slider.set_style_border_color(lv.color_hex(0x333943), lv.PART.MAIN)
slider.set_style_border_width(5, lv.PART.MAIN)
slider.set_style_pad_all(5, lv.PART.MAIN)

style_indicator = lv.style_t()
style_indicator.init()
style_indicator.set_bg_color(lv.color_hex(0x37B9F5))
style_indicator.set_bg_grad_color(lv.color_hex(0x1464F0))
style_indicator.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_indicator.set_shadow_color(lv.color_hex(0x37B9F5))
style_indicator.set_shadow_width(15)
style_indicator.set_shadow_spread(5)

style_knob = lv.style_t()
style_knob.init()
style_knob.set_bg_color(lv.color_hex(0x37B9F5))
style_knob.set_bg_grad_color(lv.color_hex(0x1464F0))
style_knob.set_bg_grad_dir(lv.GRAD_DIR.HOR)
style_knob.set_shadow_color(lv.color_hex(0x37B9F5))
style_knob.set_shadow_width(15)
style_knob.set_shadow_spread(2)
style_knob.set_outline_color(lv.color_hex(0x0096FF))
style_knob.set_outline_width(3)
style_knob.set_outline_pad(-5)


def build_gradient(begin_rgb, end_rgb, nb):
    def rgb2hex(r, g, b):
        return (r & 0xFF) << 16 | (g & 0xFF) << 8 | (b & 0xFF)

    br, bg, bb = begin_rgb
    er, eg, eb = end_rgb

    r_diff = er - br
    g_diff = eg - bg
    b_diff = eb - bb

    r_fact = r_diff / float(nb)
    g_fact = g_diff / float(nb)
    b_fact = b_diff / float(nb)

    for i in range(0, nb + 1):
        yield rgb2hex(
            int(round(br + (i * r_fact))),
            int(round(bg + (i * g_fact))),
            int(round(bb + (i * b_fact)))
        )


gradient = list(build_gradient((0, 150, 255), (255, 0, 0), 100))


def pressed_cb(_, val):
    v = ~val + 101

    if val >= 50:
        slider.set_style_outline_width(
            int((30 - 3) * ((v * 2) / 100.0)) + 3,
            lv.PART.KNOB
        )
        slider.set_style_outline_opa(
            int((255) * (v / 100.0)),
            lv.PART.KNOB
        )

        if val == 100:

            slider.set_style_outline_opa(
                255,
                lv.PART.KNOB
            )
    else:
        slider.set_style_outline_width(
            int((30 - 3) * ((val * 2) / 100.0)) + 3,
            lv.PART.KNOB
        )

        slider.set_style_outline_opa(
            int((255) * (v / 100.0)),
            lv.PART.KNOB
        )

    slider.set_style_shadow_width(
        int((50 - 15) * (val / 100.0)) + 15,
        lv.PART.KNOB
    )

    slider.set_style_shadow_spread(
        int((25 - 2) * (val / 100.0)) + 2,
        lv.PART.KNOB
    )

    slider.set_style_shadow_opa(
        int((255 - 125) * (v / 100.0)) + 125,
        lv.PART.KNOB
    )

    slider.set_style_outline_color(
        lv.color_hex(gradient[val]),
        lv.PART.KNOB
    )


def released_cb(_, val):
    v = ~val + 101

    if val == 100:
        slider.set_style_shadow_width(15, lv.PART.KNOB)
        slider.set_style_shadow_spread(2, lv.PART.KNOB)
        slider.set_style_shadow_opa(255, lv.PART.KNOB)

    else:
        slider.set_style_shadow_width(
            int((100 - 50) * (v / 100.0)) + 50,
            lv.PART.KNOB
        )

        slider.set_style_shadow_spread(
            int((50 - 25) * (v / 100.0)) + 25,
            lv.PART.KNOB
        )
        slider.set_style_shadow_opa(
            int(127 * (v / 100.0)),
            lv.PART.KNOB
        )

    slider.set_style_outline_color(
        lv.color_hex(gradient[v]),
        lv.PART.KNOB
    )


def new_pressed_anim():
    p_anim = lv.anim_t()
    p_anim.init()
    p_anim.set_var(slider)
    p_anim.set_values(0, 100)
    p_anim.set_time(300)
    p_anim.set_repeat_count(1)
    p_anim.set_path_cb(lv.anim_t.path_linear)
    p_anim.set_custom_exec_cb(pressed_cb)
    p_anim.set_deleted_cb(lambda a: pressed_cb(a, 100))
    return p_anim


def new_released_anim():
    r_anim = lv.anim_t()
    r_anim.init()
    r_anim.set_var(slider)
    r_anim.set_values(0, 100)
    r_anim.set_time(200)
    r_anim.set_repeat_count(1)
    r_anim.set_path_cb(lv.anim_t.path_linear)
    r_anim.set_custom_exec_cb(released_cb)
    r_anim.set_deleted_cb(lambda a: released_cb(a, 100))

    return r_anim


slider.add_style(style_indicator, lv.PART.INDICATOR)
slider.add_style(style_knob, lv.PART.KNOB)

current_state = lv.EVENT.RELEASED

pressed_anim = None
released_anim = None


def timer_cb(t):
    global pressed_anim
    global released_anim

    t._del()

    if pressed_anim is not None:
        lv.anim_del(slider, pressed_anim.exec_cb)
        pressed_anim = None

        if current_state == lv.EVENT.RELEASED:
            released_anim = new_released_anim()
            released_anim.start()
            new_timer()

    elif released_anim is not None:
        lv.anim_del(slider, released_anim.exec_cb)
        released_anim = None

        if current_state == lv.EVENT.PRESSED:
            pressed_anim = new_pressed_anim()
            pressed_anim.start()
            new_timer()


def new_timer():
    t = lv.timer_create(timer_cb, 150, None)
    t.set_repeat_count(1)


def event_cb(event):
    global current_state
    global pressed_anim
    global released_anim

    code = event.get_code()

    if code == lv.EVENT.PRESSED:
        if pressed_anim is None and released_anim is None:
            pressed_anim = new_pressed_anim()
            pressed_anim.start()
            new_timer()

        current_state = lv.EVENT.PRESSED

    elif code == lv.EVENT.PRESSING:
        current_state = lv.EVENT.PRESSING

    elif code == lv.EVENT.RELEASED:
        if pressed_anim is None and released_anim is None:
            released_anim = new_released_anim()
            released_anim.start()
            new_timer()

        current_state = lv.EVENT.RELEASED


slider.add_event_cb(event_cb, lv.EVENT.ALL, None)