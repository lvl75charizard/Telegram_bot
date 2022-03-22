from requests_html import HTMLSession
session = HTMLSession()

url = 'https://www.epicgames.com/store/en-US/free-games'

r = session.get(url)
r.html.render(sleep=1, keep_page=True)
info = []


def GetFreeGames():
    bothFreeGames = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div')
    freeNow = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[1]/div')
    freeNowEndDate = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[2]/div')
    comingSoon = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div[2]/div/div/a/div/div/div[3]/span[1]/div')
    comingSoonDate = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div[2]/div/div/a/div/div/div[3]/span[2]/div')
    info.append(freeNow[0].text)
    info.append(freeNowEndDate[0].text)
    info.append(comingSoon[0].text)
    info.append(comingSoonDate[0].text)
    return info

