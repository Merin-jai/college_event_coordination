from flask import *
from database import*
import uuid


admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')


@admin.route('/adminviewevent')
def adminviewevent():
	data={}
	q="SELECT * FROM EVENT INNER JOIN teacher USING(teacher_id) "
	r=select(q)
	data['events']=r
	return render_template('adminviewevent.html',data=data)


@admin.route('/adminviewresource')
def adminviewresource():
	data={}
	q="SELECT * FROM `resource` where rstatus='active'"
	r=select(q)
	data['reso']=r
	return render_template('adminviewresource.html',data=data)


@admin.route('/adminviewfacility')
def adminviewfacility():
	data={}
	q="SELECT * FROM `facilities` where fstatus='active'"
	r=select(q)
	data['faci']=r
	return render_template('adminviewfacility.html',data=data)



@admin.route('/adminmanagedepartment',methods=['get','post'])
def adminmanagedepartment():
	data={}
	q="select * from department"
	r=select(q)
	data['dept']=r
	
	if "add" in request.form:
		d=request.form['d']
		qs="INSERT INTO department VALUES(NULL,'%s','active')"%(d)
		insert(qs)
		print(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanagedepartment'))
	if "action" in request.args:
		action=request.args['action']
		did=request.args['did']
	else:
		action=None
	if "update" in request.form:
		d=request.form['d']
		q="update department set department='%s' where department_id='%s'"%(d,did)
		r=update(q)
		flash("updated successfully")

		return redirect(url_for('admin.adminmanagedepartment'))
	if action=="update":
		q="select * from  department where department_id='%s'"%(did)
		r=select(q)
		data['updatedpt']=r
	if action=="delete":
		q="update  department set dstatus='inactive' where department_id='%s'"%(did)
		delete(q)
		flash("deleted successfully")

		return redirect(url_for('admin.adminmanagedepartment'))
	return render_template('adminmanagedepartment.html',data=data)



@admin.route('/adminmanageclub',methods=['get','post'])
def adminmanageclub():
	data={}
	q="select * from club"
	r=select(q)
	data['clubs']=r
	
	if "add" in request.form:
		d=request.form['d']
		qs="INSERT INTO club VALUES(NULL,'%s','active')"%(d)
		insert(qs)
		print(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanageclub'))
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if "update" in request.form:
		d=request.form['d']
		q="update club set club='%s' where club_id='%s'"%(d,cid)
		r=update(q)
		flash("updated successfully")

		return redirect(url_for('admin.adminmanageclub'))
	if action=="update":
		q="select * from  club where club_id='%s'"%(cid)
		r=select(q)
		data['updateclub']=r
	if action=="delete":
		q="update  club set cstatus='inactive' where club_id='%s'"%(cid)
		update(q)
		flash("deleted successfully")

		return redirect(url_for('admin.adminmanageclub'))
	return render_template('adminmanageclub.html',data=data)




@admin.route('/adminmanageteacher',methods=['get','post'])
def adminmanageteacher():
	data={}
	q="select * from department where dstatus='active'"
	r=select(q)
	data['dept']=r
	if "register" in request.form:
		did=request.form['d_id']
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		de=request.form['desg']
		# uname=request.form['u']
		pwd=request.form['p']
		q="select * from login where username='%s'"%(em)
		res=select(q)
		if res:
			flash("username is already exist")
		else:
			ql="insert into login values('%s','%s','teacher')"%(em,pwd)
			rl=insert(ql)
			qs="insert into teacher values(null,'%s','%s','%s','%s','%s','%s','%s','%s','active')"%(em,did,fna,lna,pla,pho,em,de)
			insert(qs)
			print(qs)
			flash("added successfully")
			return redirect(url_for('admin.adminmanageteacher'))
	if "action" in request.args:
		action=request.args['action']
		tid=request.args['tid']
		lid=request.args['lid']
	else:
		action=None
	if "update" in request.form:
		did=request.form['d_id']
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		de=request.form['desg']
		q="select * from login inner join teacher using(username) where teacher_id='%s'"%(tid)
		print(q)
		res=select(q)
		preuname=res[0]['username']
		q="update teacher set username='%s',department_id='%s', firstname='%s',lastname='%s',place='%s',phone='%s',email='%s',designation='%s' where teacher_id='%s'"%(em,did,fna,lna,pla,pho,em,de,tid)
		r=update(q)
		q="update login set username='%s'  where username='%s'"%(em,preuname)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanageteacher'))
	if action=="update":
		q="select * from  teacher where teacher_id='%s'"%(tid)
		r=select(q)
		data['updateteacher']=r
	if action=="delete":
		q="update teacher set tstatus='inactive' where teacher_id='%s'"%(tid)
		update(q)
		q="update  login set usertype='reject' where username='%s'"%(lid)
		update(q)
		flash("inactive successfully")

		return redirect(url_for('admin.adminmanageteacher'))
	q="select * from teacher inner join department using(department_id)"
	r=select(q)
	data['teach']=r


	if "search" in request.form:
		sn=request.form['sname']+"%"
		print(sn)
		q="select * FROM department INNER JOIN `teacher` USING(`department_id`) where  designation like '%s' or department like '%s'"%(sn,sn)
		print(q)
		r=select(q)
		print(r)
		data['search']=r

	return render_template('adminmanageteacher.html',data=data)







@admin.route('/adminmanageresource',methods=['get','post'])
def adminmanageresource():
	data={}
	q="select * from resource"
	r=select(q)
	data['reso']=r
	if "add" in request.form:
		d=request.form['d']
		q=request.form['q']

		i=request.files['i']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		
		qs="insert into resource values(null,'%s','%s','%s','active')"%(d,q,path)
		insert(qs)
		print(qs)
		return redirect(url_for('admin.adminmanageresource'))
	if "action" in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None
	if "update" in request.form:
		d=request.form['d']
		q=request.form['q']
		i=request.files['i']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		
		
		q="update resource set rname='%s', quantity='%s',image='%s' where resource_id='%s'"%(d,q,path,rid)
		r=update(q)
		flash("update successfully")

		return redirect(url_for('admin.adminmanageresource'))
	if action=="update":
		q="select * from  resource where resource_id='%s'"%(rid)
		r=select(q)
		data['updateresources']=r
	if action=="delete":
		q="update resource set rstatus='inactive' where resource_id='%s'"%(rid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for('admin.adminmanageresource'))
	return render_template('adminmanageresource.html',data=data)


@admin.route('/adminmanagefacilities',methods=['get','post'])
def adminmanagefacilities():
	data={}
	q="select * from facilities"
	r=select(q)
	data['fac']=r
	if "add" in request.form:
		f=request.form['f']

		i=request.files['i']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		
		qs="insert into facilities values(null,'%s','%s','active')"%(f,path)
		insert(qs)
		print(qs)
		return redirect(url_for('admin.adminmanagefacilities'))
	if "action" in request.args:
		action=request.args['action']
		fid=request.args['fid']
	else:
		action=None
	if "update" in request.form:
		f=request.form['f']
		i=request.files['i']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		
		
		q="update facilities set fname='%s', image='%s' where facility_id='%s'"%(f,path,fid)
		r=update(q)
		return redirect(url_for('admin.adminmanagefacilities'))
	if action=="update":
		q="select * from  facilities where facility_id='%s'"%(fid)
		r=select(q)
		data['updatefac']=r
	if action=="delete":
		q="update  facilities set fstatus='inactive' where facility_id='%s'"%(fid)
		update(q)
		return redirect(url_for('admin.adminmanagefacilities'))
	return render_template('adminmanagefacilities.html',data=data)
