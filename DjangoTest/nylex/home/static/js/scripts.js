// add class navbarDark on navbar scroll
const header = document.querySelector('.navbar');

window.onscroll = function() {
    if(window.scrollY >= 100) {
        // header.classList.remove('bg-light');
        header.classList.add('bg-light');
    }
    else {
        header.classList.remove('bg-light');
        // header.classList.add('bg-light');
    }
}