from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=22,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),
    separator(),
    powerline('color1', 'dark'),

    # Weather
    widget.WidgetBox(widgets=[widget.OpenWeather(background=colors['color1'],foreground='000000',cityid='1278314',
                              format=' {humidity} Feels like: {main_feels_like} {weather_details} @ ')],
                     background=colors['color1'],text_closed='盛 ',text_open=' ',fontsize=18,foreground='000000'),
    widget.OpenWeather(background=colors['color1'],foreground='000000',cityid='1278314',
                       format='{location_city}: {main_temp}°{units_temperature}'),
    
    # Time Date
    widget.WidgetBox(widgets=[widget.Clock(**base(bg='color2'), format='%A %d %B, %Y | ')],
                     background=colors['color2'],text_closed='  ',text_open='  ',fontsize=18,foreground='000000'),
    widget.Clock(**base(bg='color2'), format='%I:%M %p'),

    # CPU/RAM
    widget.WidgetBox(widgets=[widget.CPU(**base(bg='color3'),format="CPU {freq_current}GHz {load_percent}% "),
                              widget.CPUGraph(**base(bg='color3')),
                              widget.TextBox(**base(bg='color3'),text=" RAM ")],
                     background=colors['color3'],text_closed='  ',text_open='  ',fontsize=18,foreground='000000'),
    widget.Memory(**base(bg='color3'), measure_mem="G",format="{MemUsed:.1f}{mm} / {MemTotal:.0f}{mm} "),

    # Battery
    widget.Battery(**base(bg='color4'),charge_char=' ',discharge_char=' ',full_char=' ',empty_char=' '),
    
    widget.Backlight(**base(bg='color5'),backlight_name='amdgpu_bl0',format=' {percent:2.0%} ﯦ '), 

    powerline('dark', 'color5'),

    # Notifications
    widget.WidgetBox(widgets=[#widget.Notify(),
                              icon(bg="color6", text=' '),  # Icon: nf-fa-feed
                              widget.Net(**base(bg='color6'), interface='wlo1'),
                              widget.CurrentLayoutIcon(**base(bg='color7'), scale=0.65),
                              widget.CurrentLayout(**base(bg='color7'), padding=5),
                              icon(bg="color1", text=' '), # Icon: nf-fa-download
                              widget.CheckUpdates(distro='Arch',background=colors['color1'],
                                                  colour_have_updates=colors['text'],
                                                  colour_no_updates=colors['text'],
                                                  no_update_string='0')],
                              background=colors['dark'],text_closed=' ﰪ ',text_open=' ',fontsize=18),

    # Volume
    widget.PulseVolume(background=colors['dark'],limit_max_volume='true',emoji='true'),
    # icon(bg="color3", fontsize=17, text=' ',),
    # widget.Volume(**base(bg='color3'),format='{get_volume}'),

    # System Tray
    widget.Systray(background=colors['dark'], padding=5),
    
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
