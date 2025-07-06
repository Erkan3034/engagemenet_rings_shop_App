// Main JavaScript for Engagement Rings Application

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading animation to buttons
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('btn-loading')) {
                this.classList.add('btn-loading');
                const originalText = this.innerHTML;
                this.innerHTML = '<span class="loading me-2"></span>Yükleniyor...';

                // Reset after 2 seconds (for demo purposes)
                setTimeout(() => {
                    this.classList.remove('btn-loading');
                    this.innerHTML = originalText;
                }, 2000);
            }
        });
    });

    // Product image lazy loading
    const productImages = document.querySelectorAll('.product-image');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    });

    productImages.forEach(img => {
        if (img.dataset.src) {
            imageObserver.observe(img);
        }
    });

    // Search functionality
    const searchInput = document.getElementById('search');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                // Auto-submit form after 500ms delay
                const form = this.closest('form');
                if (form) {
                    form.submit();
                }
            }, 500);
        });
    }

    // Filter form auto-submit
    const filterForm = document.getElementById('filterForm');
    if (filterForm) {
        const filterInputs = filterForm.querySelectorAll('input, select');
        filterInputs.forEach(input => {
            input.addEventListener('change', function() {
                // Don't auto-submit search input
                if (this.name !== 'search') {
                    filterForm.submit();
                }
            });
        });
    }

    // Color selection functionality
    document.querySelectorAll('.color-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            document.querySelectorAll('.color-btn').forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
        });
    });

    // Add to favorites functionality
    document.querySelectorAll('.btn-favorite').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            this.classList.toggle('active');
            const icon = this.querySelector('i');
            if (this.classList.contains('active')) {
                icon.classList.remove('far');
                icon.classList.add('fas');
                showToast('Ürün favorilere eklendi!', 'success');
            } else {
                icon.classList.remove('fas');
                icon.classList.add('far');
                showToast('Ürün favorilerden çıkarıldı!', 'info');
            }
        });
    });

    // Add to cart functionality
    document.querySelectorAll('.btn-add-cart').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            showToast('Ürün sepete eklendi!', 'success');

            // Update cart count (if cart counter exists)
            const cartCounter = document.querySelector('.cart-counter');
            if (cartCounter) {
                const currentCount = parseInt(cartCounter.textContent) || 0;
                cartCounter.textContent = currentCount + 1;
                cartCounter.classList.add('pulse');
                setTimeout(() => cartCounter.classList.remove('pulse'), 1000);
            }
        });
    });

    // Back to top button
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopBtn.className = 'btn btn-primary btn-sm position-fixed';
    backToTopBtn.style.cssText = 'bottom: 20px; right: 20px; z-index: 1000; border-radius: 50%; width: 50px; height: 50px; display: none;';
    backToTopBtn.id = 'backToTop';
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });

    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Toast notification system
    window.showToast = function(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type} border-0 position-fixed`;
        toast.style.cssText = 'top: 20px; right: 20px; z-index: 1050;';
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');

        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `;

        document.body.appendChild(toast);

        const bsToast = new bootstrap.Toast(toast, {
            autohide: true,
            delay: 3000
        });

        bsToast.show();

        toast.addEventListener('hidden.bs.toast', function() {
            document.body.removeChild(toast);
        });
    };

    // Product comparison functionality
    let compareList = [];

    window.addToCompare = function(productId, productName) {
        if (compareList.length >= 3) {
            showToast('En fazla 3 ürün karşılaştırabilirsiniz!', 'warning');
            return;
        }

        if (!compareList.includes(productId)) {
            compareList.push(productId);
            showToast(`${productName} karşılaştırma listesine eklendi!`, 'success');
            updateCompareBadge();
        } else {
            showToast('Bu ürün zaten karşılaştırma listesinde!', 'info');
        }
    };

    function updateCompareBadge() {
        let badge = document.querySelector('.compare-badge');
        if (!badge) {
            badge = document.createElement('span');
            badge.className = 'compare-badge badge bg-warning position-fixed';
            badge.style.cssText = 'top: 20px; left: 20px; z-index: 1050;';
            document.body.appendChild(badge);
        }
        badge.textContent = compareList.length;
        badge.style.display = compareList.length > 0 ? 'block' : 'none';
    }

    // Initialize compare badge
    updateCompareBadge();

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + K for search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const searchInput = document.getElementById('search');
            if (searchInput) {
                searchInput.focus();
            }
        }

        // Escape to close modals
        if (e.key === 'Escape') {
            const modals = document.querySelectorAll('.modal.show');
            modals.forEach(modal => {
                const modalInstance = bootstrap.Modal.getInstance(modal);
                if (modalInstance) {
                    modalInstance.hide();
                }
            });
        }
    });

    // Performance optimization: Debounce scroll events
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(function() {
            // Handle scroll-based animations or lazy loading here
        }, 100);
    });

    // --- Product List Slider & Color Logic ---
    const sliderTrack = document.getElementById('sliderTrack');
    const leftBtn = document.getElementById('sliderLeft');
    const rightBtn = document.getElementById('sliderRight');
    const cards = sliderTrack ? sliderTrack.querySelectorAll('.product-card') : [];
    let currentIndex = 0;
    let cardsPerView = 4;

    function updateCardsPerView() {
        if (window.innerWidth < 700) cardsPerView = 1;
        else if (window.innerWidth < 900) cardsPerView = 2;
        else if (window.innerWidth < 1200) cardsPerView = 3;
        else cardsPerView = 4;
    }
    updateCardsPerView();
    window.addEventListener('resize', () => {
        updateCardsPerView();
        moveSlider(currentIndex);
    });

    function moveSlider(index) {
        if (!sliderTrack) return;
        const maxIndex = Math.max(0, cards.length - cardsPerView);
        currentIndex = Math.max(0, Math.min(index, maxIndex));
        const cardWidth = cards[0] ? cards[0].offsetWidth + 24 : 0; // 24px margin
        sliderTrack.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
        leftBtn.disabled = currentIndex === 0;
        rightBtn.disabled = currentIndex === maxIndex;
    }

    if (leftBtn && rightBtn) {
        leftBtn.addEventListener('click', () => moveSlider(currentIndex - 1));
        rightBtn.addEventListener('click', () => moveSlider(currentIndex + 1));
    }
    moveSlider(0);

    // Color dot logic
    cards.forEach(card => {
        const colorDots = card.querySelectorAll('.color-dot');
        const img = card.querySelector('.product-image');
        const colorLabel = card.querySelector('.color-label');
        const productId = card.getAttribute('data-product-id');
        const productImages = window.productImages ? window.productImages[productId] : null;
        colorDots.forEach(dot => {
            dot.addEventListener('click', function() {
                colorDots.forEach(d => d.classList.remove('active'));
                this.classList.add('active');
                const color = this.getAttribute('data-color');
                // Change image src
                if (img && productImages && productImages[color]) {
                    img.src = productImages[color];
                } else if (img) {
                    img.src = img.src.replace(/(yellow|white|rose)/, color);
                }
                // Change label
                if (colorLabel) {
                    if (color === 'yellow') colorLabel.textContent = 'Yellow Gold';
                    else if (color === 'white') colorLabel.textContent = 'White Gold';
                    else if (color === 'rose') colorLabel.textContent = 'Rose Gold';
                }
            });
        });
    });

    // Pass product images to JS for color switching
    if (!window.productImages) {
        window.productImages = {};
        cards.forEach(card => {
            const productId = card.getAttribute('data-product-id');
            const img = card.querySelector('.product-image');
            window.productImages[productId] = {};
            ['yellow', 'white', 'rose'].forEach(color => {
                const src = img.src.replace(/(yellow|white|rose)/, color);
                window.productImages[productId][color] = src;
            });
        });
    }
    // --- End Product List Slider & Color Logic ---

    console.log('Engagement Rings Application initialized successfully!');
});