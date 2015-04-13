style = widget_inputs["check1"]
layout = widget_inputs["check2"]
paint = widget_inputs["check3"]
composite = widget_inputs["check4"]

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if style:
    commentizer("While flexbox is applied as a CSS style, the style itself doesn't change when you resize the page.")
    is_correct = is_correct and False
else:
    is_correct = True

if not layout:
    commentizer("If the geometry of the page changes (such as in a `resize` event), then layout needs to run.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not paint:
    commentizer("When the pixels on the screen need to change, the browser needs to decide where they go by running paint.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not composite:
    commentizer("When the pixels on the screen change, the compositor needs to constructor the final image.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if is_correct:
    commentizer("Nice job! Understanding the way your CSS affects the rendering pipeline is a big step towards great performance.")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)