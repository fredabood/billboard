from datetime import datetime


def chart_meta_gen(soup):

    chart_name = soup.find_all(
        'span',
        {'class': 'chart-detail-header--hidden'}
        )[0].contents[0]

    hiw_headline = soup.find_all(
        'div',
        {'class': 'how-it-works-modal__headline'}
        )[0].contents[0]

    hiw_description = soup.find_all(
        'div',
        {'class': 'how-it-works-modal__description'}
        )[0].p.contents[0]

    chart_week = soup.find_all(
        'button',
        {'class': 'chart-detail-header__date-selector-button'}
        )[0].contents[0].replace('\n', '').strip()
    chart_week = datetime.strptime(chart_week, '%B %d, %Y').strftime('%Y%m%d')

    return (chart_name, hiw_headline, hiw_description, chart_week)


def current_rank_gen(soup):

    current_rank = [1]

    for i in soup.find_all('div', {'class': 'chart-list-item__rank '}):
        current_rank.append(int(i.contents[0].replace('\n', '').strip()))

    return current_rank


def last_week_rank_gen(soup):

    last_week_rank = [None]

    for i in soup.find_all('div', {'class': 'chart-list-item__last-week'}):
        last_week_rank.append(int(i.contents[0]))

    return last_week_rank


def weeks_at_one_gen(soup):

    weeks_at_one = []

    weeks_at_one.append(int(soup.find_all(
        'div',
        {'class': 'chart-number-one__weeks-at-one'}
        )[0].contents[0]))

    for i in soup.find_all('div', {'class': 'chart-list-item__weeks-at-one'}):
        weeks_at_one.append(int(i.contents[0]))

    return weeks_at_one


def weeks_on_chart_gen(soup):

    weeks_on_chart = []

    weeks_on_chart.append(int(soup.find_all(
        'div',
        {'class': 'chart-number-one__weeks-on-chart'}
        )[0].contents[0]))

    for i in soup.find_all('div', {'class': 'chart-list-item__weeks-on-chart'}):
        weeks_on_chart.append(int(i.contents[0]))

    return weeks_on_chart


def song_title_gen(soup):

    song_title = []

    song_title.append(soup.find_all(
        'div',
        {'class': 'chart-number-one__title'}
        )[0].contents[0])

    for i in soup.find_all('span', {'class': 'chart-list-item__title-text'}):
        song_title.append(i.contents[0].replace('\n', '').strip())

    return song_title


def artist_gen(soup):

    link_to_artist = []
    artist = []

    artist.append(soup.find_all(
        'div',
        {'class': 'chart-number-one__artist'}
        )[0].a.contents[0].replace('\n', '').strip())
    try:
        link_to_artist.append(
            "https://billboard.com" + soup.find_all(
                'div',
                {'class': 'chart-number-one__artist'}
                )[0].a['href'])
    except:
        link_to_artist.append(None)

    for i in soup.find_all('div', {'class': 'chart-list-item__artist'}):
        try:
            artist.append(soup.find_all(
                'div',
                {'class': 'chart-list-item__artist'}
                )[3].a.contents[0].replace('\n', '').strip())
            link_to_artist.append("https://billboard.com" + soup.find_all(
                'div',
                {'class': 'chart-list-item__artist'})[3].a['href'])
        except:
            artist.append(soup.find_all(
                'div',
                {'class': 'chart-list-item__artist'}
                )[0].contents[0].replace('\n', '').strip())
            link_to_artist.append(None)

    return (artist, link_to_artist)


def lyric_link_gen(soup):

    link_to_lyrics = []

    try:
        link_to_lyrics.append(soup.find_all(
            'div',
            {'class': 'chart-number-one__lyrics'}
            )[0].a['href'])
    except:
        link_to_lyrics.append(None)

    for i in soup.find_all('div', {'class': 'chart-list-item__lyrics'}):
        try:
            link_to_lyrics.append(i.a['href'])
        except:
            link_to_lyrics.append(None)

    return link_to_lyrics


def award_list_gen(soup):

    all_awards = []

    artists_awards = []

    if len(soup.find_all('div', {'class': 'chart-number-one__awards'})) > 0:
        for i in soup.find_all('div', {'class': 'chart-number-one__awards'})[0].contents:

            try:
                artists_awards.append(i.contents[1].strip())
            except:
                pass

    artists_awards = artists_awards[1:]
    all_awards.append(artists_awards)

    for x in soup.find_all('div', {'class': 'chart-list-item__awards'}):

        artists_awards = []

        if len(x.contents) > 0:
            for i in x.contents:

                try:
                    artists_awards.append(i.contents[1].strip())
                except:
                    pass

            artists_awards = artists_awards[1:]
        all_awards.append(artists_awards)

    return all_awards


def chart_gen(soup):

    chart_names, hiw_headlines, hiw_descriptions, chart_weeks = chart_meta_gen(soup)
    artists, links_to_artist = artist_gen(soup)

    weekly_chart = dict(
        current_rank=current_rank_gen(soup),
        last_week_rank=last_week_rank_gen(soup),
        weeks_at_one=weeks_at_one_gen(soup),
        weeks_on_chart=weeks_on_chart_gen(soup),
        song_title=song_title_gen(soup),
        link_to_artist=links_to_artist,
        artist=artists,
        link_to_lyrics=lyric_link_gen(soup),
        all_awards=award_list_gen(soup)
    )

    chart = dict(
        chart_name=chart_names,
        hiw_headline=hiw_headlines,
        hiw_description=hiw_descriptions,
        chart_week=chart_weeks,
        chart=weekly_chart
    )

    return chart
