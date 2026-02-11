from .blog_models import BlogPost, ImpactStory, Clinic, ChallengeEntry
from .volunteer_models import VolunteerApplication
from .shop_models import Product, Order, OrderItem
from donations.models import Donation
from users.models import IndividualRegistration
from django.contrib import admin

admin.site.register(BlogPost)
admin.site.register(ImpactStory)
admin.site.register(Clinic)
admin.site.register(ChallengeEntry)
admin.site.register(VolunteerApplication)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Donation)
admin.site.register(IndividualRegistration)
