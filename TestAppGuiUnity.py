#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from pywinauto.application import Application

import time

#app = Application(backend='uia').start('notepad.exe', timeout=50)
#app = Application(backend='uia').connect(title='Untitled - Notepad', timeout=2)


#app = Application(backend='win32').connect(title='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>', timeout=10)
app = Application(backend='uia').connect(title='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>', timeout=10)

#app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').print_control_identifiers()
#app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="UnityEditor.SceneHierarchyWindow", class_name="UnityGUIViewWndClass").print_control_identifiers()

#app = Application(backend='uia').connect(title='Безымянный – Блокнот', timeout=50)

time.sleep(1)



#handle = app.window(title_re='Безымянный – Блокнот')
#handle.print_control_identifiers()
#print(handle)

#app.window(title_re='Безымянный – Блокнот').print_control_identifiers()

#textEditor = app.window(title_re='Безымянный – Блокнот').child_window(title="Текстовый редактор", auto_id="15", control_type="Edit").wrapper_object()
#textEditor.type_keys("hi hi", with_spaces=True)



#handle = app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>')
#handle.print_control_identifiers()

#fileMenu = app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="Развернуть", control_type="Button").wrapper_object()
#fileMenu = app['SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>'].child_window(title="Развернуть", control_type="Button").wrapper_object()
fileMenu = app.window(title_re='SQLTest1.*').child_window(title="Развернуть", control_type="Button").wrapper_object()
fileMenu.draw_outline()
time.sleep(1)
fileMenu.click_input()
time.sleep(1)

fileMenu = app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="File", control_type="MenuItem").wrapper_object()
fileMenu.draw_outline()
time.sleep(1)
fileMenu.click_input()
time.sleep(1)

#Необходимо прожать кнопку меню дважды. Активация меню меняет открытие кнопки меню нажатием на наведение.
fileMenu = app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="Edit", control_type="MenuItem").wrapper_object()
fileMenu.click_input()
fileMenu = app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="Edit", control_type="MenuItem").wrapper_object()
fileMenu.click_input()
time.sleep(1)

fileMenuH = app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="UnityEditor.InspectorWindow", control_type="Pane").wrapper_object()
fileMenuH.set_focus()
time.sleep(1)
fileMenuH.draw_outline()
time.sleep(1)


#app.Menu().get_menu_path("UnityEditor.SceneHierarchyWindow")[0].click()
#print_control_identifiers()
#time.sleep(2)

fileMenuH = app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="UnityEditor.SceneHierarchyWindow", control_type="Pane").wrapper_object()
#app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="UnityEditor.SceneHierarchyWindow", control_type="Pane").print_control_identifiers()
fileMenuH.draw_outline()
time.sleep(2)
#fileMenuH.click_input()
#time.sleep(1)
fileMenuH.set_focus()
time.sleep(2)
fileMenuH.type_keys("{TAB 2}")
time.sleep(1)
fileMenuH.type_keys("Cube1")
time.sleep(1)
fileMenuH.type_keys("{ENTER}")
time.sleep(1)

fileMenu = app.window(title_re='SQLTest1 - SampleScene - PC, Mac & Linux Standalone - Unity 2019.2.0b1 Personal <DX11 on DX10 GPU>').child_window(title="Восстановить", control_type="Button").wrapper_object()
fileMenu.click_input() #invoke() or click()





#fileMenu = app.window(title_re='Безымянный – Блокнот').child_window(title="Файл", control_type="MenuItem").wrapper_object()
#fileMenu.click_input()

#createNewMenu = app.window(title_re='Безымянный – Блокнот').child_window(title="Новое окно	CTRL+SHIFT+N", auto_id="8", control_type="MenuItem").wrapper_object()
#createNewMenu.click_input()

#handle = app.window(title_re='Безымянный – Блокнот')
#handle.print_control_identifiers()


#app.window(title_re='Безымянный – Блокнот').type_keys("hi hi hi", with_spaces = True)

#app.window(title_re='Безымянный – Блокнот').menu_select("Справка->О программе")

#app.window(title_re='Безымянный – Блокнот').click_input("Файл")

#app.window(title_re='Безымянный – Блокнот').menu_select('Вид->Масштаб')


#app.window(title_re='Безымянный – Блокнот').menu_select("Вид")
#app.window(title_re='Безымянный – Блокнот').menu_select("Создать")

#app.БезымянныйБлокнот.print_control_identifiers()

#app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)

#app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)

# Select a menu item
#app.UntitledNotepad.menu_select("Help->About Notepad")
#app.UntitledNotepad.menu_select("Довідка->Про програму")
#app.UntitledNotepad.menu_select("Справка->О программе")
# Click on a button
#app.AboutNotepad.OK.click()
#app.Пропрограмублокнот.ОК.click()
#app.Опрограммеблокнот.ОК.click()
# Type a text string
#app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
