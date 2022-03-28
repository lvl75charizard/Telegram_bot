from requests_html import HTMLSession

URL = 'https://www.epicgames.com/store/en-US/free-games'


def GetGames(url):  # returns a dictionary with the details
    session = HTMLSession()
    games_list = []
    r = session.get(url)
    r.html.render(sleep=1, keep_page=True)
    details_of_free_games = r.html.find('div.css-1ukp34s')
    for name in details_of_free_games:
        split_lines = name.text.split('\n')
        games_list.append(f'{split_lines[1]} {split_lines[2]}')
        split_lines.clear()
    return games_list


for game in GetGames(URL):
    print(game)