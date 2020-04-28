#!/usr/bin/env python3


steps = [
    {
        "name": "choose_which_root",
        "text": "Let's try to directly find a root of the function f. The displayed function has multiple such roots, so we'll have to pick one of them to find. Which one do you want to find?",
        "options": [
            {"name": "smallest_root", "text": "Find the smallest (leftmost) root"},
            {"name": "second_smallest_root", "text": "Find the second smallest root"},
            {"name": "penultimate_root", "text": "Find the penultimate (second from the right) root"},
            {"name": "largest_root", "text": "Find the largest (rightmost) root"},
        ]
    },
    {
        "name": "smallest_root",
        "text": "Good choice! What expression finds the smallest root?",
        "options": [
            {"name": "sup_fx_lt_zero", "text": "sup{x ∈ [a,b] :  f(x) &lt; 0}"},
            {"name": "vx_leq_zero", "text": "define V<sub>x</sub> to be V<sub>x</sub> = f([a,x]) = {f(x) : x ∈ [a,x]}. Then the root in question is sup{x ∈ [a,b] : sup V<sub>x</sub> ≤ 0}"},
            {"name": "vx_lt_zero", "text": "define V<sub>x</sub> to be V<sub>x</sub> = f([a,x]) = {f(x) : x ∈ [a,x]}. Then the root in question is sup{x ∈ [a,b] : sup V<sub>x</sub> &lt; 0}"},
        ],
    },
    {
        "name": "second_smallest_root",
        "text": "",
        "options": []
    },
    {
        "name": "penultimate_root",
        "text": "",
        "options": []
    },
    {
        "name": "largest_root",
        "text": "",
        "options": []
    },
    {
        "name": "sup_fx_lt_zero",
        "text": "",
        "options": []
    },
    {
        "name": "vx_leq_zero",
        "text": "That will work. So let c := sup{x ∈ [a,b] : sup Vx ≤ 0}. Now we have to show that this is actually a real number, i.e. that the least upper bound actually exists. To do this, we have to show that the set {x ∈ [a,b] : sup Vx ≤ 0} is nonempty and bounded above.<br><br>First let's show the set is nonempty.",
        "options": [
            {"name": "contains_a", "text": "The set is nonempty since it contains a"},
            {"name": "contains_b", "text": "The set is nonempty since it contains b"},
        ]
    },
    {
        "name": "vx_lt_zero",
        "text": "I think this will work too, but I haven't written this branch yet.",
        "options": []
    },
    {
        "name": "contains_a",
        "text": "That's right. V_a = {f(a)}. Since f(a) &lt; 0, sup V_a &lt; 0, so a is in the set.<br><br>Next, let's show that {x ∈ [a,b] : sup Vx ≤ 0} has an upper bound.",
        "options": [
            {"name": "a_is_ub", "text": "a is an upper bound of the set."},
            {"name": "b_is_ub", "text": "b is an upper bound of the set."},
            {"name": "one_is_ub", "text": "1 is an upper bound of the set."},
            {"name": "infty_is_ub", "text": "+∞ is an upper bound of the set."},
        ]
    },
    {
        "name": "contains_b",
        "text": "V_b = f([a,b]) so f(b) ∈ V_b. So sup V_b ≥ f(b) &gt; 0. This means that b cannot be in the set!",
    },
    {
        "name": "b_is_ub",
        "text": "That's right. Since {x ∈ [a,b] : sup Vx ≤ 0} is a subset of [a,b], this means that b is an upper bound.",
        "options": []
    },
]


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

    print('</div>')
    first = False


print("""</div>

</body>
</html>
""")
