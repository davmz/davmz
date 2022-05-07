document.addEventListener("DOMContentLoaded", load);

/**
 *
 */
 function load() {
    menuButton();
    stickyNavigation();
}

/**
 *
 */
 function menuButton() {
    const menuBtn = document.querySelector(".menu-btn");

    let menuOpen = false;
    menuBtn.addEventListener("click", () => {
        if(!menuOpen) {
            menuBtn.classList.add("open");
            document.body.style.overflowY = 'hidden';
            menuOpen = true;
        } else {
            menuBtn.classList.remove("open");
            document.body.style.overflowY = 'visible';
            menuOpen = false;
        }
    });
}

/**
 *
 */
function stickyNavigation() {
    window.addEventListener("scroll", () => {
        let header = document.querySelector("header");

        header.classList.toggle("scrollActive", window.scrollY > 0);
    });
}
