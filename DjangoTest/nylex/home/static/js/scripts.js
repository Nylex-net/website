// add class navbarDark on navbar scroll
const header = document.querySelector('.navbar');
const reveals = document.querySelectorAll(".reveal");
// const sideScroll = document.querySelector('.list');
// // Set a flag to control scrolling
// let scrollingPaused = false;

window.onscroll = () => {
    scrolled();
};

function scrolled() {
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

    // const scrollTop = sideScroll.getBoundingClientRect().top;
    // const scrollVisible = 0;
    // if(scrollTop < window.innerHeight - scrollVisible) {
    //     scrollingPaused = true;
    //     if(scrollingPaused) {
    //         return;
    //     }
    //     console.log(window.scrollY);
    //     sideScroll.style.transform = 'translate3d(-'+ (((window.scrollY - 920) / 920)*100) +'%, 0px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)';
    // }
}

window.addEventListener('DOMContentLoaded', scrolled());