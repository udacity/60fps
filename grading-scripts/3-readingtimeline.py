function = widget_inputs["text1"].strip().lower()
yep = widget_inputs["radio1"]
nope = widget_inputs["radio2"]

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if function == "":
    commentizer("Remember, turn on 'Causes' in DevTools to see which functions call one another.")
    is_correct = is_correct and False
elif "render" not in function:
    commentizer("Remember, when a function calls another, DevTools shows the child underneath the caller.")
    is_correct = is_correct and False
elif "render" in function:
    is_correct = True

if yep and not nope:
    commentizer("Are the frames shorter than 16ms? If not, the app won't hit 60 FPS.")
    is_correct = is_correct and False
elif not yep and not nope:
    commentizer("What do you think about the framerate? Will it hit 60 FPS?")
    is_correct = is_correct and False
elif nope and not yep:
    is_correct = is_correct and True

if is_correct:
    commentizer("Awesome job! Getting accustomed to DevTools is the first step to better performance.")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)