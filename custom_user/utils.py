def generate_otp():
        import time
        import math, random
        random.seed(time.time())
        numbers = "0123456789"
        otp = ""
        for i in range(4):
            otp += numbers[math.floor(random.random() * 10)]

        return otp