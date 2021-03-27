import WebPageOpener

print("Type in what you are searching for")
wantedItem = input()
wantedItem.replace(" ", "-")
url1 = "https://bazar.bg/obiavi?q="
url = url1 + wantedItem

if __name__ == "__main__":
    WebPageOpener.browsePage(url)
