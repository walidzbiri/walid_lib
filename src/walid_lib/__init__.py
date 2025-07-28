import requests

def main() -> dict:
    response=requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()