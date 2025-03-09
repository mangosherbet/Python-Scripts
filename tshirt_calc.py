#This is a pricing calculator for imprinted T-Shirts
#Copyright @2025 Mangsherbet 
#Please feel free to use this in any way that you see fit as long as credit is given 


#Variables
item_cost = float(input("What is the cost of the item: $"))
qty = int(input("What is the quantity: "))
imprint_colors_1 = int(input("How many imprint colors on the 1st location: "))
imprint_colors_2 = int(input("How many imprint colors on the 2nd location: "))
decoration_costs_1 = float(input("How much is the cost for decoration for the 1st location: $"))
if imprint_colors_2 <= 0:
    decoration_costs_2 = int(input("How much is the cost for decoration for the 2nd location: $"))
imprint_cost = (qty * decoration_costs_1) + (qty * decoration_costs_2)

def calculate_total_cost(item_cost, qty, imprint_cost):
    """
    Calculate the total cost of the t-shirts.
    """
    return (item_cost * qty) + imprint_cost

def calculate_retail_price(total_cost, margin=0.40):
    """
    Calculate the retail price with a 40% margin.
    """
    return total_cost / (1 - margin)

def main():
    # Inputs

    # Calculate imprint costs
    total_imprint_cost = imprint_cost

    # Calculate Set up Costs
    setup_costs = (imprint_colors_1 * 25) + (imprint_colors_2 * 25) 

    # Calculate total cost
    total_cost = calculate_total_cost(item_cost, qty, total_imprint_cost) + setup_costs

    # Calculate retail price
    retail_price = calculate_retail_price(total_cost)

    # Calculate per-item cost and retail price
    per_item_cost = total_cost / qty
    per_item_retail_price = retail_price / qty

    # Output results
    print("\n--- Results ---")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Total Retail Price (60% margin): ${retail_price:.2f}")
    print(f"Per Item Cost: ${per_item_cost:.2f}")
    print(f"Per Item Retail Price: ${per_item_retail_price:.2f}")

if __name__ == "__main__":
    main()

