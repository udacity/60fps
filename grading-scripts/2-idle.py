news = widget_inputs["check1"]
images = widget_inputs["check2"]
videos = widget_inputs["check3"]
basics = widget_inputs["check4"]
article_comments = widget_inputs["check5"]

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if not news:
    commentizer("Why not load news stories that could be used in the future?")
    is_correct = is_correct and False
else:
    is_correct = True

if not images:
    commentizer("As images are usually large, it's not a bad idea to load them in an idle state.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not videos:
    commentizer("Videos hog bandwidth. If you think users will want to watch them, loading them in an idle state could be a good idea.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if basics:
    commentizer("Any critical functionality should have been loaded before even getting to the idle state.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not article_comments:
    commentizer("As comments aren't critical, the idle state is ideal for loading them.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if is_correct:
    commentizer("Right! This is a great time to load any assets you think your users might access later.")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)