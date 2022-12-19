#!/usr/bin/env python
# coding: utf-8

# In[2]:



import qrcode
import matplotlib.pyplot as plt

data = "https://www.youtube.com/watch?v=_RBlE6Ar8mw&list=RD_RBlE6Ar8mw&start_radio=1"

filename = "My_QR_code.png"

image = qrcode.make(data)

image.save(filename)
plt.imshow(image,cmap='gray')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




