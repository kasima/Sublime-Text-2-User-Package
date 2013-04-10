import sublime_plugin


class HashRocket(sublime_plugin.TextCommand):

    def run(self, edit):
        self.edit = edit
        self.view.insert(edit, self.view.sel()[0].a, " => ")
