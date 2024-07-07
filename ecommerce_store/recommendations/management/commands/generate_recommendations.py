from django.core.management.base import BaseCommand
from orders.models import Orders
from recommendations.models import Recommendation
from products.models import Products

class Command(BaseCommand):
    help = 'Generate recommendations based on past orders'

    def handle(self, *args, **kwargs):
        # Delete all existing recommendations
        Recommendation.objects.all().delete()
        orders = Orders.objects.all()

        # Create a dict to store product pairs and their co-occurrence counts
        product_pairs = {}
        for order in orders:
            products = order.products.all()
            for i, current_product in enumerate(products):
                for related_product in products[i + 1:]:
                    # If the product pair is not in the dictionary, set count to 0
                    if (current_product.id, related_product.id) not in product_pairs:
                        product_pairs[(current_product.id, related_product.id)] = 0
                    # Increment the count for the product pair
                    product_pairs[(current_product.id, related_product.id)] += 1

        # Iterate over the product pairs and their scores
        for (current_product_id, related_product_id), score in product_pairs.items():
            current_product = Products.objects.get(id=current_product_id)
            related_product = Products.objects.get(id=related_product_id)

            # Create or update the recommendation for current_product
            recommendation1, created = Recommendation.objects.get_or_create(product=current_product)
            recommendation1.recommended_products.add(related_product)
            recommendation1.save()

            # Create or update the recommendation for related_product
            recommendation2, created = Recommendation.objects.get_or_create(product=related_product)
            recommendation2.recommended_products.add(current_product)
            recommendation2.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated recommendations'))
