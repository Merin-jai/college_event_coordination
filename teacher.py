from flask import *
from database import*

teacher=Blueprint('teacher',__name__)

@teacher.route('/teacherhome')
def teacherhome():
	data={}
	tid=session['teacherid']
	q="select * from teacher where teacher_id='%s' and tstatus='active'"%(tid)


	res=select(q)
	print(res)
	data['tea']=res
	return render_template('teacherhome.html',data=data)


@teacher.route('/teacherviewclub')
def teacherviewclub():
	data={}
	q="select * from club where cstatus='active'"
	r=select(q)
	data['clubs']=r
	return render_template('teacherviewclub.html',data=data)


@teacher.route('/teacherviewresources')
def teacherviewresources():
	data={}
	q="SELECT * FROM `resource` where rstatus='active'"
	r=select(q)
	data['reso']=r
	return render_template('teacherviewresources.html',data=data)


@teacher.route('/teacherviewfacilities')
def teacherviewfacilities():
	data={}
	q="SELECT * FROM `facilities` where fstatus='active'"
	r=select(q)
	data['faci']=r
	return render_template('teacherviewfacilities.html',data=data)



@teacher.route('/teachermanagestudent',methods=['get','post'])
def teachermanagestudent():
	data={}
	if "register" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		# uname=request.form['u']
		pwd=request.form['p']
		ql="insert into login values('%s','%s','student')"%(em,pwd)
		rl=insert(ql)
		qs="insert into student values(null,'%s','%s','%s','%s','%s','%s','active')"%(em,fna,lna,pla,pho,em)
		insert(qs)
		print(qs)
		flash("added successfully")
		return redirect(url_for('teacher.teachermanagestudent'))
	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None
	if "update" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']

		q="update student set  firstname='%s',lastname='%s',place='%s',phone='%s',email='%s' where student_id='%s'"%(fna,lna,pla,pho,em,sid)
		r=update(q)
		flash("updated successfully")

		return redirect(url_for('teacher.teachermanagestudent'))
	if action=="update":
		q="select * from  student where student_id='%s'"%(sid)
		r=select(q)
		data['updatestudent']=r
	if action=="delete":
		q="delete from student where student_id='%s'"%(sid)
		delete(q)
		flash("deleted successfully")

		return redirect(url_for('teacher.teachermanagestudent'))
	q="select * from student"
	r=select(q)
	data['stud']=r
	return render_template('teachermanagestudent.html',data=data)




@teacher.route('/teacherviewprofile',methods=['get','post'])
def teacherviewprofile():
	data={}
	tid=session['teacherid']
	q="select * from  teacher where teacher_id='%s'  "%(tid)
	r=select(q)
	data['stud']=r
	if "update" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		d=request.form['de']
		q="select * from login inner join teacher using(username) where teacher_id='%s'"%(tid)
		print(q)
		res=select(q)
		preuname=res[0]['username']
		print(preuname)	
		q="update teacher set username='%s' , firstname='%s',lastname='%s',place='%s',phone='%s',email='%s',designation='%s' where teacher_id='%s'"%(em,fna,lna,pla,pho,em,d,tid)
		r=update(q)
		q="update login set username='%s'  where username='%s'"%(em,preuname)
		r=update(q)
		flash(" profile updated successfully")
		return redirect(url_for('teacher.teacherviewprofile'))

	return render_template('teacherviewprofile.html',data=data)



@teacher.route('/teachermanageevent',methods=['get','post'])
def teachermanageevent():
	data={}
	tid=session['teacherid']
	if "register" in request.form:
		e=request.form['e']
		d=request.form['d']
		ed=request.form['ed']
		et=request.form['et']
		qs="insert into event values(null,'%s','%s','%s','%s','%s')"%(tid,e,d,ed,et)
		insert(qs)
		print(qs)
		flash("added successfully")
		return redirect(url_for('teacher.teachermanageevent'))
	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None
	if "update" in request.form:
		e=request.form['e']
		d=request.form['d']
		ed=request.form['ed']
		et=request.form['et']
		
		q="update event set  event='%s',details='%s',edate='%s',etime='%s' where event_id='%s'"%(e,d,ed,et,sid)
		r=update(q)
		flash("updated successfully")

		return redirect(url_for('teacher.teachermanageevent'))
	if action=="update":
		q="select * from  event where student_id='%s'"%(sid)
		r=select(q)
		data['updatestudent']=r
	if action=="delete":
		q="delete from event where student_id='%s'"%(sid)
		delete(q)
		flash("deleted successfully")

		return redirect(url_for('teacher.teachermanageevent'))
	q="select * from event inner join teacher using(teacher_id) where teacher_id='%s'"%(tid)
	r=select(q)
	data['events']=r
	return render_template('teachermanageevent.html',data=data)
@teacher.route('/teacherbookresource',methods=['get','post'])
def teacherbookresource():
	data={}

	e_id=request.args['e_id']

	q="select * from resource  where rstatus='active'"
	r=select(q)
	data['reso']=r

	if "add" in request.form:
		f=request.form['f_id']
		rq=request.form['rq']

		q="insert into eventchild values(null,'%s','%s','resource','%s')"%(e_id,f,rq)
		insert(q)
		return redirect(url_for('teacher.teacherbookresource',e_id=e_id))

	q="SELECT * FROM eventchild INNER JOIN EVENT USING(event_id) INNER JOIN resource ON resource.`resource_id`=eventchild.`file_id` WHERE `eventchild`.`type`= 'resource' and `eventchild`.`event_id`= '%s'"%(e_id)
	r=select(q)
	data['ress']=r
	return render_template('teacherbookresource.html',data=data)


@teacher.route('/teacherbookfacility',methods=['get','post'])
def teacherbookfacility():
	data={}
	e_id=request.args['e_id']

	q="SELECT * FROM eventchild INNER JOIN EVENT USING(event_id) INNER JOIN facilities ON facilities.`facility_id`=eventchild.`file_id` where `eventchild`.`type`= 'facility'and `eventchild`.`event_id`= '%s'"%(e_id)
	r=select(q)
	data['facc']=r
	q="select * from facilities where fstatus='active'"
	r=select(q)
	data['fa']=r

	if "add" in request.form:
		f=request.form['f_id']
		rq=request.form['rq']
		q="insert into eventchild values(null,'%s','%s','facility','%s')"%(e_id,f,rq)
		insert(q)
		return redirect(url_for('teacher.teacherbookfacility',e_id=e_id))
	return render_template('teacherbookfacility.html',data=data)


