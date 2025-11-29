# Currency Converter using Functions

def usd_to_inr(usd):
    return usd * 84.50

def inr_to_usd(inr):
    return inr / 84.50

def eur_to_inr(eur):
    return eur * 90.20

print("10 USD to INR:", usd_to_inr(10))
print("500 INR to USD:", inr_to_usd(500))
print("5 EUR to INR:", eur_to_inr(5))
