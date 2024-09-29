class Loggable:
    """the Loggable class is incorporated as an independent
    class used for handling logging functionality, and the Game class is
    enhanced to use it via composition. """
    def __init__(self):
        self.__logs = []

    @property
    def logs(self):
        return self.__logs

    def log(self, message):
        if isinstance(message, str):
            self.__logs.append(message)

    def save_logs_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write('\n'.join(self.__logs))

    def save_logs_on_exit(self):
        filename = input("Enter the filename to save logs: ")
        self.save_logs_to_file(filename)  # Corrected method call
        print(f"Logs saved to {filename}")