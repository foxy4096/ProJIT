import random
import requests

def url_gen(length=11):
    data = 'abcdefghijklmnopqrstuvwxyz1234567890-_'
    build = []
    for _ in range(length):
        # Get a random character from data variable
        append = data[random.randrange(0, len(data))]
        # If the position is less than 26, it is not a number
        if data.find(append) < 26 and random.randrange(0, 2) == 1:
            append = append.upper()
        # append the letter to our build list
        build.append(append)

    return ''.join(build)


def check_video_url(video_id):
    checker_url = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="
    video_url = checker_url + video_id

    return requests.get(video_url)


while True:
    url_id = url_gen()
    url = f"https://www.youtube.com/watch?v={url_id}"
    print(url)
    req = check_video_url(url_id)
    if req.ok:
        print(url)
        break
    else:
        print("Nope:", req.status_code)
    # print("https://i.imgur.com/" + url_gen() + ".jpg")
