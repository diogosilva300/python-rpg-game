from character import Character
from gameMenu import GameMenu
import keyboard

class GameSystem:
    monster_list = []
    main_character = None

    @staticmethod
    def clamp(minimum: int, x: int, maximum: int) -> int:
        return max(minimum, min(x, maximum))
    
    @staticmethod
    def keyboard_input():
        keyboard.add_hotkey('w', GameMenu.up)
        keyboard.add_hotkey('s', GameMenu.down)
        keyboard.add_hotkey('a', GameMenu.left)
        keyboard.add_hotkey('d', GameMenu.right)
        keyboard.add_hotkey('enter', GameMenu.done)
        keyboard.add_hotkey('space', GameMenu.done)
        keyboard.wait()

    @staticmethod
    def main():
        GameSystem.main_character = Character(Character.create_base_status())
        GameMenu.add_menu("status", GameSystem.main_character.getStatus())
        GameMenu.show_menu()
        GameSystem.keyboard_input()