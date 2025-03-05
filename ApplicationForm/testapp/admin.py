from django.contrib import admin
from testapp.models import Personal_details,Visa_Travel_LanguagesKnown_FamilyInformation, AdditionalQualification, SeminarTraining, MajorAchievement, ProjectInformation,FriendRecommendation, PreviousEmployment,PreviousEmployerDetails,PreviousEmployersDetails,GapsInEducationAndKeyResponsibilitiesCurrentAssignment,PersonalAssessment,Goals


#page1
class Personal_detailsAdmin(admin.ModelAdmin):
    list_display=['Name','FatherName','Nationality','SocialSecurityNumber','Sex','MaritalStatus','PanCardNumber',
    'DateOfBirth','PlaceOfBirth','PresentHouseNumber','PermanentHouseNumber','PresentCity','PermanentCity','PresentState',
    'PermanentState','PresentPinCode', 'PermanentPinCode','PresentPeriodOfStay','PermanentPeriodOfStay','PresentTelephoneNumber',
    'PermanentTelephoneNumber',
    'PresentMobileNumber', 
    'PermanentMobileNumber', 
    'PresentEmailId', 
    'PermanentEmailId', 
    'PresentInstantMsgSystemId', 
    'PermanentInstantMsgSystemId', 
    'PassportNumber',
    'DateOfIssue',
    'DateOfExpiry',
    'PlaceOfIssue']
    
admin.site.register(Personal_details,Personal_detailsAdmin) 

#page2
class Visa_Travel_LanguagesKnown_FamilyInformationAdmin(admin.ModelAdmin):
    list_display=['HaveAVisa',
    'AreYouOpenToTravelToUSAOrSrilanka',
    'LanguageName',
    'CanRead',
    'CanWrite',
    'CanSpeak',
    'FamilyMemberName',
    'Relationship',
    'DateOfBirth',
    'Age' 
]
admin.site.register(Visa_Travel_LanguagesKnown_FamilyInformation,Visa_Travel_LanguagesKnown_FamilyInformationAdmin) 

#page3

class AdditionalQualificationAdmin(admin.ModelAdmin):
    list_display = ['Programe', 'Institute', 'Duration', 'Percentage', 'Division']
admin.site.register(AdditionalQualification, AdditionalQualificationAdmin)

class SeminarTrainingAdmin(admin.ModelAdmin):
    list_display = ['SeminarTrainingProgram', 'ConductedBy', 'Duration']
admin.site.register(SeminarTraining, SeminarTrainingAdmin)

class MajorAchievementAdmin(admin.ModelAdmin):
    list_display = ['Description', 'Year']
admin.site.register(MajorAchievement, MajorAchievementAdmin)

class ProjectInformationAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Company', 'Client']
admin.site.register(ProjectInformation, ProjectInformationAdmin)

# page4

class FriendRecommendationAdmin(admin.ModelAdmin):
    list_display = [
        'FrndName1', 'FrndCompany1', 'FrndEmail1', 'FrndNbr1',
        'FrndName2', 'FrndCompany2', 'FrndEmail2', 'FrndNbr2'
    ]
admin.site.register(FriendRecommendation, FriendRecommendationAdmin)


class PreviousEmploymentAdmin(admin.ModelAdmin):
    list_display = [
        'CompanyName', 'LastDesignationHeld', 'EmploymentPeriod', 'EmployeeCode', 
        'HRName', 'HRContactNo', 'ReportingManagerDesignation', 'ReportingManagerContactNo', 
        'AlternativeReportingManagerName', 'AlternativeReportingManagerContactNo', 
        'AlternativeReportingManagerDesignation', 'AlternativeReportingManagerEmail',
        'EmploymentNature', 'AgencyDetails', 'Remuneration', 'ReasonForLeaving'
    ]
admin.site.register(PreviousEmployment, PreviousEmploymentAdmin)


#page5

class PreviousEmployerDetailsAdmin(admin.ModelAdmin):
    list_display = [
        'Company2', 'LastDesignationHeld2', 'EmploymentPeriod2', 'EmployeeCodePersonalNo2', 
        'NameOfHR2', 'ContactNoOfHR2', 'DesignationDepartmentOfReportingManager2', 'ContactNoOfReportingManager2', 
        'NameOfAlternativeReportingManager2', 'ContactNoOfAlternativeReportingManager2', 
        'DesignationDepartmentOfAlternativeReportingManager2', 'EmailIdOfAlternativeReportingManager2', 
        'WhetherEmploymentIsPermanentOrTemporary2', 'AgencyDetails2', 'Remuneration2', 'ReasonForLeaving2'
    ]

admin.site.register(PreviousEmployerDetails, PreviousEmployerDetailsAdmin)

#page6
class PreviousEmployersDetailsAdmin(admin.ModelAdmin):
    list_display = [
        'Company3', 'LastDesignationHeld3', 'EmploymentPeriod3', 'EmployeeCodePersonalNo3', 
        'NameOfHR3', 'ContactNoOfHR3', 'DesignationDepartmentOfReportingManager3', 'ContactNoOfReportingManager3', 
        'NameOfAlternativeReportingManager3', 'ContactNoOfAlternativeReportingManager3', 
        'DesignationDepartmentOfAlternativeReportingManager3', 'EmailIdOfAlternativeReportingManager3', 
        'WhetherEmploymentIsPermanentOrTemporary3', 'AgencyDetails3', 'Remuneration3', 'ReasonForLeaving3'
    ]

admin.site.register(PreviousEmployersDetails, PreviousEmployersDetailsAdmin)
#page7


from django.contrib import admin
from .models import GapsInEducationAndKeyResponsibilitiesCurrentAssignment

class GapsInEducationAndKeyResponsibilitiesCurrentAssignmentAdmin(admin.ModelAdmin):
    list_display = [
        "GapsFrom1", "GapsTo1", "GapsReason1", "GapsCompleteAddressAndLocation1",
        "GapsFrom2", "GapsTo2", "GapsReason2", "GapsCompleteAddressAndLocation2",
        "OrganizationChartCurrentPosition",
        "KeyResponsibilitiesCurrentAssignment1", "KeyResponsibilitiesCurrentAssignment2",
        "KeyResponsibilitiesCurrentAssignment3", "KeyResponsibilitiesCurrentAssignment4"
    ]

admin.site.register(GapsInEducationAndKeyResponsibilitiesCurrentAssignment, GapsInEducationAndKeyResponsibilitiesCurrentAssignmentAdmin)


#page8


class PersonalAssessmentAdmin(admin.ModelAdmin):
    list_display = [
        'Strength1', 'Strength2', 'Strength3', 'Strength4', 'Strength5',
        'Weakness1', 'Weakness2', 'Weakness3', 'Weakness4', 'Weakness5',
        'SportHobby_Why',
        'Referee1_Name', 'Referee2_Name', 'CreatedAt', 'UpdatedAt'
    ]


admin.site.register(PersonalAssessment, PersonalAssessmentAdmin)

#page9

class GoalsAdmin(admin.ModelAdmin):
    list_display = ['ShortTermGoals', 'LongTermGoals', 'EverAttendMnjSoftwareInterview']

admin.site.register(Goals, GoalsAdmin)



    



# Register your models here.
