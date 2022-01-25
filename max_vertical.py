from structures.slide import Slide


def max_vertical(photo_set):
    # photo.id = int
    # photo.tags = set()
    max_tags = 0
    slides = set()
    photos_seen = set()
    for photo1 in photo_set:
        for photo2 in photo_set:
            if photo1 == photo2:
                continue
            total_tags = photo1.tags.intersection(photo2.tags)
            if len(total_tags) > max_tags:
                max_tags = len(total_tags)
                slide = Slide({photo1, photo2})
        slides.add(slide)
        photo_set.remove(photo1)
        photo_set.remove(photo2)
    return slides
