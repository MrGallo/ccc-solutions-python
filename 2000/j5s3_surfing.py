def can_surf(here, there, link_map, visited=None):
    if here == there:
        return True

    if visited is None:
        visited = []
    visited.append(here)

    for link in link_map[here]:
        if link in visited:
            continue
        if can_surf(link, there, link_map, visited):
            return True
    return False


num_pages = int(input())
link_map = {}
current_site = None
i = 0
while i < num_pages:
    line = input()
    if line.startswith("<HTML>"):
        while line != "</HTML>":
            search_string = '<A HREF="'
            search_i = line.find(search_string)
            while search_i != -1:
                link_i = search_i + len(search_string)
                link_end_i = line.find("\"", link_i)
                link_url = line[link_i:link_end_i]
                link_map[current_site].append(link_url)
                print("Link from {} to {}".format(current_site, link_url))
                search_i = line.find(search_string, link_end_i)
            line = input()
        i += 1
    else:
        current_site = line
        link_map[current_site] = []


while True:
    line = input()
    if line == "The End":
        break
    here = line
    there = input()

    template_string = "{} surf from {} to {}."
    ability = "Can" if can_surf(here, there, link_map) else "Can't"
    print(template_string.format(ability, here, there))