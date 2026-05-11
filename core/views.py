from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import Treatment, Testimonial, GalleryImage
from .forms import AppointmentForm, ContactForm

TREATMENTS_DATA = [
    {'icon': 'fa-circle-nodes', 'title': 'Laparoscopy', 'slug': 'laparoscopy', 'desc': 'Minimally invasive surgical procedures with faster recovery and minimal scarring.', 'image': 'images/laparoscopy.png'},
    {'icon': 'fa-microscope', 'title': 'Hysteroscopy', 'slug': 'hysteroscopy', 'desc': 'Advanced uterine examination and treatment using a thin, lighted scope.', 'image': 'images/hysteroscopy.png'},
    {'icon': 'fa-baby', 'title': 'Infertility Treatment', 'slug': 'infertility', 'desc': 'Comprehensive infertility evaluation and personalised treatment plans for couples.', 'image': 'images/infertility.png'},
    {'icon': 'fa-heart-pulse', 'title': 'Pregnancy Care', 'slug': 'pregnancy', 'desc': 'Complete antenatal and postnatal care for a safe, healthy pregnancy journey.', 'image': 'images/pregnancy.png'},
    {'icon': 'fa-dna', 'title': 'Fibroid Treatment', 'slug': 'fibroid', 'desc': 'Modern, effective treatment options for uterine fibroids with minimal downtime.', 'image': 'images/fibroid.png'},
    {'icon': 'fa-calendar-days', 'title': 'Menstrual Disorders', 'slug': 'menstrual', 'desc': 'Diagnosis and treatment of irregular, heavy or painful menstrual cycles.', 'image': 'images/menstrual.jpg'},
    {'icon': 'fa-shield-heart', 'title': 'High Risk Pregnancy', 'slug': 'high_risk', 'desc': 'Specialised care and continuous monitoring for high-risk pregnancies.', 'image': 'images/high_risk.jpg'},
    {'icon': 'fa-circle-dot', 'title': 'Ovarian Cyst', 'slug': 'ovarian', 'desc': 'Safe and effective management of ovarian cysts using advanced techniques.', 'image': 'images/ovarian.png'},
    {'icon': 'fa-people-group', 'title': 'Family Planning', 'slug': 'family', 'desc': 'Counselling and modern solutions for family planning and contraception.', 'image': 'images/family.png'},
    {'icon': 'fa-notes-medical', 'title': 'PCOD Treatment', 'slug': 'pcod', 'desc': 'Comprehensive management and personalised lifestyle plans for PCOD/PCOS.', 'image': 'images/pcod.jpg'},
]

TESTIMONIALS_DATA = [
    {'name': 'Priya Sharma', 'review': 'Dr. Nirmala is an exceptional doctor. Her care during my high-risk pregnancy was outstanding. I felt safe and well-looked-after throughout. Highly recommended to every woman!', 'rating': 5, 'treatment': 'High Risk Pregnancy', 'initials': 'PS'},
    {'name': 'Sunita Verma', 'review': 'After years of infertility struggles, Dr. Nirmala gave us hope and results. Her expertise and compassionate approach made all the difference. We now have a beautiful baby girl!', 'rating': 5, 'treatment': 'Infertility Treatment', 'initials': 'SV'},
    {'name': 'Kavita Singh', 'review': 'The laparoscopy procedure was smooth and recovery was faster than I expected. Dr. Yaduvanshi explained everything clearly. The clinic is very clean and professional.', 'rating': 5, 'treatment': 'Laparoscopy', 'initials': 'KS'},
    {'name': 'Meena Joshi', 'review': 'I was diagnosed with PCOS and was very anxious. Dr. Nirmala\'s thorough approach and personalised treatment plan changed my life completely. I feel healthier than ever!', 'rating': 5, 'treatment': 'PCOD/PCOS Treatment', 'initials': 'MJ'},
    {'name': 'Rekha Gupta', 'review': 'Wonderful experience! The staff is caring and Dr. Nirmala is incredibly knowledgeable. She took time to listen and address all my concerns. Best gynecologist in the city!', 'rating': 5, 'treatment': 'Pregnancy Care', 'initials': 'RG'},
]

WHY_DATA = [
    {'icon': 'fa-user-doctor', 'title': 'Experienced Specialist', 'desc': '18+ years of dedicated expertise in gynecology, infertility, and advanced laparoscopic surgery.'},
    {'icon': 'fa-microscope', 'title': 'Modern Technology', 'desc': 'State-of-the-art equipment and advanced minimally invasive surgical techniques.'},
    {'icon': 'fa-shield-heart', 'title': 'Safe Procedures', 'desc': 'All procedures follow strict safety protocols for the best patient outcomes.'},
    {'icon': 'fa-hand-holding-heart', 'title': 'Personalised Care', 'desc': 'Every patient receives an individual treatment plan tailored to their unique needs.'},
    {'icon': 'fa-star', 'title': 'Hygienic Environment', 'desc': 'A spotlessly maintained, hospital-grade hygienic facility you can feel comfortable in.'},
    {'icon': 'fa-bolt', 'title': 'Faster Recovery', 'desc': 'Minimally invasive approaches ensure shorter hospital stays and quicker return to normal life.'},
]

GALLERY_PLACEHOLDERS = [
    {'icon': 'fa-hospital'},
    {'icon': 'fa-bed-pulse'},
    {'icon': 'fa-user-nurse'},
    {'icon': 'fa-syringe'},
    {'icon': 'fa-stethoscope'},
    {'icon': 'fa-heart-pulse'},
]

def index(request):
    appointment_form = AppointmentForm()
    contact_form = ContactForm()
    gallery_images = GalleryImage.objects.filter(is_active=True)[:9]
    db_testimonials = Testimonial.objects.filter(is_active=True)
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'appointment':
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                appointment_form.save()
                messages.success(request, '✓ Your appointment request has been submitted! We will contact you shortly to confirm.')
                return redirect('index')
            else:
                messages.error(request, '⚠ Please fill in all required fields correctly.')
        elif form_type == 'contact':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, '✓ Your message has been sent! We will get back to you within 24 hours.')
                return redirect('index')
            else:
                messages.error(request, '⚠ Please fill in all required fields correctly.')

    context = {
        'treatments': TREATMENTS_DATA,
        'testimonials': list(db_testimonials) if db_testimonials.exists() else TESTIMONIALS_DATA,
        'use_default_testimonials': not db_testimonials.exists(),
        'gallery_images': gallery_images,
        'gallery_placeholders': GALLERY_PLACEHOLDERS,
        'appointment_form': appointment_form,
        'contact_form': contact_form,
        'why_default': WHY_DATA,
        'year': datetime.now().year,
    }
    return render(request, 'core/index.html', context)
