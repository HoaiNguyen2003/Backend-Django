from django.shortcuts import render, redirect
from .models import CV, Task
from django.contrib.auth.models import User
from faker import Faker 
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def generate_fake_data(request):
    fake = Faker()
    for _ in range(10):
        # Tạo dữ liệu giả mạo cho mỗi user
        user = User.objects.create(username=fake.user_name(), email=fake.email())
        CV.objects.create(
            user=user,
            full_name=fake.name(),
            email=user.email,
            phone_number=fake.phone_number(),
            date_of_birth=fake.date_of_birth(),
            address=fake.address(),
            gender=fake.random_element(elements=('Male', 'Female')),
            education=fake.text(),
            work_experience=fake.text(),
            skills=fake.text(),
            projects=fake.text(),
            awards=fake.text()
        )
    return render(request, 'fake_data_generated.html')

def view_cv(request, username):
    try:
        cv = CV.objects.get(user__username=username)
    except CV.DoesNotExist:
        # Xử lý khi không tìm thấy CV cho người dùng này
        return HttpResponse("Người dùng không tồn tại trong hệ thống.")
    return render(request, 'cv_1.html', {'cv': cv})

def cv_2(request, username):
    try:
        cv = CV.objects.get(user__username=username)
    except CV.DoesNotExist:
        # Xử lý khi không tìm thấy CV cho người dùng này
        return HttpResponse("Người dùng không tồn tại trong hệ thống.")

    return render(request, 'cv_2.html', {'cv': cv})

def cv1(request):
    return render(request, 'cv1.html')

def cv2(request):
    return render(request, 'cv2.html')


