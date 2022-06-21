def main():
    import requests
    r = requests.get("google.com")
    open("output.txt" , 'wb').write(r.content)

main()
