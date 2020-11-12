from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

MajorTypes = [
    (0, "人工智能"),
    (1, "全栈工程师"),
    (2, "大数据")
]

GenderTypes = [
    (0, "男"),
    (1, "女")
]

class UserProfile(AbstractUser):
    """
    管理员
    """
    phone = models.CharField(max_length=11, verbose_name="手机号")
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", default=datetime.now)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "管理员"
        verbose_name_plural = verbose_name


class StudentClass(models.Model):
    """
    班级信息
    """
    cla_major = models.IntegerField(choices=MajorTypes, verbose_name="专业", default=0)
    cla_name = models.CharField(max_length=20, verbose_name="班级名称")
    cla_number = models.IntegerField(verbose_name="班级人数")

    def __str__(self):
        return self.cla_name

    class Meta:
        verbose_name = "班级信息"
        verbose_name_plural = verbose_name

class Student(models.Model):
    """
    学生信息
    """
    stu_id = models.CharField(max_length=30, verbose_name="学号")
    stu_name = models.CharField(max_length=10, verbose_name="学生姓名")
    stu_age = models.IntegerField(verbose_name="学生年龄")
    stu_gender = models.IntegerField(choices=GenderTypes, verbose_name="学生性别")
    stu_address = models.CharField(max_length=100, verbose_name="籍贯")
    stu_time = models.DateField(verbose_name="入校时间")
    stu_major = models.IntegerField(choices=MajorTypes, verbose_name="专业", default=0)
    stu_class = models.ForeignKey(StudentClass, verbose_name="所在班级", on_delete=models.CASCADE)

    def __str__(self):
        return self.stu_name

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

class Teacher(models.Model):
    """
    教师信息
    """
    tea_name = models.CharField(max_length=10, verbose_name="教师姓名")
    tea_phone = models.CharField(max_length=11, verbose_name="教师电话")
    tea_email = models.CharField(max_length=50, verbose_name="教师邮箱")

    def __str__(self):
        return self.tea_name

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = verbose_name

class Course(models.Model):
    """
    课程信息
    """
    cou_name = models.CharField(max_length=50, verbose_name="课程名")
    cou_desc = models.CharField(max_length=300, verbose_name="课程描述")
    cou_times = models.CharField(max_length=50, verbose_name="课程时段")
    cou_duration = models.IntegerField(default=0, verbose_name="课程时长")
    cou_teacher = models.ForeignKey(Teacher, verbose_name="讲课教师", on_delete=models.CASCADE)
    cou_class = models.ForeignKey(StudentClass, verbose_name="讲课班级", on_delete=models.CASCADE)

    def __str__(self):
        return self.cou_name

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

