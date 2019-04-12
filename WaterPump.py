class WaterPump:

    numberOfWaterPumpsLost =0

    def __init__(self,
                power=0, manufacturer = None, value=0, price=0, weight=0, colour=None, height=0):
        self.power = power
        self.manufacturer = manufacturer
        self.value = value
        self.price = price
        self.weight = weight
        self.colour = colour
        self.height = height

        WaterPump.numberOfWaterPumpsLost +=1

    def __del__(self):
        print('WaterPump {} has been deleted'.format(self.power))

    @staticmethod
    def get_numberOfWaterPumpsLost():
        return WaterPump.numberOfWaterPumpsLost

    def __str__(self):
        return ('power= {} Vat, manufacturer = {}, value = {}, price = {}$' +
                'weight = {} Kg, colour = {}, height = {} meters').format(self.power, self.manufacturer,
                                                                          self.value, self.weight,
                                                                          self.colour, self.price,
                                                                          self.height)

