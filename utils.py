print('What a Wonderful World')      

# def page_links():
#     for page in pages:
#         content = open(page['output']).read()
#         content_with_link = content.replace(page['url'], 'style="color:yellow !important"'+ " " + page['url'])
#         open(page['output'], 'w+').write(content_with_link)

        
            
# pages = [
# {
# "filename": "content/index.html",
# "output": "docs/Index.html",
# "title": "Tim Myers",
# "url": "I don't want this page to be changed",
# },

# {
# "filename": "content/about-me.html",
# "output": "docs/about-me.html",
# "title": "About Me",
# "url": 'href="about-me.html',
# },

# {
# "filename": "content/resume.html",
# "output": "docs/resume.html",
# "title": "Resume",
# "url": 'href="resume.html',
# },

# {
# "filename": "content/contact.html",
# "output": "docs/contact.html",
# "title": "Contact",
# "url": 'href="contact.html'
# }
# ]

# def main():
#     for page in pages:
#         index_content = open(page['contents']).read()
#         template = open("templates/base.html").read()
#         title_for_page = template.replace("{{title}}", page['title'])
#         finished_index_page = title_for_page.replace("{{content}}", index_content)
#         open(page['output'], "w+").write(finished_index_page) 

import glob, os, jinja2
from jinja2 import Template
all_html_files = glob.glob("content/*.html")

pages = []
def html_part():
    for html_file in all_html_files:
        file_path = html_file.replace("content/", "docs/")
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        # content_html = open(html_file).read()
        pages.append({
        "title": name_only,
        "output": file_path,
        "contents": html_file,
        "filename": file_name,
        })

def pages_part():
    for page in pages:    
        base = open("templates/base.html").read()
        content_html = open(page['contents']).read()
        template = Template(base)
        finished_file= template.render(
            title=page['title'],
            content=content_html,
            pages=pages,   
        )   
        open(page['output'], "w+").write(finished_file)

def new_page():
    new_cont = '''
        <h1>New Content!</h1>
        <p>New content...</p>
    '''
    open('content/new_content_page.html', 'w+').write(new_cont)

def build_page():
    html_part()
    pages_part()