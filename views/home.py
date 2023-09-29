from flask import Blueprint, render_template,Flask
from com.model import *
from flask import jsonify
import subprocess
import html
bp = Blueprint('home', __name__, url_prefix='/')
app = Flask(__name__)

@bp.route('/')
def index():
	statements = Statements.query.all()
	print(statements)
	pas = [p.to_dict() for p in statements]

	return render_template('index.html', data=pas)
@bp.route('/statement/<int:_id>',methods=['GET'])
def get_statements_to_confirm(_id):
	# 待使用
	statements = Statements.query.all()
	print(statements)
	pas = [p.to_dict() for p in statements]
	for item in pas:
		print(item)
		if _id == item['id']:
			statement = item['statement']
			description = item['description']
		else:
			continue
	# print(statement)
	sta = {'id': _id, 'statement': statement, 'description': description}
	return render_template('confirm.html', data=sta)
    
@bp.route('/pacemaker/<int:_id>', methods=['GET'])
def get_pacemaker(_id):
    # 获取 Pacemaker 状态
	statements = Statements.query.all()
	pas = [p.to_dict() for p in statements]
	for item in pas:
		print(item)
		if _id == item['id']:
			statement = item['statement']
			description = item['description']
		else:
			continue
	sta = statement.split()
	status = subprocess.check_output(sta)
	status = status.decode('ascii')
	status = str(status)
	print(status)
	return render_template('execute.html', data=status)
    # return status

@bp.route("/statements/<int:statement_id>", methods=["GET"])
def get_statements_by_id(statement_id):
    statement = Statements.query.get(statement_id)
    if statement is None:
        abort(404)
    return jsonify(statement.serialize())

@bp.route("/statements", methods=["GET"])
def get_statements():
	statements = Statements.query.all()
	return jsonify([statement.serialize() for statement in statements])

@bp.route("/add_statements", methods=["GET"])
def add_statements():
	# 待完善
	name = request.form['name']
    # 从请求中获取要添加的项目的名称

    new_item = Item(name)
    db.session.add(new_item)
    db.session.commit()
    # 将新项目添加到数据库并提交更改

    return 'Statements added successfully'

@app.route('/delete_statements/<int:statement_id>', methods=['POST'])
def delete_statements(statement_id):
    item = Item.query.get(statement_id)
    # 根据项目的ID获取要删除的项目

    db.session.delete(item)
    db.session.commit()
    # 从数据库中删除项目并提交更改

    return 'Statements deleted successfully'

@app.route('/update_statements/<int:statement_id>', methods=['POST'])
def update_statements(statement_id):
	# 待完善
    
	item = Item.query.get(statement_id)
    # 根据项目的ID获取要更新的项目
    new_name = request.form['new_name']
    # 从请求中获取新的项目名称
    item.name = new_name
    db.session.commit()
    # 更新项目名称并提交更改

    return 'Statements updated successfully'

