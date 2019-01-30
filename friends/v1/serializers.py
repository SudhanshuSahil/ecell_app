from rest_framework import serializers
from friends.models import Friend

# class FollowersMethods:
#     """Helper methods for followers."""

#     @staticmethod
#     def get_count(obj, status):
#         """Get count of followers with specified status."""
#         return obj.followers.filter(ues__status=status).count()

#     @staticmethod
#     def get_followers(obj, status):
#         """Get serialized followers with specified status."""
#         from users.serializers import UserProfileSerializer
#         return UserProfileSerializer(obj.followers.filter(ues__status=status), many=True).data

class FriendSerializer(serializers.ModelSerializer):
	"""Serializer for Event.

	This serializer returns only the count of followers in
	each category, i.e. interested and going and minimal
	venue info. Use `EventFullSerializer` if you want information
	on individual users and venues.
	"""

	# from locations.serializers import LocationSerializerMin
	# from bodies.serializer_min import BodySerializerMin

	# interested_count = serializers.SerializerMethodField()
	# get_interested_count = lambda self, obj: FollowersMethods.get_count(obj, 1)

	# going_count = serializers.SerializerMethodField()
	# get_going_count = lambda self, obj: FollowersMethods.get_count(obj, 2)

	# venues = LocationSerializerMin(many=True, read_only=True)

	class Meta:
		model = Friend
		fields = '__all__'

	# fields = ('id', 'str_id', 'name', 'description', 'image_url',
	#           'start_time', 'end_time', 'all_day', 'venues',
	#           'interested_count', 'going_count', 'website_url', 'weight')		  

