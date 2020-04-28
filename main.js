var step_sequence = ['choose_which_root', 'smallest_root', 'largest_root', 'vx_leq_zero'];

function toggle_show_sidebar(elem_id) {
    // hide all the stuff in the sidebar, to make room for the new element to show
    var children = document.getElementById("sidebar").children;
    for (var i = 0; i < children.length; i++) {
        children[i].style.display = "none";
    }

    var x = document.getElementById(elem_id);
    x.style.display = "block";
    // if (x.style.display === "none") {
    // } else {
    //     x.style.display = "none";
    // }
}

function next_step(next_step_elem_id, option_elem_id) {
    var option_elem = document.getElementById(option_elem_id);
    // When we select an option, we want to hide all the other branches
    // (otherwise we would be showing text from two different branches, which
    // is confusing). To hide the other branches, we look up the current step,
    // find it's index in the list of all steps, and hide all the following
    // steps. Later on, we will display the correct branch of the next step.
    var current_step_id = option_elem.closest(".step").id;
    var idx = step_sequence.findIndex(x => x === current_step_id);
    for (var i = 0; i < step_sequence.length; i++) {
        if (i > idx) {
            document.getElementById(step_sequence[i]).style.display = "none";
        }
    }

    var x = document.getElementById(next_step_elem_id);
    x.style.display = "block";
    if (! option_elem.textContent.endsWith('✓')) {
        // TODO: this is kind of a hack; it destroys the formatting of the
        // element we're appending to, since it converts everything into a
        // string. The right way to do this would be to append a child element
        // into the li element.
        option_elem.textContent += " ✓";
    }
    var all_options = option_elem.parentElement.parentElement.children;
    for (var i = 0; i < all_options.length; i++) {
        if (all_options[i].firstElementChild.id != option_elem_id) {
            all_options[i].style.color = "#ccc";
        } else {
            all_options[i].style.color = "#000";
        }
    }
}
