Treatments done on dataset 5k_stroke-data.csv

1-'Other' value removed from 'gender' since only 1 entry
2-Label encoding done of categorical variables
	-gender: 1=male, 0=female
	-ever_married: 1=yes,0=no
	-work_type: 0=Govt_job,1=Never_worked,2=Private,3=Self-employed,4=children
	-Residence_type: 0=rural,1=urban
	-smoking_status: 0=unknown,1=formerly smoked,2=never smoked,3=smokes
3-Handling missing values
	-Imputing 201 missing values of BMI with median
4-Oversampling of stroke positive entries
	-Stroke=1 oversampled using SMOTE and concatenated with the original database
5-File saved as Data1.csv