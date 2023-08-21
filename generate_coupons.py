import csv
import stripe

stripe.api_key = '<YOUR_STRIPE_SECRET_KEY>'

# Create 1000 coupons
coupon_count = 1000
coupons = []

for i in range(coupon_count):
    coupon = stripe.Coupon.create(
        amount_off=2000,  # $20 in cents
        currency='usd',
        duration='once',
        name='Unique Coupon', # change this to whatever you want
        metadata={
            'coupon_number': str(i + 1)
        }
    )

    print(f"Created coupon with ID {coupon.id}")

    coupons.append(coupon)

# Save coupons to a CSV file
filename = 'coupons.csv'
fieldnames = ['Coupon ID']

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for coupon in coupons:
        writer.writerow({
            'Coupon ID': coupon.id
        })

print(f"Coupons saved to {filename}")
