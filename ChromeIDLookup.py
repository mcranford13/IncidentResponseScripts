import webbrowser

def open_urls_in_browser(chrome_ids: str):
    # Base URL template
    base_url = "https://chrome.google.com/webstore/detail/{}/{}"
    
    # Split the chrome_ids into a list and strip whitespace
    chrome_id_list = [id_.strip() for id_ in chrome_ids.split("\n") if id_.strip()]
    
    # Use default browser to open the URLs
    for chrome_id in chrome_id_list:
        url = base_url.format("text", chrome_id)
        webbrowser.open(url)

if __name__ == "__main__":
    # Block of text containing chromeIDs
    chrome_ids = """
    cbjngbfjehiofmihfpodinolkcokdojp
    cfpenpohaapdgnkglcbgjiooipcbcebi
    efaidnbmnnnibpcajpcglclefindmkaj
    fnbdnhhicmebfgdgglcdacdapkcihcoh
    ghbmnnjooekpmoecnnnilnnbdlolhkhi
    hfapbcheiepjppjbnkphkmegjlipojba
    hmdcmlfkchdmnmnmheododdhjedfccka
    nmmhkkegccagdldgiimedpiccmgmieda
    pnjaodmkngahhkoihejjehlcdlnohgmp
    """
    
    open_urls_in_browser(chrome_ids)

