
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
