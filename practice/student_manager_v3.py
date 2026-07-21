import json
from pathlib import Path

def load_students():
    if DATA_FILE.exists():
        with open(DATA_FILE,"r",encoding="utf-8") as file:
            return json.load(file)
    return []
def save_students(students):
    with open(DATA_FILE,"w",encoding="utf-8") as file:
        json.dump(students,file,ensure_ascii=False,indent=2)
def show_menu():
    print("1.添加学生")
    print("2.查看所有学生")
    print("3.查找学生")
    print("4.删除学生")
    print("5.修改成绩")
    print("6.统计信息")
    print("0.退出")
def add_student(students):
    name=input("请输入学生姓名：").strip()
    score=int(input("请输入学生成绩："))
    student={
        "name":name,
        "score":score
    }
    students.append(student)
    save_students(students)
    print("添加成功")
def list_students(students):
    if len(students)==0:
        print("暂无学生")
        return
    for student in students:
        print(student["name"],student["score"])
def find_student(students):
    name=input("请输入要查找的姓名：").strip()
    for student in students:
        if student["name"]==name:
            print("找到了：", student["name"], student["score"])
            return
    print("没有找到这个学生")
def delete_student(students):
    name=input("请输入要删除的学生姓名：").strip()
    for student in students:
        if student["name"]==name:
            students.remove(student)
            save_students(students)
            print("删除成功")
            return
    print("没有找到这个学生")
def update_score(students):
    name=input("请输入要修改成绩的学生姓名:")
    for student in students:
        if student["name"]==name:
            student["score"]=int(input("请输入新的成绩："))
            save_students(students)
            print("修改成功")
            return
    print("没找到这个学生")
def show_statistics(students):
    if len(students)==0:
        print("暂无学生，无法统计")
        return
    total_score=0
    passed_count=0
    top_student=students[0]
    for student in students:
        total_score+=student["score"]
        if student["score"]>=60:
            passed_count+=1
        if student["score"]>top_student["score"]:
            top_student=student
    average=total_score/len(students)
    print(f"学生人数：{len(students)}")
    print(f"平均分：{average:.2f}")
    print(f"最高分学生：{top_student['name']}，{top_student['score']}")
    print(f"及格人数：{passed_count}")

DATA_FILE=Path("students.json")
students=load_students()
while True:
    show_menu()
    choice=input("请选择:").strip()
    if choice=="1":
        add_student(students)
    elif choice=="2":
        list_students(students)
    elif choice=="3":
        find_student(students)
    elif choice=="4":
        delete_student(students)
    elif choice=="5":
        update_score(students)
    elif choice=="6":
        show_statistics(students)
    elif choice=="0":
        print("退出程序")
        break
    else:
        print("无效选择")


