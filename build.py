print('What a Wonderful World')
def main():
    for page in pages:
        template = open("templates/base.html").read()
        index_content = open(page['filename']).read()
        title_for_page = template.replace("{{title}}", page['title'])
        finished_index_page = title_for_page.replace("{{content}}", index_content)
        open(page['output'], "w+").write(finished_index_page)       

def page_links():
    for page in pages:
        content = open(page['output']).read()
        content_with_link = content.replace(page['url'], 'style="color:yellow !important"'+ " " + page['url'])
        open(page['output'], 'w+').write(content_with_link)

        
            
pages = [
{
"filename": "content/index.html",
"output": "docs/Index.html",
"title": "Tim Myers",
"url": "I don't want this page to be changed",
},

{
"filename": "content/about-me.html",
"output": "docs/about-me.html",
"title": "About Me",
"url": 'href="about-me.html',
},

{
"filename": "content/resume.html",
"output": "docs/resume.html",
"title": "Resume",
"url": 'href="resume.html',
},

{
"filename": "content/contact.html",
"output": "docs/contact.html",
"title": "Contact",
"url": 'href="contact.html'
}
]


main()
page_links()