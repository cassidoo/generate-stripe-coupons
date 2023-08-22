# Generate Stripe coupons + promo codes

A small script to generate a Stripe coupon and promotion codes, and save them to a CSV file.

**Thing I learned while making this that might be worth you knowing:**
Stripe coupons and promotion codes are _different things_. A coupon is what you see on _your_ end as a seller of a product, and a promotion code is what your users see. So, you can have a bunch of different promotion codes attached to one coupon, and each of those promotion codes gives you whatever value the coupon has.

When I first made this repo, I just had it generate 1000 coupons and save it to a CSV, and now I know that I actually needed to make one coupon, with 1000 promo codes. If you actually want to bulk-generate coupons, you could go to the git history and find that script version. Good luck!

## Running it

To run the script, follow these steps:

1. Run `pip install stripe` in your terminal to install the Stripe library.
2. Replace `<YOUR_STRIPE_SECRET_KEY>` in the script with your actual Stripe secret key. You can find your Stripe secret key in the Stripe dashboard. This is not your public-facing key!
3. Replace `Unique Coupon` with the name of the coupon you want for each coupon. You can also edit the `amount_off` variable to however much off you want to offer (currently it's $20 off).
4. Open a terminal or command prompt and navigate to the directory where this repo is cloned.
5. Execute the script by running the command `python generate_coupons.py` in the terminal.
6. Wait for the script to complete. It will create a coupon with 1000 unique promo codes and save them to a CSV file named `promotion_codes.csv` in the same directory as the script.
7. After the script finishes running, you will see the output message `A total of X promo codes have been generated and saved to promotion_codes.csv`.

Make sure you have appropriate permissions to read and write files in the directory where the script is located.

_Note: Ensure that the Python version you are using is compatible with the `stripe` library._
