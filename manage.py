import utils, sys

print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    print("Build was specified")
    utils.build_page()
elif command == "new":
    print("New page was specified")
    utils.new_page()
else:
    print('Rebuild site: python manage.py build')
    print('Create new page: python manage.py new')