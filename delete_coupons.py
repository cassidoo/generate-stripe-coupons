import csv
import stripe

# Set your Stripe API key here
stripe.api_key = '<YOUR_STRIPE_SECRET_KEY>'

def delete_coupon(coupon_id):
    try:
        stripe.Coupon.delete(coupon_id)
        print(f'Successfully deleted coupon with ID {coupon_id}')
    except stripe.error.StripeError as e:
        print(f'Error deleting coupon with ID {coupon_id}: {e}')

# Read coupon IDs from the CSV file
with open('coupons.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if present
    for row in reader:
        coupon_id = row[0]
        delete_coupon(coupon_id)