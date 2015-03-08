import sublime
import sublime_plugin
import os
from threading import Timer

class BlockCursorEverywhere(sublime_plugin.EventListener):
    def show_block_cursor(self, view):
        validRegions = []
        for s in view.sel():
            if s.a != s.b:
                continue
            validRegions.append(sublime.Region(s.a, s.a + 1))
        if validRegions.__len__:
            view.add_regions('BlockCursorListener', validRegions, 'block_cursor')
        else:
            view.erase_regions('BlockCursorListener')

    def is_vintageous_installed(self):
        if int(sublime.version()) < 3000:
            return os.path.isdir(os.path.join(sublime.packages_path(), 'Vintageous'))
        else:
            return os.path.exists(os.path.join(sublime.installed_packages_path(), 'Vintageous.sublime-package'))

    def is_enabled(self, view, package_name):
        return package_name not in view.settings().get('ignored_packages', [])

    def on_selection_modified(self, view):
        is_widget = view.settings().get('is_widget')
        command_mode = view.settings().get('command_mode')

        if is_widget or not self.vi_enabled or (self.vi_enabled and not(command_mode)):
            view.erase_regions('BlockCursorListener')
            return

        self.show_block_cursor(view)

    def on_deactivated(self, view):
        view.erase_regions('BlockCursorListener')
        view.settings().clear_on_change('command_mode')
        self.current_view = None

    def on_activated(self, view):
        self.current_view = view
        self.timer = Timer(0, lambda: none)

        self.vintage_enabled = self.is_enabled(view, 'Vintage')
        self.vintageous_enabled = self.is_vintageous_installed() and self.is_enabled(view, 'Vintageous')
        self.vi_enabled = self.vintage_enabled or self.vintageous_enabled

        self.on_selection_modified(view)
        view.settings().add_on_change('command_mode', self.on_command_mode_change)

    def on_command_mode_change(self):
        # Debounce to prevent recursion and plugin crash https://github.com/karlhorky/BlockCursorEverywhere/issues/11
        self.timer.cancel()
        self.timer = Timer(0.0005, self.on_selection_modified, [self.current_view])
        self.timer.start()
