import json


def load_posts(path="posts.json"):
    posts = []
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)

    return posts


def search_posts(substr):
    found_posts = []
    posts = load_posts()
    for post in posts:
        if substr in post["content"]:
            found_posts.append(post)

    return found_posts


def save_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]

    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        return None

    picture.save(f"./uploads/images/{filename}")

    return f"uploads/images/{filename}"


def save_post_to_json(posts, path="posts.json"):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(posts, file)


def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_post_to_json(posts)