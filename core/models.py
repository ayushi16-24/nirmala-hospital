from django.db import models

TREATMENT_CHOICES = [
    ('laparoscopy', 'Laparoscopy'),
    ('hysteroscopy', 'Hysteroscopy'),
    ('infertility', 'Infertility Treatment'),
    ('pregnancy', 'Pregnancy Care'),
    ('fibroid', 'Fibroid Treatment'),
    ('menstrual', 'Menstrual Disorders'),
    ('high_risk', 'High Risk Pregnancy'),
    ('ovarian', 'Ovarian Cyst Treatment'),
    ('family', 'Family Planning'),
    ('other', 'Other'),
]

class Appointment(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    appointment_date = models.DateField()
    treatment_type = models.CharField(max_length=50, choices=TREATMENT_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date}"

    class Meta:
        ordering = ['-created_at']

class Treatment(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon_class = models.CharField(max_length=100, default='fa-heartbeat')
    short_description = models.TextField()
    full_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Testimonial(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    review = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    treatment = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.rating}★"

    class Meta:
        ordering = ['-created_at']

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('hospital', 'Hospital'),
        ('doctor', 'Doctor'),
        ('staff', 'Staff'),
        ('treatment', 'Treatment Rooms'),
        ('patient', 'Patient Care'),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='hospital')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']
