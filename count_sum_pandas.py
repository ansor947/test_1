import pandas


# data = {
#     'Дата': ['07.05.2022', '07.05.2022', '08.05.2022', '09.05.2022', '09.05.2022', '09.05.2022'],
#     'Товар': ['Банан', 'Хлеб', 'Банан', 'Хлеб', 'Яблоко', 'Хлеб'],
#     'Количество': [30, 10, 40, 8, 10, 10]
#        }


def count_sum(parameters):
    df = pandas.DataFrame(data=parameters)
    product = df.set_index('Товар')
    product_index = product.groupby(by=['Товар']).sum()
    product_index.drop('Дата', axis= 1 , inplace= True )
    return product_index

print (count_sum(data))


