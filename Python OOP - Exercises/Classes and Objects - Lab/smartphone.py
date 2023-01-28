class Smartphone:
    def __init__(self,memory:int):
        self.memory = memory
        self.apps = list()
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True
            return self.is_on
        self.is_on = False
        return self.is_on

    def install(self,app,app_memory):
        if app_memory <= self.memory and self.is_on:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"
        elif app_memory <= self.memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smp = Smartphone(500)
print(smp.install("Facebook",300))
print(smp.status())
print(smp.power())
print(smp.install("Messenger",200))
print(smp.status())