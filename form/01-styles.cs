/* 01-styles.css */

body {
    font-family: 'Roboto', sans-serif; /* Added font-family */
    line-height: 1.6; /* Added line-height */
}

.container {
    width: 80%; /* Changed width from 100% to 80% */
    margin: 0 auto; /* Added margin */
}

.btn-primary {
    display: inline-block; /* Added display property */
    padding: 0.8rem 1.5rem; /* Added padding */
    background-color: var(--color-primary); /* Added background-color property */
    color: var(--color-white); /* Added color property */
    text-decoration: none; /* Added text-decoration property */
    border: none; /* Added border property */
    border-radius: 4px; /* Added border-radius property */
    transition: background-color 0.3s ease; /* Added transition */
}

.btn-primary:hover {
    background-color: var(--color-primary-dark); /* Added background-color property */
}

.header {
    background-color: var(--color-primary); /* Added background-color property */
    color: var(--color-white); /* Added color property */
    text-align: center; /* Added text-align property */
    padding: 1rem 0; /* Added padding */
    margin-bottom: 2rem; /* Added margin-bottom */
}
