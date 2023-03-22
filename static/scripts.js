const navMenu = document.getElementById("navMenu");

function toggleMenu(){
    navMenu.classList.toggle("show");
}

document.addEventListener("mouseup", function(event) {
    if (!navMenu.contains(event.target)) {
        navMenu.classList.remove("show");
    }
});