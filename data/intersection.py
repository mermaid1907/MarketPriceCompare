import pandas as pd

migros_data = pd.read_csv('migros_data.csv')
carrefour_data = pd.read_csv('carrefour_data.csv')


cheap = list()


for product, price in migros_data.values:
    for product2, price2, _ in carrefour_data.values:
        if product.replace("_", " ").replace("Kg", "kg").replace("G","g") == product2.replace("_", " ").replace("Kg", "kg").replace("G","g"):
            if int(price)<int(price2):
                cheap.append(["Migros",product.replace("_", " "),price])
            elif int(price2)<int(price):
                cheap.append(["Carrefour",product.replace("_", " "),price2])
            elif int(price) == int(price2):
                cheap.append(["Migros",product.replace("_", " "),price])
            else:
                pass
                  
print(len(cheap))  
my_df = pd.DataFrame(cheap, columns=['Market_Name','Product_Name','Price'])
my_df.to_csv('cheapest.csv', index=False)         
