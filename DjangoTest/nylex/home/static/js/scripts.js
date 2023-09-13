// add class navbarDark on navbar scroll
const header = document.querySelector('.navbar');
const reveals = document.querySelectorAll(".reveal");

window.onscroll = () => {
    // Navbar controls
    if(window.scrollY >= 1) {
        header.classList.remove('transparentNav');
        header.classList.add('bg-light');
    }
    else {
        header.classList.remove('bg-light');
        header.classList.add('transparentNav');
        // header.classList.add('bg-light');
    }

    // Text reveal controls
    for (var i = 0; i < reveals.length; i++) {
        const windowHeight = window.innerHeight;
        const elementTop = reveals[i].getBoundingClientRect().top;
        const elementVisible = 100;
    
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add("active");
        } else {
            reveals[i].classList.remove("active");
        }
    }
};