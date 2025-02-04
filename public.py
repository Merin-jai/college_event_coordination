from flask import *
from database import*

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
	if "login" in request.form:
		uname=request.form['un']
		pwd=request.form['pa']
		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		res=select(q)
		if res:

			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
			elif res[0]['usertype']=="teacher":
				q="select * from teacher where username='%s'"%(res[0]['username'])
				r=select(q)
				if res:
					session['teacherid']=r[0]['teacher_id']
					return redirect(url_for('teacher.teacherhome'))
			elif res[0]['usertype']=="student":
				q="select * from student where username='%s'"%(res[0]['username'])
				r=select(q)
				if res:
					
					session['studentid']=r[0]['student_id']
					return redirect(url_for('student.studenthome'))
	return render_template('login.html')
