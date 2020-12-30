from libqtile import layout, widget, bar
from libqtile.lazy import lazy
from libqtile.config import Key, Screen, Group

# Window key
mod = "mod4"

keys = [
    # Switch windows (VIM <3)
    Key([mod], 'h', lazy.layout.left()),
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod], 'l', lazy.layout.right()),

    # Resize windows (VIM <3)
    Key([mod, 'shift'], 'h', lazy.layout.grow_left()),
    Key([mod, 'shift'], 'j', lazy.layout.grow_down()),
    Key([mod, 'shift'], 'k', lazy.layout.grow_up()),
    Key([mod, 'shift'], 'l', lazy.layout.grow_right()),

    # Shuffle windows (VIM <3)
    Key([mod, 'control'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'control'], 'k', lazy.layout.shuffle_up()),
    Key([mod, 'control'], 'h', lazy.layout.shuffle_left()),
    Key([mod, 'control'], 'l', lazy.layout.shuffle_right()),

    # Spawn rofi
    Key([mod], 'e', lazy.spawn('rofi -show run')),

    # Switch layout (You can choose Columns, Columns and Columns :))
    Key([mod], 'Tab', lazy.next_layout()),

    # Kill window
    Key([mod], 'w', lazy.window.kill()),

    # Spawn URXVT terminal
    Key([mod], 'Return', lazy.spawn('urxvt')),

    # Shutdown Qtile
    Key([mod, 'shift'], 'q', lazy.shutdown()),
]

layouts = [
    layout.Columns(margin=8, border_focus='#777777'),
    layout.Max(),
    layout.MonadWide(margin=8, border_focus='#777777'),
]

widgets = [
    # Left side
    widget.CurrentLayoutIcon(),
    widget.GroupBox(rounded=False, highlight_method='line',
                    this_current_screen_border='#777777'),

    # That big gap in the middle
    widget.Spacer(length=bar.STRETCH),

    # Right side
    widget.Systray(),
    widget.Clock(format='%H:%M %d-%m-%Y', foreground='f1c40f'),
    widget.Battery(format='{char} {percent:2.0%}'),
    widget.Volume(),
]

screens = [Screen(top=bar.Bar(widgets, 30, background='#1d1d1d'))]

# Dict of pairs name : key
group_keys = {
    'CODE': 'a',
    'WEB': 's',
    'TERMINAL': 'd',
    '???': 'f',
}

# Register groups
groups = [Group(name) for name in group_keys]

# Bind keys for groups
for group in groups:
    keys.append(Key([mod], group_keys[group.name],
            lazy.group[group.name].toscreen()))

