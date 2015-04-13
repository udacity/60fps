function = widget_inputs["text1"].strip().lower()

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if function == "":
    commentizer("Remember, turn on 'Causes' in DevTools to see which functions call one another.")
    is_correct = is_correct and False
elif "toteslayingoutyo" not in function:
    commentizer("What function is creating layout with a 'Forced Synchronous Layout' warning?")
    is_correct = is_correct and False
elif "toteslayingoutyo" in function:
    is_correct = True

if is_correct:
    commentizer("Nice job honing your DevTools detective skills ![detective](https://openclipart.org/image/300px/svg_to_png/26996/DooFi-Consulting-detective-with-pipe-and-magnifying-glass-silhouette-.png)")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)