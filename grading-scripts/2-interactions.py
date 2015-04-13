spinners = widget_inputs["check1"]
scrolling = widget_inputs["check2"]
drag_n_drop = widget_inputs["check3"]
pinching = widget_inputs["check4"]
pull_to_refresh = widget_inputs["check5"]
side_menu = widget_inputs["check6"]
opening_comments = widget_inputs["check7"]
forms = widget_inputs["check8"]
theme_changes = widget_inputs["check9"]

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if not spinners:
    commentizer("Check:")
    commentizer("* spinners")
    is_correct = is_correct and False
else:
    is_correct = True

if not scrolling:
    commentizer("Check:")
    commentizer("* scrolling")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not drag_n_drop:
    commentizer("Check:")
    commentizer("* drag-n-drop")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not pinching:
    commentizer("Check:")
    commentizer("* pinching")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not pull_to_refresh:
    commentizer("Check:")
    commentizer("* pull-to-refresh")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not side_menu:
    commentizer("Check:")
    commentizer("* side menu slide")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if not opening_comments:
    commentizer("Check:")
    commentizer("* opening comments")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if forms:
    commentizer("Check:")
    commentizer("* forms")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if theme_changes:
    commentizer("Check:")
    commentizer("* theme changes")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if is_correct:
    commentizer("Looks like pretty much anything that moves should run at 60 FPS... like this gif:")
    commentizer("![fat cat breathing](http://ak-hdl.buzzfed.com/static/enhanced/webdr03/2013/7/24/12/anigif_enhanced-buzz-2175-1374683221-56.gif)")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)