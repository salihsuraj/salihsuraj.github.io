from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *

def Login(request):
    return render(request, 'studentmgt/home.html')

def Home(request):
    return render(request, 'studentmgt/home.html')

def Register(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'studentmgt/register.html', context)

def allTeachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'studentmgt/allteachers.html',context)

def allStudents(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'studentmgt/allstudents.html',context)

def allExams(request):
    subjects = Exam.objects.all()
    context = {'subjects':subjects}
    return render(request,'studentmgt/allexams.html', context)

def allTests(request):
    subjects = Test.objects.all()
    context = {'subjects':subjects}
    return render(request,'studentmgt/alltests.html', context)

def addExam(request):
    form = ExamForm()
    if request.method == 'POST':
        form=ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allexams')
    context = {'form':form}
    return render(request, 'studentmgt/exam_form.html', context)

def addTest(request):
    form = TestForm()
    if request.method == 'POST':
        form=TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alltests')
    context = {'form':form}
    return render(request, 'studentmgt/test_form.html', context)

def addStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allstudents')
    context = {'form':form}
    return render(request, 'studentmgt/student_form.html', context)

def updateStudent(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('allstudents')
    context = {'student':student, 'form': form}
    return render(request, 'studentmgt/student_form.html', context)

def examEdit(request,pk):
    xm = Exam.objects.get(id=pk)
    form = ExamForm(instance=xm)
    if request.method == 'POST':
        form=ExamForm(request.POST, instance=xm)
        if form.is_valid():
            form.save()
            return redirect('allexams')
    context = {'xm':xm, 'form': form}
    return render(request, 'studentmgt/exam_form.html', context)

def testEdit(request,pk):
    tst = Test.objects.get(id=pk)
    form = TestForm(instance=tst)
    if request.method == 'POST':
        form=TestForm(request.POST, instance=tst)
        if form.is_valid():
            form.save()
            return redirect('alltests')
    context = {'tst':tst, 'form': form}
    return render(request, 'studentmgt/test_form.html', context)

def addTeacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allteachers')
    context = {'form':form}
    return render(request, 'studentmgt/teacher_form.html', context)

def updateTeacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form=TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('allteachers')
    context = {'teacher':teacher, 'form': form}
    return render(request, 'studentmgt/teacher_form.html', context)

def deleteTeacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('allteachers')
    context = {'teacher':teacher}
    return render(request, 'studentmgt/t_delete.html', context)

def deleteStudent(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('allstudents')
    context = {'student':student}
    return render(request, 'studentmgt/s_delete.html', context)





