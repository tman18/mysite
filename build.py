print('What a Wonderful World')
def main():
    for page in pages:
        template = open("templates/base.html").read()
        index_content = open(page['filename']).read()
        title_for_page = template.replace("{{title}}", page['title'])
        finished_index_page = title_for_page.replace("{{content}}", index_content)
        open(page['output'], "w+").write(finished_index_page)       

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