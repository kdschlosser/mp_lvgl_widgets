import lvgl as lv

from .._style import style as _style


class ClickableTab(lv.obj):

    def __init__(self, parent, pos):
        self.parent = parent
        super().__init__(self)

        self.set_size(72, 26)
        x, y = pos
        self.set_x(x)
        self.set_y(y)


TAB_VIEW_EVENT_TAB_CHANGING = 0xC8
TAB_VIEW_EVENT_TAB_CHANGED = 0xC9

TAB_VIEW_LEFT = 3
TAB_VIEW_RIGHT = 2
TAB_VIEW_TOP = 0
TAB_VIEW_BOTTOM = 1


class _button_bar(lv.obj):

    def __init__(self, parent):

        if not isinstance(parent, _tab_bar):
            raise ValueError('this class is for internal use only')

        super().__init__(parent)

        self.add_style(_style, 0)
        self.buttons = []

    def add_button(self):
        button = lv.btn(self)
        button.add_style(_style, 0)
        button.add_event_cb(self.on_button, lv.EVENT.CLICKED, None)
        self.buttons.append(button)
        self.setup_button(len(self.buttons) - 1)

    def setup_button(self, index):
        parent = self.get_parent()
        button = self.buttons[index]

        t = parent.get_tab(index)
        x = t.get_x()
        y = t.get_y()

        orientation = parent.orientation

        if orientation in (TAB_VIEW_RIGHT, TAB_VIEW_LEFT):
            y += 28
            height = 78
            width = 31
            x += 2
        else:
            x += 28
            y += 2
            width = 78
            height = 31

        button.set_size(height, width)
        button.set_x(x)
        button.set_y(y)

    def remove_button(self, index):
        buttons = self.buttons
        button = buttons.pop(index)
        button.delete()

        x = button.get_x()
        y = button.get_y()

        for i in range(index, len(buttons)):
            tmp_x = buttons[i].get_x()
            tmp_y = buttons[i].get_y()

            buttons[i].set_x(x)
            buttons[i].set_y(y)
            x = tmp_x
            y = tmp_y

    def on_button(self, event):
        button = event.get_target_obj()
        index = self.buttons.index(button)

        parent = self.get_parent().get_parent()

        old_t = parent.get_tab_active()

        lv.event_send(old_t, TAB_VIEW_EVENT_TAB_CHANGING, index)
        lv.event_send(parent, TAB_VIEW_EVENT_TAB_CHANGING, old_t)

        parent.set_tab_active(index)  # NOQA
        new_t = parent.get_tab_active()

        lv.event_send(new_t, TAB_VIEW_EVENT_TAB_CHANGED, old_t)
        lv.event_send(parent, TAB_VIEW_EVENT_TAB_CHANGED, new_t)


class _tab_bar(lv.obj):

    def __init__(self, parent):
        if not isinstance(parent, tab_view):
            raise ValueError('this class is for internal use only')

        super().__init__(parent)

        self.tabs = []
        self.orientation = TAB_VIEW_TOP

        self.button_bar = button_bar = _button_bar(self)
        button_bar.set_x(0)
        button_bar.set_y(0)

        self._original_bg_color = lv.color_hex(0x0A02FF)
        self._bg_color = None

    def set_width(self, value):
        self.button_bar.set_width(value)
        super().set_width(value)

    def set_height(self, value):
        self.button_bar.set_height(value)
        super().set_height(value)

    def set_size(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def change_tab_position(self, old_index, new_index):
        t = self.tabs.pop(old_index)
        self.tabs.insert(new_index, t)
        t._index = new_index

        for t in self.tabs:
            self.setup_tab(t)

    def set_style_bg_color(self, color, selector):
        if color == self._original_bg_color:
            opa = 0
            self._bg_color = None
        else:
            opa = 255
            self._bg_color = color

        for t in self.tabs:
            t.set_style_img_recolor(color, 0)
            t.set_style_img_recolor_opa(opa)

    def add_tab(self, label):
        t = _tab_bar_tab(self)
        self.tabs.append(t)
        t._index = len(self.tabs) - 1
        t.set_text(label)
        self.setup_tab(t)
        self.button_bar.add_button()
        if self._bg_color is not None:
            t.set_style_img_recolor(self._bg_color, 0)
            t.set_style_img_recolor_opa(255, 0)

        return t

    def get_tab(self, index):
        return self.tabs[index]

    def remove_tab(self, index):
        t = self.tabs.pop(index)
        self.button_bar.remove_button(index)
        t.delete()

        for i, t in enumerate(self.tabs):
            if i < index:
                continue

            t._index = index
            self.setup_tab(t)

    def set_tab_label(self, index, label):
        self.tabs[index].set_text(label)

    def get_tab_label(self, index):
        return self.tabs[index].get_text()

    def set_tab_active(self, index):
        for i, t in enumerate(self.tabs):
            if i == index:
                t.is_active = True
            elif t.is_active:
                t.is_active = False

        self.button_bar.move_foreground()

    def setup_tab(self, t):
        if self.orientation in (TAB_VIEW_BOTTOM, TAB_VIEW_TOP):
            x = t.index * 88
            y = 0

            t.set_width(133)
            t.set_height(35)
        else:
            x = 0
            y = (t.index - 1) * 88

            t.set_width(35)
            t.set_height(133)

        t.set_x(x)
        t.set_y(y)

        if self.orientation == TAB_VIEW_LEFT:
            t.set_angle(900, 0)
            t.set_angle(900, 0)
        elif self.orientation == TAB_VIEW_RIGHT:
            t.set_angle(2700, 0)
            t.label.set_angle(900, 0)
        elif self.orientation == TAB_VIEW_BOTTOM:
            t.set_angle(1800, 0)

    def set_orientation(self, orientation):
        self.orientation = orientation
        for i, t in enumerate(self.tabs):
            self.setup_tab(t)
            self.button_bar.setup_button(i)


class _tab_bar_tab(lv.img):

    _image_data = None

    def __init__(self, parent):
        if not isinstance(parent, _tab_bar):
            raise ValueError('this class is for internal use only')

        if not hasattr(parent, 'tabs'):
            raise ValueError('this class is for internal use only')

        super().__init__(parent)
        self.add_style(_style, 0)
        self.set_src(self._image_data)
        self.set_size(lv.SIZE_CONTENT, lv.SIZE_CONTENT)

        self.label = lv.label(self)
        self.label.center()
        self.label.set_style_text_font(lv.font_montserrat_12, 0)
        self.active_color = lv.color_hex(0xC8C8C8)
        self.inactive_color = lv.color_hex(0x464646)
        self.label.set_style_text_color(self.active_color, 0)

        self._index = 0

    @property
    def is_active(self):
        return self.get_style_text_color(0) == self.active_color

    @is_active.setter
    def is_active(self, value):
        if value:
            self.label.set_style_text_color(self.active_color, 0)
        else:
            self.label.set_style_text_color(self.inactive_color, 0)

    def set_text(self, text):
        self.label.set_text(text)

    def get_text(self):
        return self.label.get_text()

    def set_text_active_color(self, color):
        self.active_color = color

    def get_active_color(self):
        return self.active_color

    def set_inactive_color(self, color):
        self.inactive_color = color

    def get_inactive_color(self):
        return self.inactive_color

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value


class limit_methods_mixin(object):

    def set_style_bg_color(self, value, selector):
        raise NotImplementedError

    def get_style_bg_color(self, selector):
        raise NotImplementedError

    def set_style_bg_opa(self, value, selector):
        raise NotImplementedError

    def get_style_bg_opa(self, selector):
        raise NotImplementedError

    def set_style_shadow_color(self, value, selector):
        raise NotImplementedError

    def get_style_shadow_color(self, selector):
        raise NotImplementedError

    def set_style_shadow_opa(self, value, selector):
        raise NotImplementedError

    def get_style_shadow_opa(self, selector):
        raise NotImplementedError

    def set_style_shadow_spread(self, value, selector):
        raise NotImplementedError

    def get_style_shadow_spread(self, selector):
        raise NotImplementedError

    def set_style_shadow_width(self, value, selector):
        raise NotImplementedError

    def get_style_shadow_width(self, selector):
        raise NotImplementedError

    def set_style_shadow_ofs_x(self, value, selector):
        raise NotImplementedError

    def get_style_shadow_ofs_x(self, selector):
        raise NotImplementedError

    def set_style_shadow_ofs_y(self, value, selector):
        raise NotImplementedError

    def get_style_shadow_ofs_y(self, selector):
        raise NotImplementedError

    def set_style_border_color(self, value, selector):
        raise NotImplementedError

    def get_style_border_color(self, selector):
        raise NotImplementedError

    def set_style_border_opa(self, value, selector):
        raise NotImplementedError

    def get_style_border_opa(self, selector):
        raise NotImplementedError

    def set_style_border_width(self, value, selector):
        raise NotImplementedError

    def get_style_border_width(self, selector):
        raise NotImplementedError

    def set_style_border_post(self, value, selector):
        raise NotImplementedError

    def get_style_border_post(self, selector):
        raise NotImplementedError

    def set_style_outline_opa(self, value, selector):
        raise NotImplementedError

    def get_style_outline_opa(self, selector):
        raise NotImplementedError

    def set_style_outline_pad(self, value, selector):
        raise NotImplementedError

    def get_style_outline_pad(self, selector):
        raise NotImplementedError

    def set_style_outline_width(self, value, selector):
        raise NotImplementedError

    def get_style_outline_width(self, selector):
        raise NotImplementedError

    def set_style_outline_color(self, value, selector):
        raise NotImplementedError

    def get_style_outline_color(self, selector):
        raise NotImplementedError

    def set_x(self, value):
        raise NotImplementedError

    def get_x(self):
        raise NotImplementedError

    def set_y(self, value):
        raise NotImplementedError

    def get_y(self):
        raise NotImplementedError

    def set_width(self, value):
        raise NotImplementedError

    def get_width(self):
        raise NotImplementedError

    def set_height(self, value):
        raise NotImplementedError

    def get_height(self):
        raise NotImplementedError

    def set_pos(self, x, y):
        raise NotImplementedError

    def set_size(self, width, height):
        raise NotImplementedError


class tab(lv.obj, limit_methods_mixin):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().add_style(_style, 0)
        self._index = -1
        super().set_style_bg_opa(255, 0)

    def delete(self):
        parent = self.get_parent()

        if parent is not None:
            parent._delete_tab(self)

        super().delete()

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        parent = self.get_parent()
        if parent is None:
            raise ValueError(
                'you can only change the index once a tab '
                'has been added to the tab_view'
            )

        self._index = parent._change_tab_index(self, value)


class tab_view(lv.obj, limit_methods_mixin):

    def __init__(self, parent):
        super().__init__(parent)
        super().add_style(_style, 0)
        self._orientation = TAB_VIEW_TOP
        self._tabs = []
        self._tab_bar = _tab_bar(self)
        self._bg_color = lv.color_hex(0x0A02FF)

    def _change_tab_index(self, t, new_index):
        new_index = min(new_index, len(self._tabs) - 1)

        self._tabs.remove(t)
        self._tabs.insert(t, new_index)

        for i, t in self._tabs:
            if i != t.index:
                self._tab_bar.change_tab_position(t.index, i)
                t._index = i

    def get_tab_active(self):
        index = self._tab_bar.get_tab_active()
        return self._tabs[index]

    def set_tab_active(self, index):
        if index < len(self._tabs):
            self._tabs[index].move_foreground()
            self._tab_bar.set_tab_active(index)

    def new_tab(self, label):
        t = tab(self)
        self.add_tab(t, label)
        return t

    def add_tab(self, label, t: tab):
        t.set_parent(self)
        self._tabs.append(t)
        t._index = len(self._tabs) - 1

        if self._orientation == TAB_VIEW_TOP:
            x = 0
            y = 35
            width = self.get_self_width()
            height = self.get_self_height() - 35
        elif self._orientation == TAB_VIEW_BOTTOM:
            x = 0
            y = 0
            width = self.get_self_width()
            height = self.get_self_height() - 35

        elif self._orientation == TAB_VIEW_RIGHT:
            x = 0
            y = 0
            width = self.get_self_width() - 35
            height = self.get_self_height()
        elif self._orientation == TAB_VIEW_LEFT:
            x = 35
            y = 0
            width = self.get_self_width() - 35
            height = self.get_self_height()
        else:
            raise RuntimeError('sanity check: this should never happen')

        super(tab, t).set_x(x)
        super(tab, t).set_y(y)
        super(tab, t).set_width(width)
        super(tab, t).set_height(height)

        tbt = self._tab_bar.add_tab(label)
        super(tab, t).set_style_bg_color(self._bg_color, 0)
        tbt.set_style_bg_color(self._bg_color, 0)

    def _delete_tab(self, t):
        if t in self._tabs:
            self._tabs.remove(t)
            self._tab_bar.remove_tab(t.index)

            for i, t in enumerate(self._tabs):
                t._index = i

    def remove_tab(self, index):
        if index > len(self._tabs) - 1:
            raise ValueError('tab index does not exist')

        t = self._tabs.pop(index)
        self._tab_bar.remove_tab(index)
        t.set_parent(None)

        for i, t in enumerate(self._tabs):
            t._index = i

        return t

    def get_tab(self, index):
        if index > len(self._tabs) - 1:
            raise ValueError('tab index does not exist')

        return self._tabs[index]

    def set_tab_label(self, index, label):
        if index > len(self._tabs) - 1:
            raise ValueError('tab index does not exist')

        self._tab_bar.set_tab_label(index, label)

    def get_tab_label(self, index):
        if index > len(self._tabs) - 1:
            raise ValueError('tab index does not exist')

        return self._tab_bar.get_tab_label(index)

    def set_orientation(self, orientation):
        width = self.get_self_width()
        height = self.get_self_height()

        if orientation == TAB_VIEW_TOP:
            x = 0
            y = 0
            height = 35
        elif orientation == TAB_VIEW_BOTTOM:
            x = 0
            y = height - 35
            height = 35
        elif orientation == TAB_VIEW_LEFT:
            x = 0
            y = 0
            width = 35
        elif orientation == TAB_VIEW_RIGHT:
            x = width - 35
            y = 0
            width = 35
        else:
            raise ValueError('Incorrect orientation was given.')

        self._orientation = orientation
        self._tab_bar.set_x(x)
        self._tab_bar.set_y(y)
        self._tab_bar.set_width(width)
        self._tab_bar.set_height(height)
        self._tab_bar.set_orientation(orientation)

    def get_orientation(self):
        return self._orientation

    def set_style_bg_color(self, color, part):
        self._bg_color = color

        for t in self._tabs:
            super(tab, t).set_style_bg_color(color, 0)

        self._tab_bar.set_style_bg_color(color, part)

    def get_style_bg_color(self, part):
        return self._bg_color

    def set_x(self, value):
        super().set_x(value)

    def get_x(self):
        return super().get_x()

    def set_y(self, value):
        super().set_y(value)

    def get_y(self):
        return super().get_y()

    def set_width(self, value):
        super().set_width(value)

        if self._orientation in (TAB_VIEW_TOP, TAB_VIEW_BOTTOM):
            self._tab_bar.set_width(value)

            for t in self._tabs:
                super(tab, t).set_width(value)
        else:
            width = value - 35
            for t in self._tabs:
                super(tab, t).set_width(width)

            if self._orientation == TAB_VIEW_RIGHT:
                self._tab_bar.set_x(width)

    def get_width(self):
        return super().get_width()

    def set_height(self, value):
        super().set_height(value)

        if self._orientation in (TAB_VIEW_RIGHT, TAB_VIEW_LEFT):
            self._tab_bar.set_height(value)
            for t in self._tabs:
                super(tab, t).set_height(value)
        else:
            height = value - 35
            for t in self._tabs:
                super(tab, t).set_height(height)

            if self._orientation == TAB_VIEW_BOTTOM:
                self._tab_bar.set_y(height)

    def get_height(self):
        return super().get_height()

    def set_pos(self, x, y):
        super().set_pos(x, y)

    def set_size(self, width, height):
        self.set_width(width)
        self.set_height(height)

