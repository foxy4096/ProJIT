import random
import requests

def url_gen(length=8):
    data = 'abcdefghijklmnopqrstuvwxyz1234567890'
    build = []
    for i in range(length):
        # Get a random character from data variable
        append = data[random.randrange(0, len(data))]
        # If the position is less than 26, it is not a number
        if data.find(append) < 26:
            # 50% chance to capitalize the letter
            if random.randrange(0, 2) == 1:
                append = append.upper()
        # append the letter to our build list
        build.append(append)

    # turn the build list into a string
    build = ''.join(build)
    # return the string we built
    return build


def check_video_url(video_id):
    checker_url = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="
    video_url = checker_url + video_id

    request = requests.get(video_url)

    return request.status_code == 200


while True:
    url_id = url_gen()
    url = f"https://www.youtube.com/watch?v={url_id}"
    check = check_video_url(url_id)
    if check == True:
        print(url)
        break
    # print("https://i.imgur.com/" + url_gen() + ".jpg")
