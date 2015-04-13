try:
    answer = float(widget_inputs["text1"])
except Exception as e:
    answer = None

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if answer == None:
    commentizer("Type a number into the box!")
elif answer > 17:
    commentizer("Not quite. Your answer is too high.")
elif answer < 16 and answer != None:
    commentizer("Not quite. Your answer is too low.")
elif answer >= 16 and answer <= 17:
    is_correct = True
    commentizer("Great job! (We usually round down to 16ms per frame).")

if not is_correct:
    commentizer("Hint: divide 1000ms by 60 frames.")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)