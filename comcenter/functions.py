import webbrowser as wb


def google_search(query: str= '') -> 'Browser tab':
    """Searches the given query on goolgle search

    query: the string to search on goolgle search
    """
    if isinstance(query, str):
        wb.open_new_tab(f'https://www.google.com/search?q={query}')

    else:
        wb.open_new_tab('https://www.google.com')


def youtube_search(query: str) -> 'Browser tab':
    """Searches the given query on youtube
    
    query: the string to search on youtube
    """
    if isinstance(query, str):
        wb.open_new_tab(f'https://www.youtube.com/search?q={query}')

    else:
        wb.open_new_tab('https://www.youtube.com')


def open_site(site_name: str) -> 'Browser tab':
    """Opens the given site in browser

    site_name: name of the site to search
    """
    site_list = [
        'google',
        'youtube',
    ]

    if (isinstance(site_name, str) and
            site_name.lower() in site_list):
        wb.open_new_tab(f'https://www.{site_name.lower()}.com')
    
    else:
        wb.open_new_tab('https://www.google.com')