def main():
    import requests
    r = requests.get("http://google.com")
    open("output.txt" , 'wb').write(r.content)

main()
