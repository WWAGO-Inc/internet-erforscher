document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event triggered");
    
    const body = document.body;
    const storedTheme = getCookie('theme');
    console.log("Stored Theme:", storedTheme);

    if (storedTheme) {
        body.classList.add(storedTheme);
    }

    function setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie = name + '=' + value + ';expires=' + expires.toUTCString();
        console.log("Cookie set:", name, value, "Expires:", expires.toUTCString());
    }

    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                return cookie.substring(name.length + 1);
            }
        }
        return null;
    }

    const modeToggleBtn = document.createElement('button');
    modeToggleBtn.textContent = "Toggle Dark Mode";
    modeToggleBtn.onclick = function() {
        body.classList.toggle("dark-mode");
        if (body.classList.contains("dark-mode")) {
            setCookie('theme', 'dark-mode', 365); // Store the dark mode theme in cookies
        } else {
            setCookie('theme', '', -1); // Remove the theme cookie
        }
        console.log("Body classList:", body.classList);
    };
    document.querySelector('header').appendChild(modeToggleBtn);
});
