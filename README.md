Generate Stripe coupons
=======================

A small script to generate Stripe coupons and save them to a CSV file.

## Running it

To run the script, follow these steps:

1. Run `pip install stripe` in your terminal to install the Stripe library.
3. Replace `<YOUR_STRIPE_SECRET_KEY>` in the script with your actual Stripe secret key. You can find your Stripe secret key in the Stripe dashboard.
4. Open a terminal or command prompt and navigate to the directory where this repo is cloned.
5. Execute the script by running the command `python generate_coupons.py` in the terminal.
6. Wait for the script to complete. It will create 1000 unique coupons and save them to a CSV file named `coupons.csv` in the same directory as the script.
7. After the script finishes running, you will see the output message `Coupons saved to coupons.csv`.

Make sure you have appropriate permissions to read and write files in the directory where the script is located.

_Note: Ensure that the Python version you are using is compatible with the `stripe` library._
