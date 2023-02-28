document.addEventListener('DOMContentLoaded', () => {
    // Select the elements
    const scrollLeftBtn = document.querySelector('.scroll-left');
    const scrollRightBtn = document.querySelector('.scroll-right');
    const bookListWrapper = document.querySelector('.book-list-wrapper');
  
    // Define the scroll amount
    const scrollAmount = 300;
  
    // Add click event listeners to the buttons
    scrollLeftBtn.addEventListener('click', () => {
      bookListWrapper.scrollBy({
        left: -scrollAmount,
        behavior: 'smooth'
      });
    });
  
    scrollRightBtn.addEventListener('click', () => {
      bookListWrapper.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
      });
    });


    const relatedBooksContainer = document.getElementById('related-books-container');
    const relatedBooksBtns = document.querySelectorAll('.related-books-btn');
    
    relatedBooksBtns.forEach(btn => {
      btn.addEventListener('click', event => {
        const bookId = event.target.parentElement.getAttribute('data-book-id');
        // use bookId to fetch related books data from your database or API
        // and populate the related-books-container with that data
        if(relatedBooksContainer.style.display != 'block'){
        relatedBooksContainer.style.display = 'block';
        
        }
        else{
            relatedBooksContainer.style.display = 'none';
        }
      });
    });
    
    

});

  

