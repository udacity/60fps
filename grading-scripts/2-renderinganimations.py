dom = widget_inputs["check1"]
cssom = widget_inputs["check2"]
render_tree = widget_inputs["check3"]
layout = widget_inputs["check4"]
composite = widget_inputs["check5"]
paint = widget_inputs["check6"]

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if dom:
    commentizer("The page isn't receiving any new HTML, so the DOM doesn't need to be built.")
    is_correct = is_correct and False
else:
    is_correct = True

if cssom:
    commentizer("The page isn't receiving any new CSS, so the CSSOM doesn't need to be built.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if render_tree:
    commentizer("The page isn't receiving any new HTML or CSS, so the Render Tree doesn't need to be touched.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if layout:
    commentizer("If an `opacity` or `transform` changes affects element on its own layer, layout won't need to be run.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if paint:
    commentizer("If an `opacity` or `transform` changes affects element on its own layer, paint won't need to be run.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not composite:
    commentizer("Remember, `opacity` or `transform` will trigger composite.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if is_correct:
    commentizer("Great job! Notice how `opacity` and `transform` only trigger composite? Keep that in mind as you build your performant apps.")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)