document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab');
    const banner = document.getElementById('banner');

    tabs.forEach((tab) => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs
            tabs.forEach((t) => t.classList.remove('active'));

            // Add active class to the clicked tab
            tab.classList.add('active');

            // Change banner class and content based on the clicked tab
            const tabType = tab.getAttribute('data-tab');
            banner.className = `banner ${tabType}`;

            if (tabType === 'about') {
                banner.innerHTML = `<h1>About</h1><p>Custom Software Development Company</p>`;
            } else if (tabType === 'products') {
                banner.innerHTML = `<h1>Products</h1><p>Our latest product offerings.</p>`;
            } else if (tabType === 'technology') {
                banner.innerHTML = `<h1>Technology</h1><p>Innovative technology solutions.</p>`;
            } else if (tabType === 'downloads') {
                banner.innerHTML = `<h1>Downloads</h1><p>Download our software and resources.</p>`;
            }
        });
    });
});
