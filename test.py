def main():
    import requests
    r = requests.get("google.com")
    print(r.content)
