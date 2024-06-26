from save import SaveDataManager

class AbstractLoreObject:

    def __init__(self, name: str | None, lore_text: str | None, location: tuple[int, int] | None, starts_puzzle: str | None, lore_ordinal: int):
        """
        Template for Lore Objects
        """
        self._name = name # Name of the object
        self._lore_text = lore_text # Lore text
        self._location = location # coords
        self._starts_puzzle = starts_puzzle # String with puzzle name if it does, else None
        self._lore_ordinal = lore_ordinal # Ordering of the lore objects. 0 is the first, 1 is the second, etc. They will not appear until the player has found the previous one.

    def get_name(self) -> str:
        """Returns the name"""
        return self._name

    def get_lore_text(self) -> str:
        """Returns the lore text"""
        return self._lore_text

    def get_location(self) -> tuple[int, int]:
        """Returns the location"""
        return self._location

    def get_starts_puzzle(self) -> str | None:
        """Returns the puzzle name, if applicable"""
        return self._starts_puzzle

    def get_lore_ordinal(self) -> int:
        """Returns the lore ordinal"""
        return self._lore_ordinal

class Prescription_1(AbstractLoreObject):

    def __init__(self):
        """
        Prescription 1
        """
        self.__save_data_manager = SaveDataManager()
        name = "Prescription"
        lore_text = f"""
        CBS PHARMACY
        123 MAIN ST, ANYTOWN USA 12345
        1-800-555-5555

        Patient: {self.__save_data_manager.get_player_name()}
        ESCITALOPRAM 10MG TABLET
        TAKE ONE TABLET BY MOUTH DAILY

        Rx No. 1234567
        Qty. 30
        Dr. Best, MD - 1 Refills
        """
        location = (1400, 1700) # Bathroom Sink
        starts_puzzle = None
        lore_ordinal = 1
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_1(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 1
        """
        name = "Journal"
        lore_text = """
        12/31/2021

        I can't believe it's been a year since I started taking my medication. I feel like a completely different person. I'm not sure if it's the medication or the therapy, but I feel like I'm finally starting to get my life back on track. I still have bad days, but they're not as frequent or as intense as they used to be. I'm hopeful that things will continue to improve in the new year.
        """
        location = (800, 2800) # BR Right Dresser
        starts_puzzle = None
        lore_ordinal = 2
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_2(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 2
        """
        name = "Journal"
        lore_text = """
        05/14/2022
        
        Today, I met someone who I think I could really like. I'm not sure if they like me back, but I'm hopeful. I'm trying to be more open to new people and experiences.
        That said, I have trouble beliving sometimes that anyone would be interested in me. I'm trying to be more positive, but it's hard.  
        """
        location = (1300, 800) # Living Room Coffee Table
        starts_puzzle = None
        lore_ordinal = 3
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_3(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 3
        """
        name = "Journal"
        lore_text = """
        02/14/2022
        
        I hate this stupid holiday. It always reminds me of how alone I am. I know I have friends and family who care about me, but it's not the same as having a romantic partner. I'm tired of feeling like I'm missing out on something that everyone else seems to have. I'm tired of feeling like I'm not good enough. I'm tired of feeling like I'm broken. If only I felt like I could actually talk to more people, then maybe I wouldn't be so alone.
        """
        location = (1000, 100) # Kitchen Counter
        starts_puzzle = None
        lore_ordinal = 4
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_4(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 4
        """
        name = "Journal"
        lore_text = """
        03/01/2022

        I have barely left bed for the past few days. I can't seem to find the energy or motivation to do anything. I know I should be taking my medication, but I can't bring myself to do it. I feel like it's not even worth it. I feel like I'm not worth it. I feel like I'm never going to get better. I feel like I'm never going to be happy. I feel like I'm never going to be okay. I've been missing class for weeks and I can't find the motivation to get leave my room, which is rapidly becoming a mess...

        PUZZLE:     This puzzle is about the experience of trying to get out of bed and do basic daily tasks while struggling with depression.
        It can be hard to do this for people with depression, as it is hard to gather the motivation to start the day, and it is easy to
        stay there, skip classes, and not do anything, which can make the depression worse.

        To complete this puzzle, you need to turn all of the circles green by using WASD to move the player around. But be careful, the circles
        have a timer, and you will need to return to re-activate them if you are not fast enough. I chose this puzzle mechanic because I believe
        it is a good simulator of how hard it can be to reach the critical mass of motivation to get out of bed and do things.
        """
        location = (1200, 3300) # BR Bed
        starts_puzzle = "puzzle_1"
        lore_ordinal = 5
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Puzzle_1_Shim(AbstractLoreObject):

    def __init__(self):
        """
        Puzzle 1 Shim
        """
        name = "Puzzle Complete"
        lore_text = """
        You have completed the puzzle. You have successfully gotten out of bed and completed the task of getting out of bed and doing basic daily tasks while struggling with depression.
        """
        location = (1260, 3360)
        starts_puzzle = None
        lore_ordinal = 6
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class HospitalWristBand(AbstractLoreObject):

    def __init__(self):
        """
        Hospital Wrist Band
        """
        self.__save_data_manager = SaveDataManager()
        name = "Wrist Band (??Hospital??)"
        lore_text = f"""
        Name: {self.__save_data_manager.get_player_name()}
        DOB: 01/01/1990
        MRN: 123456789
        """
        location = (1500, 1500) # Bathroom shower
        starts_puzzle = None
        lore_ordinal = 7
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Prescription_2(AbstractLoreObject):

    def __init__(self):
        """
        Prescription 2
        """
        self.__save_data_manager = SaveDataManager()
        name = "Prescription"
        lore_text = f"""
        CBS PHARMACY
        123 MAIN ST, ANYTOWN USA 12345
        1-800-555-5555

        Patient: {self.__save_data_manager.get_player_name()}
        ALPRAZOLAM (Xanax) 0.5MG TABLET
        TAKE ONE TABLET AS NEEDED FOR ANXIETY

        Rx No. 7654322
        Qty. 90
        Dr. Best, MD - 1 Refills
        """
        location = (1500, 2000) # Roommate
        starts_puzzle = None
        lore_ordinal = 8
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_5(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 5
        """
        name = "Journal"
        lore_text = """
        03/30/2022

        I ended up in the hospital yesterday. It's my least favorite place, but my chest has been hurting. I thought it was just my anxiety, but it turns out
        that I have developed moderate GERD and my esophagus is the problem. I feel like this is making me more anxious. How am I supposed to stay calm when
        I have a chronic disease that can mimic heart and lung symptoms? I'm scared that I'm going to die. I don't want to die alone.
        """
        location = (200, 3000) # Plant Room
        starts_puzzle = None
        lore_ordinal = 9
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_6(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 6
        """
        name = "Journal"
        lore_text = """
        04/15/2022

        All I can think about is dying. It's almost funny. Sometimes I want to die, and then other times I have a panic attack because I know I'll die
        someday and I feel like I'm wasting my time, getting older and not doing anything. I've been gaining weight, and my phsyical health issues are
        getting worse. I'm only 22, but I feel like I'm 50. I'm so tired of this. I'm so tired of being tired.
        """
        location = (500, 500) # Kitchen dining table
        starts_puzzle = None
        lore_ordinal = 10
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_7(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 7
        """
        name = "Journal"
        lore_text = """
        05/01/2022

        My medical marijuana card came today. It helps me manage the pain and the anxiety. I'm not sure if it's the best thing for me, and I'm worried
        about what my mom will think if she finds out, but it helps me relax and isn't nearly as addictive as Xanax.
        """
        location = (500, 3700) # Balcony
        starts_puzzle = None
        lore_ordinal = 11
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_8(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 8
        """
        name = "Journal"
        lore_text = """
        01/15/2022

        I had a really bad panic attack today. I was trying to call my doctor's office to schedule an appointment to get my prescription refilled, but once I dialed the number and the receptionist picked up, I couldn't speak. I felt like I was suffocating, and my heart was racing. I ended up having to ask my roommate to make the call for me. I hate feeling so helpless and out of control. I wish I didn't have to rely on medication to function.
        I thought I was doing better, but I guess I still have a long way to go. I'm trying to remind myself that recovery isn't linear, but it's hard not to feel discouraged. I'm going to try to be kind to myself and remember that it's okay to have bad days.

        PUZZLE:

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
        location = (800, 3800) # Balcony Left Chair
        starts_puzzle = None
        lore_ordinal = 12
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Puzzle_2_Shim(AbstractLoreObject):

    def __init__(self):
        """
        Puzzle 2 Shim
        """
        name = "Puzzle Complete"
        lore_text = """
        You have completed the puzzle. You have successfully managed to get through a panic attack and get the help you needed.
        """
        location = (860, 3860)
        starts_puzzle = None
        lore_ordinal = 13
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_9(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 9
        """
        name = "Journal"
        lore_text = """
        09/12/2022

        I'm so happy. I somehow ended up in a situationship with the person I met in May. I'm not sure what we are, but I'm happy. But there's a catch.
        She's moving away to a foreign country in a few months. I'm not sure what to do. We're using 'I love you', and I really mean it. I'm scared of being alone again.
        """
        location = (500, 3200) # BR Desk
        starts_puzzle = None
        lore_ordinal = 14
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_10(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 10
        """
        name = "Journal"
        lore_text = """
        12/21/2022

        Whelp. She left. I'm happy that she's happy, and pursuing her dreams, but I'm so empty. I don't really know how to deal with this. I feel like I'm
        a hormonal teenager again. Even more than that, I'm dreading the holidays ahead. I'm going to be at my mom's house, because I feel bad leaving her
        alone for the holidays, but she's also a trigger for my anxiety. She was always screaming at me as a kid, and she still does the same now. As she's
        gone further down the extreme christian rabbit hole, and I've become more atheistic, we see eye to eye on increasingly less. She's the reason I have
        to stay here in this town, because she's not well and I'm the only one who can take care of her. It's not like she has any friends, and my dad is dead.
        """
        location = location = (1000, 2000) # Hallway (Midpoint roughly)
        starts_puzzle = None
        lore_ordinal = 15
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Journal_Entry_11(AbstractLoreObject):

    def __init__(self):
        """
        Journal Entry 11
        """
        name = "Journal"
        lore_text = """
        01/01/2023

        That was awful. I'm so glad the holidays are over. I hate larping as a happy family with her. I hate trying to dodge her questions about my
        faith (lack thereof) and my personal life and why I "turned out this way because she didn't raise me this way". Our conversations are like
        minefields, and I'm always on edge. I feel like I'm navigating a maze just to get through a conversation with her.

        I understand that her marriage with my father was falling to pieces and she took it out on me despite 
        trying to do the best that I was cared for as a child, but she still hasn't changed.
        She still treats me like a child, and worse, now she goes on and on about how the end of the world is coming and wants to know if I'm "born again".
        I hate her, but she's still my mother, and she still took care of me, and still needs me in her old age. Deep down, I think I wish that she
        would just die so that I can be free; but I also know that I would be devastated if she did. I hate myself for feeling this way.
        I'm not sure how much longer I can take this. I'm not sure how much longer I can take her. I'm not sure how much longer I can take myself.

        PUZZLE:

        This puzzle is meant to simulate the experience of having a stressful conversation where you have to navigate a minefield of triggers and
        intrusive thoughts. You will be presented with a maze, and you will need to navigate it to get to the end goal (the green square).
        """
        location = (1350, 2800) # BR Sound System
        starts_puzzle = "puzzle_3"
        lore_ordinal = 16
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)

class Puzzle_3_Shim(AbstractLoreObject):

    def __init__(self):
        """
        Puzzle 3 Shim
        """
        name = "Puzzle Complete"
        lore_text = """
        You have completed the puzzle. You have successfully navigated the stressful conversation with your mother.
        """
        location = (1410, 2860)
        starts_puzzle = None
        lore_ordinal = 17
        super().__init__(name, lore_text, location, starts_puzzle, lore_ordinal)
