def getIndexHtml():
    with open('./src/html/index.html', 'r') as file:
        content = file.read().replace('\n', '')
        
    return content