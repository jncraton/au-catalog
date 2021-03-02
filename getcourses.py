import re

with open('catalog.md') as f:
    catalog = f.read()

    # Find all courses for a department
    # (([A-Z]{4}) Courses
    courses = re.findall(r"^(([A-Z]{4}) Courses)|((\d\d\d\d)\s+([\s\w]+?)\s+(\d+)[^\=\-]*?OFFERED:[^\n]+?)$", catalog, flags=re.M|re.DOTALL)
    #courses = re.findall(r"^(([A-Z]{4}) Courses)$", catalog, flags=re.M|re.DOTALL)

    department = ''

    for course in courses:
        if course[1]:
            department = course[1]
        else:
            print(department, course[3], course[4], course[5])
