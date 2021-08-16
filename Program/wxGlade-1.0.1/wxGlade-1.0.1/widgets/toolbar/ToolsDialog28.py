# -*- coding: CP1252 -*-
#
# generated by wxGlade 1.0.0a8 on Sun Oct  4 20:06:14 2020
#

import wx




class ToolsDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((900, 600))
        self.SetTitle("Toolbar Editor")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_5, 0, wx.EXPAND, 0)

        grid_sizer = wx.FlexGridSizer(7, 2, 0, 0)
        sizer_5.Add(grid_sizer, 3, wx.EXPAND, 0)

        self.label_6 = wx.StaticText(self, wx.ID_ANY, "Label:")
        self.label_6.SetToolTipString("The menu entry text;\nenter & for access keys (using ALT key)\nappend e.g. \\\\tCtrl-X for keyboard shortcut")
        grid_sizer.Add(self.label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.label = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label.SetToolTipString("The menu entry text;\nenter & for access keys (using ALT key)\nappend e.g. \\\\tCtrl-X for keyboard shortcut")
        grid_sizer.Add(self.label, 1, wx.EXPAND, 0)

        label_11 = wx.StaticText(self, wx.ID_ANY, "Primary Bitmap:")
        grid_sizer.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        sizer_primary_bitmap = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer.Add(sizer_primary_bitmap, 1, wx.EXPAND, 0)

        self.bitmap1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.bitmap1.SetToolTipString("If the bitmap should be loaded from a file, use the \"...\" button or just\ndrop a file on the text field.\nWhen dropping a file from inside the project directory, a relative path is\nentered unless you hold the ALT or CTRL key.")
        sizer_primary_bitmap.Add(self.bitmap1, 1, 0, 0)

        self.bitmap1_button_ART = wx.Button(self, wx.ID_ANY, "A")
        self.bitmap1_button_ART.SetMinSize((20, -1))
        self.bitmap1_button_ART.SetToolTipString("Select standard art")
        sizer_primary_bitmap.Add(self.bitmap1_button_ART, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 0)

        self.bitmap1_button = wx.Button(self, wx.ID_ANY, "...")
        sizer_primary_bitmap.Add(self.bitmap1_button, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 0)

        label_12 = wx.StaticText(self, wx.ID_ANY, "Disabled Bitmap:")
        grid_sizer.Add(label_12, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        sizer_primary_bitmap = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer.Add(sizer_primary_bitmap, 1, wx.EXPAND, 0)

        self.bitmap2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.bitmap2.SetToolTipString("If the bitmap should be loaded from a file, use the \"...\" button or just\ndrop a file on the text field.\nWhen dropping a file from inside the project directory, a relative path is\nentered unless you hold the ALT or CTRL key.")
        sizer_primary_bitmap.Add(self.bitmap2, 1, 0, 0)

        self.bitmap2_button = wx.Button(self, wx.ID_ANY, "...")
        sizer_primary_bitmap.Add(self.bitmap2_button, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 0)

        self.label_7 = wx.StaticText(self, wx.ID_ANY, "Event Handler:")
        self.label_7.SetToolTipString("Enter the name of an event handler method; this will be created as stub")
        grid_sizer.Add(self.label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.handler = wx.TextCtrl(self, wx.ID_ANY, "")
        self.handler.SetToolTipString("Enter the name of an event handler method; this will be created as stub")
        grid_sizer.Add(self.handler, 1, wx.EXPAND, 0)

        self.label_9 = wx.StaticText(self, wx.ID_ANY, "Short Help:")
        self.label_9.SetToolTipString("This will be displayed as tooltip")
        grid_sizer.Add(self.label_9, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.short_help = wx.TextCtrl(self, wx.ID_ANY, "")
        self.short_help.SetToolTipString("This will be displayed as tooltip")
        grid_sizer.Add(self.short_help, 1, wx.EXPAND, 0)

        label_13 = wx.StaticText(self, wx.ID_ANY, "Long Help:")
        label_13.SetToolTipString("This will be displayed in the status bar")
        grid_sizer.Add(label_13, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.long_help = wx.TextCtrl(self, wx.ID_ANY, "")
        self.long_help.SetToolTipString("This will be displayed in the status bar")
        grid_sizer.Add(self.long_help, 1, wx.EXPAND, 0)

        self.label_10 = wx.StaticText(self, wx.ID_ANY, "ID:")
        self.label_10.SetToolTipString("optional: enter wx ID")
        grid_sizer.Add(self.label_10, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.id = wx.TextCtrl(self, wx.ID_ANY, "")
        self.id.SetToolTipString("optional: enter wx ID")
        grid_sizer.Add(self.id, 0, 0, 0)

        self.type = wx.RadioBox(self, wx.ID_ANY, "Type", choices=["Normal", "Checkable", "Radio"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.type.SetSelection(0)
        sizer_5.Add(self.type, 0, wx.ALL, 4)

        sizer_5.Add((20, 20), 1, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_6, 0, wx.EXPAND, 0)

        self.ok = wx.Button(self, wx.ID_OK, "&OK")
        self.ok.SetToolTipString("Alt+O or Alt+Enter or Ctrl+Enter")
        sizer_6.Add(self.ok, 0, wx.ALL, 5)

        self.cancel = wx.Button(self, wx.ID_CANCEL, "&Cancel")
        self.cancel.SetToolTipString("Alt+C or Alt+F4")
        sizer_6.Add(self.cancel, 0, wx.ALL, 5)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)

        self.move_up = wx.Button(self, wx.ID_ANY, "Up")
        self.move_up.SetToolTipString("Move selected item up (Alt-Up)")
        sizer_2.Add(self.move_up, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 8)

        self.move_down = wx.Button(self, wx.ID_ANY, "Down")
        self.move_down.SetToolTipString("Move selected item down (Alt-Down)")
        sizer_2.Add(self.move_down, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 8)

        sizer_2.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL, 0)

        self.add = wx.Button(self, wx.ID_ANY, "&Add")
        self.add.SetToolTipString("Alt+A")
        sizer_2.Add(self.add, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 8)

        self.remove = wx.Button(self, wx.ID_ANY, "&Remove")
        self.remove.SetToolTipString("Alt+R")
        sizer_2.Add(self.remove, 0, wx.BOTTOM | wx.TOP, 8)

        self.add_sep = wx.Button(self, wx.ID_ANY, "Add &Separator")
        self.add_sep.SetToolTipString("Alt+S")
        sizer_2.Add(self.add_sep, 0, wx.ALL, 8)

        sizer_2.Add((20, 20), 2, wx.ALIGN_CENTER_VERTICAL, 0)

        self.items = wx.ListCtrl(self, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_EDIT_LABELS | wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.items.SetToolTipString("For navigation use the mouse or the up/down arrows")
        self.items.InsertColumn(0, "Label", format=wx.LIST_FORMAT_LEFT, width=180)
        self.items.InsertColumn(1, "Primary Bitmap", format=wx.LIST_FORMAT_LEFT, width=180)
        self.items.InsertColumn(2, "Disabled Bitmap", format=wx.LIST_FORMAT_LEFT, width=120)
        self.items.InsertColumn(3, "Short Help", format=wx.LIST_FORMAT_LEFT, width=120)
        self.items.InsertColumn(4, "Long Help", format=wx.LIST_FORMAT_LEFT, width=180)
        self.items.InsertColumn(5, "Type", format=wx.LIST_FORMAT_LEFT, width=50)
        self.items.InsertColumn(6, "Event Handler", format=wx.LIST_FORMAT_LEFT, width=120)
        self.items.InsertColumn(7, "Id", format=wx.LIST_FORMAT_LEFT, width=50)
        sizer_1.Add(self.items, 1, wx.EXPAND, 0)

        grid_sizer.AddGrowableCol(1)

        self.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_TEXT, self.on_label_edited, self.label)
        self.Bind(wx.EVT_TEXT, self.on_bitmap1_edited, self.bitmap1)
        self.Bind(wx.EVT_BUTTON, self.select_bitmap1_art, self.bitmap1_button_ART)
        self.Bind(wx.EVT_BUTTON, self.select_bitmap1, self.bitmap1_button)
        self.Bind(wx.EVT_TEXT, self.on_bitmap2_edited, self.bitmap2)
        self.Bind(wx.EVT_BUTTON, self.select_bitmap2, self.bitmap2_button)
        self.Bind(wx.EVT_TEXT, self.on_event_handler_edited, self.handler)
        self.Bind(wx.EVT_TEXT, self.on_help_str_edited, self.short_help)
        self.Bind(wx.EVT_TEXT, self.on_long_help_str_edited, self.long_help)
        self.Bind(wx.EVT_TEXT, self.on_id_edited, self.id)
        self.Bind(wx.EVT_RADIOBOX, self.on_type_edited, self.type)
        self.Bind(wx.EVT_BUTTON, self.on_OK, self.ok)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.cancel)
        self.Bind(wx.EVT_BUTTON, self.move_item_up, self.move_up)
        self.Bind(wx.EVT_BUTTON, self.move_item_down, self.move_down)
        self.Bind(wx.EVT_BUTTON, self.add_item, self.add)
        self.Bind(wx.EVT_BUTTON, self.remove_item, self.remove)
        self.Bind(wx.EVT_BUTTON, self.add_separator, self.add_sep)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.on_label_edited, self.items)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.show_item, self.items)

    def on_label_edited(self, event):
        print("Event handler 'on_label_edited' not implemented!")
        event.Skip()

    def on_bitmap1_edited(self, event):
        print("Event handler 'on_bitmap1_edited' not implemented!")
        event.Skip()

    def select_bitmap1_art(self, event):
        print("Event handler 'select_bitmap1_art' not implemented!")
        event.Skip()

    def select_bitmap1(self, event):
        print("Event handler 'select_bitmap1' not implemented!")
        event.Skip()

    def on_bitmap2_edited(self, event):
        print("Event handler 'on_bitmap2_edited' not implemented!")
        event.Skip()

    def select_bitmap2(self, event):
        print("Event handler 'select_bitmap2' not implemented!")
        event.Skip()

    def on_event_handler_edited(self, event):
        print("Event handler 'on_event_handler_edited' not implemented!")
        event.Skip()

    def on_help_str_edited(self, event):
        print("Event handler 'on_help_str_edited' not implemented!")
        event.Skip()

    def on_long_help_str_edited(self, event):
        print("Event handler 'on_long_help_str_edited' not implemented!")
        event.Skip()

    def on_id_edited(self, event):
        print("Event handler 'on_id_edited' not implemented!")
        event.Skip()

    def on_type_edited(self, event):
        print("Event handler 'on_type_edited' not implemented!")
        event.Skip()

    def on_OK(self, event):
        print("Event handler 'on_OK' not implemented!")
        event.Skip()

    def on_cancel(self, event):
        print("Event handler 'on_cancel' not implemented!")
        event.Skip()

    def move_item_up(self, event):
        print("Event handler 'move_item_up' not implemented!")
        event.Skip()

    def move_item_down(self, event):
        print("Event handler 'move_item_down' not implemented!")
        event.Skip()

    def add_item(self, event):
        print("Event handler 'add_item' not implemented!")
        event.Skip()

    def remove_item(self, event):
        print("Event handler 'remove_item' not implemented!")
        event.Skip()

    def add_separator(self, event):
        print("Event handler 'add_separator' not implemented!")
        event.Skip()

    def show_item(self, event):
        print("Event handler 'show_item' not implemented!")
        event.Skip()

