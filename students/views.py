from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Course, Marks, Attendance


@login_required
def student_list(request):
    query = request.GET.get('search', '')
    if query:
        students = Student.objects.filter(name__icontains=query) | Student.objects.filter(roll_no__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students, 'search_query': query})


@login_required
def add_student(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)

        Student.objects.create(
            name=name, roll_no=roll_no, email=email,
            phone=phone, course=course
        )
        return redirect('student_list')

    return render(request, 'students/add_student.html', {'courses': courses})


@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_no = request.POST.get('roll_no')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        course_id = request.POST.get('course')
        student.course = Course.objects.get(id=course_id)
        student.save()
        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student, 'courses': courses})


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            return render(request, 'students/login.html', {'error': 'Invalid username or password'})
    return render(request, 'students/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def marks_list(request):
    marks = Marks.objects.all()
    return render(request, 'students/marks_list.html', {'marks': marks})


@login_required
def add_marks(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject = request.POST.get('subject')
        marks_obtained = request.POST.get('marks_obtained')
        total_marks = request.POST.get('total_marks')
        student = Student.objects.get(id=student_id)

        Marks.objects.create(
            student=student, subject=subject,
            marks_obtained=marks_obtained, total_marks=total_marks
        )
        return redirect('marks_list')

    return render(request, 'students/add_marks.html', {'students': students})



@login_required
def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request, 'students/attendance_list.html', {'attendance': attendance})


@login_required
def add_attendance(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        date = request.POST.get('date')
        status = request.POST.get('status')
        student = Student.objects.get(id=student_id)

        Attendance.objects.create(student=student, date=date, status=status)
        return redirect('attendance_list')

    return render(request, 'students/add_attendance.html', {'students': students})