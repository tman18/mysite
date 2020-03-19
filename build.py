top = open("templates/top.html").read()
index = open("content/index.html").read()
bottom = open("templates/bottom.html").read()
full = top + index + bottom
open("docs/index.html", "w+").write(full)

top = open("templates/top.html").read()
index = open("content/about-me.html").read()
bottom = open("templates/bottom.html").read()
full = top + index + bottom
open("docs/about-me.html", "w+").write(full)

top = open("templates/top.html").read()
index = open("content/resume.html").read()
bottom = open("templates/bottom.html").read()
full = top + index + bottom
open("docs/resume.html", "w+").write(full)

top = open("templates/top.html").read()
index = open("content/contact.html").read()
bottom = open("templates/bottom.html").read()
full = top + index + bottom
open("docs/contact.html", "w+").write(full)

