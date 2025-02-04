from flask import *
from database import*

student=Blueprint('student',__name__)

@student.route('/studenthome')
def studenthome():
	data={}
	sid=session['studentid']
	q="select * from student where student_id='%s' "%(sid)
	res=select(q)
	data['stude']=res
	return render_template('studenthome.html',data=data)


@student.route('/studentviewclub')
def studentviewclub():
	data={}
	q="select * from club where cstatus='active'"
	r=select(q)
	data['clubs']=r
	return render_template('studentviewclub.html',data=data)

@student.route('/studentviewevents')
def studentviewevents():
	data={}
	q="SELECT * FROM EVENT INNER JOIN teacher USING(teacher_id)"
	r=select(q)
	data['events']=r
	return render_template('studentviewevents.html',data=data)


@student.route('/studentviewresource')
def studentviewresource():
	data={}
	q="SELECT * FROM `resource` where rstatus='active'"
	r=select(q)
	data['reso']=r
	return render_template('studentviewresource.html',data=data)


@student.route('/studentviewfacility')
def studentviewfacility():
	data={}
	q="SELECT * FROM `facilities` where fstatus='active' "
	r=select(q)
	data['faci']=r
	return render_template('studentviewfacility.html',data=data)

@student.route('/studenteditprofile',methods=['get','post'])
def studenteditprofile():
	data={}
	sid=session['studentid']
	q="select * from  student where student_id='%s' and sstatus='active' "%(sid)
	r=select(q)
	data['updatestudent']=r
	
	if "update" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		q="select * from login inner join student using(username) where student_id='%s'"%(sid)
		print(q)
		res=select(q)
		preuname=res[0]['username']
		print(preuname)
		q="update student set username='%s',firstname='%s',lastname='%s',place='%s',phone='%s',email='%s' where student_id='%s'"%(em,fna,lna,pla,pho,em,sid)
		print(q)
		r=update(q)
		q="update login set username='%s' where username='%s'"%(em,preuname)
		update(q)
		flash(" profile updated successfully")
		return redirect(url_for('student.studenteditprofile'))


		
	

	return render_template('studenteditprofile.html',data=data)
