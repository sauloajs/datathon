def getNavBarHtml(linkActive:str = '{index-active}'):
    with open('./src/html/nav.html', 'r') as file:
        nav = file.read().replace('\n', '')
    
    nav = nav.replace(linkActive, 'link--active')
    
    return nav