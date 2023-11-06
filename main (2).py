


def linearSearchProduct(productlist,targetproduct,index):
  indices=[]
  for indices, product in enumerate(productlist):
     if product == targetproduct:
        indices.append(index)
        
  return indices
  products=["shoes","boot","loafer","shoes","sandal","shoes"]
  
  target="shoes"
  result=linearSearchProduct(products,target)
  print(result)