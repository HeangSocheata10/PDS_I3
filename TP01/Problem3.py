def celsius_to_fahrenheit(celsuis, round_to=1):
    f= celsuis * 9 / 5 + 32 
    return f
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(32))

def fahrenheit_to_celsuis(farenhiet, round_to=1):
    c= (farenhiet - 32) * 5 / 9
    return c
print(fahrenheit_to_celsuis(98.6))
print(fahrenheit_to_celsuis(32))

