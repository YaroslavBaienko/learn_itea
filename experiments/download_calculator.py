class Volume:
    def __init__(self, sizen: float, form: str, speed=6.0):
        self.sizen = sizen
        self.form = form
        self.speed = speed
        if form == "Mb":
            self.sizen = self.sizen
        elif form == "Gb":
            self.sizen = self.sizen * 1000.0
        elif form == "Kb":
            self.sizen = self.sizen / 1000.0

    # def kbtomb(self) -> float:
    #     self.sizen = self.sizen / 1000.0
    #     return self.sizen
    #
    # def mbtokb(self) -> float:
    #     self.sizen = self.sizen * 1000.0
    #     return self.sizen
    #
    # def gbtomb(self) -> float:
    #     self.sizen = self.sizen * 1000.0
    #     return self.sizen

    def calc_download_time(self):
        self.sizen = self.sizen / self.speed
        self.sizen = self.sizen / 60.0
        self.sizen = self.sizen / 60.0
        return f'До конца загрузки осталось {self.sizen} часов'


one_tb = Volume(9.5, "Gb", 2.2).calc_download_time()
two_tb = Volume(20000, "Mb", 6).calc_download_time()

if __name__ == "__main__":
    print({one_tb: two_tb})
