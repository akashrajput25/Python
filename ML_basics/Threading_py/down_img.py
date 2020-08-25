import requests
import time
import concurrent.futures


img_urls = [
    'https://images.unsplash.com/photo-1593642702749-b7d2a804fbcf' ,
    'https://images.unsplash.com/photo-1596550428712-af2f48174951' ,
    'https://images.unsplash.com/photo-1596553346783-8c66f631279b'
]

t1 = time.perf_counter()

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name , 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image , img_urls)

t2 = time.perf_counter()

print(f'finished in {t2-t1} seconds')