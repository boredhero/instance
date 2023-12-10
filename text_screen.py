import pygame

def get_puzzle_1_intro_text():
    """
    Get the text for puzzle 1 intro
    """
    return """
    This puzzle is about the experience of trying to get out of bed and do basic daily tasks while struggling with depression.
    It can be hard to do this for people with depression, as it is hard to gather the motivation to start the day, and it is easy to
    stay there, skip classes, and not do anything, which can make the depression worse.

    To complete this puzzle, you need to turn all of the circles green by using WASD to move the player around. But be careful, the circles
    have a timer, and you will need to return to re-activate them if you are not fast enough. I chose this puzzle mechanic because I believe
    it is a good simulator of how hard it can be to reach the critical mass of motivation to get out of bed and do things.
    """

def get_puzzle_2_intro_text():
    """
    Get the text for puzzle 2 intro
    """
    return """
    This puzzle is about how difficult it can be to navigate basic life tasks while struggling with social anxiety. Even a simple task such
    as calling the doctor to make an appointment can be a daunting task for someone with social anxiety. It can be hard to remember what to
    say, and the resulting perceived embarrassment can be a huge deterrent to making the call. I often forget what I want to say when I make
    calls, and I have to write down a script to read from. Intrusive negative thoughts can result in a thought loop, causing you to freeze up
    and become unable to talk.

    To be able to complete this puzzle, you'll be shown a question that you need to answer. You'll be presented choices, but they will move
    around the screen, and you will need to try to click the right one to answer the question correctly. There will be one right answer,
    and a lot of incorrect ones, or intrusive thoughts that make it harder to track the right thought and answer the question. I chose this
    puzzle mechanic because I believe it simulates the difficulty of sifting through intrusive looping thoughts to get a word out.
    """

class TextScreen:

    def __init__(self, screen, text, button_text="OK"):
        """
        Class to display a screen with text and a button
        Useful for puzzle intros and outros
        """
        self.screen = screen
        self.text = text
        self.button_text = button_text
        self.font = pygame.font.Font(None, 36)
        self.button_font = pygame.font.Font(None, 30)
        self.button_rect = pygame.Rect(0, 0, 100, 50)
        self.button_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 100)

    def draw(self):
        """
        Draw the page
        """
        # Draw the text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surface, text_rect)
        # Draw the button
        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect)  # White button
        button_text_surface = self.button_font.render(self.button_text, True, (0, 0, 0))  # Black text
        button_text_rect = button_text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text_surface, button_text_rect)

    def handle_event(self, event):
        """
        Handle the MOUSEBUTTONDOWN event on the button to click
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return True  # Indicates the button was pressed
        return False
