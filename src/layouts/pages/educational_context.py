def getMainSectionContent():
    with open('./src/html/educational_context/main_section.html', 'r') as file:
        content = file.read().replace('\n', '')
        
    return content

def getCommentsSectionContent():
    with open('./src/html/educational_context/comments_section.html', 'r') as file:
        content = file.read().replace('\n', '')
        
    return content