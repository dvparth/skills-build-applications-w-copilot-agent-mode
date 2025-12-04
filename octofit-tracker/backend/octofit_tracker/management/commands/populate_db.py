from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        heroes = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
        ]
        user_objs = [User.objects.create(**hero) for hero in heroes]

        # Create activities
        Activity.objects.create(user=user_objs[0], type='Running', duration=30)
        Activity.objects.create(user=user_objs[1], type='Cycling', duration=45)
        Activity.objects.create(user=user_objs[2], type='Swimming', duration=60)
        Activity.objects.create(user=user_objs[3], type='Yoga', duration=20)

        # Create workouts
        workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        workout2 = Workout.objects.create(name='Strength Training', description='Full body strength routine')
        workout1.suggested_for.set(user_objs)
        workout2.suggested_for.set(user_objs)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=100)
        Leaderboard.objects.create(team=dc, total_points=80)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
