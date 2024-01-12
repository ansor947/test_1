import pandas

def count_sum(parameters):
    df = pandas.DataFrame(data=parameters)
    product = df.set_index('product_name')
    product_index = product.groupby(by=['product_name']).sum()
    product_index.drop('date', axis= 1 , inplace= True )
    return product_index

# print (count_sum(data))


