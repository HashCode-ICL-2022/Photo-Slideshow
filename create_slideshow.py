from score import pair_score

class CreateSlideshow:

    def __init__(self, slides):
        self.slides = slides
        self.slideshow = []
    
    def create(self):

        # Take initial random slide
        # Loop through all remaining slides and find best first pair
        slide = self.slides.pop()
        self.slideshow.append(slide)
        best_score = 0
        for other_slide in self.slides:
            score = pair_score(slide, other_slide)
            if score > best_score:
                next_slide = other_slide
        self.slideshow.append(other_slide)

        pass
