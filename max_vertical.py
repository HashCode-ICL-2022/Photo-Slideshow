from slide import Slide


def max_vertical(photo_set):
    # photo.id = int
    # photo.tags = set()
    max_tags = 0
    slides = set()
    for photo1 in photo_set:
        slide = Slide()
        for photo2 in photo_set:
            if photo1 == photo2:
                continue
            total_tags = photo1.tags.intersection(photo2.tags)
            if len(total_tags) > max_tags:
                max_tags = total_tags
                slide.ids = [photo1.id, photo2.id]
        slides.add(slide)
        photo_set.remove(photo1)
        photo_set.remove(photo2)
    return slides
