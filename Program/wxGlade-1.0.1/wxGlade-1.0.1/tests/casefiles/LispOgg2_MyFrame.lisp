;;; generated by wxGlade "faked test version"
;;;

(asdf:operate 'asdf:load-op 'wxcl)
(use-package "FFI")
(ffi:default-foreign-language :stdc)


;;; begin wxGlade: dependencies
(use-package :wxButton)
(use-package :wxCL)
(use-package :wxCheckBox)
(use-package :wxColour)
(use-package :wxEvent)
(use-package :wxEvtHandler)
(use-package :wxFrame)
(use-package :wxGrid)
(use-package :wxNotebook)
(use-package :wxPanel)
(use-package :wxRadioBox)
(use-package :wxSizer)
(use-package :wxStaticLine)
(use-package :wxStaticText)
(use-package :wxTextCtrl)
(use-package :wxWindow)
(use-package :wx_main)
(use-package :wx_wrapper)
;;; end wxGlade

;;; begin wxGlade: extracode
;;; useless extra code for LispOgg2_MyFrame
;;; end wxGlade


(defclass LispOgg2_MyFrame()
        ((top-window :initform nil :accessor slot-top-window)
        (label-1 :initform nil :accessor slot-label-1)
        (text-ctrl-1 :initform nil :accessor slot-text-ctrl-1)
        (button-3 :initform nil :accessor slot-button-3)
        (grid-sizer-1 :initform nil :accessor slot-grid-sizer-1)
        (notebook-1-pane-1 :initform nil :accessor slot-notebook-1-pane-1)
        (radio-box-1 :initform nil :accessor slot-radio-box-1)
        (sizer-4 :initform nil :accessor slot-sizer-4)
        (notebook-1-pane-2 :initform nil :accessor slot-notebook-1-pane-2)
        (text-ctrl-2 :initform nil :accessor slot-text-ctrl-2)
        (sizer-3 :initform nil :accessor slot-sizer-3)
        (notebook-1-pane-3 :initform nil :accessor slot-notebook-1-pane-3)
        (label-2 :initform nil :accessor slot-label-2)
        (text-ctrl-3 :initform nil :accessor slot-text-ctrl-3)
        (button-4 :initform nil :accessor slot-button-4)
        (checkbox-1 :initform nil :accessor slot-checkbox-1)
        (grid-sizer-2 :initform nil :accessor slot-grid-sizer-2)
        (notebook-1-pane-4 :initform nil :accessor slot-notebook-1-pane-4)
        (notebook-1 :initform nil :accessor slot-notebook-1)
        (static-line-1 :initform nil :accessor slot-static-line-1)
        (button-5 :initform nil :accessor slot-button-5)
        (button-2 :initform nil :accessor slot-button-2)
        (button-1 :initform nil :accessor slot-button-1)
        (sizer-2 :initform nil :accessor slot-sizer-2)
        (sizer-1 :initform nil :accessor slot-sizer-1)
        (grid-1 :initform nil :accessor slot-grid-1)
        (static-line-2 :initform nil :accessor slot-static-line-2)
        (button-6 :initform nil :accessor slot-button-6)
        (grid-sizer-3 :initform nil :accessor slot-grid-sizer-3)
        (sizer-5 :initform nil :accessor slot-sizer-5)))

(defun make-LispOgg2_MyFrame ()
        (let ((obj (make-instance 'LispOgg2_MyFrame)))
          (init obj)
          (set-properties obj)
          (do-layout obj)
          obj))

(defmethod init ((obj LispOgg2_MyFrame))
"Method creates the objects contained in the class."
        ;;; begin wxGlade: LispOgg2_MyFrame.__init__
        (setf (slot-top-window obj) (wxFrame_create nil wxID_ANY "" -1 -1 -1 -1 wxDEFAULT_FRAME_STYLE))
        (slot-top-window obj).wxWindow_SetSize((400, 300))
        (wxFrame_SetTitle (slot-top-window obj) (_"FrameOggCompressionDetails"))
        
        (setf (slot-sizer-5 obj) (wxBoxSizer_Create wxVERTICAL))
        
        (setf (slot-grid-sizer-3 obj) (wxGridSizer_Create 3 1 0 0))
        (wxSizer_AddSizer (slot-sizer-5 obj) (slot-grid-sizer-3 obj) 1 wxEXPAND 0 nil)
        
        (setf (slot-grid-1 obj) (wxGrid_Create (slot-top-window obj) wxID_ANY -1 -1 -1 -1 wxWANTS_CHARS))
        (wxGrid_CreateGrid (slot-grid-1 obj) 8 3 0)
        (wxSizer_AddWindow (slot-grid-sizer-3 obj) (slot-grid-1 obj) 1 wxEXPAND 0 nil)
        
        (setf (slot-static-line-2 obj) (wxStaticLine_Create (slot-top-window obj) wxID_ANY -1 -1 -1 -1 wxLI_HORIZONTAL))
        (wxSizer_AddWindow (slot-grid-sizer-3 obj) (slot-static-line-2 obj) 0 (logior wxALL wxEXPAND) 5 nil)
        
        (setf (slot-button-6 obj) (wxButton_Create (slot-top-window obj) wxID_CLOSE "" -1 -1 -1 -1 0))
        (wxWindow_SetFocus (slot-button-6 obj))
        (wxButton_SetDefault (slot-button-6 obj))
        (wxSizer_AddWindow (slot-grid-sizer-3 obj) (slot-button-6 obj) 0 (logior wxALIGN_RIGHT wxALL) 5 nil)
        
        (wxFlexGridSizer_AddGrowableRow (slot-grid-sizer-3 obj) 0)
        (wxFlexGridSizer_AddGrowableCol (slot-grid-sizer-3 obj) 0)
        
        (wxWindow_SetSizer (slot-top-window obj) (slot-sizer-5 obj))
        
        (wxFrame_layout (slot-FrameOggCompressionDetails self))
        ;;; end wxGlade
        )

(defmethod set-properties ((obj LispOgg2_MyFrame))
        )

(defmethod do-layout ((obj LispOgg2_MyFrame))
        )

;;; end of class LispOgg2_MyFrame


