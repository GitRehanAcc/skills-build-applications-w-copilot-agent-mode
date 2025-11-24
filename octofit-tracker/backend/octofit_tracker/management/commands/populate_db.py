from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True)
        User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel', is_superhero=True)
        User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True)
        User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True)

        # Activities
        Activity.objects.create(user='ironman@marvel.com', type='run', duration=30, timestamp='2025-11-24T10:00:00Z')
        Activity.objects.create(user='spiderman@marvel.com', type='swim', duration=45, timestamp='2025-11-24T11:00:00Z')
        Activity.objects.create(user='batman@dc.com', type='cycle', duration=60, timestamp='2025-11-24T12:00:00Z')
        Activity.objects.create(user='wonderwoman@dc.com', type='yoga', duration=50, timestamp='2025-11-24T13:00:00Z')

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='medium')
        Workout.objects.create(name='Plank', description='Hold plank position', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
