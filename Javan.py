from datetime import date
class Entity:
    def get_att(self):
        d = self.__dict__
        s = ''
        for v in d.values():
            s+=str(v)+'$'
        s = s[:len(s)-1]
        s+='#'
        return s
    
    def save(self,filename):
        att = self.get_att()
        f = open(filename,'a+',encoding='utf-8')
        f.write(att)
        f.close()
        
    def edit(self,filename,t):
        old = self.get_att()
        new = ''
        for v in t:
             new+=str(v)+'$'
        new = new[:len(new)-1]
        new+='#'
        f = open(filename,'r',encoding='utf-8')
        s = f.read()
        f.close()
        s = s.replace(old,new)
        f = open(filename,'w',encoding='utf-8')
        f.write(s)
        f.close()
        
    def delete(self,filename):
        att = self.get_att()
        f = open(filename,'r',encoding='utf-8')
        s = f.read()
        f.close()
        s = s.replace(att,'')
        f = open(filename,'w',encoding='utf-8')
        f.write(s)
        f.close()
        
        
class Store(Entity):
    #anbar
    filename = "store.txt"
    def __init__(self,name,code_store,addres_store,tel_store,type_store):
        self.name = name
        self.code_store = code_store
        self.addres_store = addres_store
        self.tel_store = tel_store
        self.type_store = type_store
        self.lst_store = []
    
    @property
    def code_store(self):
        return self.__code_store
    @code_store.setter
    def code_store(self,value):
        if value>=0:
            self.__code_store = value
        else:
            raise ValueError('Erorr')
                                     
    @property
    def tel_store(self):
        return self.__tel_store
    @tel_store.setter
    def tel_store(self,value):
        if value>8:
            self.__tel_store = value
        else:
            raise ValueError('Erorr')
        
    def __str__(self):
        return self.name+"  " 
            
    def edit(self,*t):
        super().edit(Store.filename,t)
    
    def delete(self):
        super().delete(Store.filename)
    
    def save(self):
        super().save(Store.filename)
    
    @classmethod
    def read_file(cls):
        file = open(Store.filename,'r',encoding='utf8')
        s = file.read().split('#')
        lst = []
        s.pop()
        for v in s:
            t = v.split('$')
            lst.append(Store(t[0],int(t[1]),t[2],int(t[3]),t[4]))
        file.close()
        return lst
        
        
class People(Entity):
    #subClass
    def __init__(self,ferst_name,last_name,tel_1,tel_2,addres):
        self.ferst_name = ferst_name
        self.last_name =last_name
        self.tel_1 = tel_1
        self.tel_2 = tel_2
        self.addres = addres
        #self.lst_people = []

      
class User(People):
        #Anbardar
    failename = "user.txt"
    def __init__(self,ferst_name,last_name,tel_1,tel_2,addres,shift,username,password):
        People.__init__(self,ferst_name,last_name,tel_1,tel_2,addres)
        self.shift = shift
        self.username = username
        self.password = password
        
        
        #self.lst_user = []

    # @property
    # def shift(self):
    #     return self.__shift
    # @shift.setter
    # def shift(self,value):
    #     if (value==1) or (value==2):
    #         self.__shift = value
    #     else:
    #         raise ValueError('Erorr')
        
    # @property
    # def username(self):
    #     return self.__username
    # @username.setter
    # def username(self,value):
    #     if value>=8:
    #         self.__username = value
    #     else:
    #         raise ValueError('Erorr')

    # @property
    # def password(self):
    #     return self.__password
    # @password.setter
    # def password(self,value):
    #     if value>=8:
    #         self.__password = value
    #     else:
    #         raise ValueError('Erorr')


    # @property
    # def tel_1(self):
    #     return self.__tel_1
    # @tel_1.setter
    # def tel_1(self,value):
    #     if value>8:
    #         self.__tel_1 = value
    #     else:
    #         raise ValueError('Erorr')

    # @property
    # def tel_2(self):
    #     return self.__tel_2
    # @tel_2.setter
    # def tel_2(self,value):
    #     if value>11:
    #         self.__tel_2 = value
    #     else:
    #         raise ValueError('Erorr')
        
    def __str__(self):
        return self.ferst_name+"  "+self.last_name
    
    def edit(self,*t):
        super().edit(User.failename,t)
        
    def delete(self):
        super().delete(User.filename)
       
    def save(self):
        super().save(User.failename)
    
    @classmethod
    def read_file(cls):
        file = open(User.failename,'r',encoding='utf8')
        s = file.read().split('#')
        lst = []
        s.pop()
        for v in s:
            t = v.split('$')
            lst.append(User(t[0],t[1],int(t[2]),int(t[3]),t[4],t[5],t[6],t[7]))
        file.close()
        return lst
    
    
class Customer(People):
    filename = "customer.txt"
    def __init__(self,ferst_name,last_name,tel_1,tel_2 ,addres,conteract,code):
        People.__init__(self,ferst_name,last_name,tel_1,tel_2,addres)      
        self.conteract = conteract 
        self.code = code
        #self.lst_customer = []

    @property
    def tel_1(self):
        return self.__tel_1
    @tel_1.setter
    def tel_1(self,value):
        if value>8:
            self.__tel_1 = value
        else:
            raise ValueError('Erorr')

    @property
    def tel_2(self):
        return self.__tel_2
    @tel_2.setter
    def tel_2(self,value):
        if value>11:
            self.__tel_2 = value
        else:
            raise ValueError('Erorr')
    
    @property
    def code(self):
       return self.__code
    @code.setter
    def code(self,value):
       if value>0:
           self.__code = value
       else:
           raise ValueError('Erorr')

    def __str__(self):
        return self.ferst_name+"  "+self.last_name
    
    def edit(self,*t):
        super().edit(Customer.filename,t)
        
    def delete(self):
        super().delete(Customer.filename)
       
    def save(self):
        super().save(Customer.filename)
        
    @classmethod
    def read_file(cls):
        file = open(Customer.filename,'r',encoding="utf-8")
        s = file.read().split('#')
        lst = []
        s.pop()
        for v in s:
            t = v.split('$')
            lst.append(Customer(t[0],t[1],int(t[2]),int(t[3]),t[4],t[5],int(t[6])))
        file.close()
        return lst


class Kala(Entity):
    #kala
    failename = "c_kala.txt"
    def __init__(self,name,code_kala,unit_1,unit_2,n_unit,type_kala,description,count):
        self.name = name
        self.code_kala = code_kala
        self.unit_1 = unit_1
        self.unit_2 = unit_2
        self.n_unit = n_unit
        self.type_kala = type_kala
        self.description = description
        self.count = count
        self.lst_kala = []

    @property
    def code_kala(self):
        return self.__code_kala
    @code_kala.setter
    def code_kala(self,value):
        if value>0:
            self.__code_kala = value
        else:
            raise ValueError('Erorr')
        
    @property
    def n_unit(self):
        return self.__n_unit
    @n_unit.setter
    def n_unit(self,value):
        if value>0:
            self.__n_unit = value
        else:
            raise ValueError('Erorr')
    #add_mojodi_kala
    @property    
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self,value):
        if value>=0:
            self.__stock = value
        else:
            raise ValueError('invalid')
            
    def __str__(self):
        return self.name+" "+self.unit_1+" "+str(self.count)
    
    def edit(self,*t):
        super().edit(Kala.failename,t)
        
    def delete(self):
        super().delete(Kala.failename)
           
    def save(self):
        super().save(Kala.failename)

    @classmethod
    def read_file(cls):
        file = open(Kala.failename,'r',encoding="utf-8")
        s = file.read().split('#')
        lst = []
        s.pop()
        for v in s:
            t = v.split('$')
            lst.append(Kala(t[0],int(t[1]),t[2],t[3],int(t[4]),t[5],t[6],int(t[7])))
        file.close()
        return lst
        
        
class Cardex_kala:
    #cardex_mojodi_kala
    def __init__(self,count_in_pack):
        self.count_in_pack = count_in_pack
        # self.lst_cardex = []
        
    def add_kala(self,name,count):
        self.lst_kala.append([name,count])


class Factor(Entity):
    def __init__(self,code_factor,date_of_factor,user_name,customer,store):
        self.code_factor = code_factor
        self.date_of_factor = date_of_factor
        self.user_name = user_name
        self.customer = customer
        self.store = store
        self.lst = []
        

class Factor_bay(Factor):
    failename = "buy.txt"
    def __init__(self,code_factor,date_of_factor,user_name,customer,store):
        Factor.__init__(self,code_factor,date_of_factor,user_name,customer,store)
        # self.lst_bay = []
        
    @property
    def code_factor(self):
        return self.__code_factor
    @code_factor.setter
    def code_factor(self,value):
        if value>1:
            self.__code_factor = value
        else:
           raise ValueError('Erorr')

       
    def add_stock(self,count):
        old = self.get_att()
        
        self.stock+=count
        new = self.get_att()
        
        f=open(Kala.filename,'r',encoding='utf-8')
        s=f.read()
        f.close()
        s=s.replace(old,new)
        f=open('kala.txt','w',encoding='utf-8')
        f.write(s)
        f.close()
        
        
    def __str__(self):
        return str(self.code_factor)+"  "+str(self.date_of_factor)+"  "
        
    def add_kala(self,name,code_kala,count,unit_2,n_unit):
        self.lst_kala.append([code_kala,name,count,unit_2,n_unit])
    
    def save(self):
        super().save(Factor_bay.failename)
            
    @classmethod
    def read_file(cls):
        file = open(Factor_bay.failename,'r',encoding="utf8")
        s = file.read().split('#')
        lst = []
        s.pop()
        for v in s:
            t = v.split('$')
            lst.append(Factor_bay(int(t[0]),t[1],t[2],t[3],t[4]))
        file.close()
        return lst
    
class Factor_sell(Factor):
    failename = "sell.txt"
    def __init__(self,code_factor,date_of_factor,user_name,customer,store):
        Factor.__init__(self,code_factor,date_of_factor,user_name,customer,store)
        # self.lst_sell = []
        # self.radif = radif 
    @property
    def code_factor(self):
        return self.__code_factor
    @code_factor.setter
    def code_factor(self,value):
        if value>=1:
            self.__code_factor = value
        else:
            raise ValueError('Erorr')
    
    # @property
    # def radif(self):
    #     return self.radif
    # @radif.setter
    # def radif(self,value):
    #     value = i
    #     for i in range(1,50):
    #         yield i
    #     self.radif = i
            
    def clr_stock(self,count):
        old = self.get_att()
        
        self.stock-=count
        new = self.get_att()
        
        f=open(Kala.filename,'r',encoding='utf-8')
        s=f.read()
        f.close()
        s=s.replace(old,new)
        f=open('kala.txt','w',encoding='utf-8')
        f.write(s)
        f.close()
        
    def __str__(self):
        return str(self.code_factor)+"  "+str(self.date_of_factor)+"  "
         
    def add_kala(self,code_kala,count,unit_2,n_unit):
        self.lst_kala.append([code_kala,count,unit_2,n_unit])

    def save(self):
        super().save(Factor_sell.failname)

    @classmethod
    def read_file(cls):
        file = open(Factor_sell.failename,'r',encoding="utf8")
        s = file.read().split('#')
        lst = []
        s.pop()
        for v in s:
            t = v.split('$')
            lst.append(Factor_sell(int(t[0]),t[1],t[2],t[3],t[4]))
        file.close()
        return lst
    
    def radif():
        for i in range(1,50):
            yield i
        x = next(i)
        
class Lst_factor_buy:
    def __init__(self,count):
        self.count = count
        
    def add_factor_buy(self,code_factor,customer):
        self.lst_factor_buy.append([code_factor,customer])
    
     
class Lst_factor_sell:
    def __init__(self,count):
        self.count = count
        
    def add_factor_buy(self,code_factor,customer):
        self.lst_factor_buy.append([code_factor,customer])   


class Handling_store:
    def __init__(self,date):
        self.date = date
    
    def add_cardex_kala(self,name,count):
        self.lst_cardex_kala.append([name,count])
    
    @classmethod
    def read_file(cls):
        file = open(Kala.failename,'r',encoding="utf8")
        s = file.read().split('#')
        lst = []
        s.pop()
        for v in s:
            t = v.split('$')
            lst.append(Kala(int(t[0])))
        file.close()
        return lst
