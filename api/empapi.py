"""
    员工模块的增删改查请求
"""
import app


class Employee:
    # 初始化函数——封装资源路径
    def __init__(self):
        self.emp_url = app.base_url + '/api/sys/user'

    def add_emp(self, session, username=None, mobile=None, timeOfEntry=None, formOfEmployment=None, workNumber=None,
                departmentName=None, departmentId=None, correctionTime=None):
        my_add = {"username": username,
                  "mobile": mobile,
                  "timeOfEntry": timeOfEntry,
                  "formOfEmployment": formOfEmployment,
                  "workNumber": workNumber,
                  "departmentName": departmentName,
                  "departmentId": departmentId,
                  "correctionTime": correctionTime}
        return session.post(self.emp_url, json=my_add, headers={"Authorization": "Bearer " + app.TOKEN})

    def update_emp(self, session, id, username=None, mobile=None, timeOfEntry=None, formOfEmployment=None,
                   workNumber=None, departmentName=None, departmentId=None, correctionTime=None):
        my_update = {"username": username,
                     "mobile": mobile,
                     "timeOfEntry": timeOfEntry,
                     "formOfEmployment": formOfEmployment,
                     "workNumber": workNumber,
                     "departmentName": departmentName,
                     "departmentId": departmentId,
                     "correctionTime": correctionTime}
        return session.put(self.emp_url + '/' + id, json=my_update, headers={"Authorization": "Bearer " + app.TOKEN})

    def select_emp(self, session, id):
        return session.get(self.emp_url + '/' + id, headers={"Authorization": "Bearer " + app.TOKEN})

    def delete_emp(self, session, id):
        return session.delete(self.emp_url + '/' + id, headers={"Authorization": "Bearer " + app.TOKEN})
