import urllib.request
import os.path

from game_item_class import game_item

GAME_URL = 'https://www.warofdragons.com/'
GAME_URL_ATRIFACT = 'https://www.warofdragons.com/artifact_info.php?artikul_id='

# 3514, 3518, 3500

def find_and_cut(file, what_to_find='', how_much=300, offset=0):
    where = file.find(what_to_find)
    return file[where+offset:where+how_much+offset]

def get_game_item_object(link=''):
    try:
        url = urllib.request.urlopen(link)
    except:
        print('Te, działa Ci internet ziomek?')

    item_data = str(url.read())

    item_id = find_and_cut(link, 'id=', 4, 3)

    item_description = find_and_cut(item_data, 'tbl-sts_bg-light')
    item_description = find_and_cut(item_description, 'color', 500)

    item_color = find_and_cut(item_description, '', 6, 7)

    find_length_of_item_name = item_description.find('<') 
    item_name = find_and_cut(item_description, '', find_length_of_item_name-15, 15)

    item_image_url = find_and_cut(item_data, 'images/data/')
    find_length_of_item_image = item_image_url.find('"')
    item_image_url = find_and_cut(item_image_url, '', find_length_of_item_image)

    item_image_name = str.lower(str.replace(item_name, ' ', '_')) + '.gif'

    get_item_image_file_by_name(item_image_url, item_image_name)

    return game_item(item_id, item_name, item_color, item_image_name, item_image_url)


def get_item_image_file_by_name(item_image_url, image_name):
    image_path = './images/items/' + image_name
    if (not(os.path.isfile(image_path))):
        try:
            urllib.request.urlretrieve(GAME_URL + item_image_url, image_path)
        except:
            print('Nie udało się pobrać obrazka: ', image_name)

def get_item_image_file_by_id(item_id, image_name):
    image_path = './images/items/' + image_name
    if (not(os.path.isfile(image_path))):
        try:
            urllib.request.urlretrieve(GAME_URL_ATRIFACT + item_id, image_path)
        except:
            print('Nie udało się pobrać obrazka: ', image_name)
