import comcenter.functions as fn

com_dict = {
    'search': fn.google_search,
    'google': fn.google_search,
    'youtube' : fn.youtube_search,
    'play': fn.youtube_search,
    'open': fn.open_site,
    'default': fn.google_search,
}

if __name__ == '__main__':
    print('\nAvailable functions are:')
    print(*com_dict.keys())