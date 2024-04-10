styles = """
<style>
    .social-container {
        display: flex;
        justify-content: center; /* Center horizontally */
        align-items: center; /* Center vertically */
        height: 100%; /* Make sure the container takes full height */
    }
    .social-link {
        margin-right: 50px; /* Adjust the horizontal distance between logos */
    }
    .social-logo {
        width: 50px; /* Adjust the initial width as needed */
        height: 50px; /* Adjust the initial height as needed */
        transition: transform 0.2s ease-in-out;
    }
    .social-logo:hover {
        transform: scale(1.1); /* Scale up by 10% on hover */
    }
    .social-logo:last-child {
        margin-right: 0; /* Remove right margin for the last logo */
    }
</style>
"""

get_ipython().run_line_magic('store', 'styles')
