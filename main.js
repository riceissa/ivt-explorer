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
    var x = document.getElementById(next_step_elem_id);
    x.style.display = "block";
    var y = document.getElementById(option_elem_id);
    if (! y.textContent.endsWith('✓')) {
        y.textContent += " ✓";
    }
    var all_options = y.parentElement.parentElement.children;
    console.log(all_options);
    for (var i = 0; i < all_options.length; i++) {
        if (all_options[i].firstChild.id != option_elem_id) {
            all_options[i].style.color = "#ccc";
        }
    }
}
