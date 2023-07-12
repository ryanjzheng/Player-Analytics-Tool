import psycopg2.extras
from collections import defaultdict

conn = psycopg2.connect(
    host="<host>",
    port="5432",
    database="scrapper-db",
    user="<user>",
    password="<password>"
)

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def mouse_analytics():
    query = 'SELECT mouse, COUNT (mouse) as value_occurrence ' \
            'FROM analytics ' \
            'GROUP BY mouse ' \
            'ORDER BY value_occurrence DESC'

    cursor.execute(query)

    mice = defaultdict(int)

    for mouse in cursor.fetchall():
        if 'Not Listed' in mouse[0]:
            continue
        elif 'Logitech G Pro X Superlight' in mouse[0]:
            mice['Logitech G Pro X Superlight'] = mice['Logitech G Pro X Superlight'] + mouse[1]
        elif 'Razer Deathadder V3 Pro' in mouse[0]:
            mice['Razer Deathadder V3 Pro'] = mice['Razer Deathadder V3 Pro'] + mouse[1]
        else:
            mice[mouse[0]] = mice[mouse[0]] + mouse[1]

    print(f'Top 3 Mice Used By Pros:')
    for i in range(3):
        top_mouse = max(mice, key=mice.get)
        print([top_mouse, mice[top_mouse]])
        del mice[top_mouse]

    print('')

def edpi_analytics():
    query = 'SELECT edpi FROM analytics'
    cursor.execute(query)

    total = 0
    i = 0
    for edpi in cursor.fetchall():
        if 'Unknown' not in edpi[0]:
            total += float(edpi[0])
            i += 1
    avg = float(total) / i
    print(f'Average EDPI of Pros: {avg}\n')



def monitor_analytics():
    query = 'SELECT monitor, COUNT (monitor) as value_occurrence ' \
            'FROM analytics ' \
            'GROUP BY monitor ' \
            'ORDER BY value_occurrence DESC ' \
            'LIMIT 4;'

    cursor.execute(query)
    monitor_arr = cursor.fetchall()

    print(f'Top 3 Monitors Used By Pros:')
    for i in range(1, 4):
        print(monitor_arr[i])
    print('')


def audio_analytics():
    query = 'SELECT audio, COUNT (mouse) as value_occurrence ' \
            'FROM analytics ' \
            'GROUP BY audio ' \
            'ORDER BY value_occurrence DESC ' \
            'LIMIT 4;'

    cursor.execute(query)
    audio_arr = cursor.fetchall()

    print(f'Top 3 Audio Configurations Used By Pros:')
    for i in range(1, 4):
        print(audio_arr[i])
    print('')


def kb_analytics():
    query = 'SELECT keyboard, COUNT (keyboard) as value_occurrence ' \
            'FROM analytics ' \
            'GROUP BY keyboard ' \
            'ORDER BY value_occurrence DESC ' \
            'LIMIT 4;'

    cursor.execute(query)
    kb_arr = cursor.fetchall()

    print(f'Top 3 Keyboards Used By Pros:')
    for i in range(1, 4):
        print(kb_arr[i])


if __name__ == '__main__':
    print('''\nCSGO Pro Player Peripheral Analytical Tool\n''')
    edpi_analytics()
    monitor_analytics()
    audio_analytics()
    mouse_analytics()
    kb_analytics()
