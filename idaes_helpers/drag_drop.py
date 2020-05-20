########################################################################
#                                                                      #
#                    IDAES Drag-N-Drop Helpers                         #
#                                                                      #
#  This file contains methods for adding drag-n-drop functionality to  #
#  the IDAES Flowsheet Editor program.                                 #
#                                                                      #
#  Author:  Timothy A. Fuller                                          #
#  Date:  5/20/2020                                                    #
#                                                                      #
#  Version:  1.0.0                                                     #
#                                                                      #
########################################################################


# Module imports
import tkinter


# Define the Drag-N-Drop Handler class
class DndHandler:

    root = None

    # Initialize this instance of the handler class
    def __init__(self, source, event):
        if event.num > 5:
            return
        root = event.widget._root()
        try:
            root.__dnd
            return # Don't start recursive dnd
        except AttributeError:
            root.__dnd = self
            self.root = root
        self.source = source
        self.target = None
        self.initial_button = button = event.num
        self.initial_widget = widget = event.widget
        self.release_pattern = "<B%d-ButtonRelease-%d>" % (button, button)
        self.save_cursor = widget['cursor'] or ""
        widget.bind(self.release_pattern, self.on_release)
        widget.bind("<Motion>", self.on_motion)
        widget['cursor'] = "hand2"

    # Delete this instance of the handler class
    def __del__(self):
        root = self.root
        self.root = None
        if root:
            try:
                del root.__dnd
            except AttributeError:
                pass

    # Handle the drag
    def on_motion(self, event):
        x, y = event.x_root, event.y_root
        target_widget = self.initial_widget.winfo_containing(x, y)
        source = self.source
        new_target = None
        while target_widget:
            try:
                attr = target_widget.dnd_accept
            except AttributeError:
                pass
            else:
                new_target = attr(source, event)
                if new_target:
                    break
            target_widget = target_widget.master
        old_target = self.target
        if old_target is new_target:
            if old_target:
                old_target.dnd_motion(source, event)
        else:
            if old_target:
                self.target = None
                old_target.dnd_leave(source, event)
            if new_target:
                new_target.dnd_enter(source, event)
                self.target = new_target

    # Handle the drop
    def on_release(self, event):
        self.finish(event, 1)

    # Cancel the drag-n-drop operation
    def cancel(self, event=None):
        self.finish(event, 0)

    # Finish the drag-n-drop operation
    def finish(self, event, commit=0):
        target = self.target
        source = self.source
        widget = self.initial_widget
        root = self.root
        try:
            del root.__dnd
            self.initial_widget.unbind(self.release_pattern)
            self.initial_widget.unbind("<Motion>")
            widget['cursor'] = self.save_cursor
            self.target = self.source = self.initial_widget = self.root = None
            if target:
                if commit:
                    target.dnd_commit(source, event)
                else:
                    target.dnd_leave(source, event)
        finally:
            source.dnd_end(target, event)
