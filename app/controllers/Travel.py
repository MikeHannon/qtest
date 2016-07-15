from system.core.controller import *
from flask import Flask, flash, session

class Travel(Controller):
    def __init__(self, action):
        super(Travel, self).__init__(action)
        self.load_model('Travel')
        # self.db = self._app.db

    def add_travel(self):
        return self.load_view('addplan.html')

    def add_plan(self):
        trip_info = {
            'destination' : request.form['destination'],
            'plan' : request.form['plan'],
            'start_date' : request.form['start_date'],
            'end_date' : request.form['end_date']
        }
        trips = self.models['Travel'].add_trip(trip_info)

        if  trips['status'] == False:
            #switch error message from array to Falsh and redirect to login page again
            for message in trips['errors']:
                flash(message)
            return self.load_view('addplan.html')
            # return redirect('/dashboard')
        else:
            # return self.load_view('addplan.html')
            return redirect('/dashboard')

    def dashboard(self):
        mytrips = self.models['Travel'].my_trip()
        print ('%' * 25)
        print mytrips
        print ('%' * 25)
        trip_joined = self.models['Travel'].trip_joined()
        print ('$' * 25)
        print trip_joined
        print ('$' * 25)
        others_trip = self.models['Travel'].others_trip()
        print ('!' * 25)
        print others_trip
        print ('!' * 25)
        return self.load_view('dashboard.html', mytrips=mytrips, trips_joined=trip_joined, others_trips=others_trip)

    def details(self, id):
        trip_details = self.models['Travel'].trip_details(id)
        print ('~' * 25)
        print trip_details
        print ('~' * 25)
        friends_joined = self.models['Travel'].friends_joined(id)
        return self.load_view('details.html', trip_details=trip_details, friends_joined=friends_joined)

    def join_trip(self, id):
        join_trip = self.models['Travel'].join_trip(id)
        print ('/' * 25)
        print join_trip
        print ('/' * 25)
        return redirect('/dashboard')