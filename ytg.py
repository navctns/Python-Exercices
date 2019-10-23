print("1.Book\t2.Pen/n3.Pencils/t4.Gum/n5.Bag/t6.Bottle/n7.Color Box/t8.Rubix Cube")
i=int(input("1.Book\t2.Pen/n3.Pencils/t4.Gum/n5.Bag/t6.Bottle/n7.Color Box/t8.Rubix Cube"))
if(i==1):
    print("your selected item is book")
    a=int(input("1.Buy Now\t 2.Add to Cart"))
    if a==1:
        print("Your item will be delivered on 17-10-19")
    elif a==2:
        print("Item is added to Cart")
