import thread
import time

from odoorpc import ODOO

odoo = ODOO(host='123.207.157.205', port=8888)
uid = odoo.login('custormdb', 'Administrator@woniu66.com', '8hd3kf6ds9')

q_db = odoo.env['kaikong.qq.list']
q = q_db.search([['buddy.buddy', '=', '1501831170']])
q = q_db.browse(q)
cluster = q.clusters
#cluster = cluster.clusters_id
cc = cluster.search([])


def test():
    task, object, param = odoo.execute_kw('kaikong.qq.task', 'getTask', ('1501831170',))
    print task, object, param


for i in range(0, 20):
    thread.start_new_thread(test)

time.sleep(20)
print 'main thread exit...\n'
