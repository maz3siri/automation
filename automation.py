try:
    from colorama import Fore
    import ctypes, pyautogui, keyboard, os, time
    from datetime import datetime
except ImportError:
    input("Error while importing modules. Type 'pip install -r requirements.txt'")

ascii_text = """
                ############################################################# 
                ###################################################   ####### 
                ###############################################   /~\\   #####
                ############################################   _- `~~~', ####
                ##########################################  _-~       )  ####
                #######################################  _-~          |  ####
                ####################################  _-~            ;  #####
                ##########################  __---___-~              |   #####
                #######################   _~   ,,                  ;  `,,  ##
                #####################  _-~    ;'                  |  ,'  ; ##
                ###################  _~      '                    `~'   ; ###
                ############   __---;                                 ,' ####
                ########   __~~  ___                                ,' ######
                #####  _-~~   -~~ _                               ,' ########
                ##### `-_         _                              ; ##########
                #######  ~~----~~~   ;                          ; ###########
                #########  /          ;                        ; ############
                #######  /             ;                      ; #############
                #####  /                `                    ; ##############
                ###  /                                      ; ###############
                #                                            ################
                         Custom Automation Script v2
                         - by Mazen 
                         - Github > @maz3siri 
"""


class AutomationScript:

    def __init__(self):
        self.action_count = 0
        self.stop_flag = False
        self.positions = []
        self.repeat_count = 1
        self.click_delay = 0.5

    def get_positions(self):
        self.positions = []
        self.print_console("Position collection started. Press 'F' to save each position. Press 'Q' to finish.")
        
        while True:
            if keyboard.is_pressed("F"):
                self.positions.append(pyautogui.position())
                self.print_console(f"Saved position at {self.positions[-1]}")
                time.sleep(0.5)

            if keyboard.is_pressed("Q"):
                self.print_console("Position collection finished.")
                break

    def perform_sequence(self):
        self.update_title()
        self.print_console(f"Starting automation... Sequence will repeat {self.repeat_count} time(s).")
        self.print_console(f"Delay between clicks: {self.click_delay} second(s)")
        self.print_console("Press 'ESC' to stop at any time.")
        
        for repeat in range(self.repeat_count):
            if self.stop_flag or keyboard.is_pressed("ESC"):
                self.print_console("Automation stopped by user.")
                break

            self.print_console(f"Starting repeat {repeat + 1}/{self.repeat_count}")
            for pos in self.positions:
                if self.stop_flag or keyboard.is_pressed("ESC"):
                    self.print_console("Automation stopped by user.")
                    return
                pyautogui.moveTo(pos)
                pyautogui.click()
                self.print_console(f"Clicked at {pos}")
                self.action_count += 1
                self.update_title()
                time.sleep(self.click_delay)

    def update_title(self):
        now = time.time()
        elapsed = str(int(now - self.started_time))
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"AutomationScript | Actions Performed: {self.action_count} | Elapsed: {elapsed}s | by : @maz3siri"
        )

    def print_console(self, arg):
        print(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] {arg}")

    def main(self):
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("Automation Script | by : Mazen Asiri")
        print(Fore.RED + ascii_text)
        
        self.get_positions()
        
        if not self.positions:
            self.print_console("No positions recorded. Exiting...")
            return
        
        while True:
            try:
                self.repeat_count = int(input("\nHow many times do you want to repeat the sequence? (1-100): "))
                if 1 <= self.repeat_count <= 100:
                    break
                else:
                    self.print_console("Please enter a valid number between 1 and 100.")
            except ValueError:
                self.print_console("Invalid input. Please enter a number.")
        
        while True:
            try:
                self.click_delay = float(input("\nHow many seconds between each click? (e.g., 0.5, 1, 2): "))
                if self.click_delay >= 0:
                    break
                else:
                    self.print_console("Please enter a positive number.")
            except ValueError:
                self.print_console("Invalid input. Please enter a valid number.")

        ready = input("\nAre you ready to start automation? (Y/N): ").strip().lower()
        if ready != 'y':
            self.print_console("Automation canceled by user.")
            return
        
        self.started_time = time.time()
        self.perform_sequence()
        
        self.print_console(f"Sequence completed after {self.action_count} actions.")


if __name__ == "__main__":
    obj = AutomationScript()
    obj.main()
