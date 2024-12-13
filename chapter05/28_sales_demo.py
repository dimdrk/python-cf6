from functools import reduce

def main():
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    sales = [12_000, 14_500, 13_200, 15_000, 20_000, 18_500, 16_000, 15_500,
             14_000, 19_000, 22_500, 24_000]
    
    # Create a dictionary with months and sales
    my_dict = {}
    for i, month in enumerate(months):
        my_dict[month] = sales[i]
    print(my_dict)

    monthly_sales = dict(zip(months, sales))
    print("Monthly sales:", monthly_sales)

    print("-" * 40)
    for month, value in monthly_sales.items():
        print(f"{month:<9}:{value:>6}k")

    print("Months with sales >= 15.000")
    high_sales_months = dict(filter(lambda month_tuple: month_tuple[1] >= 15_000, monthly_sales.items()))
    print(high_sales_months)

    # Apply discount of 10% for all sales above 20.000 (end-of year promotion)
    discounted_sales = {
        month: value * 0.9 if value > 20_000 else value
        for month, value in monthly_sales.items()
    }
    print("Discounted sales:", discounted_sales)

    # Taxes (15%)
    sales_after_taxes = {
        month: value * 0.85
        for month, value in discounted_sales.items()
    }
    print("Sales after taxes:", sales_after_taxes)

    # Total sales
    total_annual_sales = sum(monthly_sales.values())
    print("Total annual sales:", total_annual_sales)

    # Alternative way for total sales
    total_an_sales = reduce(lambda x, y: x + y, monthly_sales.values())
    print("Alternative way for total sales:", total_an_sales)

    # Best and worst performing months
    best_month = max(monthly_sales, key=monthly_sales.get)
    worst_month = min(monthly_sales, key=monthly_sales.get)
    print(f"Best month: {best_month} with sales: {monthly_sales[best_month]}K")
    print(f"Worst month: {worst_month} with sales: {monthly_sales[worst_month]}K")

if __name__ == '__main__':
    main()