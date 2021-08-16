#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Mon Jul  5 08:17:17 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Microscope(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Microscope.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1280, 720))
        self.SetTitle("frame")

        # Menu Bar
        self.main_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Save", "")
        self.Bind(wx.EVT_MENU, self.save_image, item)
        wxglade_tmp_menu.Append(wx.ID_ANY, "Exit", "")
        self.main_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, "Focus down", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "Focus up", "")
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_ANY, "Move left", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "Move right", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "Move down", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "Move up", "")
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_ANY, "Speed increase", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "Speed decrease", "")
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_ANY, "Increase light", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "Decrease light", "")
        self.main_menubar.Append(wxglade_tmp_menu, "Controls")
        self.SetMenuBar(self.main_menubar)
        # Menu Bar end

        self.mainPanel = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.controlPanel = wx.Panel(self.mainPanel, wx.ID_ANY)
        self.controlPanel.SetMinSize((320, 720))
        sizer_1.Add(self.controlPanel, 1, wx.EXPAND, 0)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        self.navigationPanel = wx.Panel(self.controlPanel, wx.ID_ANY)
        sizer_2.Add(self.navigationPanel, 1, wx.EXPAND, 0)

        grid_sizer_1 = wx.GridSizer(6, 3, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.up_button = wx.BitmapButton(self.navigationPanel, wx.ID_ANY, wx.Bitmap("D:/Personal/Microscope/Program/icons/up_arrow.png", wx.BITMAP_TYPE_ANY), style=wx.BU_AUTODRAW | wx.BU_BOTTOM | wx.BU_EXACTFIT | wx.BU_NOTEXT)
        self.up_button.SetSize(self.up_button.GetBestSize())
        grid_sizer_1.Add(self.up_button, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.left_button = wx.BitmapButton(self.navigationPanel, wx.ID_ANY, wx.Bitmap("D:/Personal/Microscope/Program/icons/left_arrow.png", wx.BITMAP_TYPE_ANY))
        self.left_button.SetSize(self.left_button.GetBestSize())
        grid_sizer_1.Add(self.left_button, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.right_button = wx.BitmapButton(self.navigationPanel, wx.ID_ANY, wx.Bitmap("D:/Personal/Microscope/Program/icons/right_arrow.png", wx.BITMAP_TYPE_ANY))
        self.right_button.SetMinSize((1032, 1032))
        grid_sizer_1.Add(self.right_button, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.bitmap_button_2 = wx.BitmapButton(self.navigationPanel, wx.ID_ANY, wx.Bitmap("D:/Personal/Microscope/Program/icons/down_arrow.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        grid_sizer_1.Add(self.bitmap_button_2, 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.capturePanel = wx.Panel(self.controlPanel, wx.ID_ANY)
        sizer_2.Add(self.capturePanel, 1, wx.EXPAND, 0)

        self.viewPanel = wx.Panel(self.mainPanel, wx.ID_ANY)
        self.viewPanel.SetMinSize((960, 720))
        sizer_1.Add(self.viewPanel, 1, wx.ALL | wx.EXPAND, 0)

        self.navigationPanel.SetSizer(grid_sizer_1)

        self.controlPanel.SetSizer(sizer_2)

        self.mainPanel.SetSizer(sizer_1)

        self.Layout()
        self.ShowFullScreen(True)

        self.Bind(wx.EVT_KEY_DOWN, self.onKey, self.mainPanel)
        # end wxGlade

    def save_image(self, event):  # wxGlade: Microscope.<event_handler>
        print("Event handler 'save_image' not implemented!")
        event.Skip()

    def onKey(self, event):  # wxGlade: Microscope.<event_handler>
        print("Event handler 'onKey' not implemented!")
        event.Skip()

# end of class Microscope

class MyApp(wx.App):
    def OnInit(self):
        self.frame = Microscope(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
