from django.db import models


# Create your models here.
class login(models.Model):
        username= models.CharField(max_length=20)
        password=models.CharField(max_length=20)

class Customer(models.Model):
    Cust_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=13)
    Cnic_no = models.CharField(max_length=18)
    V_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Cust_name


class Item(models.Model):
    Item_name = models.CharField(max_length=100)
    choiceType = (
        ('Car Parts', 'Parts used in cars or other vehicles'),
        ('CNG Kit Parts', 'Parts of CNG Kit installation or fixing'),
    )
    Item_Type = models.CharField(max_length=30,choices=choiceType,default='Select Type')
    Quantity = models.IntegerField()
    Price = models.IntegerField()

    def __str__(self):
        return self.Item_name


class Service(models.Model):
    Service_name = models.CharField(max_length=50)
    Charges = models.IntegerField()

    def __str__(self):
        return self.Service_name


class Supplier(models.Model):
    Supplier_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    Phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.Supplier_name


class Supplier_Order(models.Model):
    Order_Date = models.CharField(max_length=20)
    Item_n = models.ForeignKey(Item, on_delete=models.CASCADE)
    Item_Qty = models.IntegerField()
    Supp_Date = models.CharField(max_length=20)
    Supplier_n = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total_amount = models.IntegerField()


class Purchase(models.Model):
    Purchase_date = models.CharField(max_length=20)
    Item_n = models.ForeignKey(Item, on_delete=models.CASCADE)
    It_quantity = models.IntegerField()
    Items_Price = models.IntegerField()
    Service_n = models.ForeignKey(Service, on_delete=models.CASCADE)
    Total_Amount = models.IntegerField()
