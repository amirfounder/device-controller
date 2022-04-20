import webbrowser

REGISTER_INFO = [
    ('chrome', 'C:\Program Files\Google\Chrome\Application\chrome.exe'),
]

for name, path in REGISTER_INFO:
    webbrowser.register(name, None, webbrowser.BackgroundBrowser(path))


class Browser:
    @staticmethod
    def open(url: str):
        webbrowser.get('chrome').open(url)

    @staticmethod
    def open_new_tab(url: str):
        webbrowser.get('chrome').open_new_tab(url)

    def search_google(self, query: str):
        query.replace(' ', '+')
        url = f'https://google.com/search?q={query}'
        self.open_new_tab(url)
