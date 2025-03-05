from django.db import models

# Create your models here.
#page1
class Personal_details(models.Model):
    Name = models.CharField(max_length=123)
    FatherName = models.CharField(max_length=123)
    Nationality = models.CharField(max_length=123)
    SocialSecurityNumber = models.IntegerField()
    Sex = models.CharField(max_length=123)
    MaritalStatus = models.CharField(max_length=123) 
    PanCardNumber = models.CharField(max_length=123)
    DateOfBirth = models.DateField()
    PlaceOfBirth = models.CharField(max_length=123)
    PresentHouseNumber = models.IntegerField()
    PermanentHouseNumber = models.IntegerField()
    PresentCity = models.CharField(max_length=123)
    PermanentCity = models.CharField(max_length=123)
    PresentState = models.CharField(max_length=123)
    PermanentState = models.CharField(max_length=123)
    PresentPinCode = models.IntegerField()
    PermanentPinCode = models.IntegerField()
    PresentPeriodOfStay = models.CharField(max_length=123)
    PermanentPeriodOfStay = models.CharField(max_length=123)
    PresentTelephoneNumber = models.IntegerField()
    PermanentTelephoneNumber = models.IntegerField()
    PresentMobileNumber = models.IntegerField()
    PermanentMobileNumber = models.IntegerField()
    PresentEmailId = models.EmailField(max_length=123)
    PermanentEmailId = models.EmailField(max_length=123)
    PresentInstantMsgSystemId = models.CharField(max_length=123)
    PermanentInstantMsgSystemId = models.CharField(max_length=123)
    PassportNumber = models.CharField(max_length=123)
    DateOfIssue = models.DateField(max_length=123)
    DateOfExpiry = models.DateField(max_length=123)
    PlaceOfIssue = models.CharField(max_length=123)
    

    def __str__(self):
        return self.Name

#page2        

class Visa_Travel_LanguagesKnown_FamilyInformation(models.Model):
    HaveAVisa = models.CharField(max_length=120)
    AreYouOpenToTravelToUSAOrSrilanka = models.CharField(max_length=120)
    LanguageName = models.CharField(max_length=100)
    CanRead = models.BooleanField(default=False)
    CanWrite = models.BooleanField(default=False)
    CanSpeak = models.BooleanField(default=False)
    FamilyMemberName = models.CharField(max_length=100)
    Relationship = models.CharField(max_length=50)
    DateOfBirth = models.DateField(null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)


    def __str__(self):    
        return self.LanguageName


# page3

class AdditionalQualification(models.Model):
    Programe = models.CharField(max_length=255)
    Institute = models.CharField(max_length=255)
    Duration = models.DateField()
    Percentage = models.CharField(max_length=10)
    Division = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Programe} at {self.Institute}"

class SeminarTraining(models.Model):
    SeminarTrainingProgram = models.CharField(max_length=255)
    ConductedBy = models.CharField(max_length=255)
    Duration = models.DateField()

    def __str__(self):
        return f"{self.SeminarTrainingProgram} by {self.ConductedBy}"

class MajorAchievement(models.Model):
    Description = models.TextField()
    Year = models.IntegerField()

    def __str__(self):
        return f"Achievement in {self.Year}: {self.Description[:50]}..."

class ProjectInformation(models.Model):
    Title = models.CharField(max_length=255)
    Company = models.CharField(max_length=255)
    Client = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Title} for {self.Client} at {self.Company}"

# page4

class FriendRecommendation(models.Model):
    FrndName1 = models.CharField(max_length=255)
    FrndCompany1 = models.CharField(max_length=255)
    FrndEmail1 = models.EmailField()
    FrndNbr1 = models.CharField(max_length=20)
    FrndName2 = models.CharField(max_length=255)
    FrndCompany2 = models.CharField(max_length=255)
    FrndEmail2 = models.EmailField()
    FrndNbr2 = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.FrndName1} & {self.FrndName2}"

class PreviousEmployment(models.Model):
    CompanyName = models.CharField(max_length=255)
    LastDesignationHeld = models.CharField(max_length=255)
    Address = models.TextField()
    Telephone = models.CharField(max_length=20)
    EmploymentPeriod = models.DateField()
    EmployeeCode = models.CharField(max_length=50)
    HRName = models.CharField(max_length=255)
    HRContactNo = models.CharField(max_length=20)
    ReportingManagerDesignation = models.CharField(max_length=255)
    ReportingManagerContactNo = models.CharField(max_length=20)
    AlternativeReportingManagerName = models.CharField(max_length=255)
    AlternativeReportingManagerContactNo = models.CharField(max_length=20)
    AlternativeReportingManagerDesignation = models.CharField(max_length=255)
    AlternativeReportingManagerEmail = models.EmailField()
    EmploymentNature = models.CharField(max_length=20, choices=[('Permanent', 'Permanent'), ('Temporary', 'Temporary')])
    AgencyDetails = models.TextField(blank=True, null=True)
    Remuneration = models.DecimalField(max_digits=10, decimal_places=2)
    ReasonForLeaving = models.TextField()

    def __str__(self):
        return f"{self.CompanyName} - {self.LastDesignationHeld}"


#page5

class PreviousEmployerDetails(models.Model):
    Company2 = models.CharField(max_length=255)
    LastDesignationHeld2 = models.CharField(max_length=255)
    AddressMainOfficeAndBranch2 = models.CharField(max_length=255)
    Telephone2 = models.CharField(max_length=15)
    EmploymentPeriod2 = models.DateField()
    EmployeeCodePersonalNo2 = models.CharField(max_length=50)
    NameOfHR2 = models.CharField(max_length=255)
    ContactNoOfHR2 = models.CharField(max_length=15)
    DesignationDepartmentOfReportingManager2 = models.CharField(max_length=255)
    ContactNoOfReportingManager2 = models.CharField(max_length=15)
    NameOfAlternativeReportingManager2 = models.CharField(max_length=255)
    ContactNoOfAlternativeReportingManager2 = models.CharField(max_length=15)
    DesignationDepartmentOfAlternativeReportingManager2 = models.CharField(max_length=255)
    EmailIdOfAlternativeReportingManager2 = models.EmailField()
    WhetherEmploymentIsPermanentOrTemporary2 = models.CharField(
        max_length=10, choices=[('Permanent', 'Permanent'), ('Temporary', 'Temporary')]
    )
    AgencyDetails2 = models.TextField()
    Remuneration2 = models.DecimalField(max_digits=15, decimal_places=2)
    ReasonForLeaving2 = models.TextField()

    def __str__(self):
        return self.Company2


#page6
class PreviousEmployersDetails(models.Model):
    Company3 = models.CharField(max_length=255)
    LastDesignationHeld3 = models.CharField(max_length=255)
    AddressMainOfficeAndBranch3 = models.CharField(max_length=255)
    Telephone3 = models.CharField(max_length=15)
    EmploymentPeriod3 = models.DateField()
    EmployeeCodePersonalNo3 = models.CharField(max_length=50)
    NameOfHR3 = models.CharField(max_length=255)
    ContactNoOfHR3 = models.CharField(max_length=15)
    DesignationDepartmentOfReportingManager3 = models.CharField(max_length=255)
    ContactNoOfReportingManager3 = models.CharField(max_length=15)
    NameOfAlternativeReportingManager3 = models.CharField(max_length=255)
    ContactNoOfAlternativeReportingManager3 = models.CharField(max_length=15)
    DesignationDepartmentOfAlternativeReportingManager3 = models.CharField(max_length=255)
    EmailIdOfAlternativeReportingManager3 = models.EmailField(null=True, blank=True)
    WhetherEmploymentIsPermanentOrTemporary3 = models.CharField(
        max_length=10, choices=[('Permanent', 'Permanent'), ('Temporary', 'Temporary')]
    )
    AgencyDetails3 = models.TextField()
    Remuneration3 = models.DecimalField(max_digits=15, decimal_places=2)
    ReasonForLeaving3 = models.TextField()

    def __str__(self):
        return self.Company3

#page7

class GapsInEducationAndKeyResponsibilitiesCurrentAssignment(models.Model):
    GapsFrom1 = models.IntegerField()
    GapsTo1 = models.IntegerField()
    GapsReason1 = models.TextField()
    GapsCompleteAddressAndLocation1 = models.TextField()

    GapsFrom2 = models.IntegerField()
    GapsTo2 = models.IntegerField()
    GapsReason2 = models.TextField()
    GapsCompleteAddressAndLocation2 = models.TextField()

    OrganizationChartCurrentPosition = models.TextField()

    KeyResponsibilitiesCurrentAssignment1 = models.TextField()
    KeyResponsibilitiesCurrentAssignment2 = models.TextField()
    KeyResponsibilitiesCurrentAssignment3 = models.TextField()
    KeyResponsibilitiesCurrentAssignment4 = models.TextField()

    def __str__(self):
        return self.GapsCompleteAddressAndLocation2

#page8 

class PersonalAssessment(models.Model):
    Strength1 = models.TextField(null=True, blank=True)
    Strength2 = models.TextField(null=True, blank=True)
    Strength3 = models.TextField(null=True, blank=True)
    Strength4 = models.TextField(null=True, blank=True)
    Strength5 = models.TextField(null=True, blank=True)

    Weakness1 = models.TextField(null=True, blank=True)
    Weakness2 = models.TextField(null=True, blank=True)
    Weakness3 = models.TextField(null=True, blank=True)
    Weakness4 = models.TextField(null=True, blank=True)
    Weakness5 = models.TextField(null=True, blank=True)

    Referee1_Name = models.TextField(null=True, blank=True)
    Referee1_Company = models.TextField(null=True, blank=True)
    Referee1_Address = models.TextField(null=True, blank=True)
    Referee1_Contact = models.TextField(null=True, blank=True)
    Referee1_YearsAcquaintance = models.TextField(null=True, blank=True)

    Referee2_Name = models.TextField(null=True, blank=True)
    Referee2_Company = models.TextField(null=True, blank=True)
    Referee2_Address = models.TextField(null=True, blank=True)
    Referee2_Contact = models.TextField(null=True, blank=True)
    Referee2_YearsAcquaintance = models.TextField(null=True, blank=True)

   
    SportHobby_Why = models.TextField(null=True, blank=True)

   
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Strengths: {self.Strength1 or 'N/A'}, Weaknesses: {self.Weakness1 or 'N/A'}, Referee1: {self.Referee1_Name or 'N/A'}, Hobby: {self.SportHobby_Why or 'N/A'}"


#page9

class Goals(models.Model):
   
    ShortTermGoals = models.TextField()
    LongTermGoals = models.TextField()
    EverAttendMnjSoftwareInterview = models.TextField()
    def __str__(self):
        return f"Short Term Goals: {self.ShortTermGoals or 'N/A'}, Long Term Goals: {self.LongTermGoals or 'N/A'}, Interview Details: {self.EverAttendMnjSoftwareInterview or 'N/A'}"




    

    

    

    

    

    






