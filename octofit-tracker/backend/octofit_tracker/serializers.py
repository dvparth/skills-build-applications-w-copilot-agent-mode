
from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = Team
        fields = ['_id', 'name']

class UserSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = serializers.CharField(source='team._id', read_only=True)
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(source='user._id', read_only=True)
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'user_id', 'type', 'duration', 'timestamp']

class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    suggested_for = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'suggested_for']

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = serializers.CharField(source='team._id', read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'team_id', 'total_points', 'last_updated']
