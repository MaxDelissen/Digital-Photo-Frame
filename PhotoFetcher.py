import random
from google_apis import create_service

def get_service():
    return create_service('credentials.json', 'photoslibrary', 'v1', [
        'https://www.googleapis.com/auth/photoslibrary',
        'https://www.googleapis.com/auth/photoslibrary.sharing'
    ])

def fetch_album(service, album_title):
    albums = service.albums().list(pageSize=50).execute().get('albums', [])
    return next((album for album in albums if album['title'] == album_title), None)

def fetch_media_items(service, album_id):
    media_items, next_page_token = [], None
    while True:
        body = {'albumId': album_id, 'pageSize': 100, 'pageToken': next_page_token}
        response = service.mediaItems().search(body=body).execute()
        media_items.extend(item for item in response.get('mediaItems', []) if not item['mimeType'].startswith('video/'))
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
    return media_items

def get_random_images_from_album(album_title, max_recent_items, num_items_to_select, screen_width, screen_height, cropImages):
    service = get_service()
    album = fetch_album(service, album_title)
    if not album:
        print('Album not found.')
        return []

    media_items = fetch_media_items(service, album['id'])
    if not media_items:
        print('No media items found in the album.')
        return []

    recent_media_items = sorted(media_items, key=lambda item: item['mediaMetadata']['creationTime'], reverse=True)[:max_recent_items]
    chosen_media_items = random.sample(recent_media_items, num_items_to_select)
    suffix = f"=w{screen_width}-h{screen_height}-c" if cropImages else f"=w{screen_width}-h{screen_height}"
    return [f"{item['baseUrl']}{suffix}" for item in chosen_media_items]

def get_marked_images_from_album(album_title, screen_width, screen_height, cropImages):
    service = get_service()
    album = fetch_album(service, album_title)
    if not album:
        print('Album not found.')
        return []

    media_items = fetch_media_items(service, album['id'])
    if not media_items:
        print('No media items found in the album.')
        return []

    marked_media_items = [item for item in media_items if '!altijd!' in item.get('description', '')]
    if not marked_media_items:
        print('No marked media items found in the album.')
        return []

    suffix = f"=w{screen_width}-h{screen_height}-c" if cropImages else f"=w{screen_width}-h{screen_height}"
    return [f"{item['baseUrl']}{suffix}" for item in marked_media_items]