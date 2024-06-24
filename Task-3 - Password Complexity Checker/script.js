document.getElementById('passwordInput').addEventListener('input', function() {
    const password = this.value;
    const feedback = document.getElementById('feedback');
    const strength = checkPasswordStrength(password);
    feedback.innerHTML = `Strength: <span class="strength ${strength.class}">${strength.text}</span>`;
});

function checkPasswordStrength(password) {
    let strength = {
        text: 'Weak',
        class: 'weak'
    };

    const regexes = {
        length: /.{8,}/,
        uppercase: /[A-Z]/,
        lowercase: /[a-z]/,
        number: /\d/,
        special: /[!@#$%^&*(),.?":{}|<>]/
    };

    let passedTests = 0;

    for (const key in regexes) {
        if (regexes[key].test(password)) {
            passedTests++;
        }
    }

    if (passedTests >= 4) {
        strength = {
            text: 'Strong',
            class: 'strong'
        };
    } else if (passedTests >= 2) {
        strength = {
            text: 'Medium',
            class: 'medium'
        };
    }

    return strength;
}
