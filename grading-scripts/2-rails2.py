images_above = widget_inputs["check1"]
flipping = widget_inputs["check2"]
async = widget_inputs["check3"]
images_below = widget_inputs["check4"]

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if images_above:
    commentizer("Check the images above-the-fold. They should have already been downloaded and visible.")
    is_correct = is_correct and False
else:
    is_correct = True

if not flipping:
    commentizer("While the app has some downtime, why not start precomputing FLIP animations?")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not async:
    commentizer("You could try starting below-the-fold requests now so that they'll be ready by the time users reach them.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not images_below:
    commentizer("Like any below-the-fold content, images are great to request after the initial page load.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if is_correct:
    commentizer("Great job! You're thinking [#perfmatters](https://twitter.com/hashtag/perfmatters)!")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)