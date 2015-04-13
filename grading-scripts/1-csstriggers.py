layout_paint_composite = [
    "align-content",
    "align-items",
    "align-self",
    "border-bottom-width",
    "border-collapse",
    "border-left-width",
    "border-right-width",
    "border-top-width",
    "bottom",
    "box-sizing",
    "clear",
    "cursor",
    "direction",
    "display",
    "flex-basis",
    "flex-direction",
    "flex-grow",
    "flex-shrink",
    "flex-wrap",
    "float",
    "font-family",
    "font-kerning",
    "font-size",
    "font-style",
    "font-variant",
    "font-variant-ligatures",
    "font-weight",
    "height",
    "justify-content",
    "left",
    "letter-spacing",
    "line-height",
    "list-style-image",
    "list-style-position",
    "list-style-type",
    "margin",
    "margin-bottom",
    "margin-left",
    "margin-right",
    "margin-top",
    "max-height",
    "max-width",
    "min-height",
    "min-width",
    "order",
    "orphans",
    "outline",
    "outline-color",
    "outline-style",
    "outline-width",
    "overflow-wrap",
    "overflow-x",
    "overflow-y",
    "padding",
    "padding-bottom",
    "padding-left",
    "padding-right",
    "padding-top",
    "pointer-events",
    "position",
    "right",
    "table-layout",
    "text-align",
    "text-decoration",
    "text-indent",
    "text-rendering",
    "text-transform",
    "top",
    "unicode-bidi",
    "vertical-align",
    "visibility",
    "white-space",
    "widows",
    "width",
    "word-break",
    "word-spacing",
    "word-wrap"
]

paint_composite = [
    "backface-visibility",
    "background",
    "background-attachment",
    "background-blend-mode",
    "background-clip",
    "background-color",
    "background-image",
    "background-origin",
    "background-position",
    "background-repeat",
    "background-size",
    "border",
    "border-bottom-color",
    "border-bottom-left-radius",
    "border-bottom-right-radius",
    "border-bottom-style",
    "border-image-outset",
    "border-image-repeat",
    "border-image-slice",
    "border-image-source",
    "border-image-width",
    "border-left-color",
    "border-left-style",
    "border-right-color",
    "border-right-style",
    "border-top-color",
    "border-top-left-radius",
    "border-top-right-radius",
    "border-top-style",
    "box-shadow",
    "clip",
    "color",
    "opacity",
    "outline-offset",
    "text-shadow",
    "transform-origin",
    "z-index"
]

composite = [
    "perspective",
    "perspective-origin",
    "transform",
    "transform-style"
]


lpc = widget_inputs["text1"]
pc = widget_inputs["text2"]
c = widget_inputs["text3"]

is_correct = False

comments = []
def commentizer(new):
    if new not in comments:
        comments.append(new)

if lpc not in layout_paint_composite:
    commentizer("Check your entry for Layout, Paint, Composite. Your response was not in the list.")
    is_correct = is_correct and False
else:
    is_correct = True

if pc not in paint_composite:
    commentizer("Check your entry for Paint, Composite. Your response was not in the list.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if c not in composite:
    commentizer("Check your entry for Composite. Your response was not in the list.")
    is_correct = is_correct and False
else:
    is_correct = is_correct and True

if is_correct:
    commentizer("Nice! [csstriggers.com](http://csstriggers.com) is a super useful resource. (There's yet another plug for you, Paul. When should I expect my check?)")

grade_result["correct"] = is_correct
grade_result["comment"] = "\n\n".join(comments)