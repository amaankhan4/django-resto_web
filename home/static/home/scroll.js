function smoothScroll(target) {
    document.querySelector(`a[href="${target}"]`).addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(target).scrollIntoView({
            behavior: 'smooth'
        });
    });
}

smoothScroll('#book-a-table');
smoothScroll('#menu');
smoothScroll('#service');
smoothScroll('#about');
smoothScroll('#contact');