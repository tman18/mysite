print('What a Wonderful World')
def main():
    for page in pages:
        template = open("templates/base.html").read()
        index_content = open(page['filename']).read()
        title_for_page = template.replace("{{title}}", page['title'])
        finished_index_page = title_for_page.replace("{{content}}", index_content)
        open(page['output'], "w+").write(finished_index_page)       

def page_links():
    content = open('docs/about-me.html').read()
    content_with_link = content.replace('href="about-me.html', 'style= "color:yellow !important" href="about-me.html')
    open('docs/about-me.html', 'w+').write(content_with_link)

    content = open('docs/resume.html').read()
    content_with_link = content.replace('href="resume.html', 'style= "color:yellow !important" href="resume.html')
    open('docs/resume.html', 'w+').write(content_with_link)   

    content = open('docs/contact.html').read()
    content_with_link = content.replace('href="contact.html', 'style= "color:yellow !important" href="contact.html')
    open('docs/contact.html', 'w+').write(content_with_link)

        
            
pages = [
{
"filename": "content/index.html",
"output": "docs/Index.html",
"title": "Tim Myers",
},

{
"filename": "content/about-me.html",
"output": "docs/about-me.html",
"title": "About Me",
},

{
"filename": "content/resume.html",
"output": "docs/resume.html",
"title": "Resume",
},

{
"filename": "content/contact.html",
"output": "docs/contact.html",
"title": "Contact",
}
]


main()
page_links()