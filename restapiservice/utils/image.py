# def upload_product(instance,filename):
#     return "/".join(['Products',str(instance.name),filename])


# def upload_product_images(instance,filename):
#     return "/".join(['Products',str(instance.product.name),filename])
def upload_product(instance,filename):
    return "/".join(['Products',str(instance.name).replace(" ", ""),filename])


def upload_product_images(instance,filename):
    return "/".join(['Products',str(instance.product.name).replace(" ", ""),filename])