class Products:  
  productlist=[]
  sold_product=0
  sold_quantity=0
  def parameter(self,obj):
    obj.name=input("enter the products")
    obj.quantity=input("enter the quantity")
    if obj.quantity.isdigit()==True:
      self.productlist.append(obj)
    else:
      print("enter a valid number for quantity")
  def display(self):
    for i in self.productlist:
       print(str(self.productlist.index(i)+1) +":" +str(i.name)+ ":" +str(i.quantity))
  def buy_operation(self):     
    if bool(self.productlist)==True:
      pro=input("which product you want")
      quan=input("how much you want")
      pro=int(pro)
      quan=int(quan)
      p=self.productlist[pro-1]
      p.quantity=int(p.quantity)
      if p.quantity>=quan:
         p.quantity=p.quantity-quan
         self.sold_quantity=quan
         self.sold_product=p.name
         self.display()
      else:
        print("that much product is  not available")
    else:
      print("no product")
      return None  
class Products_operation:
  def add_products(self):
    c="y"
    while c=="y":
      b=Products()
      productsobj.parameter(b)
      c=input("Add any more product y or n")
  def buy_products(self):
    productsobj.display()
    productsobj.buy_operation()
  def sold_product(self):
    print(str(productsobj.sold_product)+":"+str(productsobj.sold_quantity))
productsobj=Products()   
operation=Products_operation()
print ("1.add new product with its stocks. 2. buy products 3. list the sold product quantity 4.quit")
while True:
  n=input("enter your choice of operation")
  if n=='1':
    operation.add_products()
  elif n=='2':
    operation.buy_products()
  elif n=='3':  
    operation.sold_product()
  elif n=='4':
    break
  else:
    print("your choice is invalid")
    break
     
