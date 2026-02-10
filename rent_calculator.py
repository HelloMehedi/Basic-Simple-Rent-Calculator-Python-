def rent_calculator ():
  try:
    # Rent Expenses
    rent_cost = int(input("Enter Flat/House Rent = "))
    
    # Food Cost 
    food_cost_daily = int(input("Enter Daily Food Cost = "))
    food_cost_monthly = food_cost_daily * 30
    
    #Utility Bill
    
    electricity_used_monthly = int(input("Enter Monthly Electricity Units Used = "))
    electricity_cost_units = int(input("Enter Unit Charge Per Unit = "))
    electricity_cost_monthly = electricity_used_monthly * electricity_cost_units
    
    
    internet_bill = int(input("Enter Monthly Internet Bill = "))
    
    gas_bill = int(input("Enter Monthly Gas Bill = "))
    
    utility_cost_monthly = electricity_cost_monthly + internet_bill + gas_bill
    
    #Total Cost
    total_cost = rent_cost + food_cost_monthly + utility_cost_monthly
    
    #per person costs
    
    persons = int(input("Enter Total Persons = "))
    
    per_person_cost = total_cost // persons
    
    print("Food Cost Daily = ", food_cost_daily)
    print("Food Cost Monthly = ", food_cost_monthly)
    print("Electricity Cost Monthly = ", electricity_cost_monthly)
    print("Internet Bill and Gas Bill Cost = ", internet_bill + gas_bill)
    print("Utility Cost Monthly = ", utility_cost_monthly)
    print("Total Cost = ", total_cost)
    print("Per Person Cost = ", per_person_cost)
    
    
    
  except ValueError:
      print("Please enter valid numbers!")
      
rent_calculator()

    
    