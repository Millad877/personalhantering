from CompanyGuiClassFile import CompanyGui
from CompanyClassFile import Company

comp = Company("DICE", "Stockholm")
comp_gui = CompanyGui(comp)
comp_gui.create_pic()
comp_gui.create_buttons()
comp_gui.create_menu()
comp_gui.start()

