from bs4 import BeautifulSoup
import requests
import time
import psycopg2


def find_player_stats():
    conn = psycopg2.connect(
        host="<host>",
        port="5432",
        database="scrapper-db",
        user="<user>",
        password="password"
    )

    cursor = conn.cursor()

    url = 'https://profilerr.net/cs-go/pro-players/settings/'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    players = soup.find_all('div', class_='border-b c-card-player-settings c-accordion__item js-accordion-item')

    for player in players:
        player.find('div', class_='c-card-player-settings__title').find('span').replace_with('')
        p_name = player.find('div', class_='c-card-player-settings__title').text.replace(' ', '')
        device_list = player.find_all('dd', class_='truncate')
        if device_list:
            p_monitor = device_list[0].text
            p_audio = device_list[1].text
            p_mouse = device_list[2].text
            p_keyboard = device_list[3].text
        else:
            p_monitor = "Not Listed"
            p_audio = "Not Listed"
            p_mouse = "Not Listed"
            p_keyboard = "Not Listed"
        p_edpi = player.find_all('dd', class_='c-card-player-settings__collapse-item-desc', )[2].text

        insert_query = 'DO $$ ' \
                       'BEGIN ' \
                       'IF EXISTS (SELECT FROM analytics WHERE name = %s) THEN ' \
                       'UPDATE analytics SET edpi = %s, monitor = %s, ' \
                       'audio = %s, mouse = %s, keyboard = %s WHERE name = %s; ' \
                       'ELSE ' \
                       'INSERT INTO analytics (name, edpi, monitor, audio, mouse, keyboard) ' \
                       'VALUES (%s, %s, %s, %s, %s,%s); ' \
                       'END IF; ' \
                       'END $$; '

        values = (p_name, p_edpi, p_monitor, p_audio, p_mouse, p_keyboard, p_name,
                  p_name, p_edpi, p_monitor, p_audio, p_mouse, p_keyboard)

        cursor.execute(insert_query, values)

        conn.commit()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    while True:
        find_player_stats()
        time_wait = 604800
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait)
