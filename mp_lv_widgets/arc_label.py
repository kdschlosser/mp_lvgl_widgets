import lvgl as lv
from ._utils import point_on_circle as _point_on_circle


class _Attrs(object):

    def __init__(self, obj, key=None):
        self._obj = obj
        self._key = key
        self._storage = {}

    def __getitem__(self, item):
        if item in self._storage:
            value = self._storage[item]
        else:
            if self._key is None:
                if item.startswith('set'):
                    key = 'g' + item[1:]
                    value = self._storage[item] = _Attrs(self._obj, key)
                elif item == 'set_long_mode':
                    value = self._storage[item] = 0
                elif item == 'enable_style_refresh':
                    value = self._storage[item] = False
                elif item in ('add_state', 'add_flag'):
                    value = self._storage[item] = []
                elif item in ('add_event_cb', 'add_style'):
                    value = self._storage[item] = {}
                else:
                    value = self._storage[item] = []
            else:
                value = getattr(self._obj, self._key)(item)

        return value

    def __setitem__(self, key, value):
        _ = self[key]

        self._storage[key] = value

    def __delitem__(self, key):
        if key in self._storage:
            del self._storage[key]

    def clear(self):
        self._storage.clear()

    def items(self):
        return self._storage.items()


class ArcLabel(lv.obj):

    def __init__(self, parent,):
        super().__init__(parent)
        obj = lv.label(self)
        obj.add_flag(lv.obj.FLAG.HIDDEN)
        obj.set_x(-500)
        obj.set_y(-500)
        obj.clear_flag(lv.obj.FLAG.CLICKABLE)

        self.__attrs = _Attrs(obj)
        self._text_len = 0
        self._text = None
        self._start_angle = None
        self._stop_angle = None
        self._angle_range = None
        self._labels = []

    @property
    def __is_ready(self):
        return None not in (self._text, self._start_angle, self._stop_angle)

    def __init(self):

        radius = int(round(
            min(super().get_self_width(), super().get_self_height()) / 2
        ))

        start_angle = self._start_angle
        stop_angle = self._stop_angle

        angle_range = self._angle_range = stop_angle - start_angle

        self._text_len = text_len = len(self._text)

        for label in self._labels[:]:
            label._del()

        del self.labels[:]

        angle_step = float(angle_range) / (text_len + 1)
        angle = start_angle + angle_step

        text = list(self._text)

        if 90 < start_angle < 180 or 270 < start_angle < 360:
            text.reverse()

        if 180 < start_angle and 360 > stop_angle:
            size_res = lv.point_t()

            lv.txt_get_size(
                size_res,
                self._text,
                self.__attrs['set_style_text_font'][0],
                self.__attrs['set_style_text_letter_space'][0],
                self.__attrs['set_style_text_line_space'][0],
                lv.COORD.MAX,
                0
            )
            rad_dif = radius
            radius -= size_res.y
            rad_dif -= radius

        else:
            rad_dif = 0

        for char in text:
            t_angle = 2700 - (3600 - int(round(angle, 1) * 10))

            if 180 < start_angle and 360 > stop_angle:
                t_angle += 1800

            label = lv.label(self)
            label.set_text(char)
            label.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)

            if 180 < start_angle and 360 > stop_angle:
                l_height = label.get_self_height()
            else:
                l_height = 0

            x, y = _point_on_circle(angle, radius, radius, radius + rad_dif - l_height)

            label.set_style_transform_angle(t_angle, 0)
            label.set_x(x)
            label.set_y(y)

            for attr, attr_value in self._attrs.items():
                if isinstance(attr_value, _Attrs):
                    for key, value in attr_value.items():
                        getattr(label, attr)(value, key)
                elif isinstance(attr_value, dict):
                    for key, value in attr_value.items():
                        getattr(label, attr)(*key, value)
                elif isinstance(attr_value, list):
                    for value in attr_value:
                        getattr(label, attr)(value)
                else:
                    getattr(label, attr)(attr_value)

            self._labels.append(label)

            angle += angle_step

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if item.startswith('_'):
            try:
                return getattr(super(), item)
            except AttributeError:
                pass

        raise AttributeError('{0} not found'.format(item))

    def get_angle_start(self):
        return self._start_angle

    def get_angle_end(self):
        return self._stop_angle

    def set_start_angle(self, start_angle):
        self._start_angle = start_angle

        if self.__is_ready:
            self.__init()

    def set_end_angle(self, stop_angle):
        self._stop_angle = stop_angle

        if self.__is_ready:
            self.__init()

    def set_angles(self, start_angle, stop_angle):
        self._start_angle = start_angle
        self._stop_angle = stop_angle

        if self.__is_ready:
            self.__init()

    def set_style_text_opa(self, opa, part):
        for label in self.labels:
            label.set_style_text_opa(opa, part)

        self.__attrs['set_style_text_opa'][part] = opa

    def get_text(self):
        text = ''

        for label in self.labels:
            text += label.get_text()

        if 90 < self.start_angle < 180 or 270 < self.start_angle < 360:
            text = list(text)
            text.reverse()
            text = ''.join(text)

        return text.strip()

    def set_text(self, value):
        self._text = value
        if not self._labels and self.__is_ready:
            self.__init()
            return

        elif self.__is_ready and len(value) > self._text_len:
            self.__init()
            return

        elif self._labels:
            remainder = self.text_len - len(value)

            value = (' ' * int(remainder / 2)) + value

            remainder += remainder % 2
            value += ' ' * int(remainder / 2)

            value = list(value)
            if 90 < self.start_angle < 180 or 270 < self.start_angle < 360:
                value.reverse()

            for i, char in enumerate(value):
                self.labels[i].set_text(char)

    def add_event_cb(self, cb, event, user_data):  # labels
        for label in self._labels:
            label.add_event_cb(cb, event, user_data)

        self.__attrs['add_event_cb'][(cb, event)] = user_data

    def add_flag(self, flag):  # labels
        for label in self._labels:
            label.add_flag(flag)

        if flag not in self.__attrs['add_flag']:
            self.__attrs['add_flag'].append(flag)

    def add_state(self, state):  # labels
        for label in self._labels:
            label.add_state(state)

        if state not in self.__attrs['add_state']:
            self.__attrs['add_state'].append(state)

    def add_style(self, style, part):  # labels
        for label in self._labels:
            label.add_style(style, part)

        self.__attrs['add_style'][part] = style

    def clear_flag(self, flag):  # labels
        for label in self._labels:
            label.clear_flag(flag)

        if flag in self.__attrs['add_flag']:
            self.__attrs['add_flag'].remove(flag)

    def cut_text(self):  # labels
        raise NotImplementedError

    def enable_style_refresh(self, en):
        for label in self._labels:
            label.enable_style_refresh(en)
        self.__attrs['enable_style_refresh'] = en

    def get_style_bg_color(self, part):  # labels
        return self.__attrs['set_style_bg_color'][part]

    def get_style_bg_color_filtered(self, part):  # labels
        return self.__attrs['set_style_bg_color_filtered'][part]

    def get_style_bg_dither_mode(self, part):  # labels
        return self.__attrs['set_style_bg_dither_mode'][part]

    def get_style_bg_grad(self, part):  # labels
        return self.__attrs['set_style_bg_grad'][part]

    def get_style_bg_grad_color(self, part):  # labels
        return self.__attrs['set_style_bg_grad_color'][part]

    def get_style_bg_grad_color_filtered(self, part):  # labels
        return self.__attrs['set_style_bg_grad_color_filtered'][part]

    def get_style_bg_grad_dir(self, part):  # labels
        return self.__attrs['set_style_bg_grad_dir'][part]

    def get_style_bg_grad_stop(self, part):  # labels
        return self.__attrs['set_style_bg_grad_stop'][part]

    def get_style_bg_img_opa(self, part):  # labels
        return self.__attrs['set_style_bg_img_opa'][part]

    def get_style_bg_img_recolor(self, part):  # labels
        return self.__attrs['set_style_bg_img_recolor'][part]

    def get_style_bg_img_recolor_filtered(self, part):  # labels
        return self.__attrs['set_style_bg_img_recolor_filtered'][part]

    def get_style_bg_img_recolor_opa(self, part):  # labels
        return self.__attrs['set_style_bg_img_recolor_opa'][part]

    def get_style_bg_img_src(self, part):  # labels
        return self.__attrs['set_style_bg_img_src'][part]

    def get_style_bg_img_tiled(self, part):  # labels
        return self.__attrs['set_style_bg_img_tiled'][part]

    def get_style_bg_main_stop(self, part):  # labels
        return self.__attrs['set_style_bg_main_stop'][part]

    def get_style_bg_opa(self, part):  # labels
        return self.__attrs['set_style_bg_opa'][part]

    def get_style_blend_mode(self, part):  # labels
        return self.__attrs['set_style_blend_mode'][part]

    def get_style_border_color(self, part):  # labels
        return self.__attrs['set_style_border_color'][part]

    def get_style_border_color_filtered(self, part):  # labels
        return self.__attrs['set_style_border_color_filtered'][part]

    def get_style_border_opa(self, part):  # labels
        return self.__attrs['set_style_border_opa'][part]

    def get_style_border_post(self, part):  # labels
        return self.__attrs['set_style_border_post'][part]

    def get_style_border_side(self, part):  # labels
        return self.__attrs['set_style_border_side'][part]

    def get_style_border_width(self, part):  # labels
        return self.__attrs['set_style_border_width'][part]

    def get_style_clip_corner(self, part):  # labels
        return self.__attrs['set_style_clip_corner'][part]

    def get_style_color_filter_dsc(self, part):  # labels
        return self.__attrs['set_style_color_filter_dsc'][part]

    def get_style_color_filter_opa(self, part):  # labels
        return self.__attrs['set_style_color_filter_opa'][part]

    def get_style_img_opa(self, part):  # labels
        return self.__attrs['set_style_img_opa'][part]

    def get_style_img_recolor(self, part):  # labels
        return self.__attrs['set_style_img_recolor'][part]

    def get_style_img_recolor_filtered(self, part):  # labels
        return self.__attrs['style_text_opa'][part]

    def get_style_img_recolor_opa(self, part):  # labels
        return self.__attrs['set_style_img_recolor_opa'][part]

    def get_style_margin_bottom(self, part):  # labels
        return self.__attrs['set_style_margin_bottom'][part]

    def get_style_margin_left(self, part):  # labels
        return self.__attrs['set_style_margin_left'][part]

    def get_style_margin_right(self, part):  # labels
        return self.__attrs['set_style_margin_right'][part]

    def get_style_margin_top(self, part):  # labels
        return self.__attrs['set_style_margin_top'][part]

    def get_style_outline_color(self, part):  # labels
        return self.__attrs['set_style_outline_color'][part]

    def get_style_outline_color_filtered(self, part):  # labels
        return self.__attrs['set_style_outline_color_filtered'][part]

    def get_style_outline_opa(self, part):  # labels
        return self.__attrs['set_style_outline_opa'][part]

    def get_style_outline_pad(self, part):  # labels
        return self.__attrs['set_style_outline_pad'][part]

    def get_style_outline_width(self, part):  # labels
        return self.__attrs['set_style_outline_width'][part]

    def get_style_pad_bottom(self, part):  # labels
        return self.__attrs['set_style_pad_bottom'][part]

    def get_style_pad_column(self, part):  # labels
        return self.__attrs['set_style_pad_column'][part]

    def get_style_pad_left(self, part):  # labels
        return self.__attrs['set_style_pad_left'][part]

    def get_style_pad_right(self, part):  # labels
        return self.__attrs['set_style_pad_right'][part]

    def get_style_pad_row(self, part):  # labels
        return self.__attrs['set_style_pad_row'][part]

    def get_style_pad_top(self, part):  # labels
        return self.__attrs['set_style_pad_top'][part]

    def get_style_radius(self, part):
        return self.radius

    def get_style_shadow_color(self, part):  # labels
        return self.__attrs['set_style_radius'][part]

    def get_style_shadow_color_filtered(self, part):  # labels
        return self.__attrs['set_style_shadow_color_filtered'][part]

    def get_style_shadow_ofs_x(self, part):  # labels
        return self.__attrs['set_style_shadow_ofs_x'][part]

    def get_style_shadow_ofs_y(self, part):  # labels
        return self.__attrs['set_style_shadow_ofs_y'][part]

    def get_style_shadow_opa(self, part):  # labels
        return self.__attrs['set_style_shadow_opa'][part]

    def get_style_shadow_spread(self, part):  # labels
        return self.__attrs['set_style_shadow_spread'][part]

    def get_style_shadow_width(self, part):  # labels
        return self.__attrs['set_style_shadow_width'][part]

    def get_style_space_bottom(self, part):  # labels
        return self.__attrs['set_style_space_bottom'][part]

    def get_style_space_left(self, part):  # labels
        return self.__attrs['set_style_space_left'][part]

    def get_style_space_right(self, part):  # labels
        return self.__attrs['set_style_space_right'][part]

    def get_style_space_top(self, part):  # labels
        return self.__attrs['set_style_space_top'][part]

    def get_style_text_color(self, part):  # labels
        return self.__attrs['set_style_text_color'][part]

    def get_style_text_color_filtered(self, part):  # labels
        return self.__attrs['set_style_text_color_filtered'][part]

    def get_style_text_decor(self, part):  # labels
        return self.__attrs['set_style_text_decor'][part]

    def get_style_text_font(self, part):  # labels
        return self.__attrs['set_style_text_font'][part]

    def get_style_text_letter_space(self, part):  # labels
        return self.__attrs['set_style_text_letter_space'][part]

    def get_style_text_line_space(self, part):  # labels
        return self.__attrs['set_style_text_line_space'][part]

    def get_style_text_opa(self, part):  # labels
        return self.__attrs['set_style_text_opa'][part]

    def get_text_selection_end(self):  # labels
        pass

    def get_text_selection_start(self):  # labels
        pass

    def has_flag(self, flag):  # labels
        return flag in self.__attrs['add_flag']

    def has_flag_any(self, flags):  # labels
        for flag in self.__attrs['add_flag']:
            if not flags & flag:
                return True
        return False

    def hit_test(self, point):  # label
        for label in self._labels:
            if label.hit_test(point):
                return True

        return False

    def ins_text(self):  # labels
        raise NotImplementedError

    def is_char_under_pos(self):
        raise NotImplementedError

    def is_editable(self):  # labels
        for label in self._labels:
            if label.is_editable():
                return True

        return False

    def refresh_style(self, selector, prop):  # label
        for label in self._labels:
            label.refresh_style(selector, prop)

    def remove_event_cb(self, event_cb):  # labels
        for label in self._labels:
            label.remove_event_cb(event_cb)

        for key in list(self.__attrs['add_event_cb'].keys())[:]:
            cb, event = key
            if cb == event_cb:
                del self.__attrs['add_event_cb'][key]

    def remove_event_cb_with_user_data(self, event_cb, user_data):  # labels
        for label in self._labels:
            label.remove_event_cb_with_user_data(event_cb, user_data)

        for key, value in list(self.__attrs['add_event_cb'].items())[:]:
            cb, event = key
            if cb == event_cb and user_data == value:
                del self.__attrs['add_event_cb'][key]

    def remove_style(self, selector):  # labels
        for label in self.labels:
            label.remove_style(selector)

        if selector in self.__attrs['add_style']:
            del self.__attrs['add_style'][selector]

    def remove_style_all(self):  # labels
        for label in self.labels:
            label.remove_style_all()

        self.__attrs['add_style'].clear()

    def set_ext_click_area(self, size):  # labels
        for label in self.labels:
            label.set_ext_click_area(size)

        self.__attrs['set_ext_click_area'] = size

    def set_flex_align(self, main_place, cross_place, track_cross_place):  # disable
        raise NotImplementedError

    def set_flex_flow(self, flow):  # disable
        raise NotImplementedError

    def set_flex_grow(self, grow):  # disable
        raise NotImplementedError

    def set_grid_align(self, column_align, row_align):  # disable
        raise NotImplementedError

    def set_grid_cell(self, column_align, col_pos, col_span, row_align, row_pos, row_span):  # disable
        raise NotImplementedError

    def set_grid_dsc_array(self, col_dsc, row_dsc):  # disable
        raise NotImplementedError

    def set_long_mode(self, long_mode):  # labels
        for label in self._labels:
            label.set_long_mode(long_mode)

        self.__attrs['set_long_mode'] = long_mode

    def set_style_bg_color(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_color(value, part)

        self.__attrs['set_style_bg_color'][part] = value

    def set_style_bg_dither_mode(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_dither_mode(value, part)

        self.__attrs['set_style_bg_dither_mode'][part] = value

    def set_style_bg_grad(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_grad(value, part)

        self.__attrs['set_style_bg_grad'][part] = value

    def set_style_bg_grad_color(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_grad_color(value, part)

        self.__attrs['set_style_bg_grad_color'][part] = value

    def set_style_bg_grad_dir(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_grad_dir(value, part)

        self.__attrs['set_style_bg_grad_dir'][part] = value

    def set_style_bg_grad_stop(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_grad_stop(value, part)

        self.__attrs['set_style_bg_grad_stop'][part] = value

    def set_style_bg_img_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_img_opa(value, part)

        self.__attrs['set_style_bg_img_opa'][part] = value

    def set_style_bg_img_recolor(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_img_recolor(value, part)

        self.__attrs['set_style_bg_img_recolor'][part] = value

    def set_style_bg_img_recolor_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_img_recolor_opa(value, part)

        self.__attrs['set_style_bg_img_recolor_opa'][part] = value

    def set_style_bg_img_src(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_img_src(value, part)

        self.__attrs['set_style_bg_img_src'][part] = value

    def set_style_bg_img_tiled(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_img_tiled(value, part)

        self.__attrs['set_style_bg_img_tiled'][part] = value

    def set_style_bg_main_stop(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_main_stop(value, part)

        self.__attrs['set_style_bg_main_stop'][part] = value

    def set_style_bg_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_bg_opa(value, part)

        self.__attrs['set_style_bg_opa'][part] = value

    def set_style_blend_mode(self, value, part):  # labels
        for label in self.labels:
            label.set_style_blend_mode(value, part)

        self.__attrs['set_style_blend_mode'][part] = value

    def set_style_border_color(self, value, part):  # labels
        for label in self.labels:
            label.set_style_border_color(value, part)

        self.__attrs['set_style_border_color'][part] = value

    def set_style_border_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_border_opa(value, part)

        self.__attrs['set_style_border_opa'][part] = value

    def set_style_border_post(self, value, part):  # labels
        for label in self.labels:
            label.set_style_border_post(value, part)

        self.__attrs['set_style_border_post'][part] = value

    def set_style_border_side(self, value, part):  # labels
        for label in self.labels:
            label.set_style_border_side(value, part)

        self.__attrs['set_style_border_side'][part] = value

    def set_style_border_width(self, value, part):  # labels
        for label in self.labels:
            label.set_style_border_width(value, part)

        self.__attrs['set_style_border_width'][part] = value

    def set_style_clip_corner(self, value, part):  # labels
        for label in self.labels:
            label.set_style_clip_corner(value, part)

        self.__attrs['set_style_clip_corner'][part] = value

    def set_style_color_filter_dsc(self, value, part):  # labels
        for label in self.labels:
            label.set_style_color_filter_dsc(value, part)

        self.__attrs['set_style_color_filter_dsc'][part] = value

    def set_style_color_filter_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_color_filter_opa(value, part)

        self.__attrs['set_style_color_filter_opa'][part] = value

    def set_style_flex_cross_place(self, *args, **kwargs):  # disable
        pass

    def set_style_flex_flow(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_flex_grow(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_flex_main_place(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_flex_track_place(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_cell_column_pos(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_cell_column_span(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_cell_row_pos(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_cell_row_span(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_cell_x_align(self, *args, **kwargs):# disable
        raise NotImplementedError

    def set_style_grid_cell_y_align(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_column_align(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_column_dsc_array(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_row_align(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_grid_row_dsc_array(self, *args, **kwargs): # disable
        raise NotImplementedError

    def set_style_img_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_img_opa(value, part)

        self.__attrs['set_style_img_opa'][part] = value

    def set_style_img_recolor(self, value, part):  # labels
        for label in self.labels:
            label.set_style_img_recolor(value, part)

        self.__attrs['set_style_img_recolor'][part] = value

    def set_style_img_recolor_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_img_recolor_opa(value, part)

        self.__attrs['set_style_img_recolor_opa'][part] = value

    def set_style_margin_all(self, value, part):  # labels
        for label in self.labels:
            label.set_style_margin_all(value, part)

        self.__attrs['set_style_margin_all'][part] = value

    def set_style_margin_bottom(self, value, part):  # labels
        for label in self.labels:
            label.set_style_margin_bottom(value, part)

        self.__attrs['set_style_margin_bottom'][part] = value

    def set_style_margin_hor(self, value, part):  # labels
        for label in self.labels:
            label.set_style_margin_hor(value, part)

        self.__attrs['set_style_margin_hor'][part] = value

    def set_style_margin_left(self, value, part):  # labels
        for label in self.labels:
            label.set_style_margin_left(value, part)

        self.__attrs['set_style_margin_left'][part] = value

    def set_style_margin_right(self, value, part):  # labels
        for label in self.labels:
            label.set_style_margin_right(value, part)

        self.__attrs['set_style_margin_right'][part] = value

    def set_style_margin_top(self, value, part):  # labels
        for label in self.labels:
            label.set_style_margin_top(value, part)

        self.__attrs['set_style_margin_top'][part] = value

    def set_style_margin_ver(self, value, part):  # labels
        for label in self.labels:
            label.set_style_margin_ver(value, part)

        self.__attrs['set_style_margin_ver'][part] = value

    def set_style_outline_color(self, value, part):  # labels
        for label in self.labels:
            label.set_style_outline_color(value, part)

        self.__attrs['set_style_outline_color'][part] = value

    def set_style_outline_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_outline_opa(value, part)

        self.__attrs['set_style_outline_opa'][part] = value

    def set_style_outline_pad(self, value, part):  # labels
        for label in self.labels:
            label.set_style_outline_pad(value, part)

        self.__attrs['set_style_outline_pad'][part] = value

    def set_style_outline_width(self, value, part):  # labels
        for label in self.labels:
            label.set_style_outline_width(value, part)

        self.__attrs['set_style_outline_width'][part] = value

    def set_style_pad_all(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_all(value, part)

        self.__attrs['set_style_pad_all'][part] = value

    def set_style_pad_bottom(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_bottom(value, part)

        self.__attrs['set_style_pad_bottom'][part] = value

    def set_style_pad_column(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_column(value, part)

        self.__attrs['set_style_pad_column'][part] = value

    def set_style_pad_gap(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_gap(value, part)

        self.__attrs['set_style_pad_gap'][part] = value

    def set_style_pad_hor(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_hor(value, part)

        self.__attrs['set_style_pad_hor'][part] = value

    def set_style_pad_left(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_left(value, part)

        self.__attrs['set_style_pad_left'][part] = value

    def set_style_pad_right(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_right(value, part)

        self.__attrs['set_style_pad_right'][part] = value

    def set_style_pad_row(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_row(value, part)

        self.__attrs['set_style_pad_row'][part] = value

    def set_style_pad_top(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_top(value, part)

        self.__attrs['set_style_pad_top'][part] = value

    def set_style_pad_ver(self, value, part):  # labels
        for label in self.labels:
            label.set_style_pad_ver(value, part)

        self.__attrs['set_style_pad_ver'][part] = value

    def set_style_radius(self, radius):
        self.radius = radius

    def set_style_shadow_color(self, value, part):  # labels
        for label in self.labels:
            label.set_style_shadow_color(value, part)

        self.__attrs['set_style_shadow_color'][part] = value

    def set_style_shadow_ofs_x(self, value, part):  # labels
        for label in self.labels:
            label.set_style_shadow_ofs_x(value, part)

        self.__attrs['set_style_shadow_ofs_x'][part] = value

    def set_style_shadow_ofs_y(self, value, part):  # labels
        for label in self.labels:
            label.set_style_shadow_ofs_y(value, part)

        self.__attrs['set_style_shadow_ofs_y'][part] = value

    def set_style_shadow_opa(self, value, part):  # labels
        for label in self.labels:
            label.set_style_shadow_opa(value, part)

        self.__attrs['set_style_shadow_opa'][part] = value

    def set_style_shadow_spread(self, value, part):  # labels
        for label in self.labels:
            label.set_style_shadow_spread(value, part)

        self.__attrs['set_style_shadow_spread'][part] = value

    def set_style_shadow_width(self, value, part):  # labels
        for label in self.labels:
            label.set_style_shadow_width(value, part)

        self.__attrs['set_style_shadow_width'][part] = value

    def set_style_text_color(self, value, part):  # labels
        for label in self.labels:
            label.set_style_text_color(value, part)

        self.__attrs['set_style_text_color'][part] = value

    def set_style_text_decor(self, value, part):  # labels
        for label in self.labels:
            label.set_style_text_decor(value, part)

        self.__attrs['set_style_text_decor'][part] = value

    def set_style_text_font(self, value, part):  # labels
        for label in self.labels:
            label.set_style_text_font(value, part)

        self.__attrs['set_style_text_font'][part] = value

    def set_style_text_letter_space(self, value, part):  # labels
        for label in self.labels:
            label.set_style_text_letter_space(value, part)

        self.__attrs['set_style_text_letter_space'][part] = value

    def set_style_text_line_space(self, value, part):  # labels
        for label in self.labels:
            label.set_style_text_line_space(value, part)

        self.__attrs['set_style_text_line_space'][part] = value

    def set_text_selection_end(self):  # labels
        raise NotImplementedError

    def set_text_selection_start(self):  # labels
        raise NotImplementedError

    def set_text_static(self):  # labels
        raise NotImplementedError