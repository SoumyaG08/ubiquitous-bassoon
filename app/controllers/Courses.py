"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', all_courses=courses)

    def show(self, id):
        # Note how we access the model using self.models
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('show.html', course=course)

    # This is how a method used to add a course would look
    # We would set up a POST route for this method
    def add(self):
        # in actuality, data for the new course would come 
        # from a form on our client
        course_details = {
            'title': request.form['name'],
            'description': request.form['description']
        }
        courses = self.models['Course'].add_course(course_details)
        return redirect('/')

    # This is how a method used to update a course would look
    # We would set up a POST route for this method
    def update(self, course_id):
        # in actuality, data for updating the course would come 
        # from a form on our client
        course_details = {
            'id': course_id,
            'title': 'Python 2.0',
            'description': 'This course is unreal!'
        }
        self.models['Course'].update_course(course_details)
        return redirect('/')

    def remove(self, course_id):
        course = self.models['Course'].get_course_by_id(course_id)
        return self.load_view('delete.html',course=course[0])

     # This is how a method used to delete a course would look
     # We would set up a POST route for this method
    def delete(self, course_id):
        self.models['Course'].delete_course(course_id)
        return redirect('/')

