"""
    2. 在main.py中调用skill_manager.py中实例方法。
    3. 在skill_manager.py中调用skill_deployer.py中实例方法。
    4. 在skill_deployer.py中调用list_helper.py中类方法。
"""
from my_project.skill_system.skill_deployer import D

D().show_d()


class M:
    def show_m(self):
        print("show_m")
