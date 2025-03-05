from django.shortcuts import render
from django.http import HttpResponse
from .models import Personal_details,Visa_Travel_LanguagesKnown_FamilyInformation, AdditionalQualification, SeminarTraining, MajorAchievement, ProjectInformation,FriendRecommendation, PreviousEmployment,PreviousEmployerDetails,PreviousEmployersDetails,GapsInEducationAndKeyResponsibilitiesCurrentAssignment, PersonalAssessment,Goals

#page1
def page_1_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        fathername = request.POST['fathers_name']
        nationality = request.POST['nationality']
        socialsecuritynumber = request.POST['ssn']
        sex = request.POST['sex']
        maritalstatus = request.POST['marital_status']
        pancardnumber = request.POST['pan_card']
        dateofbirth = request.POST['dob']
        placeofbirth = request.POST['place_of_birth']
        presenthousenumber = request.POST['present_house_no']
        permanenthousenumber = request.POST['permanent_house_no']
        presentcity = request.POST['present_city']
        permanentcity = request.POST['permanent_city']
        presentstate = request.POST['present_state']
        permanentstate = request.POST['permanent_state']
        presentpincode = request.POST['present_pin']
        permanentpincode = request.POST['permanent_pin']
        presentperiodstay = request.POST['present_stay']
        permanentperiodstay = request.POST['permanent_stay']
        presenttelephone = request.POST['present_telephone']
        permanenttelephone = request.POST['permanent_telephone']
        presentmobilenumber = request.POST['present_mobile']
        permanentmobilenumber = request.POST['permanent_mobile']
        presentemail = request.POST['present_email']
        permanentemail = request.POST['permanent_email']
        presentinstantmsgsymid = request.POST['present_im']
        permanentinstantmsgsymid = request.POST['permanent_im']
        passportnumber = request.POST['passport_number']
        passportissuedate = request.POST['passport_issue_date']
        passportexpirydate = request.POST['passport_expiry_date']
        passportplaceofissue = request.POST['passport_place_issue']
        if name and fathername:
            makani = Personal_details.objects.create(
                           Name=name, FatherName=fathername, Nationality=nationality, SocialSecurityNumber=socialsecuritynumber,
                           Sex=sex, MaritalStatus=maritalstatus, PanCardNumber=pancardnumber, DateOfBirth=dateofbirth, PlaceOfBirth=placeofbirth,
                            PresentHouseNumber=presenthousenumber, PermanentHouseNumber=permanenthousenumber, PresentCity=presentcity, PermanentCity=permanentcity,
                            PresentState=presentstate, PermanentState=permanentstate, PresentPinCode=presentpincode, PermanentPinCode=permanentpincode,
                            PresentPeriodOfStay=presentperiodstay, PermanentPeriodOfStay=permanentperiodstay, PresentTelephoneNumber=presenttelephone,
                            PermanentTelephoneNumber=permanenttelephone, PresentMobileNumber=presentmobilenumber, PermanentMobileNumber=permanentmobilenumber,
                            PresentEmailId=presentemail, PermanentEmailId=permanentemail, PresentInstantMsgSystemId=presentinstantmsgsymid,
                             PermanentInstantMsgSystemId=permanentinstantmsgsymid, PassportNumber=passportnumber, DateOfIssue=passportissuedate,
                             DateOfExpiry=passportexpirydate, PlaceOfIssue=passportplaceofissue)
            makani.save()
            return HttpResponse("Data Saved Successfully!")          
        
    return render(request, 'page_1.html')


#page2
def page_2_view(request):
    if request.method == 'POST':
        visa_status = request.POST.get('visa_status', 'no') == 'on'
        relocate_status = request.POST.get('relocate_status', 'no') == 'on'
        language1 = request.POST.get('languages_Known1', '')
        read1 = request.POST.get('read1', 'no') == 'on'
        write1 = request.POST.get('write1', 'no') == 'on'
        speak1 = request.POST.get('speak1', 'no') == 'on'
        language2 = request.POST.get('languages_Known2', '')
        read2 = request.POST.get('read2', 'no') == 'on'
        write2 = request.POST.get('write2', 'no') == 'on'
        speak2 = request.POST.get('speak2', 'no') == 'on'
        language3 = request.POST.get('languages_Known3', '')
        read3 = request.POST.get('read3', 'no') == 'on'
        write3 = request.POST.get('write3', 'no') == 'on'
        speak3 = request.POST.get('speak3', 'no') == 'on'

        familymembername1 = request.POST.get('relation1', '')
        relationship1 = request.POST.get('relationship1', '')
        dateofbirthofrelation1 = request.POST.get('date_of_birth_of_relation1', '')
        ageofrelation1 = request.POST.get('age_of_relation1', '')

        familymembername2 = request.POST.get('relation2', '')
        relationship2 = request.POST.get('relationship2', '')
        dateofbirthofrelation2 = request.POST.get('date_of_birth_of_relation2', '')
        ageofrelation2 = request.POST.get('age_of_relation2', '')

        familymembername3 = request.POST.get('relation3', '')
        relationship3 = request.POST.get('relationship3', '')
        dateofbirthofrelation3 = request.POST.get('date_of_birth_of_relation3', '')
        ageofrelation3 = request.POST.get('age_of_relation3', '')

        familymembername4 = request.POST.get('relation4', '')
        relationship4 = request.POST.get('relationship4', '')
        dateofbirthofrelation4 = request.POST.get('date_of_birth_of_relation4', '')
        ageofrelation4 = request.POST.get('age_of_relation4', '')


        
        if language1 and familymembername1:
            ponnur_visa = Visa_Travel_LanguagesKnown_FamilyInformation.objects.create(
                HaveAVisa=visa_status, 
                AreYouOpenToTravelToUSAOrSrilanka=relocate_status
            )
            ponnur_visa.save()

        
        if language1:
            Visa_Travel_LanguagesKnown_FamilyInformation.objects.create(
                LanguageName=language1, CanRead=read1, CanWrite=write1, CanSpeak=speak1
            )
        
        if language2:
            Visa_Travel_LanguagesKnown_FamilyInformation.objects.create(
                LanguageName=language2, CanRead=read2, CanWrite=write2, CanSpeak=speak2
            )
        
        if language3:
            Visa_Travel_LanguagesKnown_FamilyInformation.objects.create(
                LanguageName=language3, CanRead=read3, CanWrite=write3, CanSpeak=speak3
            )
        
        if familymembername1:
            Visa_Travel_LanguagesKnown_FamilyInformation.objects.create(
                FamilyMemberName=familymembername1, 
                Relationship=relationship1, 
                DateOfBirth=dateofbirthofrelation1, 
                Age=ageofrelation1
            )
        
        if familymembername2:
            Visa_Travel_LanguagesKnown_FamilyInformation.objects.create(
                FamilyMemberName=familymembername2, 
                Relationship=relationship2, 
                DateOfBirth=dateofbirthofrelation2, 
                Age=ageofrelation2
            )
        
        if familymembername3:
            Visa_Travel_LanguagesKnown_FamilyInformation.objects.create(
                FamilyMemberName=familymembername3, 
                Relationship=relationship3, 
                DateOfBirth=dateofbirthofrelation3, 
                Age=ageofrelation3
            )

        if familymembername4:
            Visa_Travel_LanguagesKnown_FamilyInformation.objects.create(
               FamilyMemberName=familymembername4, 
                Relationship=relationship4, 
                DateOfBirth=dateofbirthofrelation4, 
                Age=ageofrelation4
            )

        return HttpResponse("Data is saved successfully")

    return render(request, 'page_2.html')

#page3

def page_3_view(request):
    if request.method == "POST":
        qualifications = []
        for i in range(1, 4):
            qualifications.append(AdditionalQualification(
                Programe=request.POST.get(f'programe{i}'),
                Institute=request.POST.get(f'institute{i}'),
                Duration=request.POST.get(f'duration{i}'),
                Percentage=request.POST.get(f'divition{i}'),
                Division=request.POST.get(f'divition{i}')
            ))
        AdditionalQualification.objects.bulk_create(qualifications)

        
        seminars = []
        for i in range(1, 4):
            seminars.append(SeminarTraining(
                SeminarTrainingProgram=request.POST.get(f'seminar/traing programe{i}'),
                ConductedBy=request.POST.get(f'conducted_by{i}'),
                Duration=request.POST.get(f'duration{i}')
            ))
        SeminarTraining.objects.bulk_create(seminars)

        
        achievements = []
        for i in range(1, 3):
            achievements.append(MajorAchievement(
                Description=request.POST.get(f'discription{i}'),
                Year=request.POST.get(f'year{i}')
            ))
        MajorAchievement.objects.bulk_create(achievements)

        
        projects = []
        for i in range(1, 4):
            projects.append(ProjectInformation(
                Title=request.POST.get(f'title{i}'),
                Company=request.POST.get(f'company{i}'),
                Client=request.POST.get(f'client{i}')
            ))
        ProjectInformation.objects.bulk_create(projects)

        return HttpResponse("data submitted successfully")

    return render(request, 'page_3.html')

# page4

def page_4_view(request):
    if request.method == 'POST':
        frnd_name1 = request.POST.get('frnd name1')
        frnd_company1 = request.POST.get('frnd company1')
        frnd_email1 = request.POST.get('frnd emai1')
        frnd_nbr1 = request.POST.get('frnd nbr')

        frnd_name2 = request.POST.get('frnd name2')
        frnd_company2 = request.POST.get('frnd company2')
        frnd_email2 = request.POST.get('frnd emai12')
        frnd_nbr2 = request.POST.get('frnd nbr2')

        
        FriendRecommendation.objects.create(
            FrndName1=frnd_name1,
            FrndCompany1=frnd_company1,
            FrndEmail1=frnd_email1,
            FrndNbr1=frnd_nbr1,
            FrndName2=frnd_name2,
            FrndCompany2=frnd_company2,
            FrndEmail2=frnd_email2,
            FrndNbr2=frnd_nbr2
        )

        
        company1 = request.POST.get('company1')
        last_designation_held1 = request.POST.get('last designation held1')
        address1 = request.POST.get('Address(main office and branch where worked)1')
        telephone1 = request.POST.get('telephone1')
        employment_period1 = request.POST.get('Employment Period:(date,month,year)1')
        employee_code1 = request.POST.get('Employee code/Personal No1')
        hr_name1 = request.POST.get('Name of HR1')
        hr_contact_no1 = request.POST.get('contact no.of HR1')
        reporting_manager_designation1 = request.POST.get('Designation&Department of Reporting Manager1')
        reporting_manager_contact_no1 = request.POST.get('Contact no. of Reporting Manager1')
        alternative_reporting_manager_name1 = request.POST.get('Name of alternative Reporting manager1')
        alternative_reporting_manager_contact_no1 = request.POST.get('Contact no.of alternative Reporting manager1')
        alternative_reporting_manager_designation1 = request.POST.get('Designation&Department of alternative Reporting manager1')
        alternative_reporting_manager_email1 = request.POST.get('email id of alternative Reporting manager1')
        employment_nature1 = request.POST.get('Whether Employment is of permannent or temporary nature/permanent1')
        agency_details1 = request.POST.get('Agency details1')
        remuneration1 = request.POST.get('Remuneration1')
        reason_for_leaving1 = request.POST.get('reason for Leaving1')

        
        PreviousEmployment.objects.create(
            CompanyName=company1,
            LastDesignationHeld=last_designation_held1,
            Address=address1,
            Telephone=telephone1,
            EmploymentPeriod=employment_period1,
            EmployeeCode=employee_code1,
            HRName=hr_name1,
            HRContactNo=hr_contact_no1,
            ReportingManagerDesignation=reporting_manager_designation1,
            ReportingManagerContactNo=reporting_manager_contact_no1,
            AlternativeReportingManagerName=alternative_reporting_manager_name1,
            AlternativeReportingManagerContactNo=alternative_reporting_manager_contact_no1,
            AlternativeReportingManagerDesignation=alternative_reporting_manager_designation1,
            AlternativeReportingManagerEmail=alternative_reporting_manager_email1,
            EmploymentNature=employment_nature1,
            AgencyDetails=agency_details1,
            Remuneration=remuneration1,
            ReasonForLeaving=reason_for_leaving1
        )

        return HttpResponse("data Submitted Successfully")

    return render(request, 'page_4.html')  


#page5

def page_5_view(request):
    if request.method == "POST":
        company2 = request.POST.get('company2')
        last_designation_held2 = request.POST.get('last designation held2')
        address2 = request.POST.get('Address(main office and branch where worked)2')
        telephone2 = request.POST.get('telephone2')
        employment_period2 = request.POST.get('Employment Period:(date,month,year)2')
        employee_code2 = request.POST.get('Employee code/Personal No2')
        hr_name2 = request.POST.get('Name of HR2')
        hr_contact_no2 = request.POST.get('contact no.of HR2')
        reporting_manager_designation2 = request.POST.get('Designation&Department of Reporting Manager2')
        reporting_manager_contact_no2 = request.POST.get('Contact no. of Reporting Manager2')
        alternative_reporting_manager_name2 = request.POST.get('Name of alternative Reporting manager2')
        alternative_reporting_manager_contact_no2 = request.POST.get('Contact no.of alternative Reporting manager2')
        alternative_reporting_manager_designation2 = request.POST.get('Designation&Department of alternative Reporting manager2')
        alternative_reporting_manager_email2 = request.POST.get('email id of alternative Reporting manager2')
        employment_nature2 = request.POST.get('Whether Employment is of permannent or temporary nature/permanent2')
        agency_details2 = request.POST.get('Agency details2')
        remuneration2 = request.POST.get('Remuneration2')
        reason_for_leaving2 = request.POST.get('reason for Leaving2')

        PreviousEmployerDetails.objects.create(
            Company2=company2,
            LastDesignationHeld2=last_designation_held2,
            AddressMainOfficeAndBranch2=address2,
            Telephone2=telephone2,
            EmploymentPeriod2=employment_period2,
            EmployeeCodePersonalNo2=employee_code2,
            NameOfHR2=hr_name2,
            ContactNoOfHR2=hr_contact_no2,
            DesignationDepartmentOfReportingManager2=reporting_manager_designation2,
            ContactNoOfReportingManager2=reporting_manager_contact_no2,
            NameOfAlternativeReportingManager2=alternative_reporting_manager_name2,
            ContactNoOfAlternativeReportingManager2=alternative_reporting_manager_contact_no2,
            DesignationDepartmentOfAlternativeReportingManager2=alternative_reporting_manager_designation2,
            EmailIdOfAlternativeReportingManager2=alternative_reporting_manager_email2,
            WhetherEmploymentIsPermanentOrTemporary2=employment_nature2,
            AgencyDetails2=agency_details2,
            Remuneration2=remuneration2,
            ReasonForLeaving2=reason_for_leaving2
        )

        return HttpResponse("Data submitted successfully")
    
    return render(request, 'page_5.html')


#page6
def page_6_view(request):
    if request.method == "POST":
        company3 = request.POST.get('company3')
        last_designation_held3 = request.POST.get('last designation held3')
        address3 = request.POST.get('Address(main office and branch where worked)3')
        telephone3 = request.POST.get('telephone3')
        employment_period3 = request.POST.get('Employment Period:(date,month,year)3')
        employee_code3 = request.POST.get('Employee code/Personal No3')
        hr_name3 = request.POST.get('Name of HR3')
        hr_contact_no3 = request.POST.get('contact no.of HR3')
        reporting_manager_designation3 = request.POST.get('Designation&Department of Reporting Manager3')
        reporting_manager_contact_no3 = request.POST.get('Contact no. of Reporting Manager3')
        alternative_reporting_manager_name3 = request.POST.get('Name of alternative Reporting manager3')
        alternative_reporting_manager_contact_no3 = request.POST.get('Contact no.of alternative Reporting manager3')
        alternative_reporting_manager_designation3 = request.POST.get('Designation&Department of alternative Reporting manager3')
        alternative_reporting_manager_email3 = request.POST.get('email id of alternative Reporting manager3')
        employment_nature3 = request.POST.get('Whether Employment is of permannent or temporary nature/permanent3')
        agency_details3 = request.POST.get('Agency details3')
        remuneration3 = request.POST.get('Remuneration3')
        reason_for_leaving3 = request.POST.get('reason for Leaving3')

        PreviousEmployersDetails.objects.create(
            Company3=company3,
            LastDesignationHeld3=last_designation_held3,
            AddressMainOfficeAndBranch3=address3,
            Telephone3=telephone3,
            EmploymentPeriod3=employment_period3,
            EmployeeCodePersonalNo3=employee_code3,
            NameOfHR3=hr_name3,
            ContactNoOfHR3=hr_contact_no3,
            DesignationDepartmentOfReportingManager3=reporting_manager_designation3,
            ContactNoOfReportingManager3=reporting_manager_contact_no3,
            NameOfAlternativeReportingManager3=alternative_reporting_manager_name3,
            ContactNoOfAlternativeReportingManager3=alternative_reporting_manager_contact_no3,
            DesignationDepartmentOfAlternativeReportingManager3=alternative_reporting_manager_designation3,
            EmailIdOfAlternativeReportingManager3=alternative_reporting_manager_email3,
            WhetherEmploymentIsPermanentOrTemporary3=employment_nature3,
            AgencyDetails3=agency_details3,
            Remuneration3=remuneration3,
            ReasonForLeaving3=reason_for_leaving3
        )

        return HttpResponse("Data submitted successfully")
    
    return render(request, 'page_6.html')


#page7

def page_7_view(request):
    if request.method == "POST":
        gaps_from1 = request.POST.get("gaps from1")
        gaps_to1 = request.POST.get("gaps to1")
        gaps_reason1 = request.POST.get("gaps reason1")
        gaps_address1 = request.POST.get("gaps compleate address and location1")
        
        gaps_from2 = request.POST.get("gaps from2")
        gaps_to2 = request.POST.get("gaps to2")
        gaps_reason2 = request.POST.get("gaps reason2")
        gaps_address2 = request.POST.get("gaps compleate address and location2")

        organization_chart = request.POST.get("organization chart showing your current position in the current assignment")

        key_resp1 = request.POST.get(" key responsibities at current assignment1")
        key_resp2 = request.POST.get(" key responsibities at current assignment2")
        key_resp3 = request.POST.get(" key responsibities at current assignment3")
        key_resp4 = request.POST.get(" key responsibities at current assignment4")

    
        GapsInEducationAndKeyResponsibilitiesCurrentAssignment.objects.create(
            GapsFrom1=gaps_from1, GapsTo1=gaps_to1, GapsReason1=gaps_reason1, GapsCompleteAddressAndLocation1=gaps_address1,
            GapsFrom2=gaps_from2, GapsTo2=gaps_to2, GapsReason2=gaps_reason2, GapsCompleteAddressAndLocation2=gaps_address2,
            OrganizationChartCurrentPosition=organization_chart,
            KeyResponsibilitiesCurrentAssignment1=key_resp1, KeyResponsibilitiesCurrentAssignment2=key_resp2,
            KeyResponsibilitiesCurrentAssignment3=key_resp3, KeyResponsibilitiesCurrentAssignment4=key_resp4
        )

        return HttpResponse("data saved")  

    return render(request, "page_7.html")

#page8

def page_8_view(request):
    if request.method == "POST":
        strength1 = request.POST.get("strengths1")
        strength2 = request.POST.get("strengths2")
        strength3 = request.POST.get("strengths3")
        strength4 = request.POST.get("strengths4")
        strength5 = request.POST.get("strengths5")
        
        weakness1 = request.POST.get("weaknesses1")
        weakness2 = request.POST.get("weaknesses2")
        weakness3 = request.POST.get("weaknesses3")
        weakness4 = request.POST.get("weaknesses4")
        weakness5 = request.POST.get("weaknesses5")
        
        referee1_name = request.POST.get("referees_name1")
        referee2_name = request.POST.get("referees_name2")
        
        sport_hobby = request.POST.get("sport_hobby")


        PersonalAssessment.objects.create(
            Strength1=strength1,
            Strength2=strength2,
            Strength3=strength3,
            Strength4=strength4,
            Strength5=strength5,
            Weakness1=weakness1,
            Weakness2=weakness2,
            Weakness3=weakness3,
            Weakness4=weakness4,
            Weakness5=weakness5,
            Referee1_Name=referee1_name,
            Referee2_Name=referee2_name,
            SportHobby_Why=sport_hobby
        )

        
        return HttpResponse("Data saved successfully")

   
    return render(request, "page_8.html")



#page9

def page_9_view(request):
    if request.method == "POST":
        short_term_goals = request.POST.get("short term goals")
        long_term_goals = request.POST.get("long term goals")
        ever_attended_interview = request.POST.get("ever attend the mnj software interview ")

        Goals.objects.create(
            ShortTermGoals=short_term_goals,
            LongTermGoals=long_term_goals,
            EverAttendMnjSoftwareInterview=ever_attended_interview
        )

        
        return HttpResponse("Data saved successfully")

    return render(request, "page_9.html")








    
     