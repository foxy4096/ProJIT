import requests

from os import system, name


def clear_screen():
    """
    Clears the screen.
    """
    if name == "nt":
        system("cls")
    else:
        system("clear")


clear_screen()


def fetch_repos(username, page=1):
    """
    Fetches a list of repositories for a given user.

    Args:
        username (str): The username of the user to fetch repositories for.
        page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
        list[dict]: A list of dictionaries containing the repository data.
    """
    url = f"https://api.github.com/users/{username}/repos"
    params = {"page": page}
    return requests.get(url, params=params).json()


def main():
    username = input("Enter your GitHub username ~> ")
    page_num = 1

    while True:
        repos = fetch_repos(username, page_num)
        if not repos:
            break

        for repo in repos:
            print(f" ~ {repo['full_name']}: {repo['description']} \n")

        prompt = input("Next? [y/N] ~> ")
        if prompt.lower() != "y":
            break

        page_num += 1

    print("Goodbye!")


if __name__ == "__main__":
    main()
