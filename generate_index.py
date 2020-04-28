#!/usr/bin/env python3

from data import steps


print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <script src="./main.js"></script>
  <link href="./basic.css" rel="stylesheet" type="text/css" />
  <title>IVT</title>
</head>
<body>

<div id="main_window">
  <p>In this module, you will explore how the intermediate value theorem works. You can click below on <span class="clickable" onclick="toggle_show_sidebar('sidebar_tips')">wavy</span> text to display notes in the sidebar.</p>
  <p><strong>Theorem</strong> (Intermediate value theorem)<strong>.</strong>
  Let a, b be <span onclick="toggle_show_sidebar('why_real')" class="clickable">real numbers</span> such that <span class="clickable" onclick="toggle_show_sidebar('why_a_lt_b')">a &lt; b</span>.
    Let f: [a,b] → R be a continuous function such that f(a) &lt; 0 and f(b) &gt; 0.
    Then there exists c ∈ [a,b] such that f(c) = 0.
  <p>
  <p>How do we prove this theorem?
  There are several approaches, but here we will directly use the least upper bound property of the real numbers, which says that any <span class="clickable" onclick="toggle_show_sidebar('why_nonempty_and_bounded_set')">nonempty set of real numbers which is bounded above</span> has a <i>least</i> upper bound.</p>
""")

first = True
for step in steps:
    if first:
        print('<div class="step" id="%s">' % step['name'])
    else:
        print('<div class="step" id="%s" style="display: none;">' % step['name'])

    print(step['text'])
    if "options" in step:
        print("<ul>")
        for option in step['options']:
            print("<li>")
            print(option['text'])
            print('''<span class="clickable" id="%s" onclick="next_step('%s', this.id)">[pick]</span>''' % (option['name'] + "_option", option['name']))
            print("</li>")
        print("</ul>")

    print('</div>')  # closes class="step"
    first = False

print("</div>")  # closes id="main_window"

with open("sidebar.html", "r") as f:
    print(f.read())

print("""</body>
</html>
""")
