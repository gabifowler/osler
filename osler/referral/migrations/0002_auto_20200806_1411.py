# Generated by Django 3.0.5 on 2020-08-06 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referral', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('core', '0002_auto_20200806_1411'),
        ('followup', '0002_auto_20200806_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='referral',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='referral',
            name='kind',
            field=models.ForeignKey(help_text='The kind of care the patient should recieve at the referral location.', on_delete=django.db.models.deletion.PROTECT, to='core.ReferralType'),
        ),
        migrations.AddField(
            model_name='referral',
            name='location',
            field=models.ManyToManyField(to='core.ReferralLocation'),
        ),
        migrations.AddField(
            model_name='referral',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Patient'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='appointment_location',
            field=models.ManyToManyField(blank=True, help_text='Where did the patient make an appointment?', to='core.ReferralLocation'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='contact_method',
            field=models.ForeignKey(help_text='What was the method of contact?', on_delete=django.db.models.deletion.PROTECT, to='core.ContactMethod'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='contact_status',
            field=models.ForeignKey(help_text='Did you make contact with the patient about this referral?', on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='followup_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referral.FollowupRequest'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='no_apt_reason',
            field=models.ForeignKey(blank=True, help_text="If the patient didn't make an appointment, why not?", null=True, on_delete=django.db.models.deletion.PROTECT, to='followup.NoAptReason', verbose_name='No appointment reason'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='no_show_reason',
            field=models.ForeignKey(blank=True, help_text="If the patient didn't go to the appointment, why not?", null=True, on_delete=django.db.models.deletion.PROTECT, to='followup.NoShowReason'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Patient'),
        ),
        migrations.AddField(
            model_name='patientcontact',
            name='referral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='referral.Referral'),
        ),
        migrations.AddField(
            model_name='followuprequest',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followuprequest',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='followuprequest',
            name='completion_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='referral_followuprequest_completed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followuprequest',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Patient'),
        ),
        migrations.AddField(
            model_name='followuprequest',
            name='referral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referral.Referral'),
        ),
    ]
