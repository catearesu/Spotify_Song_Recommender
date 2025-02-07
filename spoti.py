def spoti_open(song_name):
    from dotenv import load_dotenv
    import os

    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    import time
    import webbrowser

    load_dotenv()
    user=os.getenv("client")
    password=os.getenv("secret")
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=user, client_secret=password))

    opensong=sp.search(q=song_name, limit=1)
    browser=opensong["tracks"]["items"][0]["external_urls"]["spotify"]
    time.sleep(2)
    webbrowser.open(browser)


def spoti_recommend(song):
    from dotenv import load_dotenv
    import os

    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    import time
    import webbrowser

    load_dotenv()
    user=os.getenv("client")
    password=os.getenv("secret")
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=user, client_secret=password))

    results=sp.search(q=song, limit=50)
    for i in results["tracks"]["items"]:
            isyoursong=input(f'Is your song {i["name"]} by {i["artists"][0]["name"]}')
            if isyoursong.lower() in ["yes", "y", "si", "sí"]:  # es esta tu canción? o esta? o esta? (hasta que diga que sí)
                songproposed=i["name"]
                artistproposed=i["artists"][0]["name"]
                artistid=i["artists"][0]["id"]
    #una vez tengamos la canción y el artista correcto, haremos una query para buscar específicamente una recomendación que no sea del mismo artista. 
                recommendations=sp.search(q=f'{songproposed+artistproposed}', limit=50)
                for j in recommendations["tracks"]["items"]:
                    if j["artists"][0]["id"]!=artistid:
                        print(f'I recommend you {j["name"]} by {j["artists"][0]["name"]}')
                        time.sleep(3)

                        browser=j["external_urls"]["spotify"]
                        webbrowser.open(browser)
                        return
    print("I am never gonna give you up... but we did not find a recommendation for your song. Good luck next time!")
    time.sleep(2)
    webbrowser.open("https://open.spotify.com/track/4PTG3Z6ehGkBFwjybzWkR8")
    return