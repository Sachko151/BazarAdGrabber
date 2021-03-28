import WebPageOpener
import AdReader
if __name__ == "__main__":
    print("Which site? Bazar or OLX")
    wantedSite = input()
    if wantedSite == "Bazar":
        print("Type in what you are searching for")
        wantedItem = input()
        wantedItem.replace(" ", "-")
        url1 = "https://bazar.bg/obiavi?q="
        url = url1 + wantedItem
        WebPageOpener.browsePageBazar(url)
    elif wantedSite == "OLX":
        print("Type in what you are searching for")
        wantedItem = input()
        wantedItem.replace(" ", "-")
        url1 = "https://www.olx.bg/ads/q-"
        url = url1 + wantedItem + "/"
        WebPageOpener.browsePageOlx(url)
    else:
        print("Error")

