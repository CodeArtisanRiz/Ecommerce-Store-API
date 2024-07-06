from django.core.management.base import BaseCommand
from orders.models import Orders
from recommendations.models import Recommendation
from products.models import Products

class Command(BaseCommand):
    help = 'Generate recommendations based on past orders'

    def handle(self, *args, **kwargs):
        Recommendation.objects.all().delete()
        orders = Orders.objects.all()

        product_pairs = {}
        for order in orders:
            products = order.products.all()
            for i, product1 in enumerate(products):
                for product2 in products[i + 1:]:
                    if (product1.id, product2.id) not in product_pairs:
                        product_pairs[(product1.id, product2.id)] = 0
                    product_pairs[(product1.id, product2.id)] += 1

        for (product1_id, product2_id), score in product_pairs.items():
            product1 = Products.objects.get(id=product1_id)
            product2 = Products.objects.get(id=product2_id)

            # Create or update the recommendation for product1
            recommendation1, created = Recommendation.objects.get_or_create(product=product1)
            recommendation1.recommended_products.add(product2)
            recommendation1.save()

            # Create or update the recommendation for product2
            recommendation2, created = Recommendation.objects.get_or_create(product=product2)
            recommendation2.recommended_products.add(product1)
            recommendation2.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated recommendations'))
