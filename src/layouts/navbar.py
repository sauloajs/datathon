def getNavBarHtml():
    with open('./src/html/nav.html', 'r') as file:
        nav = file.read().replace('\n', '')
    
    return nav