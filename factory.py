class DisplayFactory:
    def create_display(self):
        pass

class PhoneDisplayFactory(DisplayFactory):
    def create_display(self):
        return PhoneDisplay()

class TVDisplayFactory(DisplayFactory):
    def create_display(self):
        return TVDisplay()

class Display:
    def show(self, message):
        pass

class PhoneDisplay(Display):
    def show(self, message):
        print(f"Phone Display: {message}")

class TVDisplay(Display):
    def show(self, message):
        print(f"TV Display: {message}")
