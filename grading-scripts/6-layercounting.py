try:
    layers = int(widget_inputs["text1"])
except Exception as e:
    try: 
        layers = float(widget_inputs["text1"])
    except Exception as e:
        layers = None
will_change = widget_inputs["radio1"]
overlap = widget_inputs["radio2"]
trans = widget_inputs["radio3"]
accelerated = widget_inputs["radio4"]
animates = widget_inputs["radio5"]

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if layers == None:
    commentizer("How many layers do you think there are? Type a number into the box.")
    is_correct = is_correct and False
elif layers > 2:
    commentizer("There aren't that many layers!")
    is_correct = is_correct and False
elif layers == 1:
    commentizer("Almost! There might be another layer.")
    is_correct = is_correct and False
elif layers < 1:
    commentizer("There is at least 1 layer on the page.")
    is_correct = is_correct and False
elif layers == 2:
    is_correct = True

if not will_change and not overlap and not trans and not accelerated and not animates:
    commentizer("Why do you think `#totes-promoted` was promoted?")
    is_correct = is_correct and False
elif will_change:
    commentizer("Nope. It doesn't have will-change. Take another look at the Compositing Reasons.")
    is_correct = is_correct and False
elif trans:
    commentizer("Nope. It doesn't have a 3d transform. Take another look at the Compositing Reasons.")
    is_correct = is_correct and False
elif accelerated:
    commentizer("Nope. It isn't a hardware accelerated canvas. Take another look at the Compositing Reasons.")
    is_correct = is_correct and False
elif animates:
    commentizer("Nope. It doesn't accelerate a transform. Take another look at the Compositing Reasons.")
    is_correct = is_correct and False
elif overlap:
    is_correct = is_correct and True

if is_correct:
    commentizer("Right-o! You're getting to know some advanced DevTools.")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)