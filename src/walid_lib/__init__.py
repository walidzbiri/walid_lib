import requests

def main() -> None:
    response=requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()