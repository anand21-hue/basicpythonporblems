import pandas as pd
ds = pd.read_csv("amazon.csv")
ds = ds.dropna(subset=["rating_count"])
ds["actual_price"]=(
    ds["actual_price"]
    .str.replace("₹","",regex=False)
    .str.replace(",","",regex=False)
    .astype(float)
)
ds["discounted_price"]=(
    ds["discounted_price"]
    .str.replace("₹","",regex=False)
    .str.replace(",","",regex=False)
    .astype(float)
)
ds["rating"]= pd.to_numeric(ds["rating"],errors="coerce")
ds["rating_count"]=pd.to_numeric(ds["rating_count"],errors="coerce")

#categories wise average
categoryprice=ds.groupby("category")["discounted_price"].mean()
print("average discounted price by category")
print(categoryprice)

category_rating=ds.groupby("category")["rating"].mean().sort_values(ascending=False)
print("average ratings")
print(category_rating)

ds["discount_amount"] = ds["actual_price"] - ds["discounted_price"]
top_discounts = ds.sort_values("discount_amount", ascending=False).head(5)
print("\nTop 5 products with highest discount:")
print(top_discounts[["product_name", "actual_price", "discounted_price", "discount_amount"]])

best_product=ds[
    (ds["rating"]>=4.5)&(ds["rating_count"]>=100)
    ].sort_values("rating",ascending=False)
print("\nbest rated products")
print(best_product[["product_name","rating","rating_count"]].head(5))
