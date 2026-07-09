"""Hi"""
Price = int(input())
Service = Price*0.1
if Service < 50:
    Service = 50
elif Service > 1000:
    Service = 1000

sum1 = Price + Service
sum2 = sum1*1.07
print(f"{sum2:.2f}")