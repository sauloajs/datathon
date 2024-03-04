def getPageContent():
    with open('./src/html/educational_context/index.html', 'r') as file:
        content = file.read().replace('\n', '')
        
    return content