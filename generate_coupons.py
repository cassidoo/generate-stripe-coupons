import csv
import stripe

# Set your Stripe API key
stripe.api_key = '<YOUR_STRIPE_SECRET_KEY>'

# Create a coupon
coupon = stripe.Coupon.create(
    name='Unique Coupon',
    duration='once',
    amount_off=2000,  # $20 in cents
    currency='usd',
)

# Generate promotion codes
promotion_codes = []

for _ in range(1000):
    promotion_code = stripe.PromotionCode.create(coupon=coupon.id)
    promotion_codes.append([promotion_code.code])
    print(f"Generated promotion code {promotion_code.code}")

# Save promotion codes to a CSV file
with open('promotion_codes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(promotion_codes)

print(
    f"A total of {len(promotion_codes)} promo codes have been generated and saved to promotion_codes.csv.")
