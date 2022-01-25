from score import pair_score


class CreateSlideshowInjector:
    def __init__(self, slides):
        self.slides = slides
        self.slideshow = []
        self.algoscore = 0
        self.slideshow_scores = []

        # Tracking params
        self.injections = [0, 0]

    def inject_slide(self, next_slide):
        # Score every possible position we can inject this slide
        # Score front edge add
        frontscore = pair_score(self.slideshow[0], next_slide)

        # Score back edge add
        backscore = pair_score(self.slideshow[-1], next_slide)

        # Get best of both
        if backscore > frontscore:
            best_score = backscore
            inject_loc = "back"
        else:
            best_score = frontscore
            inject_loc = "front"

        # Score injection adds
        for i in range(len(self.slideshow) - 1):
            # Calc scores for adding the slide between two
            inject_left_score = pair_score(self.slideshow[i], next_slide)
            inject_right_score = pair_score(self.slideshow[i + 1], next_slide)

            # Net increase in score is both minus original slideshow score
            score_increase = inject_left_score + inject_right_score - self.slideshow_scores[
                i]

            if score_increase > best_score:
                best_score = score_increase
                inject_scores = (inject_left_score, inject_right_score
                                 )  # Save so we don't have to recalculate
                inject_loc = i

        # Increase score
        self.algoscore += best_score

        # Perform the injection
        if inject_loc == "back":
            self.slideshow.append(next_slide)
            self.slideshow_scores.append(best_score)
            self.injections[0] += 1
        elif inject_loc == "front":
            self.slideshow.insert(0, next_slide)
            self.slideshow_scores.insert(0, best_score)
            self.injections[0] += 1
        else:
            self.injections[1] += 1
            self.slideshow.insert(inject_loc, next_slide)
            self.slideshow_scores[inject_loc] = inject_scores[0]
            self.slideshow_scores.insert(inject_loc, inject_scores[1])

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
                best_score = score

        self.algoscore += best_score
        self.slideshow_scores += [best_score]
        self.slideshow.append(next_slide)
        self.slides.remove(next_slide)

        for next_slide in self.slides:
            self.inject_slide(next_slide)

        return self.slideshow, self.algoscore