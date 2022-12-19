class ProductSerializer(object):

    @staticmethod
    def serialize(product):
        return {
            'reference': product.reference,
            'brand_id': product.brand_id
        }
