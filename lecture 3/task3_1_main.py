import task3_1_module

x = None

x = input("Enter  your favourite website google or facebook or youtube or w3school or firefox :  ")

if x.lower().strip() == 'google':
    task3_1_module.google() 

if x.lower().strip() == 'facebook':
    task3_1_module.facebook()

if x.lower().strip() == 'youtube':
    task3_1_module.youtube()

if x.lower().strip() == 'w3school':
    task3_1_module.w3school()

if x.lower().strip() == 'firefox':
    task3_1_module.firfox()