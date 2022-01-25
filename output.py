def output(slideshow, file_name):
    lines = [str(len(slideshow))]
    for slide in slideshow:
        id1 = slide.ids.pop()
        if slide.ids:
            id2 = slide.ids.pop()
            lines.append(str(id1) + " " + str(id2) + "\n")
        else:
            lines.append(str(id1) + "\n")

    f = open(file_name, "w")
    f.writelines(lines)
    f.close()
