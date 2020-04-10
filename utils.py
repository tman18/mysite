print('What a Wonderful World')      

import glob, os, jinja2
from jinja2 import Template
all_html_files = glob.glob("content/*.html")

pages = []
def html_part():
    for html_file in all_html_files:
        file_path = html_file.replace("content/", "docs/")
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
        "title": name_only.replace('-', ' ').replace('index', 'Tim Myers'),
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