command = widget_inputs["text1"].strip().lower()

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if command == "":
    commentizer("Remember, turn on 'Paint' in the DevTools Timeline to see what paint commands the browser runs to generate the page.")
    is_correct = is_correct and False
elif "save" not in command:
    commentizer("If you've turned on the Paint Profiler, you can find paint information in the details pane. What's the first command listed?")
    is_correct = is_correct and False
elif "save" in command:
    is_correct = True

if is_correct:
    commentizer("Nice! Now you've got a tool to measure and bust paint jank.")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)