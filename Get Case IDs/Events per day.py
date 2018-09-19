import csv
from datetime import datetime
from datetime import timedelta, date
from pandas import datetime as dt

#vectors
outlierdata = []
data = []
allactivities = []
outliercases = []
nonoutliercases = []

#input files
inputfile = 'Only Outliers Events Per Day BPI2012.csv'
for line in open(inputfile, 'r').readlines():
    elements=line.split(',')
    row = [element.rstrip('\n') for element in elements]
    outlierdata.append(row)

#Adjust for every data set
firstline = []

if inputfile == 'Only Outliers Events Per Day BPI2012.csv':
    caseID = []
    activity = []
    resource = []
    completetimestamp = []
    variantcase = []
    variant = []
    amount_req = []
    conceptname = []
    lifecycletransition = []

if inputfile == 'Only Outliers Events Per Day BPI2017.csv':
    caseID = []
    activity = []
    resource = []
    starttimestamp = []
    completetimestamp = []
    variantcase = []
    variant = []
    applicationtype = []
    loangoal = []
    requested_Amount = []
    accepted = []
    action = []
    creditscore = []
    eventID = []
    eventorigin = []
    firstwithdrawalamount = []
    monthlycost = []
    numberofterms = []
    offerID = []
    offeramount = []
    selected = []
    lifecycletransition = []

if inputfile == 'Only Outliers Events Per Day Sepsis.csv':
    caseID = []
    activity = []
    completetimestamp = []
    Variantcase = []
    Variant = []
    Age = []
    CRP = []
    Diagnose = []
    DiagnosticArtAstrup = []
    DiagnosticBlood = []
    DiagnosticECG = []
    DiagnosticIC = []
    DiagnosticLacticAcid = []
    DiagnosticLiquor = []
    DiagnosticOther = []
    DiagnosticSputum = []
    DiagnosticUrinaryCulture = []
    DiagnosticUrinarySediment = []
    DiagnosticXthorax = []
    DisfuncOrg = []
    Hypotensie = []
    Hypoxie = []
    InfectionSuspected = []
    Infusion = []
    LacticAcid = []
    Leucocytes = []
    Oligurie = []
    SIRSCritHeartRate = []
    SIRSCritLeucos = []
    SIRSCritTachypnea = []
    SIRSCritTemperature = []
    SIRSCriteria2OrMore = []
    Lifecycletransition = []
    OrgGroup = []

if inputfile == 'Only Outliers Events Per Day Road Traffic Fine.csv':
    caseID = []
    activity = []
    Resource = []
    completetimestamp = []
    Variantcase = []
    Variant = []
    Amount = []
    Article = []
    Dismissal = []
    Expense = []
    LastSent = []
    lifecycleTransition = []
    Matricola = []
    NotificationType = []
    PaymentAmount = []
    Points = []
    TotalPaymentAmount = []
    VehicleClass = []

if inputfile == 'Only Outliers Events Per Day Hospital Log.csv':
    caseID = []
    activity = []
    completetimestamp = []
    variantcase = []
    variant = []
    age = []
    age1 = []
    age2 = []
    age3 = []
    age4 = []
    age5 = []
    diagnosis = []
    diagnosistreatmentcombinationID = []
    diagnosistreatmentcombinationID1 = []
    diagnosistreatmentcombinationID10 = []
    diagnosistreatmentcombinationID11 = []
    diagnosistreatmentcombinationID12 = []
    diagnosistreatmentcombinationID13 = []
    diagnosistreatmentcombinationID14 = []
    diagnosistreatmentcombinationID15 = []
    diagnosistreatmentcombinationID2 = []
    diagnosistreatmentcombinationID3 = []
    diagnosistreatmentcombinationID4 = []
    diagnosistreatmentcombinationID5 = []
    diagnosistreatmentcombinationID6 = []
    diagnosistreatmentcombinationID7 = []
    diagnosistreatmentcombinationID8 = []
    diagnosistreatmentcombinationID9 = []
    diagnosiscode = []
    diagnosiscode1 = []
    diagnosiscode10 = []
    diagnosiscode11 = []
    diagnosiscode12 = []
    diagnosiscode13 = []
    diagnosiscode14 = []
    diagnosiscode15 = []
    diagnosiscode2 = []
    diagnosiscode3 = []
    diagnosiscode4 = []
    diagnosiscode5 = []
    diagnosiscode6 = []
    diagnosiscode7 = []
    diagnosiscode8 = []
    diagnosiscode9 = []
    diagnosis1 = []
    diagnosis10 = []
    diagnosis11 = []
    diagnosis12 = []
    diagnosis13 = []
    diagnosis14 = []
    diagnosis15 = []
    diagnosis2 = []
    diagnosis3 = []
    diagnosis4 = []
    diagnosis5 = []
    diagnosis6 = []
    diagnosis7 = []
    diagnosis8 = []
    diagnosis9 = []
    specialismcode = []
    specialismcode1 = []
    specialismcode10 = []
    specialismcode11 = []
    specialismcode12 = []
    specialismcode13 = []
    specialismcode14 = []
    specialismcode15 = []
    specialismcode2 = []
    specialismcode3 = []
    specialismcode4 = []
    specialismcode5 = []
    specialismcode6 = []
    specialismcode7 = []
    specialismcode8 = []
    specialismcode9 = []
    treatmentcode = []
    treatmentcode1 = []
    treatmentcode10 = []
    treatmentcode11 = []
    treatmentcode12 = []
    treatmentcode13 = []
    treatmentcode14 = []
    treatmentcode15 = []
    treatmentcode2 = []
    treatmentcode3 = []
    treatmentcode4 = []
    treatmentcode5 = []
    treatmentcode6 = []
    treatmentcode7 = []
    treatmentcode8 = []
    treatmentcode9 = []
    activitycode = []
    numberofexecutions = []
    producercode = []
    section = []
    gewoonspecialismcode = []
    lifecycleTransition = []
    orgGroup = []

if inputfile == 'Only Outliers Events Per Day Hospital Billing.csv':
    caseID = []
    activity = []
    resource = []
    completetimestamp = []
    variantcase = []
    variant = []
    actOrange = []
    actRed = []
    blocked = []
    caseType = []
    closeCode = []
    diagnosis = []
    flagA = []
    flagB = []
    flagC = []
    flagD = []
    isCancelled = []
    isClosed = []
    lifecycleTransition = []
    msgCode = []
    msgCount = []
    msgType = []
    speciality = []
    state = []
    version = []

inputfile = 'BPI_Challenge_2012.csv'
for line in open(inputfile, 'r').readlines():
    elements = line.split(';')
    row = [element.rstrip('\n') for element in elements]
    data.append(row)

    if inputfile == 'BPI_Challenge_2012.csv':
        caseID.append(row[0])
        activity.append(row[1])
        resource.append(row[2])
        completetimestamp.append(row[3])
        variantcase.append(row[4])
        variant.append(row[5])
        amount_req.append(row[6])
        conceptname.append(row[7])
        lifecycletransition.append(row[8])

    if inputfile == 'BPI Challenge 2017.csv':
        caseID.append(row[0])
        activity.append(row[1])
        resource.append(row[2])
        starttimestamp.append(row[3])
        completetimestamp.append(row[4])
        variantcase.append(row[5])
        variant.append(row[6])
        applicationtype.append(row[7])
        loangoal.append(row[8])
        requested_Amount.append(row[9])
        accepted.append(row[10])
        action.append(row[11])
        creditscore.append(row[12])
        eventID.append(row[13])
        eventorigin.append(row[14])
        firstwithdrawalamount.append(row[15])
        monthlycost.append(row[16])
        numberofterms.append(row[17])
        offerID.append(row[18])
        offeramount.append(row[19])
        selected.append(row[20])
        lifecycletransition.append(row[21])

    if inputfile == 'Sepsis_Cases.csv':
        caseID.append(row[0])
        activity.append(row[1])
        completetimestamp.append(row[2])
        Variantcase.append(row[3])
        Variant.append(row[4])
        Age.append(row[5])
        CRP.append(row[6])
        Diagnose.append(row[7])
        DiagnosticArtAstrup.append(row[8])
        DiagnosticBlood.append(row[9])
        DiagnosticECG.append(row[10])
        DiagnosticIC.append(row[11])
        DiagnosticLacticAcid.append(row[12])
        DiagnosticLiquor.append(row[13])
        DiagnosticOther.append(row[14])
        DiagnosticSputum.append(row[15])
        DiagnosticUrinaryCulture.append(row[16])
        DiagnosticUrinarySediment.append(row[17])
        DiagnosticXthorax.append(row[18])
        DisfuncOrg.append(row[19])
        Hypotensie.append(row[20])
        Hypoxie.append(row[21])
        InfectionSuspected.append(row[22])
        Infusion.append(row[23])
        LacticAcid.append(row[24])
        Leucocytes.append(row[25])
        Oligurie.append(row[26])
        SIRSCritHeartRate.append(row[27])
        SIRSCritLeucos.append(row[28])
        SIRSCritTachypnea.append(row[29])
        SIRSCritTemperature.append(row[30])
        SIRSCriteria2OrMore.append(row[31])
        Lifecycletransition.append(row[32])
        OrgGroup.append(row[33])

    if inputfile == 'Road_Traffic_Fine_Management_Process.csv':
        caseID.append(row[0])
        activity.append(row[1])
        Resource.append(row[2])
        completetimestamp.append(row[3])
        Variantcase.append(row[4])
        Variant.append(row[5])
        Amount.append(row[6])
        Article.append(row[7])
        Dismissal.append(row[8])
        Expense.append(row[9])
        LastSent.append(row[10])
        lifecycleTransition.append(row[11])
        Matricola.append(row[12])
        NotificationType.append(row[13])
        PaymentAmount.append(row[14])
        Points.append(row[15])
        TotalPaymentAmount.append(row[16])
        VehicleClass.append(row[17])

    if inputfile == 'Hospital_log.csv':
        caseID.append(row[0])
        activity.append(row[1])
        completetimestamp.append(row[2])
        variantcase.append(row[3])
        variant.append(row[4])
        age.append(row[5])
        age1.append(row[6])
        age2.append(row[7])
        age3.append(row[8])
        age4.append(row[9])
        age5.append(row[10])
        diagnosis.append(row[11])
        diagnosistreatmentcombinationID.append(row[12])
        diagnosistreatmentcombinationID1.append(row[13])
        diagnosistreatmentcombinationID10.append(row[14])
        diagnosistreatmentcombinationID11.append(row[15])
        diagnosistreatmentcombinationID12.append(row[16])
        diagnosistreatmentcombinationID13.append(row[17])
        diagnosistreatmentcombinationID14.append(row[18])
        diagnosistreatmentcombinationID15.append(row[19])
        diagnosistreatmentcombinationID2.append(row[20])
        diagnosistreatmentcombinationID3.append(row[21])
        diagnosistreatmentcombinationID4.append(row[22])
        diagnosistreatmentcombinationID5.append(row[23])
        diagnosistreatmentcombinationID6.append(row[24])
        diagnosistreatmentcombinationID7.append(row[25])
        diagnosistreatmentcombinationID8.append(row[26])
        diagnosistreatmentcombinationID9.append(row[27])
        diagnosiscode.append(row[28])
        diagnosiscode1.append(row[29])
        diagnosiscode10.append(row[30])
        diagnosiscode11.append(row[31])
        diagnosiscode12.append(row[32])
        diagnosiscode13.append(row[33])
        diagnosiscode14.append(row[34])
        diagnosiscode15.append(row[35])
        diagnosiscode2.append(row[36])
        diagnosiscode3.append(row[37])
        diagnosiscode4.append(row[38])
        diagnosiscode5.append(row[39])
        diagnosiscode6.append(row[40])
        diagnosiscode7.append(row[41])
        diagnosiscode8.append(row[42])
        diagnosiscode9.append(row[43])
        diagnosis1.append(row[44])
        diagnosis10.append(row[45])
        diagnosis11.append(row[46])
        diagnosis12.append(row[47])
        diagnosis13.append(row[48])
        diagnosis14.append(row[49])
        diagnosis15.append(row[50])
        diagnosis2.append(row[51])
        diagnosis3.append(row[52])
        diagnosis4.append(row[53])
        diagnosis5.append(row[54])
        diagnosis6.append(row[55])
        diagnosis7.append(row[56])
        diagnosis8.append(row[57])
        diagnosis9.append(row[58])
        specialismcode.append(row[59])
        specialismcode1.append(row[60])
        specialismcode10.append(row[61])
        specialismcode11.append(row[62])
        specialismcode12.append(row[63])
        specialismcode13.append(row[64])
        specialismcode14.append(row[65])
        specialismcode15.append(row[66])
        specialismcode2.append(row[67])
        specialismcode3.append(row[68])
        specialismcode4.append(row[69])
        specialismcode5.append(row[70])
        specialismcode6.append(row[71])
        specialismcode7.append(row[72])
        specialismcode8.append(row[73])
        specialismcode9.append(row[74])
        treatmentcode.append(row[75])
        treatmentcode1.append(row[76])
        treatmentcode10.append(row[77])
        treatmentcode11.append(row[78])
        treatmentcode12.append(row[79])
        treatmentcode13.append(row[80])
        treatmentcode14.append(row[81])
        treatmentcode15.append(row[82])
        treatmentcode2.append(row[83])
        treatmentcode3.append(row[84])
        treatmentcode4.append(row[85])
        treatmentcode5.append(row[86])
        treatmentcode6.append(row[87])
        treatmentcode7.append(row[88])
        treatmentcode8.append(row[89])
        treatmentcode9.append(row[90])
        activitycode.append(row[91])
        numberofexecutions.append(row[92])
        producercode.append(row[93])
        section.append(row[94])
        gewoonspecialismcode.append(row[95])
        lifecycleTransition.append(row[96])
        orgGroup.append(row[97])

    if inputfile == 'Hospital_Billing.csv':
        caseID.append(row[0])
        activity.append(row[1])
        resource.append(row[2])
        completetimestamp.append(row[3])
        variantcase.append(row[4])
        variant.append(row[5])
        actOrange.append(row[6])
        actRed.append(row[7])
        blocked.append(row[8])
        caseType.append(row[9])
        closeCode.append(row[10])
        diagnosis.append(row[11])
        flagA.append(row[12])
        flagB.append(row[13])
        flagC.append(row[14])
        flagD.append(row[15])
        isCancelled.append(row[16])
        isClosed.append(row[17])
        lifecycleTransition.append(row[18])
        msgCode.append(row[19])
        msgCount.append(row[20])
        msgType.append(row[21])
        speciality.append(row[22])
        state.append(row[23])
        version.append(row[24])

if inputfile == 'BPI_Challenge_2012.csv':
    firstline.append(caseID[0])
    firstline.append(activity[0])
    firstline.append(resource[0])
    firstline.append(completetimestamp[0])
    firstline.append(variantcase[0])
    firstline.append(variant[0])
    firstline.append(amount_req[0])
    firstline.append(conceptname[0])
    firstline.append(lifecycletransition[0])
    caseID.pop(0)
    activity.pop(0)
    resource.pop(0)
    completetimestamp.pop(0)
    variant.pop(0)
    variantcase.pop(0)
    amount_req.pop(0)
    conceptname.pop(0)
    lifecycletransition.pop(0)

if inputfile == 'BPI Challenge 2017.csv':
    firstline.append(caseID[0])
    firstline.append(activity[0])
    firstline.append(resource[0])
    firstline.append(starttimestamp[0])
    firstline.append(completetimestamp[0])
    firstline.append(variantcase[0])
    firstline.append(variant[0])
    firstline.append(applicationtype[0])
    firstline.append(loangoal[0])
    firstline.append(requested_Amount[0])
    firstline.append(accepted[0])
    firstline.append(action[0])
    firstline.append(creditscore[0])
    firstline.append(eventID[0])
    firstline.append(eventorigin[0])
    firstline.append(firstwithdrawalamount[0])
    firstline.append(monthlycost[0])
    firstline.append(numberofterms[0])
    firstline.append(offerID[0])
    firstline.append(offeramount[0])
    firstline.append(selected[0])
    firstline.append(lifecycletransition[0])

    caseID.pop(0)
    activity.pop(0)
    resource.pop(0)
    starttimestamp.pop(0)
    completetimestamp.pop(0)
    variantcase.pop(0)
    variant.pop(0)
    applicationtype.pop(0)
    loangoal.pop(0)
    requested_Amount.pop(0)
    accepted.pop(0)
    action.pop(0)
    creditscore.pop(0)
    eventID.pop(0)
    eventorigin.pop(0)
    firstwithdrawalamount.pop(0)
    monthlycost.pop(0)
    numberofterms.pop(0)
    offerID.pop(0)
    offeramount.pop(0)
    selected.pop(0)
    lifecycletransition.pop(0)

if inputfile == 'Sepsis_Cases.csv':
    firstline.append(caseID[0])
    firstline.append(activity[0])
    firstline.append(completetimestamp[0])
    firstline.append(Variantcase[0])
    firstline.append(Variant[0])
    firstline.append(Age[0])
    firstline.append(CRP[0])
    firstline.append(Diagnose[0])
    firstline.append(DiagnosticArtAstrup[0])
    firstline.append(DiagnosticBlood[0])
    firstline.append(DiagnosticECG[0])
    firstline.append(DiagnosticIC[0])
    firstline.append(DiagnosticLacticAcid[0])
    firstline.append(DiagnosticLiquor[0])
    firstline.append(DiagnosticOther[0])
    firstline.append(DiagnosticSputum[0])
    firstline.append(DiagnosticUrinaryCulture[0])
    firstline.append(DiagnosticUrinarySediment[0])
    firstline.append(DiagnosticXthorax[0])
    firstline.append(DisfuncOrg[0])
    firstline.append(Hypotensie[0])
    firstline.append(Hypoxie[0])
    firstline.append(InfectionSuspected[0])
    firstline.append(Infusion[0])
    firstline.append(LacticAcid[0])
    firstline.append(Leucocytes[0])
    firstline.append(Oligurie[0])
    firstline.append(SIRSCritHeartRate[0])
    firstline.append(SIRSCritLeucos[0])
    firstline.append(SIRSCritTachypnea[0])
    firstline.append(SIRSCritTemperature[0])
    firstline.append(SIRSCriteria2OrMore[0])
    firstline.append(Lifecycletransition[0])
    firstline.append(OrgGroup[0])
    caseID.pop(0)
    activity.pop(0)
    completetimestamp.pop(0)
    Variantcase.pop(0)
    Variant.pop(0)
    Age.pop(0)
    CRP.pop(0)
    Diagnose.pop(0)
    DiagnosticArtAstrup.pop(0)
    DiagnosticBlood.pop(0)
    DiagnosticECG.pop(0)
    DiagnosticIC.pop(0)
    DiagnosticLacticAcid.pop(0)
    DiagnosticLiquor.pop(0)
    DiagnosticOther.pop(0)
    DiagnosticSputum.pop(0)
    DiagnosticUrinaryCulture.pop(0)
    DiagnosticUrinarySediment.pop(0)
    DiagnosticXthorax.pop(0)
    DisfuncOrg.pop(0)
    Hypotensie.pop(0)
    Hypoxie.pop(0)
    InfectionSuspected.pop(0)
    Infusion.pop(0)
    LacticAcid.pop(0)
    Leucocytes.pop(0)
    Oligurie.pop(0)
    SIRSCritHeartRate.pop(0)
    SIRSCritLeucos.pop(0)
    SIRSCritTachypnea.pop(0)
    SIRSCritTemperature.pop(0)
    SIRSCriteria2OrMore.pop(0)
    Lifecycletransition.pop(0)
    OrgGroup.pop(0)

if inputfile == 'Road_Traffic_Fine_Management_Process.csv':
    firstline.append(caseID[0])
    firstline.append(activity[0])
    firstline.append(Resource[0])
    firstline.append(completetimestamp[0])
    firstline.append(Variantcase[0])
    firstline.append(Variant[0])
    firstline.append(Amount[0])
    firstline.append(Article[0])
    firstline.append(Dismissal[0])
    firstline.append(Expense[0])
    firstline.append(LastSent[0])
    firstline.append(lifecycleTransition[0])
    firstline.append(Matricola[0])
    firstline.append(NotificationType[0])
    firstline.append(PaymentAmount[0])
    firstline.append(Points[0])
    firstline.append(TotalPaymentAmount[0])
    firstline.append(VehicleClass[0])
    caseID.pop(0)
    activity.pop(0)
    Resource.pop(0)
    completetimestamp.pop(0)
    Variantcase.pop(0)
    Variant.pop(0)
    Amount.pop(0)
    Article.pop(0)
    Dismissal.pop(0)
    Expense.pop(0)
    LastSent.pop(0)
    lifecycleTransition.pop(0)
    Matricola.pop(0)
    NotificationType.pop(0)
    PaymentAmount.pop(0)
    Points.pop(0)
    TotalPaymentAmount.pop(0)
    VehicleClass.pop(0)

if inputfile == 'Hospital_log.csv':
    firstline.append(caseID[0])
    firstline.append(activity[0])
    firstline.append(completetimestamp[0])
    firstline.append(variantcase[0])
    firstline.append(variant[0])
    firstline.append(age[0])
    firstline.append(age1[0])
    firstline.append(age2[0])
    firstline.append(age3[0])
    firstline.append(age4[0])
    firstline.append(age5[0])
    firstline.append(diagnosis[0])
    firstline.append(diagnosistreatmentcombinationID[0])
    firstline.append(diagnosistreatmentcombinationID1[0])
    firstline.append(diagnosistreatmentcombinationID10[0])
    firstline.append(diagnosistreatmentcombinationID11[0])
    firstline.append(diagnosistreatmentcombinationID12[0])
    firstline.append(diagnosistreatmentcombinationID13[0])
    firstline.append(diagnosistreatmentcombinationID14[0])
    firstline.append(diagnosistreatmentcombinationID15[0])
    firstline.append(diagnosistreatmentcombinationID2[0])
    firstline.append(diagnosistreatmentcombinationID3[0])
    firstline.append(diagnosistreatmentcombinationID4[0])
    firstline.append(diagnosistreatmentcombinationID5[0])
    firstline.append(diagnosistreatmentcombinationID6[0])
    firstline.append(diagnosistreatmentcombinationID7[0])
    firstline.append(diagnosistreatmentcombinationID8[0])
    firstline.append(diagnosistreatmentcombinationID9[0])
    firstline.append(diagnosiscode[0])
    firstline.append(diagnosiscode1[0])
    firstline.append(diagnosiscode10[0])
    firstline.append(diagnosiscode11[0])
    firstline.append(diagnosiscode12[0])
    firstline.append(diagnosiscode13[0])
    firstline.append(diagnosiscode14[0])
    firstline.append(diagnosiscode15[0])
    firstline.append(diagnosiscode2[0])
    firstline.append(diagnosiscode3[0])
    firstline.append(diagnosiscode4[0])
    firstline.append(diagnosiscode5[0])
    firstline.append(diagnosiscode6[0])
    firstline.append(diagnosiscode7[0])
    firstline.append(diagnosiscode8[0])
    firstline.append(diagnosiscode9[0])
    firstline.append(diagnosis1[0])
    firstline.append(diagnosis10[0])
    firstline.append(diagnosis11[0])
    firstline.append(diagnosis12[0])
    firstline.append(diagnosis13[0])
    firstline.append(diagnosis14[0])
    firstline.append(diagnosis15[0])
    firstline.append(diagnosis2[0])
    firstline.append(diagnosis3[0])
    firstline.append(diagnosis4[0])
    firstline.append(diagnosis5[0])
    firstline.append(diagnosis6[0])
    firstline.append(diagnosis7[0])
    firstline.append(diagnosis8[0])
    firstline.append(diagnosis9[0])
    firstline.append(specialismcode[0])
    firstline.append(specialismcode1[0])
    firstline.append(specialismcode10[0])
    firstline.append(specialismcode11[0])
    firstline.append(specialismcode12[0])
    firstline.append(specialismcode13[0])
    firstline.append(specialismcode14[0])
    firstline.append(specialismcode15[0])
    firstline.append(specialismcode2[0])
    firstline.append(specialismcode3[0])
    firstline.append(specialismcode4[0])
    firstline.append(specialismcode5[0])
    firstline.append(specialismcode6[0])
    firstline.append(specialismcode7[0])
    firstline.append(specialismcode8[0])
    firstline.append(specialismcode9[0])
    firstline.append(treatmentcode[0])
    firstline.append(treatmentcode1[0])
    firstline.append(treatmentcode10[0])
    firstline.append(treatmentcode11[0])
    firstline.append(treatmentcode12[0])
    firstline.append(treatmentcode13[0])
    firstline.append(treatmentcode14[0])
    firstline.append(treatmentcode15[0])
    firstline.append(treatmentcode2[0])
    firstline.append(treatmentcode3[0])
    firstline.append(treatmentcode4[0])
    firstline.append(treatmentcode5[0])
    firstline.append(treatmentcode6[0])
    firstline.append(treatmentcode7[0])
    firstline.append(treatmentcode8[0])
    firstline.append(treatmentcode9[0])
    firstline.append(activitycode[0])
    firstline.append(numberofexecutions[0])
    firstline.append(producercode[0])
    firstline.append(section[0])
    firstline.append(gewoonspecialismcode[0])
    firstline.append(lifecycleTransition[0])
    firstline.append(orgGroup[0])

    caseID.pop(0)
    activity.pop(0)
    completetimestamp.pop(0)
    variantcase.pop(0)
    variant.pop(0)
    age.pop(0)
    age1.pop(0)
    age2.pop(0)
    age3.pop(0)
    age4.pop(0)
    age5.pop(0)
    diagnosis.pop(0)
    diagnosistreatmentcombinationID.pop(0)
    diagnosistreatmentcombinationID1.pop(0)
    diagnosistreatmentcombinationID10.pop(0)
    diagnosistreatmentcombinationID11.pop(0)
    diagnosistreatmentcombinationID12.pop(0)
    diagnosistreatmentcombinationID13.pop(0)
    diagnosistreatmentcombinationID14.pop(0)
    diagnosistreatmentcombinationID15.pop(0)
    diagnosistreatmentcombinationID2.pop(0)
    diagnosistreatmentcombinationID3.pop(0)
    diagnosistreatmentcombinationID4.pop(0)
    diagnosistreatmentcombinationID5.pop(0)
    diagnosistreatmentcombinationID6.pop(0)
    diagnosistreatmentcombinationID7.pop(0)
    diagnosistreatmentcombinationID8.pop(0)
    diagnosistreatmentcombinationID9.pop(0)
    diagnosiscode.pop(0)
    diagnosiscode1.pop(0)
    diagnosiscode10.pop(0)
    diagnosiscode11.pop(0)
    diagnosiscode12.pop(0)
    diagnosiscode13.pop(0)
    diagnosiscode14.pop(0)
    diagnosiscode15.pop(0)
    diagnosiscode2.pop(0)
    diagnosiscode3.pop(0)
    diagnosiscode4.pop(0)
    diagnosiscode5.pop(0)
    diagnosiscode6.pop(0)
    diagnosiscode7.pop(0)
    diagnosiscode8.pop(0)
    diagnosiscode9.pop(0)
    diagnosis1.pop(0)
    diagnosis10.pop(0)
    diagnosis11.pop(0)
    diagnosis12.pop(0)
    diagnosis13.pop(0)
    diagnosis14.pop(0)
    diagnosis15.pop(0)
    diagnosis2.pop(0)
    diagnosis3.pop(0)
    diagnosis4.pop(0)
    diagnosis5.pop(0)
    diagnosis6.pop(0)
    diagnosis7.pop(0)
    diagnosis8.pop(0)
    diagnosis9.pop(0)
    specialismcode.pop(0)
    specialismcode1.pop(0)
    specialismcode10.pop(0)
    specialismcode11.pop(0)
    specialismcode12.pop(0)
    specialismcode13.pop(0)
    specialismcode14.pop(0)
    specialismcode15.pop(0)
    specialismcode2.pop(0)
    specialismcode3.pop(0)
    specialismcode4.pop(0)
    specialismcode5.pop(0)
    specialismcode6.pop(0)
    specialismcode7.pop(0)
    specialismcode8.pop(0)
    specialismcode9.pop(0)
    treatmentcode.pop(0)
    treatmentcode1.pop(0)
    treatmentcode10.pop(0)
    treatmentcode11.pop(0)
    treatmentcode12.pop(0)
    treatmentcode13.pop(0)
    treatmentcode14.pop(0)
    treatmentcode15.pop(0)
    treatmentcode2.pop(0)
    treatmentcode3.pop(0)
    treatmentcode4.pop(0)
    treatmentcode5.pop(0)
    treatmentcode6.pop(0)
    treatmentcode7.pop(0)
    treatmentcode8.pop(0)
    treatmentcode9.pop(0)
    activitycode.pop(0)
    numberofexecutions.pop(0)
    producercode.pop(0)
    section.pop(0)
    gewoonspecialismcode.pop(0)
    lifecycleTransition.pop(0)
    orgGroup.pop(0)

if inputfile == 'Hospital_Billing.csv':
    firstline.append(caseID[0])
    firstline.append(activity[0])
    firstline.append(resource[0])
    firstline.append(completetimestamp[0])
    firstline.append(variantcase[0])
    firstline.append(variant[0])
    firstline.append(actOrange[0])
    firstline.append(actRed[0])
    firstline.append(blocked[0])
    firstline.append(caseType[0])
    firstline.append(closeCode[0])
    firstline.append(diagnosis[0])
    firstline.append(flagA[0])
    firstline.append(flagB[0])
    firstline.append(flagC[0])
    firstline.append(flagD[0])
    firstline.append(isCancelled[0])
    firstline.append(isClosed[0])
    firstline.append(lifecycleTransition[0])
    firstline.append(msgCode[0])
    firstline.append(msgCount[0])
    firstline.append(msgType[0])
    firstline.append(speciality[0])
    firstline.append(state[0])
    firstline.append(version[0])

    caseID.pop(0)
    activity.pop(0)
    resource.pop(0)
    completetimestamp.pop(0)
    variantcase.pop(0)
    variant.pop(0)
    actOrange.pop(0)
    actRed.pop(0)
    blocked.pop(0)
    caseType.pop(0)
    closeCode.pop(0)
    diagnosis.pop(0)
    flagA.pop(0)
    flagB.pop(0)
    flagC.pop(0)
    flagD.pop(0)
    isCancelled.pop(0)
    isClosed.pop(0)
    lifecycleTransition.pop(0)
    msgCode.pop(0)
    msgCount.pop(0)
    msgType.pop(0)
    speciality.pop(0)
    state.pop(0)
    version.pop(0)

#Make dates from dates
completetimestamp2 = []
for date in completetimestamp:
    object = datetime.strftime(datetime.strptime(date,'%Y/%m/%d %H:%M:%S.%f'), '%Y-%m-%d')
    completetimestamp2.append(object)

outlierdates = []
for i in range(1, len(outlierdata)):
    outlierdata[i][0] = datetime.strftime(datetime.strptime(outlierdata[i][0],'%Y-%m-%d %H:%M:%S'), '%Y-%m-%d')
    outlierdates.append(object)

#Make floats
for i in range(1,len(outlierdata)):
    for j in range(1,len(outlierdata[i])):
        outlierdata[i][j] = int(outlierdata[i][j])

#Find case ID's that are outliers
for i in range(1,len(outlierdata)):
    for j in range(1, len(outlierdata[i])):
        if outlierdata[i][j] == 1:
            for k in range(0, len(caseID)):
                if completetimestamp2[k] == outlierdata[i][0]:
                    if caseID[k] not in outliercases:
                        outliercases.append(caseID[k])

#Find case ID's that are not outliers
for i in range(0,len(caseID)):
    if caseID[i] not in outliercases:
        nonoutliercases.append(caseID[i])

#Make CSV's outliers and non outliers

with open('Outliers file Events Per Day BPI2012.csv','w', newline ='') as f:
    writer = csv.writer(f)
    temp = []
    for i in range(0,len(firstline)):
        temp.append(firstline[i])
    writer.writerow(temp)
    for i in range(0, len(caseID)):
        if caseID[i] in outliercases:
            temp = []

            if inputfile == 'BPI_Challenge_2012.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(resource[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(amount_req[i])
                temp.append(conceptname[i])
                temp.append(lifecycletransition[i])

            if inputfile == 'BPI Challenge 2017.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(resource[i])
                temp.append(starttimestamp[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(applicationtype[i])
                temp.append(loangoal[i])
                temp.append(requested_Amount[i])
                temp.append(accepted[i])
                temp.append(action[i])
                temp.append(creditscore[i])
                temp.append(eventID[i])
                temp.append(eventorigin[i])
                temp.append(firstwithdrawalamount[i])
                temp.append(monthlycost[i])
                temp.append(numberofterms[i])
                temp.append(offerID[i])
                temp.append(offeramount[i])
                temp.append(selected[i])
                temp.append(lifecycletransition[i])

            if inputfile == 'Sepsis_Cases.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(completetimestamp[i])
                temp.append(Variantcase[i])
                temp.append(Variant[i])
                temp.append(Age[i])
                temp.append(CRP[i])
                temp.append(Diagnose[i])
                temp.append(DiagnosticArtAstrup[i])
                temp.append(DiagnosticBlood[i])
                temp.append(DiagnosticECG[i])
                temp.append(DiagnosticIC[i])
                temp.append(DiagnosticLacticAcid[i])
                temp.append(DiagnosticLiquor[i])
                temp.append(DiagnosticOther[i])
                temp.append(DiagnosticSputum[i])
                temp.append(DiagnosticUrinaryCulture[i])
                temp.append(DiagnosticUrinarySediment[i])
                temp.append(DiagnosticXthorax[i])
                temp.append(DisfuncOrg[i])
                temp.append(Hypotensie[i])
                temp.append(Hypoxie[i])
                temp.append(InfectionSuspected[i])
                temp.append(Infusion[i])
                temp.append(LacticAcid[i])
                temp.append(Leucocytes[i])
                temp.append(Oligurie[i])
                temp.append(SIRSCritHeartRate[i])
                temp.append(SIRSCritLeucos[i])
                temp.append(SIRSCritTachypnea[i])
                temp.append(SIRSCritTemperature[i])
                temp.append(SIRSCriteria2OrMore[i])
                temp.append(Lifecycletransition[i])
                temp.append(OrgGroup[i])

            if inputfile == 'Road_Traffic_Fine_Management_Process.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(Resource[i])
                temp.append(completetimestamp[i])
                temp.append(Variantcase[i])
                temp.append(Variant[i])
                temp.append(Amount[i])
                temp.append(Article[i])
                temp.append(Dismissal[i])
                temp.append(Expense[i])
                temp.append(LastSent[i])
                temp.append(lifecycleTransition[i])
                temp.append(Matricola[i])
                temp.append(NotificationType[i])
                temp.append(PaymentAmount[i])
                temp.append(Points[i])
                temp.append(TotalPaymentAmount[i])
                temp.append(VehicleClass[i])

            if inputfile == 'Hospital_log.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(age[i])
                temp.append(age1[i])
                temp.append(age2[i])
                temp.append(age3[i])
                temp.append(age4[i])
                temp.append(age5[i])
                temp.append(diagnosis[i])
                temp.append(diagnosistreatmentcombinationID[i])
                temp.append(diagnosistreatmentcombinationID1[i])
                temp.append(diagnosistreatmentcombinationID10[i])
                temp.append(diagnosistreatmentcombinationID11[i])
                temp.append(diagnosistreatmentcombinationID12[i])
                temp.append(diagnosistreatmentcombinationID13[i])
                temp.append(diagnosistreatmentcombinationID14[i])
                temp.append(diagnosistreatmentcombinationID15[i])
                temp.append(diagnosistreatmentcombinationID2[i])
                temp.append(diagnosistreatmentcombinationID3[i])
                temp.append(diagnosistreatmentcombinationID4[i])
                temp.append(diagnosistreatmentcombinationID5[i])
                temp.append(diagnosistreatmentcombinationID6[i])
                temp.append(diagnosistreatmentcombinationID7[i])
                temp.append(diagnosistreatmentcombinationID8[i])
                temp.append(diagnosistreatmentcombinationID9[i])
                temp.append(diagnosiscode[i])
                temp.append(diagnosiscode1[i])
                temp.append(diagnosiscode10[i])
                temp.append(diagnosiscode11[i])
                temp.append(diagnosiscode12[i])
                temp.append(diagnosiscode13[i])
                temp.append(diagnosiscode14[i])
                temp.append(diagnosiscode15[i])
                temp.append(diagnosiscode2[i])
                temp.append(diagnosiscode3[i])
                temp.append(diagnosiscode4[i])
                temp.append(diagnosiscode5[i])
                temp.append(diagnosiscode6[i])
                temp.append(diagnosiscode7[i])
                temp.append(diagnosiscode8[i])
                temp.append(diagnosiscode9[i])
                temp.append(diagnosis1[i])
                temp.append(diagnosis10[i])
                temp.append(diagnosis11[i])
                temp.append(diagnosis12[i])
                temp.append(diagnosis13[i])
                temp.append(diagnosis14[i])
                temp.append(diagnosis15[i])
                temp.append(diagnosis2[i])
                temp.append(diagnosis3[i])
                temp.append(diagnosis4[i])
                temp.append(diagnosis5[i])
                temp.append(diagnosis6[i])
                temp.append(diagnosis7[i])
                temp.append(diagnosis8[i])
                temp.append(diagnosis9[i])
                temp.append(specialismcode[i])
                temp.append(specialismcode1[i])
                temp.append(specialismcode10[i])
                temp.append(specialismcode11[i])
                temp.append(specialismcode12[i])
                temp.append(specialismcode13[i])
                temp.append(specialismcode14[i])
                temp.append(specialismcode15[i])
                temp.append(specialismcode2[i])
                temp.append(specialismcode3[i])
                temp.append(specialismcode4[i])
                temp.append(specialismcode5[i])
                temp.append(specialismcode6[i])
                temp.append(specialismcode7[i])
                temp.append(specialismcode8[i])
                temp.append(specialismcode9[i])
                temp.append(treatmentcode[i])
                temp.append(treatmentcode1[i])
                temp.append(treatmentcode10[i])
                temp.append(treatmentcode11[i])
                temp.append(treatmentcode12[i])
                temp.append(treatmentcode13[i])
                temp.append(treatmentcode14[i])
                temp.append(treatmentcode15[i])
                temp.append(treatmentcode2[i])
                temp.append(treatmentcode3[i])
                temp.append(treatmentcode4[i])
                temp.append(treatmentcode5[i])
                temp.append(treatmentcode6[i])
                temp.append(treatmentcode7[i])
                temp.append(treatmentcode8[i])
                temp.append(treatmentcode9[i])
                temp.append(activitycode[i])
                temp.append(numberofexecutions[i])
                temp.append(producercode[i])
                temp.append(section[i])
                temp.append(gewoonspecialismcode[i])
                temp.append(lifecycleTransition[i])
                temp.append(orgGroup[i])

            if inputfile == 'Hospital_Billing.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(resource[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(actOrange[i])
                temp.append(actRed[i])
                temp.append(blocked[i])
                temp.append(caseType[i])
                temp.append(closeCode[i])
                temp.append(diagnosis[i])
                temp.append(flagA[i])
                temp.append(flagB[i])
                temp.append(flagC[i])
                temp.append(flagD[i])
                temp.append(isCancelled[i])
                temp.append(isClosed[i])
                temp.append(lifecycleTransition[i])
                temp.append(msgCode[i])
                temp.append(msgCount[i])
                temp.append(msgType[i])
                temp.append(speciality[i])
                temp.append(state[i])
                temp.append(version[i])

            writer.writerow(temp)

with open('NonOutliers file Events Per Day BPI2012.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    temp = []
    for i in range(0,len(firstline)):
        temp.append(firstline[i])
    writer.writerow(temp)
    for i in range(0, len(caseID)):
        if caseID[i] not in outliercases:
            temp = []

            if inputfile == 'BPI_Challenge_2012.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(resource[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(amount_req[i])
                temp.append(conceptname[i])
                temp.append(lifecycletransition[i])
                writer.writerow(temp)

            if inputfile == 'BPI Challenge 2017.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(resource[i])
                temp.append(starttimestamp[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(applicationtype[i])
                temp.append(loangoal[i])
                temp.append(requested_Amount[i])
                temp.append(accepted[i])
                temp.append(action[i])
                temp.append(creditscore[i])
                temp.append(eventID[i])
                temp.append(eventorigin[i])
                temp.append(firstwithdrawalamount[i])
                temp.append(monthlycost[i])
                temp.append(numberofterms[i])
                temp.append(offerID[i])
                temp.append(offeramount[i])
                temp.append(selected[i])
                temp.append(lifecycletransition[i])

            if inputfile == 'Sepsis_Cases.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(completetimestamp[i])
                temp.append(Variantcase[i])
                temp.append(Variant[i])
                temp.append(Age[i])
                temp.append(CRP[i])
                temp.append(Diagnose[i])
                temp.append(DiagnosticArtAstrup[i])
                temp.append(DiagnosticBlood[i])
                temp.append(DiagnosticECG[i])
                temp.append(DiagnosticIC[i])
                temp.append(DiagnosticLacticAcid[i])
                temp.append(DiagnosticLiquor[i])
                temp.append(DiagnosticOther[i])
                temp.append(DiagnosticSputum[i])
                temp.append(DiagnosticUrinaryCulture[i])
                temp.append(DiagnosticUrinarySediment[i])
                temp.append(DiagnosticXthorax[i])
                temp.append(DisfuncOrg[i])
                temp.append(Hypotensie[i])
                temp.append(Hypoxie[i])
                temp.append(InfectionSuspected[i])
                temp.append(Infusion[i])
                temp.append(LacticAcid[i])
                temp.append(Leucocytes[i])
                temp.append(Oligurie[i])
                temp.append(SIRSCritHeartRate[i])
                temp.append(SIRSCritLeucos[i])
                temp.append(SIRSCritTachypnea[i])
                temp.append(SIRSCritTemperature[i])
                temp.append(SIRSCriteria2OrMore[i])
                temp.append(Lifecycletransition[i])
                temp.append(OrgGroup[i])

            if inputfile == 'Road_Traffic_Fine_Management_Process.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(Resource[i])
                temp.append(completetimestamp[i])
                temp.append(Variantcase[i])
                temp.append(Variant[i])
                temp.append(Amount[i])
                temp.append(Article[i])
                temp.append(Dismissal[i])
                temp.append(Expense[i])
                temp.append(LastSent[i])
                temp.append(lifecycleTransition[i])
                temp.append(Matricola[i])
                temp.append(NotificationType[i])
                temp.append(PaymentAmount[i])
                temp.append(Points[i])
                temp.append(TotalPaymentAmount[i])
                temp.append(VehicleClass[i])

            if inputfile == 'Hospital_log.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(age[i])
                temp.append(age1[i])
                temp.append(age2[i])
                temp.append(age3[i])
                temp.append(age4[i])
                temp.append(age5[i])
                temp.append(diagnosis[i])
                temp.append(diagnosistreatmentcombinationID[i])
                temp.append(diagnosistreatmentcombinationID1[i])
                temp.append(diagnosistreatmentcombinationID10[i])
                temp.append(diagnosistreatmentcombinationID11[i])
                temp.append(diagnosistreatmentcombinationID12[i])
                temp.append(diagnosistreatmentcombinationID13[i])
                temp.append(diagnosistreatmentcombinationID14[i])
                temp.append(diagnosistreatmentcombinationID15[i])
                temp.append(diagnosistreatmentcombinationID2[i])
                temp.append(diagnosistreatmentcombinationID3[i])
                temp.append(diagnosistreatmentcombinationID4[i])
                temp.append(diagnosistreatmentcombinationID5[i])
                temp.append(diagnosistreatmentcombinationID6[i])
                temp.append(diagnosistreatmentcombinationID7[i])
                temp.append(diagnosistreatmentcombinationID8[i])
                temp.append(diagnosistreatmentcombinationID9[i])
                temp.append(diagnosiscode[i])
                temp.append(diagnosiscode1[i])
                temp.append(diagnosiscode10[i])
                temp.append(diagnosiscode11[i])
                temp.append(diagnosiscode12[i])
                temp.append(diagnosiscode13[i])
                temp.append(diagnosiscode14[i])
                temp.append(diagnosiscode15[i])
                temp.append(diagnosiscode2[i])
                temp.append(diagnosiscode3[i])
                temp.append(diagnosiscode4[i])
                temp.append(diagnosiscode5[i])
                temp.append(diagnosiscode6[i])
                temp.append(diagnosiscode7[i])
                temp.append(diagnosiscode8[i])
                temp.append(diagnosiscode9[i])
                temp.append(diagnosis1[i])
                temp.append(diagnosis10[i])
                temp.append(diagnosis11[i])
                temp.append(diagnosis12[i])
                temp.append(diagnosis13[i])
                temp.append(diagnosis14[i])
                temp.append(diagnosis15[i])
                temp.append(diagnosis2[i])
                temp.append(diagnosis3[i])
                temp.append(diagnosis4[i])
                temp.append(diagnosis5[i])
                temp.append(diagnosis6[i])
                temp.append(diagnosis7[i])
                temp.append(diagnosis8[i])
                temp.append(diagnosis9[i])
                temp.append(specialismcode[i])
                temp.append(specialismcode1[i])
                temp.append(specialismcode10[i])
                temp.append(specialismcode11[i])
                temp.append(specialismcode12[i])
                temp.append(specialismcode13[i])
                temp.append(specialismcode14[i])
                temp.append(specialismcode15[i])
                temp.append(specialismcode2[i])
                temp.append(specialismcode3[i])
                temp.append(specialismcode4[i])
                temp.append(specialismcode5[i])
                temp.append(specialismcode6[i])
                temp.append(specialismcode7[i])
                temp.append(specialismcode8[i])
                temp.append(specialismcode9[i])
                temp.append(treatmentcode[i])
                temp.append(treatmentcode1[i])
                temp.append(treatmentcode10[i])
                temp.append(treatmentcode11[i])
                temp.append(treatmentcode12[i])
                temp.append(treatmentcode13[i])
                temp.append(treatmentcode14[i])
                temp.append(treatmentcode15[i])
                temp.append(treatmentcode2[i])
                temp.append(treatmentcode3[i])
                temp.append(treatmentcode4[i])
                temp.append(treatmentcode5[i])
                temp.append(treatmentcode6[i])
                temp.append(treatmentcode7[i])
                temp.append(treatmentcode8[i])
                temp.append(treatmentcode9[i])
                temp.append(activitycode[i])
                temp.append(numberofexecutions[i])
                temp.append(producercode[i])
                temp.append(section[i])
                temp.append(gewoonspecialismcode[i])
                temp.append(lifecycleTransition[i])
                temp.append(orgGroup[i])

            if inputfile == 'Hospital_Billing.csv':
                temp.append(caseID[i])
                temp.append(activity[i])
                temp.append(resource[i])
                temp.append(completetimestamp[i])
                temp.append(variantcase[i])
                temp.append(variant[i])
                temp.append(actOrange[i])
                temp.append(actRed[i])
                temp.append(blocked[i])
                temp.append(caseType[i])
                temp.append(closeCode[i])
                temp.append(diagnosis[i])
                temp.append(flagA[i])
                temp.append(flagB[i])
                temp.append(flagC[i])
                temp.append(flagD[i])
                temp.append(isCancelled[i])
                temp.append(isClosed[i])
                temp.append(lifecycleTransition[i])
                temp.append(msgCode[i])
                temp.append(msgCount[i])
                temp.append(msgType[i])
                temp.append(speciality[i])
                temp.append(state[i])
                temp.append(version[i])

            writer.writerow(temp)


# usefuldata = []
# for i in range(0,len(outliercases)):
#     usefuldata.append([])
#
# for i in range(0,len(allactivities)):
#     for j in range(0,len(usefuldata)):
#         usefuldata[j].append(0)
#
# usefuldata[0] = allactivities
# for i in range(0,len(caseID)):
#     for j in range(0, len(outliercases)):
#         for k in range(0, len(allactivities)):
#             if outliercases[j] == caseID[i] and allactivities[k] == activity[i]:

