try:
    world = int(widget_inputs["text1"])
except Exception as e:
    try: 
        world = float(widget_inputs["text1"])
    except Exception as e:
        world = None

try:
    slide_menu = int(widget_inputs["text2"])
except Exception as e:
    try: 
        slide_menu = float(widget_inputs["text2"])
    except Exception as e:
        slide_menu = None

try:
    nav_bar = int(widget_inputs["text3"])
except Exception as e:
    try: 
        nav_bar = float(widget_inputs["text3"])
    except Exception as e:
        nav_bar = None

try:
    article_header = int(widget_inputs["text4"])
except Exception as e:
    try: 
        article_header = float(widget_inputs["text4"])
    except Exception as e:
        article_header = None

try:
    video = int(widget_inputs["text5"])
except Exception as e:
    try: 
        video = float(widget_inputs["text5"])
    except Exception as e:
        video = None

try:
    article = int(widget_inputs["text6"])
except Exception as e:
    try: 
        article = float(widget_inputs["text6"])
    except Exception as e:
        article = None

elements = {"world": world, "slide_menu": slide_menu, "nav_bar": nav_bar, "article_header": article_header, "video": video, "article": article}


comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

def check_all_elems_have_numbers():
    for i, elem in elements.iteritems():
        if elem == None:
            commentizer("There is at least one element that is either missing a number or contains an invalid string.")
            return False

def check_specific_elems():
    is_correct = False

    for elem, val in elements.iteritems():
        if elem != "world" and elem != "slide_menu" and val == world:
            commentizer("Looks like you've got an incorrect element on the same layer as:")
            commentizer("* the 'World' `div`")
            is_correct = is_correct and False
        elif world == slide_menu:
            is_correct = True
    for elem, val in elements.iteritems():
        if elem != "world" and elem != "slide_menu" and val == slide_menu:
            commentizer("Looks like you've got an incorrect element on the same layer as:")
            commentizer("* the slide out menu")
            is_correct = is_correct and False
        elif world == slide_menu:
            is_correct = is_correct and True

    for elem, val in elements.iteritems():
        if elem != "nav_bar" and val == nav_bar:
            commentizer("Looks like you've got an incorrect element on the same layer as:")
            commentizer("* the nav bar")
            is_correct = is_correct and False
    else:
        is_correct = is_correct and True

    for elem, val in elements.iteritems():
        if elem != "article_header" and elem != "video" and elem != "article" and val == article_header:
            commentizer("Looks like you've got an incorrect element on the same layer as:")
            commentizer("* the article header")
            is_correct = is_correct and False
        elif article_header == video == article:
            is_correct = is_correct and True
    for elem, val in elements.iteritems():
        if elem != "article_header" and elem != "video" and elem != "article" and val == video:
            commentizer("Looks like you've got an incorrect element on the same layer as:")
            commentizer("* the video")
            is_correct = is_correct and False
        elif article_header == video == article:
            is_correct = is_correct and True
    for elem, val in elements.iteritems():
        if elem != "article_header" and elem != "video" and elem != "article" and val == article:
            commentizer("Looks like you've got an incorrect element on the same layer as:")
            commentizer("* the full article")
            is_correct = is_correct and False
        elif article_header == video == article:
            is_correct = is_correct and True

    if world != slide_menu:
        commentizer("Will the 'World' `div` and the whole slide-in menu move together?")
        is_correct = is_correct and False
    if article_header != video or video != article or article_header != article:
        commentizer("Will all the elements in the articles move together?")
        is_correct = is_correct and False

    if is_correct:
        commentizer("Awesome job! You've got all the elements that move together layered together.")

    grade_result["correct"] = is_correct
    grade_result["comment"] = "\n\n".join(comments)

if check_all_elems_have_numbers() != False:
    check_specific_elems()
else:
    grade_result["correct"] = False
    grade_result["comment"] = "\n\n".join(comments)