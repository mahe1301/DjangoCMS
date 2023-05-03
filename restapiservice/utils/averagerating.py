from ..models import CustomerRating, Product


def calc_average_rating(productid):
    avg_rating = 0
    try:
        cust_rating_objs = CustomerRating.objects.filter(Product_id=productid)
        prod_obj = Product.objects.get(id=productid)
        if len(cust_rating_objs) != 0:
            avg_dict = {1:0,2:0,3:0,4:0,5:0}
            total_ratings = 0
            cal_ratings = 0
            for obj in cust_rating_objs:
                avg_dict[obj.rating] = avg_dict[obj.rating] + 1
            for d in avg_dict.keys():
                total_ratings = total_ratings + avg_dict[d]
                avg_dict[d] = avg_dict[d] * d
                cal_ratings = cal_ratings + avg_dict[d]
            avg_rating = cal_ratings/total_ratings
            prod_obj.averageRating = avg_rating
            prod_obj.save()
    except Exception:
        pass