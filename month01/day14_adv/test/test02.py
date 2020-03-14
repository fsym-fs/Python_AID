"""
将学生信息管理系统拆分为4个模块:
    model.py--->xxxModel
    bll.py ---->xxxControls
    usl.py ---->xxxViews
    main.py --->调用xxxViews
"""
from month01.day14_adv.test.usl import StudentManagerView
if __name__== "__main__":
    view = StudentManagerView()
    view.main()
