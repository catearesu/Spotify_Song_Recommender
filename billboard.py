def billboard100():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    songs=[]
    artists=[]
    lw_rank=[]
    weeks_on_chart=[]
    for song in soup.select("li h3", class_ = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")[:100]:
        songs.append(song.get_text().strip())
    for artist in soup.select("li ul li span", class_= "c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")[::7]:
        artists.append(artist.get_text().strip())
    for i in soup.select("div ul li ul li span", class_= "c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet")[1::7]:
        lw_rank.append(i.get_text().strip())
    for i in soup.select("div ul li ul li span", class_= "c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet")[3::7]:
        weeks_on_chart.append(i.get_text().strip())
    df = pd.DataFrame({"Song" : songs, "Artist" : artists, "Last_week_rank": lw_rank, "Weeks_on_chart": weeks_on_chart})
    return df