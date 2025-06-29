import random
import time
import pygame
import os

pygame.init()

# Add this near the top of your file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR ="assets"

try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Error initializing mixer: {e}")
    exit()

COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Email Verification Game")

font = pygame.font.Font(None, 28)

try:
    correct_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'correct.wav'))
    incorrect_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'incorrect.wav'))
    print("Sound effects loaded successfully.")
except pygame.error as e:
    print(f"Error loading sound files: {e}")
    correct_sound = incorrect_sound = None
try:
    pygame.mixer.music.load(os.path.join(ASSETS_DIR, 'background_music.mp3'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    print("Background music started successfully.")
except pygame.error as e:
    print(f"Error loading background music: {e}")


def animate_text(text, x, y):
    """Animate text with slower animation speed."""
    screen.fill(COLOR_BLACK)
    y_offset = y
    for line in text.split("\n"):
        for char in line:
            rendered_char = font.render(char, True, COLOR_YELLOW)
            screen.blit(rendered_char, (x, y_offset))
            pygame.display.flip()
            pygame.time.delay(50)
            x += font.size(char)[0]
        x = 50
        y_offset += 30


def add_line_breaks(text, line_length=100):
    """Break the email text into lines of a given length."""
    return '\n'.join([text[i:i + line_length] for i in range(0, len(text), line_length)])


def generate_random_email():
    """Generate random email content (real or phishing)."""

    phishing_subjects = [
        "Immediate Action Required: Account Deactivation in 24 Hours",
        "Your account has been compromised! Urgent: Verify your details",
        "Suspicious Activity Detected on Your Account",
        "Security Alert: Unusual Login Attempt Detected",
        "Urgent: Verify your identity or your account will be locked"
    ]

    phishing_senders = [
        "support@securebanking.com",
        "admin@online-transaction.com",
        "admin@banking-secure.com",
        "verification@fraudulentbank.com",
        "info@banking-services.com"
    ]

    legitimate_subjects = [
        "Important Account Verification Update",
        "Transaction Alert: Suspicious Activity Detected",
        "Account Security Update",
        "Important: Action Required to Secure Your Account",
        "Verify Your Identity to Avoid Account Suspension"
    ]

    legitimate_senders = [
        "support@mybank.com",
        "noreply@securepayment.com",
        "services@trustedbank.com",
        "alerts@banking-secure.com",
        "no-reply@bankingservice.com"
    ]

    is_phishing = random.choice([True, False])

    if is_phishing:
        sender = random.choice(phishing_senders)
        subject = random.choice(phishing_subjects)
        email_content = (
            f"From: {sender}\n"
            f"Subject: {subject}\n\n"
            "Dear Valued Customer,\n"
            "We have detected suspicious activity on your account. In order to protect your funds, "
            "we urgently request that you verify your identity and take action immediately.\n\n"
            "Failure to verify your account within the next 24 hours will result in the temporary suspension "
            "of your account. Please click the link below to verify your details:\n"
            "https://secure-banking.com/verify-now\n\n"
            "This is a critical request. Please take immediate action.\n\n"
            "Thank you,\n"
            "The Fraud Prevention Team\n"
        )
    else:
        sender = random.choice(legitimate_senders)
        subject = random.choice(legitimate_subjects)
        email_content = (
            f"From: {sender}\n"
            f"Subject: {subject}\n\n"
            "Dear Customer,\n"
            "We are performing a routine security check on your account as part of our ongoing efforts to "
            "ensure the safety and security of our customers. We have noticed some unusual login attempts and "
            "need you to verify your identity.\n"
            "To proceed with the verification process, please follow the link below:\n"
            "https://secure-mybank.com/verify-identity\n\n"
            "This is a time-sensitive action and should be completed at your earliest convenience.\n\n"
            "Thank you for being a valued customer,\n"
            "Best regards,\n"
            "The Security Compliance Team\n"
        )

    email_content = add_line_breaks(email_content, line_length=100)
    return email_content


def is_email_legitimate(email):
    """Check if an email is legitimate (based on the domain)."""
    return "securebanking.com" not in email


def main():
    running = True
    correct_guesses = 0
    screen.fill(COLOR_BLACK)
    welcome_text = font.render("Welcome to the Email Verification Game!", True, COLOR_GREEN)
    instructions_text = font.render("Press 'R' for real or 'F' for fake.", True, COLOR_YELLOW)
    screen.blit(welcome_text, (50, 50))
    screen.blit(instructions_text, (50, 100))
    pygame.display.flip()
    time.sleep(3)

    for i in range(3):
        email = generate_random_email()
        animate_text(email, 50, 100)

        response = None
        while response not in ["real", "fake"]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.unicode == 'r':
                        response = 'real'
                    elif event.unicode == 'f':
                        response = 'fake'

        is_legit = is_email_legitimate(email)
        if (is_legit and response == "real") or (not is_legit and response == "fake"):
            correct_guesses += 1
            if correct_sound:
                correct_sound.play()
            result_text = "Correct! This email is " + ("legitimate." if is_legit else "a phishing attempt.")
        else:
            if incorrect_sound:
                incorrect_sound.play()
            result_text = "Incorrect. This email is " + ("legitimate." if is_legit else "a phishing attempt.")

        screen.fill(COLOR_BLACK)
        result_rendered = font.render(result_text, True, COLOR_GREEN if "Correct" in result_text else COLOR_RED)
        screen.blit(result_rendered, (50, 250))
        pygame.display.flip()
        time.sleep(2)

    screen.fill(COLOR_BLACK)
    if correct_guesses == 3:
        final_text = "Congratulations! You won a prize!"
    else:
        final_text = f"You guessed correctly {correct_guesses} out of 3. Better luck next time!"

    final_rendered = font.render(final_text, True, COLOR_YELLOW if correct_guesses < 3 else COLOR_GREEN)
    screen.blit(final_rendered, (50, 250))
    pygame.display.flip()
    time.sleep(3)

    pygame.quit()


if __name__ == "__main__":
    main()
