#!/usr/bin/env python
# coding: utf-8

# In[11]:


from abc import abstractmethod, ABC


# ## Encapsulation

# In[12]:


class encapsulation:
    def __init__(self, input_nama, input_kegiatan, input_keinginan):
        self.nama = input_nama
        self.kegiatan = input_kegiatan
        self.keinginan = input_keinginan
        
    def cetak(self):
        print(f'{self.nama} {self.kegiatan} {self.keinginan}')
    
    def tampilkan(self):
        print(f'Buahnya adalah jeruk')   


# # Abstraction

# In[13]:


class abstrak(ABC):
    def cetak2(self, i):
        print('Selamat anda mendapatkan : ', i)
        
    @abstractmethod
    def gacha(self):
        pass

    
class pertama(abstrak):
    def gacha(self):
        print('Kamu sedang melakukan gacha dan...')

        
class kedua(abstrak):
    def gacha():
        print('Kamu melakukan gacha lagi dan...')


# # Inheritance

# In[14]:


class bintang(object):
    def __init__(self, nama_bintang, jarak, konstelasi):
        self.nama_bintang = nama_bintang
        self.jarak = jarak
        self.konstelasi = konstelasi
        
    def awal(self):
        print('Nama bintang paling terang ialah :')
        
    def akhir(self):
        print(f'{self.nama_bintang}, ia adalah bintang paling terang pertama, dengan jarak {self.jarak} tahun cahaya, \n'
              f'dan ia berada dikonstelasi {self.konstelasi}')        
    
    
class bintang2(bintang):
    def __init__(self, nama_bintang, jarak, konstelasi, spektrum, tipe):
        super().__init__(nama_bintang, jarak, konstelasi)
        self.spektrum = spektrum
        self.tipe = tipe
    
    def awal2(self):
        print('Nama bintang paling terang kedua adalah : ')
        
    def akhir2(self):
        print(f'{self.nama_bintang}, ia adalah bintang paling terang kedua, dengan jarak {self.jarak} tahun cahaya,\n'
              f'dan ia berada dikonstelasi {self.konstelasi}, {self.nama_bintang} termasuk dalam spektrum {self.spektrum},\n'
              f'dengan tipe {self.tipe}')


# # Polymorphism

# In[15]:


class Hewan(object):
  def __init__(self, nama, warna, tempat_tinggal):
    self.nama = nama
    self.warna = warna
    self.temt = tempat_tinggal

  def gatau(self):
    print("Nama Hewan :")

  def info(self):
    print(f"{self.nama}, ia berwarna : {self.warna}, dan ia tinggal {self.temt}")
  
  def info2(self):
     print(f'Nama ilmiah dari hewan ini adalah {self.ni}')
   

class Hewan2(Hewan):
    def __init__(self,  nama, warna, tempat_tinggal, nama_ilmiah):
        super().__init__(nama, warna, tempat_tinggal)
        self.ni = nama_ilmiah

        
class Hewan3(Hewan):
  def __init__(self, nama, warna, tempat_tinggal, nama_ilmiah, tipe):
    super().__init__(nama, warna, tempat_tinggal)
    self.tipe = tipe
    self.ni = nama_ilmiah
    
  def info3(self):
    print(f"Hewan ini adalah {self.tipe}")  

